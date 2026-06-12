import base64
import hashlib
import json
import logging
import os
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import places, supa
from .scoring import base_score, haversine_km

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("israelle")

app = FastAPI(title="israelle")

# Comma-separated origins, e.g. "https://israel-e.com,https://*.vercel.app".
_origins_raw = os.environ.get("ALLOWED_ORIGINS", "").strip()
if not _origins_raw:
    log.warning("ALLOWED_ORIGINS unset — falling back to '*'. Set this on Railway in prod.")
    _origins = ["*"]
else:
    _origins = [o.strip() for o in _origins_raw.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    max_age=86400,
)

ROOT = Path(__file__).parent.parent
FRONTEND = ROOT / "frontend"
DOCS = ROOT / "docs"
DATA = ROOT / "data"
SERVE_FRONTEND = os.environ.get("SERVE_FRONTEND", "0") == "1"

_border_path = DATA / "israel.geojson"
if not _border_path.exists():
    raise RuntimeError(f"missing required data file: {_border_path}")
ISRAEL_BORDER = json.loads(_border_path.read_text(encoding="utf-8"))

IL_TZ = ZoneInfo("Asia/Jerusalem")
# Day #1 of IsraelE (public launch). Puzzle numbers are (today - EPOCH).days + 1.
EPOCH = date(2026, 6, 14)


def _il_today_iso() -> str:
    return datetime.now(IL_TZ).date().isoformat()


def _day_number(d_iso: str) -> int:
    return (date.fromisoformat(d_iso) - EPOCH).days + 1


def _jwt(request: Request) -> str | None:
    h = request.headers.get("Authorization", "")
    return h[7:].strip() if h.startswith("Bearer ") else None


# Daily picks cache: pins pick_or_create_daily's result for the day so
# /api/today and /api/today/guess always see identical round_idx → place_id.
# If the RPC ever returns a different order between calls, this prevents
# silent score/place mismatches. Self-heals at midnight (new date key).
_PICKS_CACHE: dict[str, list[int]] = {}


def _daily_picks(d: str) -> list[int]:
    hit = _PICKS_CACHE.get(d)
    if hit is not None:
        return hit
    raw = supa.rpc("pick_or_create_daily", {"p_date": d})
    picks = [int(pid) for pid in raw]
    _PICKS_CACHE[d] = picks
    # Bound memory; keys are date strings so this stays tiny.
    if len(_PICKS_CACHE) > 7:
        for k in sorted(_PICKS_CACHE)[:-7]:
            _PICKS_CACHE.pop(k, None)
    return picks


def _rank_and_percentile(date_iso: str, my_score: int) -> dict:
    """Caller's rank, percentile beaten, and average across all of today's scores.
    One DB call; payload is one int per game (cheap)."""
    rows = supa.select("games", select="total_score", puzzle_date=f"eq.{date_iso}")
    scores = [r["total_score"] for r in rows if r.get("total_score") is not None]
    total = len(scores)
    if total == 0:
        return {"rank": 1, "percentile": 100, "total_players": 1, "average_score": my_score}
    higher = sum(1 for s in scores if s > my_score)
    beaten = sum(1 for s in scores if s < my_score)
    return {
        "rank": higher + 1,
        "percentile": round(100 * beaten / total),
        "total_players": total,
        "average_score": round(sum(scores) / total),
    }


def _current_streak(player_ids: list[str], today_iso: str) -> int:
    """Count consecutive days ending today (or yesterday) with at least one game.
    Accepts multiple player_ids so signed-in users with a prior guest history
    get credit for the whole chain."""
    from datetime import timedelta
    if not player_ids:
        return 0
    ids_csv = ",".join(player_ids)
    rows = supa.select(
        "games",
        select="puzzle_date",
        player_id=f"in.({ids_csv})",
        order="puzzle_date.desc",
        limit=400,
    )
    if not rows:
        return 0
    dates = {r["puzzle_date"] for r in rows}
    cur = date.fromisoformat(today_iso)
    # If today not yet logged, count from yesterday (still a live streak).
    if cur.isoformat() not in dates:
        cur = cur - timedelta(days=1)
    n = 0
    while cur.isoformat() in dates:
        n += 1
        cur -= timedelta(days=1)
    return n


def _require_player_access(player_id: str, request: Request) -> None:
    """Reject reads of another user's data. Guests (auth_user_id NULL) stay
    open — same risk surface as before for that bucket, but signed-in users
    are now protected from horizontal access by UUID guessing/leaking."""
    rows = supa.select("players", select="auth_user_id", id=f"eq.{player_id}")
    if not rows:
        return  # unknown player_id — nothing to leak yet
    owner = rows[0].get("auth_user_id")
    if not owner:
        return  # guest row, no auth attached
    jwt = _jwt(request)
    caller = supa.verify_jwt(jwt) if jwt else None
    if caller != owner:
        raise HTTPException(403, "not your data")


class GuessIn(BaseModel):
    player_id: str
    name: str | None = None
    round_idx: int
    lat: float
    lon: float


def _tile_hash(d: str, coords: list[tuple[float, float]]) -> str:
    """Pack today's six (lat, lon) pairs into an obfuscated string the client
    can recover synchronously, so the reveal animation can start the instant
    the user taps — without waiting for the network round-trip on the score
    endpoint. Server still owns scoring; this is purely a UX shortcut."""
    payload = json.dumps([[round(la, 6), round(lo, 6)] for la, lo in coords], separators=(",", ":")).encode("utf-8")
    key = hashlib.sha256(f"ils-puzzle-{d}".encode("utf-8")).digest()
    cipher = bytes(b ^ key[i % len(key)] for i, b in enumerate(payload))
    return base64.b64encode(cipher).decode("ascii")


# ─── static + map data ───────────────────────────────────────────────────────


@app.get("/api/israel-border")
def israel_border():
    return ISRAEL_BORDER


@app.get("/api/healthz")
def healthz():
    """Lightweight ping. Used by Railway's healthcheck so the container stays
    warm + by uptime monitors. Does NOT hit Supabase to keep it cheap."""
    return {"ok": True}


@app.on_event("startup")
def _warmup() -> None:
    """Open the Supabase HTTP client + do a tiny no-op query so the first user
    request after deploy doesn't eat the TCP/TLS handshake cost (~1-2s)."""
    try:
        supa._c()  # initialize httpx.Client + connection pool
        # Touch one cheap row so DNS, TLS, and PostgREST routing are all warm.
        supa.select("places", select="id", limit=1)
        log.info("supabase warmup ok")
    except Exception as e:
        log.warning("supabase warmup failed: %s", e)


# ─── daily puzzle ────────────────────────────────────────────────────────────


def _build_puzzle(d: str) -> dict:
    place_ids = _daily_picks(d)
    rounds = []
    coords: list[tuple[float, float]] = []
    for ix, pid in enumerate(place_ids):
        p = places.get(int(pid))
        if not p:
            raise HTTPException(500, f"missing place id {pid} in local CSV")
        rounds.append({
            "round_idx": ix,
            "name_he": p["name_he"],
            "name_en": p["name_en"],
            "type": p["type"],
            "category": p["category"],
            "multiplier": p["multiplier"],
        })
        coords.append((p["lat"], p["lon"]))
    return {
        "date": d,
        "day_number": _day_number(d),
        "rounds": rounds,
        "tile_hash": _tile_hash(d, coords),
    }


@app.get("/api/today")
def today():
    return _build_puzzle(_il_today_iso())


@app.get("/api/puzzle/{d}")
def puzzle_day(d: str):
    """Archive: replay any past day. Read-only, no DB writes."""
    try:
        target = date.fromisoformat(d)
    except ValueError:
        raise HTTPException(400, "bad date format (expected YYYY-MM-DD)")
    today_d = date.fromisoformat(_il_today_iso())
    if target >= today_d:
        raise HTTPException(400, "use /api/today for today's puzzle")
    if target < EPOCH:
        raise HTTPException(400, f"archive begins {EPOCH.isoformat()}")
    return _build_puzzle(d)


@app.post("/api/puzzle/{d}/guess")
def puzzle_guess(d: str, body: GuessIn):
    """Stateless score for an archive guess. No leaderboard, no persistence."""
    try:
        target = date.fromisoformat(d)
    except ValueError:
        raise HTTPException(400, "bad date")
    today_d = date.fromisoformat(_il_today_iso())
    if target >= today_d:
        raise HTTPException(400, "use /api/today/guess")
    if target < EPOCH:
        raise HTTPException(400, "before epoch")
    place_ids = _daily_picks(d)
    if not (0 <= body.round_idx < len(place_ids)):
        raise HTTPException(400, "bad round_idx")
    place_id = place_ids[body.round_idx]
    p = places.get(place_id)
    if not p:
        raise HTTPException(500, "place missing")
    dist = haversine_km(body.lat, body.lon, p["lat"], p["lon"])
    base = base_score(dist)
    return {
        "distance_km": round(dist, 2),
        "base_score": base,
        "multiplier": p["multiplier"],
        "round_score": round(base * p["multiplier"]),
        "true_lat": p["lat"],
        "true_lon": p["lon"],
        "polygon": places.get_polygon(place_id),
        "round_idx": body.round_idx,
        "is_last": body.round_idx == len(place_ids) - 1,
        "name_he": p["name_he"],
        "name_en": p["name_en"],
        "description": p.get("description", ""),
        "image_url": p.get("image_url", ""),
        "source_url": p.get("source_url", ""),
        "archive": True,
    }


@app.get("/api/me/today")
def me_today(request: Request, hint: str | None = None):
    """Canonical 'have I played today?' lookup by Google identity.
    Cross-references all player rows linked to auth_user_id, returning the
    one with today's game (if any) so the client can rebind localStorage.

    `hint` is the caller's current localStorage player_id. When this auth
    account has no claimed player row yet AND the hint points to an
    unclaimed player row, we claim it — so a guest who played before
    signing in still gets their game attached to their account.
    """
    jwt = _jwt(request)
    auth_user_id = supa.verify_jwt(jwt) if jwt else None
    if not auth_user_id:
        raise HTTPException(401, "sign in required")
    d = _il_today_iso()
    players = supa.select("players", select="id,name", auth_user_id=f"eq.{auth_user_id}")
    if not players and hint:
        # No claimed player yet. Try to claim the guest row the client is on.
        # RLS players_update.USING accepts rows whose auth_user_id IS NULL.
        try:
            supa.update(
                "players",
                {"id": f"eq.{hint}", "auth_user_id": "is.null"},
                {"auth_user_id": auth_user_id},
                jwt=jwt,
            )
            players = supa.select("players", select="id,name", auth_user_id=f"eq.{auth_user_id}")
        except httpx.HTTPStatusError:
            pass
    if not players:
        return {"player_id": None, "name": None, "done": False, "guesses": [], "total_score": 0}
    ids = ",".join(p["id"] for p in players)
    games = supa.select(
        "games",
        select="id,player_id,total_score,completed_at",
        player_id=f"in.({ids})",
        puzzle_date=f"eq.{d}",
    )
    if not games:
        return {"player_id": players[0]["id"], "name": players[0]["name"],
                "done": False, "guesses": [], "total_score": 0}
    g = games[0]
    guesses = supa.select(
        "guesses",
        select="round_idx,place_id,distance_km,base_score,round_score,guess_lat,guess_lon",
        game_id=f"eq.{g['id']}",
        order="round_idx.asc",
    )
    for gs in guesses:
        p = places.get(int(gs["place_id"]))
        if p:
            gs["name_he"] = p["name_he"]
            gs["name_en"] = p["name_en"]
            gs["type"] = p["type"]
            gs["category"] = p["category"]
            gs["multiplier"] = p["multiplier"]
            gs["true_lat"] = p["lat"]
            gs["true_lon"] = p["lon"]
            gs["polygon"] = places.get_polygon(int(gs["place_id"]))
            gs["description"] = p.get("description", "")
            gs["image_url"] = p.get("image_url", "")
            gs["source_url"] = p.get("source_url", "")
    owner = next((pl for pl in players if pl["id"] == g["player_id"]), players[0])
    done = len(guesses) >= len(_daily_picks(d))
    payload = {
        "player_id": g["player_id"],
        "name": owner["name"],
        "total_score": g["total_score"],
        "guesses": guesses,
        "done": done,
    }
    if done:
        payload.update(_rank_and_percentile(d, g["total_score"]))
        payload["streak"] = _current_streak([p["id"] for p in players], d)
    return payload


@app.get("/api/today/me")
def today_me(player_id: str, request: Request):
    _require_player_access(player_id, request)
    date = _il_today_iso()
    games = supa.select(
        "games",
        select="id,total_score,completed_at",
        player_id=f"eq.{player_id}",
        puzzle_date=f"eq.{date}",
    )
    if not games:
        return {"played_rounds": [], "total_score": 0, "done": False}
    g = games[0]
    guesses = supa.select(
        "guesses",
        select="round_idx,place_id,distance_km,base_score,round_score,guess_lat,guess_lon",
        game_id=f"eq.{g['id']}",
        order="round_idx.asc",
    )
    # enrich with hebrew name + true coords for reveal-rendering on resume
    for gs in guesses:
        p = places.get(int(gs["place_id"]))
        if p:
            gs["name_he"] = p["name_he"]
            gs["name_en"] = p["name_en"]
            gs["type"] = p["type"]
            gs["category"] = p["category"]
            gs["multiplier"] = p["multiplier"]
            gs["true_lat"] = p["lat"]
            gs["true_lon"] = p["lon"]
            gs["polygon"] = places.get_polygon(int(gs["place_id"]))
            gs["description"] = p.get("description", "")
            gs["image_url"] = p.get("image_url", "")
            gs["source_url"] = p.get("source_url", "")
    done = len(guesses) >= len(_daily_picks(date))
    payload = {
        "game_id": g["id"],
        "total_score": g["total_score"],
        "guesses": guesses,
        "done": done,
    }
    if done:
        payload.update(_rank_and_percentile(date, g["total_score"]))
        payload["streak"] = _current_streak([player_id], date)
    return payload



@app.post("/api/today/guess")
def today_guess(body: GuessIn, request: Request):
    date = _il_today_iso()
    place_ids = _daily_picks(date)
    if not (0 <= body.round_idx < len(place_ids)):
        raise HTTPException(400, "bad round_idx")
    place_id = place_ids[body.round_idx]
    p = places.get(place_id)
    if not p:
        raise HTTPException(500, "place missing locally")

    dist = haversine_km(body.lat, body.lon, p["lat"], p["lon"])
    base = base_score(dist)
    round_score = round(base * p["multiplier"])

    # Resolve auth (optional). When signed in, forward the user's JWT so RLS
    # sees auth.uid() = their id; anon writes still go through the publishable key.
    jwt = _jwt(request)
    auth_user_id = supa.verify_jwt(jwt or "")
    user_jwt = jwt if auth_user_id else None

    # 1) Upsert player. Ignore-duplicates so the row exists, then patch name/auth.
    try:
        row = {"id": body.player_id, "name": body.name or "אנונימי"}
        if auth_user_id:
            row["auth_user_id"] = auth_user_id
        supa.insert(
            "players", row,
            prefer="return=minimal,resolution=ignore-duplicates",
            jwt=user_jwt,
        )
    except httpx.HTTPStatusError:
        pass
    patch = {}
    if body.name:
        patch["name"] = body.name
    if auth_user_id:
        patch["auth_user_id"] = auth_user_id
    if patch:
        supa.update("players", {"id": f"eq.{body.player_id}"}, patch, jwt=user_jwt)

    # 2) Upsert game row (one per player per day).
    game_row = supa.upsert(
        "games",
        {"player_id": body.player_id, "puzzle_date": date, "total_score": 0},
        on_conflict="player_id,puzzle_date",
        jwt=user_jwt,
    )
    game_id = game_row[0]["id"]

    # 3) Insert guess (idempotent on (game_id, round_idx)).
    try:
        supa.insert(
            "guesses",
            {
                "game_id": game_id,
                "round_idx": body.round_idx,
                "place_id": place_id,
                "guess_lat": body.lat,
                "guess_lon": body.lon,
                "distance_km": round(dist, 2),
                "base_score": base,
                "round_score": round_score,
            },
            prefer="return=minimal",
            jwt=user_jwt,
        )
    except httpx.HTTPStatusError as e:
        if e.response is not None and "23505" in e.response.text:
            raise HTTPException(409, "round already played")
        raise

    # 4) Recompute total from rows (cheap; ≤6 rows).
    rows = supa.select("guesses", select="round_score", game_id=f"eq.{game_id}")
    total = sum(r["round_score"] for r in rows)
    supa.update("games", {"id": f"eq.{game_id}"}, {"total_score": total}, jwt=user_jwt)

    # Compute rank + streak only on the last guess — wasted work on earlier rounds.
    rank_info = _rank_and_percentile(date, total) if body.round_idx == len(place_ids) - 1 else None
    if rank_info is not None:
        rank_info["streak"] = _current_streak([body.player_id], date)

    out = {
        "distance_km": round(dist, 2),
        "base_score": base,
        "multiplier": p["multiplier"],
        "round_score": round_score,
        "total_score": total,
        "true_lat": p["lat"],
        "true_lon": p["lon"],
        "polygon": places.get_polygon(place_id),
        "round_idx": body.round_idx,
        "is_last": body.round_idx == len(place_ids) - 1,
        "game_id": game_id,
        "name_he": p["name_he"],
        "name_en": p["name_en"],
        "description": p.get("description", ""),
        "image_url": p.get("image_url", ""),
        "source_url": p.get("source_url", ""),
    }
    if rank_info:
        out.update(rank_info)
    return out


# ─── history + leaderboard ───────────────────────────────────────────────────


@app.get("/api/me/history")
def history(request: Request):
    jwt = _jwt(request)
    auth_user_id = supa.verify_jwt(jwt) if jwt else None
    if not auth_user_id:
        raise HTTPException(401, "sign in to view history")
    players = supa.select("players", select="id,name", auth_user_id=f"eq.{auth_user_id}")
    if not players:
        return {"games": [], "player_name": None}
    ids = ",".join(p["id"] for p in players)
    games = supa.select(
        "games",
        select="id,puzzle_date,total_score,completed_at",
        player_id=f"in.({ids})",
        order="puzzle_date.desc",
        limit=60,
    )
    return {"games": games, "player_name": players[0]["name"]}


@app.get("/api/me/stats")
def my_stats(player_id: str, request: Request):
    """Returns games played, current streak, max streak, score histogram.
    Works anonymously for guest players; requires matching JWT for claimed ones."""
    _require_player_access(player_id, request)
    rows = supa.select(
        "games",
        select="puzzle_date,total_score",
        player_id=f"eq.{player_id}",
        order="puzzle_date.desc",
    )
    if not rows:
        return {"games_played": 0, "current_streak": 0, "max_streak": 0,
                "avg_score": 0, "best_score": 0, "histogram": [0]*5}

    dates = sorted({r["puzzle_date"] for r in rows}, reverse=True)
    scores = [r["total_score"] for r in rows]
    today_iso = _il_today_iso()
    # streaks
    from datetime import timedelta
    def streak_from(start_iso: str) -> int:
        cur = date.fromisoformat(start_iso)
        n = 0
        ds = set(date.fromisoformat(x) for x in dates)
        while cur in ds:
            n += 1
            cur -= timedelta(days=1)
        return n
    # current: start counting back from today (or yesterday if today not played)
    current = streak_from(today_iso)
    if current == 0:
        yest = (date.fromisoformat(today_iso) - timedelta(days=1)).isoformat()
        current = streak_from(yest)
    # max: longest consecutive run in dates set
    max_s = 0
    ds_set = set(date.fromisoformat(x) for x in dates)
    for d_ in ds_set:
        if (d_ - timedelta(days=1)) in ds_set:
            continue  # not a run start
        n = 0
        cur = d_
        while cur in ds_set:
            n += 1
            cur += timedelta(days=1)
        if n > max_s:
            max_s = n

    # 5-bucket histogram: 0-200, 200-400, 400-600, 600-800, 800-1000
    histogram = [0] * 5
    for s in scores:
        bucket = min(4, s // 200)
        histogram[bucket] += 1

    return {
        "games_played": len(rows),
        "current_streak": current,
        "max_streak": max_s,
        "avg_score": round(sum(scores) / len(scores)),
        "best_score": max(scores),
        "histogram": histogram,
    }


@app.get("/api/leaderboard")
def leaderboard(date: str | None = None, player_id: str | None = None):
    """Top 10 + caller's row when they're outside the top 10."""
    date = date or _il_today_iso()
    rows = supa.select(
        "games",
        select="player_id,total_score,completed_at,players(name)",
        puzzle_date=f"eq.{date}",
        order="total_score.desc",
    )

    def _name(r):
        return (r["players"]["name"] if r.get("players") and r["players"] else "אנונימי")

    top = []
    me_in_top = False
    for i, r in enumerate(rows[:10]):
        is_me = bool(player_id and r["player_id"] == player_id)
        if is_me:
            me_in_top = True
        top.append({
            "rank": i + 1,
            "name": _name(r),
            "score": r["total_score"],
            "completed_at": r["completed_at"],
            "is_me": is_me,
        })

    me = None
    if player_id and not me_in_top:
        for i, r in enumerate(rows):
            if r["player_id"] == player_id:
                me = {
                    "rank": i + 1,
                    "name": _name(r),
                    "score": r["total_score"],
                    "completed_at": r["completed_at"],
                    "is_me": True,
                }
                break

    return {"date": date, "top": top, "me": me, "total_players": len(rows)}


# ─── SEO: dynamic sitemap with all archive days ──────────────────────────────


@app.get("/sitemap.xml")
def sitemap():
    from fastapi.responses import Response
    base = "https://israel-e.com"
    today_d = date.fromisoformat(_il_today_iso())
    urls = [
        f"<url><loc>{base}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>",
        f"<url><loc>{base}/privacy</loc><priority>0.3</priority></url>",
        f"<url><loc>{base}/terms</loc><priority>0.3</priority></url>",
    ]
    cur = EPOCH
    from datetime import timedelta
    while cur < today_d:
        urls.append(f"<url><loc>{base}/?date={cur.isoformat()}</loc><priority>0.6</priority></url>")
        cur += timedelta(days=1)
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(urls) +
        "</urlset>"
    )
    return Response(content=body, media_type="application/xml")


# ─── tiny endpoint so frontend can find supabase client params ───────────────


@app.get("/api/config")
def config():
    # Publishable key is safe in the browser by design.
    return {"supabase_url": supa.URL, "supabase_key": supa.KEY}


# ─── static mounts + index ───────────────────────────────────────────────────
# Only mount frontend/docs locally (SERVE_FRONTEND=1). In prod, Vercel serves
# the SPA, so the backend doesn't need the frontend dir at all.


@app.middleware("http")
async def no_cache_static(request: Request, call_next):
    response = await call_next(request)
    path = request.url.path
    if path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
    elif path.startswith("/static/") or path == "/":
        response.headers["Cache-Control"] = "no-cache, must-revalidate"
    return response


if SERVE_FRONTEND and FRONTEND.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND)), name="static")
    if DOCS.exists():
        app.mount("/docs", StaticFiles(directory=str(DOCS)), name="docs")

    @app.get("/")
    def index():
        return FileResponse(FRONTEND / "index.html", headers={"Cache-Control": "no-cache, must-revalidate"})
else:
    log.info("frontend mount disabled (SERVE_FRONTEND=%s, exists=%s)", SERVE_FRONTEND, FRONTEND.exists())
