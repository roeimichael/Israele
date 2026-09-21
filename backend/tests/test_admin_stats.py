from datetime import date, timedelta

from backend import supa as supa_module
from backend.main import _il_today_iso

CITY = 27132996        # Eilat, category "city"
LANDMARK = 278469922   # museum, category "landmark"


def _fake_select(games=None, guesses=None):
    games = games or []
    guesses = guesses or []

    def _select(table, **params):
        if table == "games":
            return games
        if table == "guesses":
            return guesses
        raise AssertionError(f"unexpected table {table!r}")
    return _select


def test_admin_stats_missing_token_env_is_503(client, monkeypatch):
    """ADMIN_TOKEN not configured -> fail closed, not "any token works"."""
    monkeypatch.delenv("ADMIN_TOKEN", raising=False)
    r = client.get("/api/admin/stats", headers={"X-Admin-Token": "whatever"})
    assert r.status_code == 503


def test_admin_stats_wrong_token_is_401(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    r = client.get("/api/admin/stats", headers={"X-Admin-Token": "wrong-token"})
    assert r.status_code == 401


def test_admin_stats_missing_header_is_401(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    r = client.get("/api/admin/stats")
    assert r.status_code == 401


def test_admin_stats_correct_token_is_200(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    monkeypatch.setattr(supa_module, "select", _fake_select())
    r = client.get("/api/admin/stats", headers={"X-Admin-Token": "correct-token"})
    assert r.status_code == 200


def test_admin_stats_days_param_is_clamped(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    monkeypatch.setattr(supa_module, "select", _fake_select())
    headers = {"X-Admin-Token": "correct-token"}
    r_low = client.get("/api/admin/stats", params={"days": 0}, headers=headers)
    r_high = client.get("/api/admin/stats", params={"days": 999}, headers=headers)
    assert r_low.json()["window_days"] == 1
    assert r_high.json()["window_days"] == 90


def test_admin_stats_dau_and_retention_shape(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    today = date.fromisoformat(_il_today_iso())
    yesterday_iso = (today - timedelta(days=1)).isoformat()
    today_iso = today.isoformat()
    games = [
        {"player_id": "p1", "puzzle_date": yesterday_iso, "total_score": 100},
        {"player_id": "p2", "puzzle_date": yesterday_iso, "total_score": 200},
        {"player_id": "p1", "puzzle_date": today_iso, "total_score": 300},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games))
    r = client.get(
        "/api/admin/stats",
        params={"days": 2},
        headers={"X-Admin-Token": "correct-token"},
    )
    body = r.json()
    dau_by_date = {d["date"]: d["count"] for d in body["daily_active_players"]}
    assert dau_by_date[yesterday_iso] == 2
    assert dau_by_date[today_iso] == 1
    # today's retention: 1 of yesterday's 2 players returned
    ret = next(x for x in body["retention"] if x["date"] == today_iso)
    assert ret["prev_day_active"] == 2
    assert ret["returning_from_prev_day"] == 1
    assert ret["retention_pct"] == 50.0


def test_admin_stats_score_distribution(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    games = [
        {"player_id": "p1", "puzzle_date": "2026-06-01", "total_score": 50},
        {"player_id": "p2", "puzzle_date": "2026-06-01", "total_score": 850},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games))
    r = client.get(
        "/api/admin/stats",
        params={"days": 1},
        headers={"X-Admin-Token": "correct-token"},
    )
    dist = r.json()["score_distribution"]
    assert dist["count"] == 2
    assert dist["min"] == 50
    assert dist["max"] == 850
    assert dist["avg"] == 450
    assert dist["histogram"] == [1, 0, 0, 0, 1]


def test_admin_stats_category_accuracy_groups_by_place_category(client, monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "correct-token")
    guesses = [
        {"place_id": CITY, "distance_km": 0.0, "round_score": 100,
         "games": {"puzzle_date": "2026-06-01"}},
        {"place_id": LANDMARK, "distance_km": 10.0, "round_score": 50,
         "games": {"puzzle_date": "2026-06-01"}},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(guesses=guesses))
    r = client.get(
        "/api/admin/stats",
        params={"days": 1},
        headers={"X-Admin-Token": "correct-token"},
    )
    by_cat = {c["category"]: c for c in r.json()["category_accuracy"]}
    assert by_cat["city"]["guesses"] == 1
    assert by_cat["city"]["avg_distance_km"] == 0.0
    assert by_cat["landmark"]["guesses"] == 1
    assert by_cat["landmark"]["avg_round_score"] == 50
