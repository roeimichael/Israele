"""High-PRECISION enrichment of the 'sourceless' places. Only accepts a
source we can trust is about THIS specific place:
  - wikidata official website (P856), or
  - wikidata sitelink (he/en/ar) — the entity's own article, or
  - Wikipedia geosearch hit whose TITLE matches the place name (<=300m).
Blind nearest-article matches are rejected (they're usually a different
nearby feature). Cached + resumable. Writes results to .preview-shots/.
"""
import csv
import json
import re
from pathlib import Path

import httpx

ROOT = Path(__file__).parent.parent
OUT = ROOT / ".preview-shots"
CACHE_PATH = ROOT / "data" / "raw" / "enrich_cache.json"
UA = "IsraelE-dev-enrichment/1.0 (roeym111@gmail.com)"
cli = httpx.Client(headers={"User-Agent": UA}, timeout=20, follow_redirects=True)

CACHE = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else {}
PREFIXES = ["הר ", "תל ", "חורבת ", "חירבת ", "נחל ", "מצפה ", "תצפית ", "עין ",
            "ח' ", "ח'", "מצד ", "גבעת ", "כפר ", "אתר ", "ביר ", "ח׳ "]


def norm(s):
    s = s.strip()
    for p in PREFIXES:
        if s.startswith(p):
            s = s[len(p):]
    return re.sub(r"[\s\(\)\"'׳״\-]", "", s)


def name_match(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    return na == nb or (len(na) >= 3 and (na in nb or nb in na))


def get(url, params=None):
    r = cli.get(url, params=params)
    r.raise_for_status()
    return r.json()


def enrich(r):
    """Return (source_url, how) or (None, reason). Cached by place id."""
    pid = r["id"]
    if pid in CACHE:
        return tuple(CACHE[pid])
    name, lat, lon, qid = r["name_he"], r["lat"], r["lon"], r.get("wikidata", "").strip()
    result = (None, "none")
    try:
        if qid:
            ent = get(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")["entities"][qid]
            site = ent.get("claims", {}).get("P856")
            if site:
                result = (site[0]["mainsnak"]["datavalue"]["value"], "wd:official")
            else:
                sl = ent.get("sitelinks", {})
                for wiki, lang in [("hewiki", "he"), ("enwiki", "en"), ("arwiki", "ar")]:
                    if wiki in sl:
                        t = sl[wiki]["title"].replace(" ", "_")
                        result = (f"https://{lang}.wikipedia.org/wiki/{t}", f"wd:{lang}wiki")
                        break
        if result[0] is None:
            for lang in ("he", "en"):
                hits = get(f"https://{lang}.wikipedia.org/w/api.php", {
                    "action": "query", "list": "geosearch", "format": "json",
                    "gscoord": f"{lat}|{lon}", "gsradius": 300, "gslimit": 5,
                }).get("query", {}).get("geosearch", [])
                m = next((h for h in hits if name_match(name, h["title"])), None)
                if m:
                    t = m["title"].replace(" ", "_")
                    result = (f"https://{lang}.wikipedia.org/wiki/{t}", f"geo:{lang} {int(m['dist'])}m")
                    break
    except Exception as e:
        result = (None, "err:" + str(e)[:30])
    CACHE[pid] = list(result)
    return result


def main():
    rows = list(csv.DictReader((OUT / "places_classified.csv").open(encoding="utf-8")))
    sl = [r for r in rows if r["_tier"] == "sourceless"]
    sourced = 0
    enriched_rows = []
    for i, r in enumerate(sl):
        url, how = enrich(r)
        if url:
            sourced += 1
        enriched_rows.append({"id": r["id"], "name_he": r["name_he"], "type": r["type"],
                              "wikidata": r.get("wikidata", ""), "new_source_url": url or "",
                              "how": how})
        if i % 100 == 0:
            CACHE_PATH.write_text(json.dumps(CACHE, ensure_ascii=False), encoding="utf-8")
            print(f"  {i}/{len(sl)}  sourced={sourced}", flush=True)
    CACHE_PATH.write_text(json.dumps(CACHE, ensure_ascii=False), encoding="utf-8")
    with (OUT / "sourceless_enriched.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(enriched_rows[0].keys()))
        w.writeheader()
        w.writerows(enriched_rows)
    from collections import Counter
    hows = Counter(e["how"].split(" ")[0].split(":")[0] for e in enriched_rows)
    print(f"\nDONE  sourced {sourced}/{len(sl)}  ({100*sourced/len(sl):.0f}%)")
    print("by method:", dict(hows))


if __name__ == "__main__":
    main()
