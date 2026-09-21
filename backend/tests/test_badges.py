import uuid
from datetime import date, timedelta

from backend import supa as supa_module

LANDMARK = 278469922    # museum -> landmark, 2.5x (see test_puzzle_build.py)
CITY = 27132996         # Eilat, city


def _fake_select(games=None, guesses=None, players=None):
    """Stand-in for supa.select, dispatching by table name. Filters are
    ignored — each test crafts exactly the rows the handler should see."""
    games = games or []
    guesses = guesses or []
    players = players if players is not None else []

    def _select(table, **params):
        if table == "games":
            return games
        if table == "guesses":
            return guesses
        if table == "players":
            return players
        raise AssertionError(f"unexpected table {table!r}")
    return _select


def test_badges_no_games_returns_all_false(client, monkeypatch):
    monkeypatch.setattr(supa_module, "select", _fake_select())
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.status_code == 200
    body = r.json()
    assert body["max_streak"] == 0
    assert body["badges"] == {
        "streak_7": False, "streak_30": False, "streak_100": False,
        "perfect_round": False, "category_mastery": False,
    }


def test_badges_perfect_round_true_on_any_bullseye(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [{"game_id": 1, "place_id": CITY, "base_score": 100}]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["perfect_round"] is True


def test_badges_perfect_round_false_when_no_bullseye(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [{"game_id": 1, "place_id": CITY, "base_score": 64}]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["perfect_round"] is False


def test_badges_category_mastery_requires_two_maxed_landmarks_same_game(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [
        {"game_id": 1, "place_id": LANDMARK, "base_score": 100},
        {"game_id": 1, "place_id": LANDMARK, "base_score": 100},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["category_mastery"] is True


def test_badges_category_mastery_false_with_only_one_landmark_guess(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [{"game_id": 1, "place_id": LANDMARK, "base_score": 100}]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["category_mastery"] is False


def test_badges_category_mastery_false_when_a_landmark_guess_missed(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [
        {"game_id": 1, "place_id": LANDMARK, "base_score": 100},
        {"game_id": 1, "place_id": LANDMARK, "base_score": 90},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["category_mastery"] is False


def test_badges_category_mastery_ignores_non_landmark_categories(client, monkeypatch):
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [
        {"game_id": 1, "place_id": CITY, "base_score": 100},
        {"game_id": 1, "place_id": CITY, "base_score": 100},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.json()["badges"]["category_mastery"] is False


def test_badges_category_mastery_handles_stale_place_id(client, monkeypatch):
    """Defensive `or {}` in main.py: a place_id no longer in places.csv must
    not 500, just fail to count toward mastery."""
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    guesses = [
        {"game_id": 1, "place_id": 999999999, "base_score": 100},
        {"game_id": 1, "place_id": 999999999, "base_score": 100},
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, guesses))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.status_code == 200
    assert r.json()["badges"]["category_mastery"] is False


def test_badges_streak_7_true_on_seven_consecutive_days(client, monkeypatch):
    start = date(2026, 1, 1)
    games = [
        {"id": i, "puzzle_date": (start + timedelta(days=i)).isoformat()}
        for i in range(7)
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    body = r.json()
    assert body["max_streak"] == 7
    assert body["badges"]["streak_7"] is True
    assert body["badges"]["streak_30"] is False
    assert body["badges"]["streak_100"] is False


def test_badges_streak_ignores_gaps(client, monkeypatch):
    """Six consecutive days plus one isolated day elsewhere must not count
    as a 7-day streak."""
    start = date(2026, 1, 1)
    games = [
        {"id": i, "puzzle_date": (start + timedelta(days=i)).isoformat()}
        for i in range(6)
    ]
    games.append({"id": 99, "puzzle_date": (start + timedelta(days=30)).isoformat()})
    monkeypatch.setattr(supa_module, "select", _fake_select(games))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    body = r.json()
    assert body["max_streak"] == 6
    assert body["badges"]["streak_7"] is False


def test_badges_streak_counts_longest_ever_run_not_just_current(client, monkeypatch):
    """A 30-day run far in the past still flips streak_30, even though the
    live streak (computed by /api/me/stats) would be irrelevant here."""
    start = date(2026, 1, 1)
    games = [
        {"id": i, "puzzle_date": (start + timedelta(days=i)).isoformat()}
        for i in range(30)
    ]
    monkeypatch.setattr(supa_module, "select", _fake_select(games))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    body = r.json()
    assert body["max_streak"] == 30
    assert body["badges"]["streak_30"] is True
    assert body["badges"]["streak_100"] is False


def test_badges_denies_access_to_other_players_claimed_account(client, monkeypatch):
    """Claimed account (auth_user_id set) with no/foreign JWT -> 403, same
    guard as /api/me/stats. games/guesses must not even be queried."""
    def _select(table, **params):
        if table == "players":
            return [{"auth_user_id": "owner-uuid"}]
        raise AssertionError(f"should not query {table!r} once access is denied")
    monkeypatch.setattr(supa_module, "select", _select)
    r = client.get("/api/me/badges", params={"player_id": str(uuid.uuid4())})
    assert r.status_code == 403


def test_badges_allows_guest_player_with_no_players_row(client, monkeypatch):
    """Unknown player_id (never inserted into players, e.g. brand-new guest)
    stays open, matching /api/me/stats behavior."""
    games = [{"id": 1, "puzzle_date": "2026-06-01"}]
    monkeypatch.setattr(supa_module, "select", _fake_select(games, players=[]))
    r = client.get("/api/me/badges", params={"player_id": "p1"})
    assert r.status_code == 200
