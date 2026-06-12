"""Profile data/places.csv: counts, source-url hosts, ambiguous names."""
import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

CSV = Path(__file__).parent.parent / "data" / "places.csv"

rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
n = len(rows)
print(f"total rows: {n}\n")

# type breakdown
print("by type:", dict(Counter(r["type"] for r in rows)))

# source_url host breakdown
def host(u):
    if not u:
        return "(empty)"
    try:
        h = urlparse(u).netloc
        return h or "(bad)"
    except Exception:
        return "(bad)"

hosts = Counter(host(r.get("source_url", "")) for r in rows)
print("\nsource_url hosts (top 15):")
for h, c in hosts.most_common(15):
    print(f"  {c:5d}  {h}")

# wikidata presence
wd = sum(1 for r in rows if r.get("wikidata", "").strip())
print(f"\nhave wikidata Q-id: {wd}/{n}")
img = sum(1 for r in rows if r.get("image_url", "").strip())
print(f"have image_url:      {img}/{n}")
desc = sum(1 for r in rows if r.get("description", "").strip())
print(f"have description:    {desc}/{n}")

# duplicate Hebrew names = ambiguity
name_counts = Counter(r["name_he"].strip() for r in rows)
dup_names = {k: v for k, v in name_counts.items() if v > 1}
dup_rows = sum(v for v in dup_names.values())
print(f"\nambiguity: {len(dup_names)} distinct names appear >1x, "
      f"covering {dup_rows} rows ({100*dup_rows/n:.1f}%)")
print("top duplicated names:")
for name, c in Counter(dup_names).most_common(25):
    print(f"  {c:3d}  {name}")

# generic memorial / institutional keywords (player can't disambiguate)
GENERIC = ["יד לבנים", "אנדרטה", "אנדרטת", "בית העלמין", "בית הכנסת",
           "אתר הנצחה", "גן ציבורי", "מגדל מים", "תחנת רכבת", "ביה""ס",
           "בית ספר", "מועצה מקומית", "אולם ספורט", "בריכת", "גן משחקים"]
gen = [r for r in rows if any(g in r["name_he"] for g in GENERIC)]
print(f"\ngeneric-keyword names: {len(gen)} rows")
gk = Counter()
for r in gen:
    for g in GENERIC:
        if g in r["name_he"]:
            gk[g] += 1
for g, c in gk.most_common():
    print(f"  {c:4d}  {g}")
