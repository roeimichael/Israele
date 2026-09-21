from datetime import timedelta

from backend import places
from backend.main import EPOCH, _il_today_iso

EILAT = 27132996        # city, 1.0x
JERUSALEM = 29090735    # city, 1.0x

TODAY_ISO = _il_today_iso()
# A day just after EPOCH so it's always a valid archive day (< today),
# regardless of what real-world date the suite happens to run on.
ARCHIVE_DAY = (EPOCH + timedelta(days=7)).isoformat()


def test_guess_exact_location_is_bullseye(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    p = places.get(EILAT)
    r = client.post(
        f"/api/puzzle/{ARCHIVE_DAY}/guess",
        json={"player_id": "p1", "round_idx": 0, "lat": p["lat"], "lon": p["lon"]},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["distance_km"] == 0.0
    assert body["base_score"] == 100
    assert body["round_score"] == 100  # city multiplier is 1.0x
    assert body["is_last"] is False
    assert body["archive"] is True
    assert body["name_en"] == p["name_en"]


def test_guess_far_away_scores_zero(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    # Somewhere far outside Israel entirely.
    r = client.post(
        f"/api/puzzle/{ARCHIVE_DAY}/guess",
        json={"player_id": "p1", "round_idx": 0, "lat": 0.0, "lon": 0.0},
    )
    assert r.status_code == 200
    assert r.json()["base_score"] == 0
    assert r.json()["round_score"] == 0


def test_guess_last_round_flag(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    p = places.get(JERUSALEM)
    r = client.post(
        f"/api/puzzle/{ARCHIVE_DAY}/guess",
        json={"player_id": "p1", "round_idx": 1, "lat": p["lat"], "lon": p["lon"]},
    )
    assert r.status_code == 200
    assert r.json()["is_last"] is True


def test_guess_rejects_out_of_range_round_idx(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.post(
        f"/api/puzzle/{ARCHIVE_DAY}/guess",
        json={"player_id": "p1", "round_idx": 2, "lat": 31.0, "lon": 35.0},
    )
    assert r.status_code == 400


def test_guess_rejects_negative_round_idx(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.post(
        f"/api/puzzle/{ARCHIVE_DAY}/guess",
        json={"player_id": "p1", "round_idx": -1, "lat": 31.0, "lon": 35.0},
    )
    assert r.status_code == 400


def test_guess_rejects_today_or_future(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.post(
        f"/api/puzzle/{TODAY_ISO}/guess",
        json={"player_id": "p1", "round_idx": 0, "lat": 31.0, "lon": 35.0},
    )
    assert r.status_code == 400


def test_guess_rejects_before_epoch(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    before_epoch = (EPOCH - timedelta(days=1)).isoformat()
    r = client.post(
        f"/api/puzzle/{before_epoch}/guess",
        json={"player_id": "p1", "round_idx": 0, "lat": 31.0, "lon": 35.0},
    )
    assert r.status_code == 400


def test_guess_rejects_malformed_date(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.post(
        "/api/puzzle/not-a-date/guess",
        json={"player_id": "p1", "round_idx": 0, "lat": 31.0, "lon": 35.0},
    )
    assert r.status_code == 400


def test_guess_rejects_missing_fields(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.post(f"/api/puzzle/{ARCHIVE_DAY}/guess", json={"round_idx": 0})
    assert r.status_code == 422  # pydantic validation error


def test_archive_puzzle_get_matches_guess_picks(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.get(f"/api/puzzle/{ARCHIVE_DAY}")
    assert r.status_code == 200
    body = r.json()
    assert len(body["rounds"]) == 2
    assert body["rounds"][0]["name_en"] == places.get(EILAT)["name_en"]


def test_archive_puzzle_get_rejects_today_or_future(client, daily_picks):
    daily_picks([EILAT, JERUSALEM])
    r = client.get(f"/api/puzzle/{TODAY_ISO}")
    assert r.status_code == 400
