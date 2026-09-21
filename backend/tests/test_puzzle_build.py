from backend.main import EPOCH, _build_puzzle, _day_number

# Real ids from data/places.csv (see backend/places.py) so places.get()
# resolves without needing to fake the CSV.
EILAT = 27132996        # city
JERUSALEM = 29090735    # city
LANDMARK = 278469922    # museum -> landmark, 2.5x
VILLAGE = 278476860     # village -> settlement, 2.0x


def test_day_number_at_epoch_is_1():
    assert _day_number(EPOCH.isoformat()) == 1


def test_day_number_increments_per_day():
    assert _day_number("2026-06-15") == 2
    assert _day_number("2026-06-24") == 11


def test_day_number_before_epoch_is_not_positive():
    assert _day_number("2026-06-13") == 0
    assert _day_number("2026-01-01") < 0


def test_build_puzzle_shape_and_ordering(daily_picks):
    daily_picks([EILAT, JERUSALEM, LANDMARK])
    puzzle = _build_puzzle("2026-07-01")

    assert puzzle["date"] == "2026-07-01"
    assert puzzle["day_number"] == _day_number("2026-07-01")
    assert isinstance(puzzle["tile_hash"], str) and puzzle["tile_hash"]
    assert len(puzzle["rounds"]) == 3

    for ix, expected_id in enumerate([EILAT, JERUSALEM, LANDMARK]):
        r = puzzle["rounds"][ix]
        assert r["round_idx"] == ix
        assert r["name_en"]
        assert r["category"] in ("city", "settlement", "landmark")
        assert r["multiplier"] > 0


def test_build_puzzle_category_multipliers(daily_picks):
    daily_picks([EILAT, VILLAGE, LANDMARK])
    puzzle = _build_puzzle("2026-07-02")
    city_round, village_round, landmark_round = puzzle["rounds"]
    assert (city_round["category"], city_round["multiplier"]) == ("city", 1.0)
    assert (village_round["category"], village_round["multiplier"]) == ("settlement", 2.0)
    assert (landmark_round["category"], landmark_round["multiplier"]) == ("landmark", 2.5)


def test_build_puzzle_caches_picks_per_day(daily_picks, monkeypatch):
    daily_picks([EILAT])
    first = _build_puzzle("2026-07-03")

    # Even if the RPC would now return something else, the same day must
    # keep returning the picks it was first built with (_PICKS_CACHE).
    from backend import supa as supa_module
    monkeypatch.setattr(supa_module, "rpc", lambda name, params: [JERUSALEM])
    second = _build_puzzle("2026-07-03")

    assert first["rounds"][0]["name_en"] == second["rounds"][0]["name_en"]


def test_build_puzzle_different_days_get_independent_picks(daily_picks):
    daily_picks([EILAT])
    day_a = _build_puzzle("2026-07-04")
    daily_picks([JERUSALEM])
    day_b = _build_puzzle("2026-07-05")
    assert day_a["rounds"][0]["name_en"] != day_b["rounds"][0]["name_en"]
