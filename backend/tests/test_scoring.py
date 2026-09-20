import pytest

from backend.scoring import base_score, haversine_km

# Jerusalem <-> Tel Aviv, straight-line distance is well known (~54 km).
JERUSALEM = (31.7788472, 35.2257856)
TEL_AVIV = (32.0852999, 34.7817676)


def test_haversine_same_point_is_zero():
    assert haversine_km(31.5, 34.8, 31.5, 34.8) == pytest.approx(0.0, abs=1e-9)


def test_haversine_is_symmetric():
    a = haversine_km(*JERUSALEM, *TEL_AVIV)
    b = haversine_km(*TEL_AVIV, *JERUSALEM)
    assert a == pytest.approx(b)


def test_haversine_known_distance():
    dist = haversine_km(*JERUSALEM, *TEL_AVIV)
    assert dist == pytest.approx(54.0, abs=3.0)


def test_base_score_bullseye_clamped_to_100():
    assert base_score(0.0) == 100
    assert base_score(0.99) == 100


@pytest.mark.parametrize(
    "distance_km,expected",
    [
        (0.0, 100),
        (50.0, 64),
        (100.0, 36),
        (200.0, 4),
        (250.0, 0),
    ],
)
def test_base_score_quadratic_falloff(distance_km, expected):
    assert base_score(distance_km) == expected


def test_base_score_clamped_at_zero_beyond_zero_at_km():
    assert base_score(400.0) == 0
    assert base_score(10_000.0) == 0


def test_base_score_is_monotonically_decreasing():
    scores = [base_score(d) for d in range(0, 260, 10)]
    assert all(a >= b for a, b in zip(scores, scores[1:]))
