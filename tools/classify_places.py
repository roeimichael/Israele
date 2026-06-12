"""Classify every place in data/places.csv into quality tiers, WITHOUT
modifying the source. Writes a review CSV + summary to .preview-shots/.

Tiers
  drop_ambiguous : name shared by >1 place OR source is a wikipedia article
                   reused across places OR a generic-feature keyword name.
                   The "יד לבנים" class — unguessable from the name.
  upgrade        : google-maps fallback link BUT has a wikidata Q-id we can
                   turn into a real he.wikipedia article (deterministic).
  sourceless     : google-maps fallback, no wikidata, no description — the
                   obscure tail with no page that explains the specific spot.
  keep           : a wikipedia article unique to this place + unique name.
"""
import csv
import json
from collections import Counter
from pathlib import Path
import urllib.parse as up

ROOT = Path(__file__).parent.parent
CSV = ROOT / "data" / "places.csv"
WD = json.loads((ROOT / "data" / "raw" / "wd_titles_cache.json").read_text(encoding="utf-8"))
OUT = ROOT / ".preview-shots"
OUT.mkdir(exist_ok=True)

GENERIC_KW = ["יד לבנים", "אנדרטה", "אנדרטת", "אתר הנצחה", "מערת קבורה",
              "טחנת קמח", "קולומבריום", "בית הכנסת", "בית העלמין",
              "ספריית שביל ישראל", "מגדל מים", "בריכת", "גן ציבורי"]

rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
name_counts = Counter(r["name_he"].strip() for r in rows)
wp_url_counts = Counter(r["source_url"] for r in rows if "wikipedia.org" in r.get("source_url", ""))


def is_google(r):
    return "google.com" in r.get("source_url", "")


def wiki_from_wd(qid):
    he = (WD.get(qid) or {}).get("he")
    if not he:
        return None
    return "https://he.wikipedia.org/wiki/" + up.quote(he.replace(" ", "_"))


def classify(r):
    name = r["name_he"].strip()
    url = r.get("source_url", "")
    qid = r.get("wikidata", "").strip()
    reasons = []
    if name_counts[name] > 1:
        reasons.append(f"dup_name×{name_counts[name]}")
    if "wikipedia.org" in url and wp_url_counts[url] > 1:
        reasons.append(f"shared_article×{wp_url_counts[url]}")
    if any(k in name for k in GENERIC_KW):
        reasons.append("generic_kw")
    if reasons:
        return "drop_ambiguous", ";".join(reasons), ""
    if is_google(r):
        up_url = wiki_from_wd(qid) if qid else None
        if up_url:
            return "upgrade", f"wikidata {qid}", up_url
        return "sourceless", "google fallback, no wikidata", ""
    return "keep", "", ""


tiers = Counter()
review = []
for r in rows:
    tier, reason, new_url = classify(r)
    tiers[tier] += 1
    review.append({**r, "_tier": tier, "_reason": reason, "_new_source_url": new_url})

# write review csv (all columns + verdict)
cols = list(rows[0].keys()) + ["_tier", "_reason", "_new_source_url"]
with (OUT / "places_classified.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(review)

# summary
lines = [f"total: {len(rows)}", ""]
for t in ["keep", "upgrade", "drop_ambiguous", "sourceless"]:
    lines.append(f"  {t:16s} {tiers[t]:5d}  ({100*tiers[t]/len(rows):.1f}%)")
lines.append("")
lines.append("drop_ambiguous breakdown (reason → rows):")
rc = Counter()
for r in review:
    if r["_tier"] == "drop_ambiguous":
        rc[r["_reason"].split(";")[0].split("×")[0]] += 1
for reason, c in rc.most_common():
    lines.append(f"  {c:4d}  {reason}")
lines.append("")
lines.append("sample drop_ambiguous names:")
seen = set()
for r in review:
    if r["_tier"] == "drop_ambiguous" and r["name_he"] not in seen:
        seen.add(r["name_he"])
        lines.append(f"  {r['name_he']}  ({r['_reason']})")
    if len(seen) >= 18:
        break
lines.append("")
lines.append("sample upgrades (google → wikipedia):")
n = 0
for r in review:
    if r["_tier"] == "upgrade":
        lines.append(f"  {r['name_he']}  →  {up.unquote(r['_new_source_url'])}")
        n += 1
    if n >= 6:
        break
(OUT / "classify_summary.txt").write_text("\n".join(lines), encoding="utf-8")
print("written: places_classified.csv + classify_summary.txt")
print("tiers:", dict(tiers))
