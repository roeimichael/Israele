"""Proof-of-concept: can we source 'sourceless' places by COORDINATES?
Tries, per place: wikidata official-site / sitelinks (if Q-id), then
he/en Wikipedia geosearch near its lat/lon. Sample only."""
import csv
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).parent.parent
UA = "IsraelE-dev-enrichment/1.0 (roeym111@gmail.com)"
cli = httpx.Client(headers={"User-Agent": UA}, timeout=20, follow_redirects=True)

rows = list(csv.DictReader((ROOT / ".preview-shots" / "places_classified.csv").open(encoding="utf-8")))
sourceless = [r for r in rows if r["_tier"] == "sourceless"]

N = int(sys.argv[1]) if len(sys.argv) > 1 else 15
# sample across the list, not just the head
step = max(1, len(sourceless) // N)
sample = sourceless[::step][:N]


def wikidata_site(qid):
    if not qid:
        return None
    try:
        r = cli.get(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
        ent = r.json()["entities"][qid]
        # P856 official website
        site = ent.get("claims", {}).get("P856")
        if site:
            url = site[0]["mainsnak"]["datavalue"]["value"]
            return ("official", url)
        sl = ent.get("sitelinks", {})
        for wiki, lang in [("hewiki", "he"), ("enwiki", "en"), ("arwiki", "ar")]:
            if wiki in sl:
                title = sl[wiki]["title"].replace(" ", "_")
                return (f"{lang}wiki", f"https://{lang}.wikipedia.org/wiki/{title}")
    except Exception as e:
        return ("err", str(e)[:40])
    return None


def geosearch(lat, lon, lang="he", radius=500):
    try:
        r = cli.get(f"https://{lang}.wikipedia.org/w/api.php", params={
            "action": "query", "list": "geosearch", "format": "json",
            "gscoord": f"{lat}|{lon}", "gsradius": radius, "gslimit": 3,
        })
        hits = r.json().get("query", {}).get("geosearch", [])
        if hits:
            h = hits[0]
            return (f"{lang}-geo {int(h['dist'])}m", h["title"])
    except Exception:
        return None
    return None


print(f"sampling {len(sample)} of {len(sourceless)} sourceless places\n")
found = 0
for r in sample:
    name, lat, lon, qid = r["name_he"], r["lat"], r["lon"], r.get("wikidata", "").strip()
    res = wikidata_site(qid) or geosearch(lat, lon, "he") or geosearch(lat, lon, "en")
    if res and res[0] != "err":
        found += 1
    print(f"  {name[:24]:24s} qid={qid or '-':10s} -> {res}")
print(f"\nsourced {found}/{len(sample)}  ({100*found/len(sample):.0f}%)")
