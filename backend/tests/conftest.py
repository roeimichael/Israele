import sys
from pathlib import Path

# repo root isn't on sys.path by default (mirrors api/index.py's own shim) —
# add it so `backend.*` imports resolve when pytest is run from anywhere.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pytest
from fastapi.testclient import TestClient

from backend import main as main_module
from backend import supa as supa_module


@pytest.fixture
def client():
    return TestClient(main_module.app)


@pytest.fixture
def daily_picks(monkeypatch):
    """Stub pick_or_create_daily so puzzle-build/guess tests don't touch Supabase.
    Returns a setter: call it with the place_ids a test wants for that day."""
    def _set(place_ids):
        main_module._PICKS_CACHE.clear()
        monkeypatch.setattr(supa_module, "rpc", lambda name, params: list(place_ids))
    return _set
