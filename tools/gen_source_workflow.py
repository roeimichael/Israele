"""Generate tools/source_workflow.js with the unsourceable places baked in,
so the Workflow can fan out web-research over them (scripts can't read files)."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / ".preview-shots"

# unsourceable = sourceless rows the deterministic pass could NOT source
enr = {r["id"]: r for r in csv.DictReader((OUT / "sourceless_enriched.csv").open(encoding="utf-8"))}
meta = {r["id"]: r for r in csv.DictReader((ROOT / "data" / "places.csv").open(encoding="utf-8"))}

# scoped to high-value types that plausibly have a web page
HIGH_VALUE = {"village", "museum", "attraction"}
places = []
for pid, e in enr.items():
    if e["new_source_url"].strip():
        continue  # already sourced deterministically
    m = meta[pid]
    if m["type"] not in HIGH_VALUE:
        continue
    places.append({
        "id": pid,
        "name_he": m["name_he"],
        "name_en": m["name_en"],
        "type": m["type"],
        "lat": round(float(m["lat"]), 5),
        "lon": round(float(m["lon"]), 5),
    })

print(f"unsourceable places to research: {len(places)}")

CHUNK = 8
js = f'''export const meta = {{
  name: 'source-places',
  description: 'Web-research + verify a specific source URL for each unsourceable Israeli place',
  phases: [{{ title: 'Research' }}],
}}

const PLACES = {json.dumps(places, ensure_ascii=False)};
const CHUNK = {CHUNK};

const SCHEMA = {{
  type: 'object',
  properties: {{
    results: {{
      type: 'array',
      items: {{
        type: 'object',
        properties: {{
          id: {{ type: 'string' }},
          found: {{ type: 'boolean' }},
          url: {{ type: 'string' }},
          source_type: {{ type: 'string' }},
          confidence: {{ type: 'string', enum: ['high', 'medium', 'low', 'none'] }},
          reason: {{ type: 'string' }},
        }},
        required: ['id', 'found', 'url', 'confidence'],
      }},
    }},
  }},
  required: ['results'],
}};

const chunks = [];
for (let i = 0; i < PLACES.length; i += CHUNK) chunks.push(PLACES.slice(i, i + CHUNK));
log(`${{PLACES.length}} places, ${{chunks.length}} chunks of ${{CHUNK}}`);

function buildPrompt(chunk) {{
  const list = chunk.map(p =>
    `- id=${{p.id}} | ${{p.name_he}} (${{p.name_en}}) | type=${{p.type}} | coords=${{p.lat}},${{p.lon}}`
  ).join('\\n');
  return [
    'You source places in ISRAEL for a geography game. For EACH place below, find ONE specific,',
    'authoritative web page that describes THAT EXACT place (matching its coordinates/region), and verify it.',
    '',
    'Places:',
    list,
    '',
    'How:',
    '- Use WebSearch (try the Hebrew name + "ישראל", and the English name). You may WebFetch the top candidate to confirm.',
    '- The page MUST be about THIS specific place at ~these coordinates — NOT a different place with a similar name,',
    '  NOT a nearby different feature, NOT a generic category / map-search / aggregator page.',
    '- Prefer: official site, parks.org.il (רשות הטבע והגנים), inature.info, gov.il, an established Israeli',
    '  hiking/travel guide, or a Wikipedia article (any language) that is THIS place.',
    '- If you cannot CONFIDENTLY confirm a specific page, set found=false. A wrong link is worse than none — default to rejecting.',
    '- confidence: high = you verified (read the page) it is this exact place; medium = strong match, not page-verified;',
    '  low/none = not found.',
    '',
    `Return one entry per id for ALL ${{chunk.length}} places.`,
  ].join('\\n');
}}

const out = await pipeline(
  chunks,
  (chunk, _orig, idx) => agent(buildPrompt(chunk), {{
    label: `research:${{idx}}`, phase: 'Research', schema: SCHEMA, agentType: 'general-purpose',
  }}),
);

const all = out.filter(Boolean).flatMap(r => (r && r.results) || []);
const kept = all.filter(r => r.found && r.url && (r.confidence === 'high' || r.confidence === 'medium'));
log(`verified sources found: ${{kept.length}} / ${{PLACES.length}}`);
return {{ total: PLACES.length, researched: all.length, found: kept.length, matches: kept }};
'''

(ROOT / "tools" / "source_workflow.js").write_text(js, encoding="utf-8")
print("wrote tools/source_workflow.js")
