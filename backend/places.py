import csv
import json
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "places.csv"
POLY_PATH = Path(__file__).parent.parent / "data" / "polygons.json"

POLYGONS: dict[str, dict] = (
    json.loads(POLY_PATH.read_text(encoding="utf-8")) if POLY_PATH.exists() else {}
)


def _load() -> dict[int, dict]:
    out: dict[int, dict] = {}
    with CSV_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[int(row["id"])] = {
                "id": int(row["id"]),
                "name_en": row["name_en"],
                "name_he": row["name_he"],
                "type": row["type"],
                "lat": float(row["lat"]),
                "lon": float(row["lon"]),
                "importance": float(row["importance"]),
                "description": row.get("description", ""),
                "image_url": row.get("image_url", ""),
                "source_url": row.get("source_url", ""),
            }
    return out


def _category(place_type: str) -> tuple[str, float]:
    """Max round score = base × mult. 5 rounds/day sum to 1000:
      1 × city       (1.0×) →  1 × 100 = 100
      2 × settlement (2.0×) →  2 × 200 = 400
      2 × landmark   (2.5×) →  2 × 250 = 500
                                       ───────
                                         1000
    The 1·2·2 composition is enforced by the pick_or_create_daily RPC;
    pre-switch archive days keep their stored 2·2·2 picks (max 1100), which
    the client renders honestly via a computed per-day max.
    """
    if place_type == "city":
        return ("city", 1.0)
    if place_type == "village":
        return ("settlement", 2.0)
    return ("landmark", 2.5)


PLACES: dict[int, dict] = _load()
for _p in PLACES.values():
    cat, mult = _category(_p["type"])
    _p["category"] = cat
    _p["multiplier"] = mult


def get(round_id: int) -> dict | None:
    return PLACES.get(round_id)


def get_polygon(round_id: int) -> dict | None:
    return POLYGONS.get(str(round_id))
