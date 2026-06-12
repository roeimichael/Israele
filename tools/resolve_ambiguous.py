"""Resolve the drop_ambiguous tier: drop generic/unguessable names entirely;
for ×2 duplicates of REAL places, keep the better-sourced copy (dedupe).
Writes the ambiguity drop-list (place ids) + a summary."""
import csv
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).parent.parent / ".preview-shots"
rows = list(csv.DictReader((OUT / "places_classified.csv").open(encoding="utf-8")))

GENERIC_KW = ["יד לבנים", "אנדרטה", "אנדרטת", "אתר הנצחה", "מערת קבורה",
              "טחנת קמח", "קולומבריום", "בית הכנסת", "בית העלמין",
              "ספריית שביל ישראל", "מגדל מים", "בריכת", "גן ציבורי"]

amb = [r for r in rows if r["_tier"] == "drop_ambiguous"]
by_name = defaultdict(list)
for r in amb:
    by_name[r["name_he"].strip()].append(r)


def src_rank(r):
    # prefer a real wikipedia article, then higher importance
    wp = 1 if "wikipedia.org" in r.get("source_url", "") and "_shared" not in r.get("_reason", "") else 0
    return (wp, float(r.get("importance", 0) or 0))


drop_ids, dedupe_keep = [], []
for name, group in by_name.items():
    generic = any(k in name for k in GENERIC_KW) or len(group) >= 3
    if generic:
        drop_ids += [r["id"] for r in group]          # drop every copy
    else:
        # real ×2 — keep the best-sourced, drop the rest
        best = max(group, key=src_rank)
        dedupe_keep.append(best)
        drop_ids += [r["id"] for r in group if r["id"] != best["id"]]

(OUT / "drop_ambiguous_ids.txt").write_text("\n".join(drop_ids), encoding="utf-8")

lines = [f"ambiguous rows: {len(amb)}  (distinct names: {len(by_name)})",
         f"  dropped entirely (generic / >=3): {sum(1 for n,g in by_name.items() if any(k in n for k in GENERIC_KW) or len(g)>=3)} names",
         f"  deduped (real x2, kept 1):        {len(dedupe_keep)} names",
         f"TOTAL ids to drop (ambiguity): {len(drop_ids)}",
         "",
         "kept-by-dedupe (real places, one copy):"]
for r in sorted(dedupe_keep, key=lambda r: r["name_he"]):
    lines.append(f"  {r['name_he']}  ({'wiki' if 'wikipedia' in r.get('source_url','') else 'google'})")
(OUT / "ambiguous_summary.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"ambiguity: drop {len(drop_ids)} ids, dedupe-kept {len(dedupe_keep)} names")
