// ─── i18n ──────────────────────────────────────────────────────────────────
const STRINGS = {
  he: {
    site_title: "IsraelE — פאזל יומי של מקומות בישראל",
    site_desc: "פאזל יומי בסגנון וורדל לישראל. 5 מקומות. נקודה אחת על המפה. כמה אתם מכירים את הארץ?",
    splash_loading: "טוען",
    tagline: "כמה טוב אתם מכירים את ישראל?",
    tagline_sub: "5 מקומות חדשים בכל יום, אותו סט לכולם.",
    legend_cities: "עיר אחת",
    legend_settlements: "2 יישובים",
    legend_landmarks: "2 אתרים",
    game_total_hint_pre: "עד",
    game_total_hint_post: "נקודות",
    btn_signin_google: "התחברות עם Google",
    or_divider: "או",
    btn_play_guest: "התחל כאורח",
    btn_play: "התחל",
    guest_hint: "משחק כאורח לא ישמור היסטוריה ארוכת-טווח.",
    next_puzzle_in: "פאזל הבא בעוד",
    name_prompt: "מה השם שלכם?",
    name_subtitle: "יוצג בלוח התוצאות.",
    name_placeholder: "ישראל ישראלי",
    btn_save: "שמור",
    btn_signout: "התנתק",
    end_title: "סיום משחק",
    final_max: "מתוך {max}",
    btn_share: "📋 העתק תוצאה",
    btn_share_title: "אתגרו את החברים שלכם",
    btn_share_sub: "בדקו אם מישהו יצליח לעבור אתכם",
    btn_share_wa_title: "שתפו בוואטסאפ",
    btn_share_wa_sub: "שלחו לחברים — אתגר ישיר",
    btn_share_wa_short: "וואטסאפ",
    btn_share_short: "העתק / שתף",
    rank_top: "מקום #{rank}! 🏆",
    rank_beat: "ניצחתם {pct}% מהשחקנים היום",
    rank_solo: "אתם הראשונים היום 🇮🇱",
    rank_zero: "סיימתם את הפאזל היומי",
    streak_days: "🔥 רצף של {n} ימים",
    streak_one: "🔥 יום ראשון ברצף",
    avg_today: "ממוצע היום: {avg}",
    delta_above: "+{d} מעל הממוצע",
    delta_below: "{d} מתחת לממוצע",
    btn_leaderboard: "🏆 לוח יומי",
    btn_archive_end: "📅 ארכיון פאזלים",
    places_title: "המקומות של היום",
    btn_fresh_guest: "↺ התחל מחדש כאורח חדש",
    history_title: "היסטוריה",
    btn_close: "סגור",
    set_title: "הגדרות",
    set_sound: "צליל",
    set_tap: "אישור לחיצה",
    set_lang: "שפה",
    set_howto: "איך משחקים",
    set_stats: "סטטיסטיקות",
    lbs_your_score: "הניקוד שלך",
    lbs_rank: "מקום",
    lbs_vs_avg: "מול הממוצע",
    lbs_streak: "רצף",
    lb_title: "לוח יומי",
    stats_title: "סטטיסטיקות",
    stats_games: "משחקים",
    stats_streak: "רצף נוכחי",
    stats_max: "רצף שיא",
    stats_avg: "ממוצע",
    histogram_title: "פיזור ניקוד",
    howto_title: "איך משחקים?",
    howto_p1: "בכל סבב יופיע שם של מקום בישראל. <b>לחצו על המפה</b> איפה לדעתכם הוא נמצא.",
    howto_scoring_title: "ניקוד",
    howto_scoring_p: "ככל שלחצתם <b>קרוב יותר</b>, יותר נקודות. עד 250 לסבב בודד, עד <b>1000</b> בכל יום.",
    howto_daily_title: "פאזל יומי",
    howto_daily_p1: "כולם משחקים את אותם 5 מקומות. הפאזל מתחלף ב-<b>00:00</b> שעון ישראל.",
    howto_daily_p2: "אפשר לשתף את התוצאה כמו בוורדל ולהשוות לחברים.",
    howto_back: "חזור",
    howto_next: "הבא",
    howto_start: "התחל",
    howto_skip: "דלגו ←",
    btn_stats_tooltip: "סטטיסטיקות",
    btn_sound_tooltip: "צליל",
    btn_history_tooltip: "היסטוריה",
    btn_signout_tooltip: "התנתק מהחשבון",
    btn_help_tooltip: "איך משחקים",
    btn_archive_tooltip: "ארכיון פאזלים",
    archive_title: "ארכיון פאזלים",
    archive_hint: "לחצו על תאריך כדי לשחק את הפאזל של אותו יום.",
    prompt_where: "איפה",
    where_q: "?",
    round_n_of: "סבב {n} / 5",
    score_label: "ניקוד",
    km_from_you: "ק״מ ממך",
    btn_summary: "סיכום",
    btn_next: "הבא ←",
    click_inside_israel: "לחצו בתוך ישראל",
    score_save_fail: "שגיאה בשמירת הניקוד",
    puzzle_load_fail: "נכשלה טעינת הפאזל. נסו שוב.",
    stats_load_fail: "טעינת סטטיסטיקות נכשלה",
    lb_load_fail: "נכשלה הטעינה. נסו שוב.",
    sign_in_for_history: "התחברו כדי לראות היסטוריה",
    supabase_not_configured: "חיבור Supabase לא הוגדר",
    confirm_fresh_guest: "יישחק לך פאזל חדש כאורח. ההיסטוריה המקומית תאופס. להמשיך?",
    share_intro: "אני סיימתי את IsraelE #{day} עם {score}/1000 🇮🇱\nתעלו עליי?",
    share_final: "ניקוד סופי",
    copied: "הועתק ללוח",
    copy_failed: "העתקה נכשלה",
    sound_on: "צליל: פעיל",
    sound_off: "צליל: כבוי",
    btn_confirm_tap_tooltip: "אישור לחיצה (למניעת לחיצות בטעות)",
    btn_confirm_guess: "אישור הניחוש",
    confirm_tap_on: "אישור לחיצה: פעיל",
    confirm_tap_off: "אישור לחיצה: כבוי",
    no_lb_yet: "אין עדיין תוצאות.",
    no_games_yet: "עדיין לא שיחקתם.",
    info_link: "מידע נוסף ↗",
    archive_banner: "ארכיון: {date}",
    play_today: "→ לפאזל של היום",
    link_privacy: "פרטיות",
    link_terms: "תנאי שימוש",
    credit_dev: "פותח על ידי",
    type_city: "עיר", type_village: "יישוב", type_mountain: "הר", type_ruins: "חורבה",
    type_viewpoint: "תצפית", type_archaeological: "אתר ארכיאולוגי",
    type_memorial: "אנדרטה", type_attraction: "אתר תיירות", type_museum: "מוזיאון",
    type_monument: "אנדרטה", type_battlefield: "שדה קרב", type_tomb: "קבר",
    type_castle: "טירה", type_fort: "מבצר", type_nature_reserve: "שמורת טבע",
    type_theme_park: "פארק שעשועים", type_city_gate: "שער עיר",
    type_wayside_shrine: "מקדש דרך", type_christian_site: "אתר נוצרי",
    type_jewish_site: "אתר יהודי", type_druze_site: "אתר דרוזי",
    type_religious_site: "אתר דתי",
    cat_city: "עיר", cat_settlement: "יישוב", cat_landmark: "אתר",
  },
  en: {
    site_title: "IsraelE — Daily Israel Geography Puzzle",
    site_desc: "Daily Wordle-style geography puzzle for Israel. 5 places, one map, up to 1000 points.",
    splash_loading: "Loading",
    tagline: "How well do you know Israel?",
    tagline_sub: "5 fresh places every day. Same set for everyone.",
    legend_cities: "1 city",
    legend_settlements: "2 settlements",
    legend_landmarks: "2 landmarks",
    game_total_hint_pre: "Up to",
    game_total_hint_post: "points",
    btn_signin_google: "Sign in with Google",
    or_divider: "or",
    btn_play_guest: "Play as guest",
    btn_play: "Play",
    guest_hint: "Guest mode doesn't save long-term history.",
    next_puzzle_in: "Next puzzle in",
    name_prompt: "What's your name?",
    name_subtitle: "Shown on the leaderboard.",
    name_placeholder: "Your name",
    btn_save: "Save",
    btn_signout: "Sign out",
    end_title: "Game over",
    final_max: "out of {max}",
    btn_share: "📋 Copy result",
    btn_share_title: "Challenge your friends",
    btn_share_sub: "See if anyone can beat your score",
    btn_share_wa_title: "Share on WhatsApp",
    btn_share_wa_sub: "Send to friends — a direct challenge",
    btn_share_wa_short: "WhatsApp",
    btn_share_short: "Copy / Share",
    rank_top: "Rank #{rank}! 🏆",
    rank_beat: "You beat {pct}% of today's players",
    rank_solo: "You're the first one today 🇮🇱",
    rank_zero: "Daily puzzle complete",
    streak_days: "🔥 {n}-day streak",
    streak_one: "🔥 First day in a streak",
    avg_today: "Today's avg: {avg}",
    delta_above: "+{d} above avg",
    delta_below: "{d} below avg",
    btn_leaderboard: "🏆 Daily board",
    btn_archive_end: "📅 Archive",
    places_title: "Today's places",
    btn_fresh_guest: "↺ Start fresh as guest",
    history_title: "History",
    btn_close: "Close",
    set_title: "Settings",
    set_sound: "Sound",
    set_tap: "Tap to confirm",
    set_lang: "Language",
    set_howto: "How to play",
    set_stats: "Statistics",
    lbs_your_score: "Your score",
    lbs_rank: "Rank",
    lbs_vs_avg: "vs avg",
    lbs_streak: "Streak",
    lb_title: "Daily leaderboard",
    stats_title: "Stats",
    stats_games: "games",
    stats_streak: "current streak",
    stats_max: "max streak",
    stats_avg: "average",
    histogram_title: "Score distribution",
    howto_title: "How to play",
    howto_p1: "Each round shows the name of a place in Israel. <b>Click on the map</b> where you think it is.",
    howto_scoring_title: "Scoring",
    howto_scoring_p: "The <b>closer</b> your click, the more points. Up to 250 per round, up to <b>1000</b> per day.",
    howto_daily_title: "Daily puzzle",
    howto_daily_p1: "Everyone plays the same 5 places. Resets at <b>midnight</b> Israel time.",
    howto_daily_p2: "Share your result Wordle-style and compare with friends.",
    howto_back: "Back",
    howto_next: "Next",
    howto_start: "Play",
    howto_skip: "Skip →",
    btn_stats_tooltip: "Stats",
    btn_sound_tooltip: "Sound",
    btn_history_tooltip: "History",
    btn_signout_tooltip: "Sign out",
    btn_help_tooltip: "How to play",
    btn_archive_tooltip: "Puzzle archive",
    archive_title: "Puzzle archive",
    archive_hint: "Tap any date to play that day's puzzle.",
    prompt_where: "Where is",
    where_q: "?",
    round_n_of: "Round {n} / 5",
    score_label: "Score",
    km_from_you: "km away",
    btn_summary: "Summary",
    btn_next: "Next →",
    click_inside_israel: "Click inside Israel",
    score_save_fail: "Score save failed",
    puzzle_load_fail: "Failed to load puzzle. Try again.",
    stats_load_fail: "Stats load failed",
    lb_load_fail: "Couldn't load. Try again.",
    sign_in_for_history: "Sign in to see your history",
    supabase_not_configured: "Supabase not configured",
    confirm_fresh_guest: "A fresh guest puzzle will start. Local history will be wiped. Continue?",
    share_intro: "I scored {score}/1000 on IsraelE #{day} 🇮🇱\nThink you can beat me?",
    share_final: "Final score",
    copied: "Copied to clipboard",
    copy_failed: "Copy failed",
    sound_on: "Sound: on",
    sound_off: "Sound: off",
    btn_confirm_tap_tooltip: "Tap-to-confirm (prevents accidental guesses)",
    btn_confirm_guess: "Confirm guess",
    confirm_tap_on: "Tap-to-confirm: on",
    confirm_tap_off: "Tap-to-confirm: off",
    no_lb_yet: "No results yet.",
    no_games_yet: "No games yet.",
    info_link: "Read more ↗",
    archive_banner: "Archive: {date}",
    play_today: "→ Play today's puzzle",
    link_privacy: "Privacy",
    link_terms: "Terms",
    credit_dev: "Developed by",
    type_city: "city", type_village: "village", type_mountain: "mountain", type_ruins: "ruins",
    type_viewpoint: "viewpoint", type_archaeological: "archaeological site",
    type_memorial: "memorial", type_attraction: "attraction", type_museum: "museum",
    type_monument: "monument", type_battlefield: "battlefield", type_tomb: "tomb",
    type_castle: "castle", type_fort: "fort", type_nature_reserve: "nature reserve",
    type_theme_park: "theme park", type_city_gate: "city gate",
    type_wayside_shrine: "wayside shrine", type_christian_site: "christian site",
    type_jewish_site: "jewish site", type_druze_site: "druze site",
    type_religious_site: "religious site",
    cat_city: "city", cat_settlement: "settlement", cat_landmark: "landmark",
  },
};

function _pickLang() {
  // Explicit user choice always wins (URL or previous toggle). Default Hebrew
  // for everyone else — site is Israel-focused.
  const urlLang = new URLSearchParams(location.search).get("lang");
  if (urlLang === "he" || urlLang === "en") return urlLang;
  const saved = localStorage.getItem("israelle_lang");
  if (saved === "he" || saved === "en") return saved;
  return "he";
}
let LANG = _pickLang();

function T(key, vars) {
  let s = STRINGS[LANG]?.[key] ?? STRINGS.en[key] ?? key;
  if (vars) for (const k in vars) s = s.replace(`{${k}}`, vars[k]);
  return s;
}

function typeLabel(t) {
  const key = "type_" + t.replace(/\s+/g, "_").replace("archaeological_site", "archaeological");
  const v = STRINGS[LANG][key];
  return v || t;
}
function categoryLabel(c) {
  return STRINGS[LANG]["cat_" + c] || c;
}

// Emoji per place type — used in the in-game tag pill so the user knows
// what kind of thing they're looking for at a glance (mountain vs tomb vs city).
const TYPE_ICON = {
  city: "🏙️", village: "🏡",
  mountain: "⛰️", ruins: "🏛️",
  viewpoint: "🔭", "archaeological site": "🏺",
  memorial: "🕯️", attraction: "🎡",
  museum: "🏛️", monument: "🗿",
  battlefield: "⚔️", tomb: "⚰️",
  castle: "🏰", fort: "🛡️",
  "nature reserve": "🌲", "theme park": "🎢",
  "city gate": "🚪", "wayside shrine": "🛤️",
  "christian site": "✝️", "jewish site": "✡️",
  "druze site": "🌟", "religious site": "🕌",
};

function placeTag(r) {
  // Always show the most specific type (e.g. "אתר ארכיאולוגי" not "אתר").
  const icon = TYPE_ICON[r.type] || "📍";
  const label = typeLabel(r.type);
  return { icon, label, klass: multClass(r.multiplier) };
}

// HUD place-type pill: type label + its multiplier folded in ("עיר ×1").
function _setPlaceTag(r) {
  const tag = placeTag(r);
  const el = document.getElementById("place-type");
  el.className = `place-tag ${tag.klass}`;
  el.innerHTML = `<span class="pt-label">${escapeHtml(tag.label)}</span>`
    + `<span class="pt-mult">×${r.multiplier}</span>`;
}

function applyI18n() {
  document.documentElement.lang = LANG;
  document.documentElement.dir = LANG === "he" ? "rtl" : "ltr";
  document.title = T("site_title");
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const attr = el.getAttribute("data-i18n-attr");
    if (attr) {
      el.setAttribute(attr, T(key));
    } else if (!el.hasAttribute("data-i18n-html")) {
      el.textContent = T(key);
    }
  });
  document.querySelectorAll("[data-i18n-text]").forEach((el) => {
    el.textContent = T(el.getAttribute("data-i18n-text"));
  });
  document.querySelectorAll("[data-i18n-html]").forEach((el) => {
    el.innerHTML = T(el.getAttribute("data-i18n-html"));
  });
  const btn = document.getElementById("btn-lang");
  if (btn) {
    const v = btn.querySelector(".set-value") || btn;
    v.textContent = LANG === "he" ? "EN" : "עב";
  }
}

function toggleLang() {
  LANG = LANG === "he" ? "en" : "he";
  localStorage.setItem("israelle_lang", LANG);
  applyI18n();
  // Re-render any dynamic strings on screen
  repaintDynamic();
  // Start/signin card buttons depend on session+lang
  try { renderUserChip(); } catch {}
}

// ─── Constants ──────────────────────────────────────────────────────────────
const ISRAEL_CENTER = [34.95, 31.5];
const ISRAEL_CLICK_BBOX = { minLng: 34.0, maxLng: 35.95, minLat: 29.3, maxLat: 33.4 };
const PAN_BOUNDS = [[32.5, 27.5], [38.5, 34.8]];

const SAT_STYLE = {
  version: 8,
  sources: {
    esri_sat: {
      type: "raster",
      tiles: ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"],
      tileSize: 256, maxzoom: 19,
      attribution: "Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics",
    },
  },
  layers: [{ id: "esri_sat", type: "raster", source: "esri_sat" }],
};

const multClass = (m) => (m === 1 ? "m1" : m === 1.5 ? "m2" : "m3");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ─── State ──────────────────────────────────────────────────────────────────
let map;
let sb;            // supabase client
let session = null;
let playerId, playerName;
let soundOn = true;
let confirmTap = false;
let audioCtx;

const state = {
  rounds: [],
  played: [],
  cursor: 0,
  totalScore: 0,
  date: "",
  dayNumber: 0,
  awaitingClick: false,
  pendingGuess: null, pendingMarker: null,
  guessMarker: null, truthMarker: null, cometMarker: null,
  lineId: null, polyId: null,
  // Per-round truth coords decoded client-side from /api/today.tile_hash,
  // used to start the reveal animation before /api/today/guess returns.
  _idx: null,
  // Archive mode: when ?date=YYYY-MM-DD set, play a past day stateless (no save).
  archive: null,
  // Filled on game completion from backend rank_and_percentile (null in archive).
  rank: null, percentile: null, totalPlayers: null,
  averageScore: null, streak: null,
};

// Pull ?date= from URL once; null on the live daily puzzle.
function _readArchiveDate() {
  const d = new URLSearchParams(location.search).get("date");
  if (!d || !/^\d{4}-\d{2}-\d{2}$/.test(d)) return null;
  return d;
}

function _isArchive() { return !!state.archive; }
function _puzzleUrl() { return state.archive ? `/api/puzzle/${state.archive}` : "/api/today"; }
function _guessUrl() { return state.archive ? `/api/puzzle/${state.archive}/guess` : "/api/today/guess"; }

function repaintDynamic() {
  // Called after lang toggle. Re-render anything not handled by applyI18n.
  if (state.rounds.length && state.cursor < state.rounds.length && state.awaitingClick) {
    const r = state.rounds[state.cursor];
    document.getElementById("place-name-he").textContent = LANG === "he" ? r.name_he : (r.name_en || r.name_he);
    _setPlaceTag(r);
    document.getElementById("round-score").textContent = state.totalScore;
  }
  // Re-render reveal place name if visible
  const revPlace = document.getElementById("reveal-place");
  if (revPlace && !document.getElementById("reveal-card").classList.contains("hidden")) {
    const r = state.rounds[state.cursor];
    if (r) revPlace.textContent = LANG === "he" ? r.name_he : (r.name_en || r.name_he);
  }
  // Re-render archive banner text
  if (state.archive) {
    const tEl = document.getElementById("archive-banner-text");
    if (tEl) tEl.textContent = T("archive_banner", { date: state.archive });
  }
  // Re-render howto next button
  if (typeof state._howtoIdx === "number") {
    const nextBtn = document.getElementById("btn-howto-next");
    if (nextBtn) nextBtn.textContent = state._howtoIdx === 2 ? T("howto_start") : T("howto_next");
  }
  // Re-render places list (if on end-card)
  if (state.played.length && !document.getElementById("end-card").classList.contains("hidden")) {
    renderPlacesList();
  }
  // Re-render calendar (lang-aware month + weekday names)
  if (state._calMonth && !document.getElementById("archive-card").classList.contains("hidden")) {
    renderCalendar();
  }
}

// Israel-themed score emojis (5 buckets, best → worst):
// flag, star of david, dove (peace), camel (desert grind), cactus (סבר/ouch)
const PALETTE = ["🇮🇱", "✡️", "🕊️", "🐪", "🌵"];

// ─── Boot ───────────────────────────────────────────────────────────────────
const _splashStart = performance.now();
const MIN_SPLASH_MS = 400; // just enough to read the wordmark

async function init() {
  // Apply language + direction before anything visible renders.
  applyI18n();
  // Detect archive mode early so loadTodayIntoState routes correctly.
  state.archive = _readArchiveDate();
  if (state.archive) {
    document.getElementById("archive-banner").classList.remove("hidden");
    document.getElementById("archive-banner-text").textContent = T("archive_banner", { date: state.archive });
  }

  // ----- INSTANT WORK (no awaits, runs before any network) -----
  // Identity from localStorage — no network needed.
  playerId = localStorage.getItem("israelle_player_id");
  if (!playerId) {
    playerId = (crypto.randomUUID ? crypto.randomUUID() : ("p_" + Math.random().toString(36).slice(2)));
    localStorage.setItem("israelle_player_id", playerId);
  }
  playerName = localStorage.getItem("israelle_player_name") || "";
  soundOn = localStorage.getItem("israelle_sound") !== "off";
  confirmTap = localStorage.getItem("israelle_confirm_tap") === "on";
  applyToggleVisuals();
  renderUserChip();  // shows guest mode initially; updated when auth resolves

  // ----- KICK OFF PARALLEL FETCHES -----
  // Puzzle data is the longest network call. Start it BEFORE config + auth so
  // both run concurrently (saves ~150ms on cold cache).
  const puzzleP = fetchJSON(_puzzleUrl()).catch((e) => { console.warn("puzzle prefetch failed", e); return null; });
  const cfgP = fetch("/api/config").then((r) => r.json()).catch(() => ({}));

  // ----- MAP — construct immediately, load happens async in background -----
  // Doesn't block JS; map.on("load") fires whenever tiles are ready. By then
  // the user is usually still reading the start card.
  map = new maplibregl.Map({
    container: "map", style: SAT_STYLE, center: ISRAEL_CENTER,
    zoom: 7.3, minZoom: 6, maxZoom: 18,
    maxBounds: PAN_BOUNDS,
    dragRotate: false, pitchWithRotate: false, touchPitch: false,
    clickTolerance: 6,
    fadeDuration: 80,
    attributionControl: false,
  });
  // Compact attribution: a small ⓘ that expands on tap, instead of a wide bar.
  // MapLibre renders the compact <details> expanded and re-opens it whenever a
  // source's attribution updates, so collapse it after the map settles.
  map.addControl(new maplibregl.AttributionControl({ compact: true }), "top-right");
  const collapseAttrib = () => {
    const d = document.querySelector(".maplibregl-ctrl-attrib.maplibregl-compact");
    if (d) { d.removeAttribute("open"); d.classList.remove("maplibregl-compact-show"); }
  };
  map.on("load", collapseAttrib);
  map.on("idle", collapseAttrib);
  map.touchZoomRotate?.disableRotation();
  map.on("click", onMapClick);
  map.on("load", addIsraelMask);
  const onPress = (e) => {
    if (!state.awaitingClick) return;
    const ll = e.lngLat;
    if (!ll) return;
    spawnRipple([ll.lng, ll.lat], "#ffffff", 1.8, 380, 1);
  };
  map.on("mousedown", onPress);
  map.on("touchstart", onPress);

  // ----- AUTH (awaits config, but config was fetched in parallel) -----
  const cfg = await cfgP;
  if (cfg.supabase_url && cfg.supabase_key) {
    sb = window.supabase.createClient(cfg.supabase_url, cfg.supabase_key, {
      auth: { detectSessionInUrl: true, persistSession: true, autoRefreshToken: true },
    });
    const { data } = await sb.auth.getSession();
    session = data.session;
    sb.auth.onAuthStateChange((evt, s) => {
      const wasSignedOut = !session;
      session = s;
      renderUserChip();
      if (evt === "SIGNED_IN" && wasSignedOut && s) resyncForAuth();
    });
  }
  renderUserChip();

  // wire buttons
  document.getElementById("btn-start").onclick = onStart;
  document.getElementById("btn-next").onclick = onNext;
  document.getElementById("btn-signin").onclick = onSignIn;
  document.getElementById("btn-signout").onclick = onSignOut;
  document.getElementById("btn-history").onclick = openHistory;
  document.getElementById("btn-history-close").onclick = closeModal;
  document.getElementById("btn-leaderboard").onclick = openLeaderboard;
  document.getElementById("btn-lb-close").onclick = closeModal;
  document.getElementById("btn-share").onclick = onShare;
  document.getElementById("btn-share-wa").onclick = onShareWhatsApp;
  document.getElementById("btn-name-save").onclick = onSaveName;
  document.getElementById("btn-fresh-guest").onclick = onFreshGuest;

  // toolbar
  document.getElementById("btn-help").onclick = () => openHowto(0, true);
  document.getElementById("btn-stats").onclick = openStats;
  document.getElementById("btn-stats-close").onclick = closeModal;
  // Settings are Shoelace switches now (labeled, keyboard + screen-reader friendly).
  const swSound = document.getElementById("sw-sound");
  const swTap = document.getElementById("sw-tap");
  if (swSound) {
    swSound.checked = soundOn;
    swSound.addEventListener("sl-change", () => setSound(swSound.checked));
  }
  if (swTap) {
    swTap.checked = confirmTap;
    swTap.addEventListener("sl-change", () => setConfirmTap(swTap.checked));
  }
  document.getElementById("btn-confirm-guess").onclick = onConfirmGuess;
  wireToolbarMenu();
  wireModalDismiss();
  document.getElementById("btn-lang").onclick = toggleLang;
  document.getElementById("btn-archive").onclick = openArchive;
  document.getElementById("btn-archive-close").onclick = closeModal;
  document.getElementById("cal-prev").onclick = () => navCal(-1);
  document.getElementById("cal-next").onclick = () => navCal(+1);
  document.getElementById("btn-howto-next").onclick = () => moveHowto(+1);
  document.getElementById("btn-howto-prev").onclick = () => moveHowto(-1);
  document.getElementById("btn-howto-skip").onclick = skipHowto;

  startCountdown();
  // Pass the pre-fetched puzzle so loadTodayIntoState doesn't refetch.
  const alreadyDone = await loadTodayIntoState(await puzzleP);

  // render Lucide icons
  if (window.lucide?.createIcons) window.lucide.createIcons();

  // first-visit howto
  if (!alreadyDone) {
    if (!localStorage.getItem("israelle_seen_howto")) {
      openHowto(0);
    } else {
      animateCardIn("start-card");
    }
  }

  const elapsed = performance.now() - _splashStart;
  if (elapsed < MIN_SPLASH_MS) await sleep(MIN_SPLASH_MS - elapsed);
  hideSplash();
}

function hideSplash() {
  const s = document.getElementById("splash");
  if (!s) return;
  s.classList.add("fading");
  setTimeout(() => s.remove(), 600);
}

// Failsafe: kill splash after 8s no matter what. Railway is warm, so a long
// hang means something's wrong; show the start card so the user can retry.
setTimeout(() => {
  const s = document.getElementById("splash");
  if (s && !s.classList.contains("fading")) hideSplash();
}, 8000);

async function loadTodayIntoState(preFetched) {
  try {
    const t = preFetched || await fetchJSON(_puzzleUrl());
    if (!t) throw new Error("no puzzle data");
    state.dayNumber = t.day_number;
    state.date = t.date;
    state.rounds = t.rounds;
    // Hydrate the per-round paint index — used to draw the reveal line
    // without waiting for the score round-trip.
    if (t.tile_hash) {
      try {
        state._idx = await _initPaintIndex(t.tile_hash, t.date);
        console.log("[ils] paint index ready, rounds=", state._idx?.length);
      } catch (e) {
        state._idx = null;
        console.warn("[ils] paint index failed:", e);
      }
    } else {
      console.warn("[ils] puzzle missing tile_hash");
    }
    const tag = document.getElementById("day-num-start");
    if (tag) tag.textContent = `#${t.day_number}`;

    // Archive mode: skip the "have I played today" lookup — past days are
    // stateless replay. Always start fresh.
    if (state.archive) {
      state.played = [];
      state.totalScore = 0;
      return false;
    }

    // Prefer auth identity when signed in: the canonical player_id may differ
    // from whatever's in localStorage (e.g. user signed out, played as guest,
    // then signed back in). Backend looks up by auth_user_id, returns the row
    // that owns today's game if any.
    let me = null;
    if (session?.access_token) {
      try {
        // Pass the current localStorage id as a hint so the backend can
        // claim a guest player row this account hasn't seen yet (e.g. user
        // played as guest, then signed in for the first time today).
        const url = `/api/me/today?hint=${encodeURIComponent(playerId)}`;
        const authMe = await fetchJSON(url, {
          headers: { Authorization: `Bearer ${session.access_token}` },
        });
        if (authMe.player_id && authMe.player_id !== playerId) {
          playerId = authMe.player_id;
          localStorage.setItem("israelle_player_id", playerId);
        }
        if (authMe.name) {
          playerName = authMe.name;
          localStorage.setItem("israelle_player_name", playerName);
        }
        me = authMe;
      } catch (e) {
        console.warn("auth /me/today failed, falling back to anon", e);
      }
    }
    if (!me) {
      me = await fetchJSON(`/api/today/me?player_id=${encodeURIComponent(playerId)}`, authHeaders());
    }

    if (me.done) {
      state.played = me.guesses || [];
      state.totalScore = me.total_score || 0;
      state.rank = me.rank ?? null;
      state.percentile = me.percentile ?? null;
      state.totalPlayers = me.total_players ?? null;
      state.averageScore = me.average_score ?? null;
      state.streak = me.streak ?? null;
      showEnd(true);
      return true;
    }
    // Resume mid-game: server has 1-5 guesses already. Jump straight back
    // into the next round so a refresh doesn't drop the user at the start card.
    if (me.guesses && me.guesses.length > 0 && me.guesses.length < state.rounds.length) {
      state.played = me.guesses;
      state.totalScore = me.total_score || 0;
      state.cursor = me.guesses.length;
      showCard(null);
      await loadRound();
      return true;
    }
  } catch (e) {
    console.warn("puzzle load failed", e);
  }
  return false;
}

async function resyncForAuth() {
  // Called after a SIGNED_IN event mid-session. Re-resolve today's state
  // using auth identity and jump to the end card if the user already played.
  const wasDone = await loadTodayIntoState();
  if (wasDone) {
    // Hide any mid-game UI; showEnd already swapped to end-card.
    document.getElementById("hud").classList.add("hidden");
    state.awaitingClick = false;
  }
}

function animateCardIn(cardId) {
  if (!window.anime) return;
  const card = document.getElementById(cardId);
  if (!card || card.classList.contains("hidden")) return;
  card.style.opacity = "0";
  card.style.transform = "translateY(12px) scale(0.98)";
  anime.animate(card, {
    opacity: 1,
    translateY: 0,
    scale: 1,
    duration: 280,
    ease: "outQuart",
  });
}


// ─── Auth UI ────────────────────────────────────────────────────────────────
function renderUserChip() {
  const chip = document.getElementById("user-chip");
  const signinArea = document.getElementById("signin-area");
  const statsBtn = document.getElementById("btn-stats");
  const startBtn = document.getElementById("btn-start");
  const guestHint = document.querySelector("#start-card .signin-hint");
  if (session) {
    chip.classList.remove("hidden");
    document.getElementById("user-name").textContent =
      session.user.user_metadata?.full_name || session.user.email || "";
    signinArea?.classList.add("hidden");
    statsBtn?.classList.remove("hidden");
    if (startBtn) {
      startBtn.textContent = T("btn_play");
      startBtn.classList.remove("btn-secondary");
    }
    guestHint?.classList.add("hidden");
  } else {
    chip.classList.add("hidden");
    signinArea?.classList.remove("hidden");
    statsBtn?.classList.add("hidden");
    if (startBtn) {
      startBtn.textContent = T("btn_play_guest");
      startBtn.classList.add("btn-secondary");
    }
    guestHint?.classList.remove("hidden");
  }
}

async function onSignIn() {
  if (!sb) { flashToast(T("supabase_not_configured")); return; }
  await sb.auth.signInWithOAuth({
    provider: "google",
    options: { redirectTo: location.origin },
  });
}

async function onSignOut() {
  if (!sb) return;
  try { await sb.auth.signOut(); } catch {}
  resetToGuest();
}

function resetToGuest() {
  localStorage.removeItem("israelle_player_id");
  localStorage.removeItem("israelle_player_name");
  location.reload();
}

function onFreshGuest() {
  if (!confirm(T("confirm_fresh_guest"))) return;
  // If signed in too, sign out first so we don't immediately re-resume the account
  if (sb && session) {
    sb.auth.signOut().finally(resetToGuest);
  } else {
    resetToGuest();
  }
}

// ─── Israel mask + border ───────────────────────────────────────────────────
// data/israel.geojson is curated land-only (Natural Earth 10m, IL ∪ PSE).
// Use as-is for both the dark mask hole and the border outline.

function _pointInRing(lon, lat, ring) {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const xi = ring[i][0], yi = ring[i][1];
    const xj = ring[j][0], yj = ring[j][1];
    if (((yi > lat) !== (yj > lat)) &&
        (lon < (xj - xi) * (lat - yi) / (yj - yi) + xi)) {
      inside = !inside;
    }
  }
  return inside;
}

async function addIsraelMask() {
  const border = await fetch("/api/israel-border").then((r) => r.json());
  const polys = border.geometry.type === "Polygon"
    ? [border.geometry.coordinates[0]]
    : border.geometry.coordinates.map((p) => p[0]);
  state._borderRings = polys;     // cached for point-in-polygon click filter
  const worldRing = [[-180, -85], [180, -85], [180, 85], [-180, 85], [-180, -85]];
  map.addSource("il-mask", { type: "geojson",
    data: { type: "Feature", geometry: { type: "Polygon", coordinates: [worldRing, ...polys] } } });
  map.addLayer({ id: "il-mask-fill", type: "fill", source: "il-mask",
    paint: { "fill-color": "#0a1424", "fill-opacity": 0.65 } });
  map.addSource("il-border", { type: "geojson",
    data: { type: "Feature", geometry: { type: "Polygon", coordinates: polys } } });
  map.addLayer({ id: "il-border-glow", type: "line", source: "il-border",
    layout: { "line-cap": "round", "line-join": "round" },
    paint: { "line-color": "#4d7df0", "line-width": 6, "line-opacity": 0.25, "line-blur": 3 } });
  map.addLayer({ id: "il-border-line", type: "line", source: "il-border",
    layout: { "line-cap": "round", "line-join": "round" },
    paint: { "line-color": "#ffffff", "line-width": 2.4, "line-opacity": 0.85, "line-blur": 0.3 } });
}

// ─── Game flow ──────────────────────────────────────────────────────────────
async function onStart() {
  // Archive mode: skip the name prompt entirely. Scores aren't saved.
  if (!state.archive && !playerName) {
    showCard("name-card");
    document.getElementById("name-input").value = "";
    setTimeout(() => document.getElementById("name-input").focus(), 50);
    return;
  }
  await beginDay();
}

async function onSaveName() {
  const v = document.getElementById("name-input").value.trim();
  if (!v) { document.getElementById("name-input").focus(); return; }
  playerName = v.slice(0, 20);
  localStorage.setItem("israelle_player_name", playerName);
  await beginDay();
}

async function beginDay() {
  // Fast path: init() pre-loaded state. No network on click.
  if (state.rounds.length && state.date) {
    if (state.played.length >= state.rounds.length) { showEnd(true); return; }
    showCard(null);
    await loadRound();
    return;
  }
  showSpinner(true);
  try {
    if (state.archive) {
      const today = await fetchJSON(_puzzleUrl());
      state.date = today.date;
      state.dayNumber = today.day_number;
      state.rounds = today.rounds;
      state.played = [];
      state.totalScore = 0;
      state.cursor = 0;
    } else {
      const [today, me] = await Promise.all([
        fetchJSON("/api/today"),
        fetchJSON(`/api/today/me?player_id=${encodeURIComponent(playerId)}`, authHeaders()),
      ]);
      state.date = today.date;
      state.dayNumber = today.day_number;
      state.rounds = today.rounds;
      state.played = me.guesses || [];
      state.totalScore = me.total_score || 0;
      state.cursor = state.played.length;
      state.rank = me.rank ?? null;
      state.percentile = me.percentile ?? null;
      state.totalPlayers = me.total_players ?? null;
      state.averageScore = me.average_score ?? null;
      state.streak = me.streak ?? null;
    }
  } catch (e) {
    flashToast(T("puzzle_load_fail"));
    showSpinner(false);
    return;
  }
  showSpinner(false);

  if (state.played.length >= state.rounds.length) {
    showEnd(true);
    return;
  }
  showCard(null);
  await loadRound();
}

async function loadRound() {
  const r = state.rounds[state.cursor];
  document.getElementById("place-name-he").textContent = LANG === "he" ? r.name_he : (r.name_en || r.name_he);
  _setPlaceTag(r);
  // Progress dots (●●●○○○) instead of "Round 3 / 6" text.
  document.getElementById("round-num").innerHTML = _renderDots(state.cursor, state.rounds.length);
  document.getElementById("round-score").textContent = state.totalScore;
  document.getElementById("hud").classList.remove("hidden");
  state.awaitingClick = true;
  document.body.classList.add("awaiting-click");
}

function _renderDots(cursor, total) {
  let s = "";
  for (let i = 0; i < total; i++) {
    const cls = i < cursor ? "done" : i === cursor ? "active" : "";
    s += `<span class="dot ${cls}"></span>`;
  }
  return s;
}

// ─── Click handler ──────────────────────────────────────────────────────────
// Hard check: ray-cast against the actual Israel polygon. Fall back to the
// permissive bbox only if the border hasn't loaded yet (offline / first paint).
function insideIsrael(lng, lat) {
  if (state._borderRings && state._borderRings.length) {
    for (const ring of state._borderRings) {
      if (_pointInRing(lng, lat, ring)) return true;
    }
    return false;
  }
  return lng >= ISRAEL_CLICK_BBOX.minLng && lng <= ISRAEL_CLICK_BBOX.maxLng
      && lat >= ISRAEL_CLICK_BBOX.minLat && lat <= ISRAEL_CLICK_BBOX.maxLat;
}

async function onMapClick(e) {
  if (!state.awaitingClick) return;
  const { lng, lat } = e.lngLat;
  if (!insideIsrael(lng, lat)) {
    flashToast(T("click_inside_israel"));
    return;
  }
  if (confirmTap) {
    setPendingGuess(lng, lat);
    return;
  }
  await submitGuess(lng, lat);
}

function setPendingGuess(lng, lat) {
  state.pendingGuess = { lng, lat };
  if (state.pendingMarker) {
    state.pendingMarker.setLngLat([lng, lat]);
  } else {
    const el = document.createElement("div");
    el.style.cssText = "width:32px;height:32px;border-radius:50%;background:#ffb86b;border:4px solid #fff;box-shadow:0 0 0 2px rgba(0,0,0,0.7),0 0 24px 4px rgba(255,184,107,1);pointer-events:none;";
    state.pendingMarker = new maplibregl.Marker({ element: el, anchor: "center" })
      .setLngLat([lng, lat]).addTo(map);
  }
  spawnRipple([lng, lat], "#ffb86b", 2.4, 700, 1);
  document.getElementById("confirm-guess").classList.remove("hidden");
}

function clearPendingGuess() {
  state.pendingGuess = null;
  state.pendingMarker?.remove();
  state.pendingMarker = null;
  document.getElementById("confirm-guess").classList.add("hidden");
}

async function onConfirmGuess() {
  if (!state.awaitingClick || !state.pendingGuess) return;
  const { lng, lat } = state.pendingGuess;
  state.pendingMarker?.remove();
  state.pendingMarker = null;
  state.pendingGuess = null;
  document.getElementById("confirm-guess").classList.add("hidden");
  await submitGuess(lng, lat);
}

// The guess POST is the one network call that must not silently brick the game.
// Mobile networks blip and the backend can cold-start, so retry a few times with
// backoff before giving up. A 4xx (e.g. 409 already-played) is returned as-is —
// it won't change on retry.
async function postGuessWithRetry(url, headers, payload, tries = 4) {
  let lastErr;
  for (let i = 0; i < tries; i++) {
    try {
      const r = await fetch(url, { method: "POST", headers, body: JSON.stringify(payload) });
      if (r.ok) return await r.json();
      if (r.status >= 400 && r.status < 500) return await r.json();
      lastErr = new Error("HTTP " + r.status);          // 5xx / cold start → retry
    } catch (e) { lastErr = e; }                          // network blip → retry
    if (i < tries - 1) await sleep(500 * (i + 1));
  }
  console.warn("[ils] guess failed after retries", lastErr);
  return { _err: lastErr || new Error("guess request failed") };
}

async function submitGuess(lng, lat) {
  state.awaitingClick = false;
  document.body.classList.remove("awaiting-click");
  chime(420);

  state.guessMarker = new maplibregl.Marker({ element: makeDot("guess") })
    .setLngLat([lng, lat]).addTo(map);
  popMarker(state.guessMarker);
  spawnRipple([lng, lat], "#ffb86b", 3.4, 1100, 2);

  // Kick off the score request in the background. Don't await yet — start
  // the reveal animation in parallel using the locally-known truth coords.
  const headers = { "Content-Type": "application/json" };
  if (!state.archive && session?.access_token) headers["Authorization"] = `Bearer ${session.access_token}`;
  const body = state.archive
    ? { player_id: playerId, round_idx: state.cursor, lat, lon: lng }
    : { player_id: playerId, name: playerName, round_idx: state.cursor, lat, lon: lng };
  const fetchP = postGuessWithRetry(_guessUrl(), headers, body);

  const localTruth = state._idx?.[state.cursor];   // [lat, lon] or undefined
  console.log("[ils] click", { round: state.cursor, fast: !!localTruth, t: Math.round(performance.now()) });
  if (localTruth) {
    const truthLngLat = [localTruth[1], localTruth[0]];
    // Simple bbox from guess+truth so the camera frames both immediately;
    // refined later if the server gives us a polygon.
    map.fitBounds([
      [Math.min(lng, truthLngLat[0]), Math.min(lat, truthLngLat[1])],
      [Math.max(lng, truthLngLat[0]), Math.max(lat, truthLngLat[1])],
    ], { padding: 120, duration: 900, maxZoom: 13 });

    await animateLine([lng, lat], truthLngLat, 2500);

    spawnRipple(truthLngLat, "#4d7df0", 5.2, 1500, 3);
    state.truthMarker = new maplibregl.Marker({ element: makeDot("truth") })
      .setLngLat(truthLngLat).addTo(map);
    popMarker(state.truthMarker, true);
  }

  const res = await fetchP;
  if (res._err || res.detail) {
    // The POST already retried internally; reaching here means a sustained
    // outage or a 4xx. Don't brick the round on a dead map — roll back the
    // reveal and re-arm the click so the player can simply tap again.
    flashToast(res.detail || T("score_save_fail"));
    clearMarkers();
    clearPolygon();
    state.awaitingClick = true;
    document.body.classList.add("awaiting-click");
    return;
  }

  // Archive: track score locally (no game_id, no total from server).
  if (state.archive) {
    res.total_score = (state.totalScore || 0) + res.round_score;
  }
  state.totalScore = res.total_score;
  // Last-round response includes rank info (live mode only).
  if (res.rank != null) {
    state.rank = res.rank;
    state.percentile = res.percentile;
    state.totalPlayers = res.total_players;
    state.averageScore = res.average_score ?? null;
    state.streak = res.streak ?? null;
  }
  state.played.push({ ...res, name_he: state.rounds[state.cursor].name_he, name_en: state.rounds[state.cursor].name_en });

  // If we didn't have local truth (no idx, e.g. first boot before hydrate),
  // run the full reveal sequence now that we have the server data.
  if (!localTruth) {
    const truthLngLat = [res.true_lon, res.true_lat];
    drawPolygon(res.polygon);
    const bbox = polygonBbox(res.polygon) ?? [
      [Math.min(lng, res.true_lon), Math.min(lat, res.true_lat)],
      [Math.max(lng, res.true_lon), Math.max(lat, res.true_lat)],
    ];
    map.fitBounds(bbox, { padding: 160, duration: 1200 });
    await animateLine([lng, lat], truthLngLat, 2500);
    spawnRipple(truthLngLat, "#4d7df0", 5.2, 1500, 3);
    state.truthMarker = new maplibregl.Marker({ element: makeDot("truth") })
      .setLngLat(truthLngLat).addTo(map);
    popMarker(state.truthMarker, true);
  } else {
    // Local-truth path already drew everything; just add the polygon if any.
    drawPolygon(res.polygon);
  }

  await sleep(300);
  showReveal(res);
}

// ─── Marker helpers (unchanged from previous) ───────────────────────────────
function makeDot(cls) {
  const wrap = document.createElement("div");
  wrap.className = "marker-wrap";
  wrap.innerHTML = `<div class="marker-pulse ${cls}"></div><div class="marker-dot ${cls}"></div>`;
  return wrap;
}

function polygonBbox(geom) {
  if (!geom) return null;
  const polys = geom.type === "Polygon" ? [geom.coordinates] : geom.coordinates;
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (const poly of polys) for (const ring of poly) for (const [x, y] of ring) {
    if (x < minX) minX = x; if (y < minY) minY = y;
    if (x > maxX) maxX = x; if (y > maxY) maxY = y;
  }
  return [[minX, minY], [maxX, maxY]];
}

function drawPolygon(geom) {
  state.polyId = "truth-polygon";
  if (map.getLayer(state.polyId + "-fill")) map.removeLayer(state.polyId + "-fill");
  if (map.getLayer(state.polyId + "-line")) map.removeLayer(state.polyId + "-line");
  if (map.getSource(state.polyId)) map.removeSource(state.polyId);
  if (!geom) return;
  map.addSource(state.polyId, { type: "geojson",
    data: { type: "Feature", geometry: geom, properties: {} } });
  map.addLayer({ id: state.polyId + "-fill", type: "fill", source: state.polyId,
    paint: { "fill-color": "#4d7df0", "fill-opacity": 0.22 } });
  map.addLayer({ id: state.polyId + "-line", type: "line", source: state.polyId,
    paint: { "line-color": "#4d7df0", "line-width": 2.5, "line-opacity": 0.95, "line-blur": 0.3 } });
}

// Straight-line path between two [lng,lat] points, sampled into `steps+1`
// points so line-gradient + dash effects have geometry to work with.
function straightPath(from, to, steps = 80) {
  const pts = [];
  for (let i = 0; i <= steps; i++) {
    const t = i / steps;
    pts.push([from[0] + (to[0] - from[0]) * t,
              from[1] + (to[1] - from[1]) * t]);
  }
  pts[0] = [from[0], from[1]];
  pts[pts.length - 1] = [to[0], to[1]];
  return pts;
}

// Build a closed hexagram (6-pointed star) LineString in lng/lat coords,
// sized so the visible star spans `screenRadiusPx` regardless of zoom.
// Uses map.project/unproject to translate screen-relative vertices into geo.
function _hexagramFeature(centerLngLat, screenRadiusPx, rotateRad) {
  const c = map.project(centerLngLat);
  const innerR = screenRadiusPx * 0.5774;     // inner radius for a regular hexagram
  const pts = [];
  for (let v = 0; v < 12; v++) {
    const r = v % 2 === 0 ? screenRadiusPx : innerR;
    const a = rotateRad + (v * Math.PI / 6) - Math.PI / 2;
    const sx = c.x + r * Math.cos(a);
    const sy = c.y + r * Math.sin(a);
    const ll = map.unproject([sx, sy]);
    pts.push([ll.lng, ll.lat]);
  }
  pts.push(pts[0]);   // close the path
  return { type: "Feature", geometry: { type: "LineString", coordinates: pts } };
}

// Star of David burst: drawn as a WebGL line layer (same primitive as the
// ribbon line, which we know works). Hexagram geometry is recomputed each
// frame from screen-radius via project/unproject so the star scales out
// visually while the geo coords adapt to the current zoom/pan.
let _magenSeq = 0;
function spawnMagenDavid(lngLat, color = "#0038b8", maxScreenRadius = 80, duration = 1400, rotateDeg = 30) {
  const id = "magen-" + (++_magenSeq);
  try {
    map.addSource(id, { type: "geojson", data: _hexagramFeature(lngLat, 5, 0) });
    map.addLayer({ id, type: "line", source: id,
      layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": color, "line-width": 3, "line-blur": 1.5, "line-opacity": 1 }});
  } catch (e) { console.warn("[magen] layer add", e); return; }

  const start = performance.now();
  const initialR = 28;                          // start big enough to be seen instantly
  function tick(now) {
    const t = Math.min(1, (now - start) / duration);
    const e = 1 - Math.pow(1 - t, 4);           // easeOutQuart — snappier than cubic
    const r = initialR + (maxScreenRadius - initialR) * e;
    const rot = rotateDeg * e * Math.PI / 180;
    const alpha = 1 - e;
    try {
      map.getSource(id)?.setData(_hexagramFeature(lngLat, r, rot));
      map.setPaintProperty(id, "line-opacity", alpha);
    } catch (_) { /* layer may have been cleared */ }
    if (t < 1) requestAnimationFrame(tick);
    else {
      try {
        if (map.getLayer(id)) map.removeLayer(id);
        if (map.getSource(id)) map.removeSource(id);
      } catch (_) {}
    }
  }
  requestAnimationFrame(tick);
}

// Animated guess→truth reveal: bezier arc, white "tallit" ribbon glow,
// blue marching flag-dashes, comet head, Magen David hexagram bursts at impact.
// Endpoint coords are forced exact and the comet snaps to the final point on
// completion so the line cannot visually drift off the truth coord.
function animateLine(from, to, durationMs = 2500) {
  state.lineId = "guess-line";
  const endpointSrcId = "guess-endpoints";
  for (const id of [state.lineId, state.lineId + "-base", state.lineId + "-glow",
                    endpointSrcId + "-glow", endpointSrcId]) {
    if (map.getLayer(id)) map.removeLayer(id);
  }
  for (const sid of [state.lineId, endpointSrcId]) {
    if (map.getSource(sid)) map.removeSource(sid);
  }

  const fullPath = straightPath(from, to, 80);

  // WebGL endpoint circles in the SAME canvas as the line — guaranteed to
  // show regardless of HTML marker rendering, and they project identically
  // with the line so the line visibly meets a solid dot at each end.
  map.addSource(endpointSrcId, { type: "geojson", data: {
    type: "FeatureCollection", features: [
      { type: "Feature", properties: { role: "guess" }, geometry: { type: "Point", coordinates: from }},
      { type: "Feature", properties: { role: "truth" }, geometry: { type: "Point", coordinates: to }},
    ]}});

  map.addSource(state.lineId, { type: "geojson", lineMetrics: true,
    data: { type: "Feature", geometry: { type: "LineString", coordinates: [from, from] } } });

  // Outer white tallit-style glow (slim — won't swallow the 22px endpoint dots).
  map.addLayer({ id: state.lineId + "-glow", type: "line", source: state.lineId,
    layout: { "line-cap": "butt", "line-join": "round" },
    paint: { "line-color": "#ffffff", "line-width": 7, "line-opacity": 0.4, "line-blur": 3.5 } });

  // Base white ribbon with gradient reveal
  map.addLayer({ id: state.lineId + "-base", type: "line", source: state.lineId,
    layout: { "line-cap": "butt", "line-join": "round" },
    paint: {
      "line-width": 3.5,
      "line-gradient": [ "interpolate", ["linear"], ["line-progress"],
        0.0, "rgba(255,255,255,0.7)",
        0.85, "rgba(255,255,255,0.95)",
        1.0, "#ffffff",
      ],
    } });

  // Blue marching dashes (Israeli flag blue)
  map.addLayer({ id: state.lineId, type: "line", source: state.lineId,
    layout: { "line-cap": "butt", "line-join": "round" },
    paint: { "line-color": "#0038b8", "line-width": 3.5, "line-dasharray": [0.55, 1.8], "line-opacity": 0.95 } });

  // Endpoint glow halo + solid dot (drawn LAST so they sit on top of the line).
  map.addLayer({ id: endpointSrcId + "-glow", type: "circle", source: endpointSrcId,
    paint: {
      "circle-radius": 15,
      "circle-color": ["match", ["get", "role"], "guess", "#ffb86b", "#34d399"],
      "circle-blur": 1.0, "circle-opacity": 0.5,
    }});
  map.addLayer({ id: endpointSrcId, type: "circle", source: endpointSrcId,
    paint: {
      "circle-radius": 8,
      "circle-color": ["match", ["get", "role"], "guess", "#ffb86b", "#34d399"],
      "circle-stroke-color": "#ffffff",
      "circle-stroke-width": 2.5,
    }});

  // Comet head — WebGL circle layer (not HTML marker; HTML overlays don't
  // render reliably on this setup). One Point feature whose coords are
  // updated each frame in onUpdate to follow the line tip.
  const cometSrcId = "comet-head";
  if (map.getLayer(cometSrcId)) map.removeLayer(cometSrcId);
  if (map.getLayer(cometSrcId + "-glow")) map.removeLayer(cometSrcId + "-glow");
  if (map.getSource(cometSrcId)) map.removeSource(cometSrcId);
  map.addSource(cometSrcId, { type: "geojson",
    data: { type: "Feature", geometry: { type: "Point", coordinates: from } }});
  map.addLayer({ id: cometSrcId + "-glow", type: "circle", source: cometSrcId,
    paint: { "circle-radius": 22, "circle-color": "#0038b8", "circle-blur": 1.2, "circle-opacity": 0.7 }});
  map.addLayer({ id: cometSrcId, type: "circle", source: cometSrcId,
    paint: { "circle-radius": 8, "circle-color": "#ffffff",
             "circle-stroke-color": "#0038b8", "circle-stroke-width": 2 }});
  const cometSrc = map.getSource(cometSrcId);

  // Marching-dash loop
  const dash = 0.55, gap = 1.8, precision = 1 / 40;
  const dashSeq = [];
  for (let i = 0; i <= dash; i += precision) dashSeq.push([i, gap, dash - i, 0]);
  for (let i = 0; i < gap;  i += precision) dashSeq.push([0, i, dash, gap - i]);
  let dashStep = 0, antRaf = null;
  const tickDash = () => {
    dashStep = (dashStep + 1) % dashSeq.length;
    if (map.getLayer(state.lineId)) map.setPaintProperty(state.lineId, "line-dasharray", dashSeq[dashStep]);
    antRaf = requestAnimationFrame(tickDash);
  };
  antRaf = requestAnimationFrame(tickDash);

  const src = map.getSource(state.lineId);
  const obj = { t: 0 };
  return new Promise((resolve) => {
    let resolved = false;
    const safeResolve = () => { if (!resolved) { resolved = true; resolve(); } };
    // Hard backstop: no matter what anime.js does, resolve after duration+buffer
    // so the caller (truth marker, ripples, fetch await) is NEVER blocked.
    const backstop = setTimeout(safeResolve, durationMs + 200);

    // The actual arrival effects — comet fade + 4 hexagram bursts. Called
    // from onUpdate the moment the line is visually arrived (t > 0.9) so
    // there's no perceptible gap between "line tip touches truth" and "boom".
    // Idempotent via `impactFired` so onComplete's safety call is a no-op.
    let impactFired = false;
    const fireImpact = () => {
      if (impactFired) return;
      impactFired = true;
      try {
        // Snap line + comet to exact truth coord.
        try { src.setData({ type: "Feature", geometry: { type: "LineString", coordinates: fullPath } }); } catch (_) {}
        try { cometSrc?.setData({ type: "Feature", geometry: { type: "Point", coordinates: to } }); } catch (_) {}
        // Comet fades over 280ms while bursts bloom in parallel.
        const fadeStart = performance.now();
        const fadeDur = 280;
        (function fade() {
          const t = Math.min(1, (performance.now() - fadeStart) / fadeDur);
          try {
            if (map.getLayer(cometSrcId)) map.setPaintProperty(cometSrcId, "circle-opacity", 1 - t);
            if (map.getLayer(cometSrcId + "-glow")) map.setPaintProperty(cometSrcId + "-glow", "circle-opacity", 0.7 * (1 - t));
          } catch (_) {}
          if (t < 1) requestAnimationFrame(fade);
          else {
            try {
              if (map.getLayer(cometSrcId)) map.removeLayer(cometSrcId);
              if (map.getLayer(cometSrcId + "-glow")) map.removeLayer(cometSrcId + "-glow");
              if (map.getSource(cometSrcId)) map.removeSource(cometSrcId);
            } catch (_) {}
          }
        })();
        const bursts = [
          { color: "#0038b8", radius:  60, dur: 650, delay:  0,  rot:  30 },
          { color: "#ffffff", radius:  85, dur: 700, delay: 60,  rot: -30 },
          { color: "#0038b8", radius: 115, dur: 800, delay: 130, rot:  30 },
          { color: "#ffffff", radius: 150, dur: 900, delay: 210, rot: -30 },
        ];
        for (const b of bursts) {
          setTimeout(() => { try { spawnMagenDavid(to, b.color, b.radius, b.dur, b.rot); } catch (e) { console.warn("[burst]", e); } }, b.delay);
        }
      } catch (e) { console.warn("[animateLine.fireImpact]", e); }
    };

    const finish = () => {
      try {
        clearTimeout(backstop);
        cancelAnimationFrame(antRaf);
        fireImpact();   // safe — idempotent
      } catch (e) { console.warn("[animateLine.finish]", e); }
      safeResolve();
    };

    anime.animate(obj, {
      t: 1, duration: durationMs, ease: "outQuart",
      onUpdate: () => {
        // Guard every frame — a single throw here would prevent onComplete.
        try {
          const last = fullPath.length - 1;
          let idx = Math.round(obj.t * last);
          if (idx < 1) idx = 1;
          const slice = fullPath.slice(0, idx + 1);
          if (idx === last) slice[slice.length - 1] = [to[0], to[1]];
          src.setData({ type: "Feature", geometry: { type: "LineString", coordinates: slice } });
          cometSrc?.setData({ type: "Feature", geometry: { type: "Point", coordinates: slice[slice.length - 1] } });
          // outQuart at t=0.9 → line is at 99.99% visually. Fire the impact
          // NOW so bursts bloom in lockstep with the arriving tip instead of
          // waiting for the easing tail to finish.
          if (obj.t > 0.9) fireImpact();
        } catch (e) { console.warn("[animateLine.onUpdate]", e); }
      },
      onComplete: finish,
    });
  });
}

// ─── Anime.js-driven helpers ────────────────────────────────────────────────
function popMarker(marker, big = false) {
  const el = marker.getElement().querySelector(".marker-dot");
  if (!el) return;
  // Start at ~60% scale (clearly visible on tap) and overshoot via outBack —
  // outElastic was slow at the start which read as "did my tap register?".
  el.style.transform = "scale(0.6)";
  if (!window.anime) { el.style.transform = "scale(1)"; return; }
  anime.animate(el, {
    scale: big ? [1.3, 1] : [1.2, 1],
    duration: 340,
    ease: "outBack(2)",
  });
  const pulseEl = marker.getElement().querySelector(".marker-pulse");
  if (pulseEl) {
    pulseEl.style.transform = "scale(0.5)";
    pulseEl.style.opacity = "0.75";
    anime.animate(pulseEl, {
      scale: 3,
      opacity: 0,
      duration: 900,
      ease: "outCubic",
      loop: big ? 1 : 3,           // guess pulses longer (covers fetch wait)
    });
  }
}

function spawnRipple(lngLat, color = "#4d7df0", maxScale = 3.6, duration = 1300, count = 1) {
  if (!window.anime) return;
  for (let i = 0; i < count; i++) {
    const wrap = document.createElement("div");
    wrap.className = "marker-wrap";
    const ring = document.createElement("div");
    ring.className = "ripple-ring";
    ring.style.borderColor = color;
    ring.style.boxShadow = `0 0 18px ${color}88`;
    ring.style.transform = "scale(0.2)";
    ring.style.opacity = "0.95";
    wrap.appendChild(ring);
    const m = new maplibregl.Marker({ element: wrap }).setLngLat(lngLat).addTo(map);
    anime.animate(ring, {
      scale: maxScale,
      opacity: 0,
      duration,
      delay: i * 200,
      ease: "outCubic",
      onComplete: () => m.remove(),
    });
  }
}

// ─── Reveal / Next / End ────────────────────────────────────────────────────
function showReveal(res) {
  chime(660);
  document.getElementById("hud").classList.add("hidden");
  document.getElementById("reveal-score").textContent = `+${res.round_score}`;
  document.getElementById("reveal-breakdown").textContent =
    `${res.base_score} × ${res.multiplier}`;
  const r = state.rounds[state.cursor];
  document.getElementById("reveal-place").textContent =
    LANG === "he" ? r.name_he : (r.name_en || r.name_he);
  const descEl = document.getElementById("reveal-desc");
  descEl.textContent = res.description || "";
  descEl.classList.toggle("hidden", !res.description);
  const srcEl = document.getElementById("reveal-source");
  if (res.source_url) {
    srcEl.href = res.source_url;
    srcEl.classList.remove("hidden");
  } else {
    srcEl.classList.add("hidden");
  }
  document.getElementById("reveal-dist").textContent = `${res.distance_km} ${T("km_from_you")}`;
  document.getElementById("btn-next").textContent = res.is_last ? T("btn_summary") : T("btn_next");
  showCard("reveal-card", true);
  state._lastWasFinal = res.is_last;
}

function onNext() {
  clearMarkers();
  if (state._lastWasFinal) {
    showEnd(false);
  } else {
    state.cursor++;
    showCard(null);
    loadRound();
    map.flyTo({ center: ISRAEL_CENTER, zoom: 7.3, duration: 800 });
  }
}

function showEnd(restored) {
  renderRoundChips();
  renderPlacesList();
  // Per-day max is computed from the rounds' multipliers (1000 for the 1·2·2
  // format, 1100 for pre-switch 2·2·2 archive days) — never hardcoded.
  const maxScore = state.rounds.reduce((s, r) => s + Math.round(100 * (r.multiplier || 0)), 0) || 1000;
  document.getElementById("final-max").textContent = T("final_max", { max: maxScore });
  // Per-user comparison stats (rank / vs-avg / streak) now live on the daily
  // board, not here — the end card stays focused on score + chips + share.
  showCard("end-card");
  if (restored) {
    document.getElementById("final-score").textContent = state.totalScore;
  } else {
    countUp(document.getElementById("final-score"), 0, state.totalScore, 1500);
  }
}

// Daily-board personal summary: your score, rank, gap-vs-average, streak.
// Moved here from the end card so post-game comparison lives in one place.
function renderLbStats() {
  const el = document.getElementById("lb-stats");
  if (!el) return;
  if (state.archive || state.rank == null) {
    el.classList.add("hidden");
    el.innerHTML = "";
    return;
  }
  const chips = [
    `<div class="lbs-chip"><b>${state.totalScore}</b><span>${escapeHtml(T("lbs_your_score"))}</span></div>`,
    `<div class="lbs-chip"><b>#${state.rank}</b><span>${escapeHtml(T("lbs_rank"))} / ${state.totalPlayers ?? 1}</span></div>`,
  ];
  if (state.averageScore != null) {
    const delta = state.totalScore - state.averageScore;
    const dtxt = (delta >= 0 ? "+" : "") + delta;
    const cls = delta >= 0 ? "delta-pos" : "delta-neg";
    chips.push(`<div class="lbs-chip"><b class="${cls}">${dtxt}</b><span>${escapeHtml(T("lbs_vs_avg"))}</span></div>`);
  }
  if ((state.streak || 0) >= 1) {
    chips.push(`<div class="lbs-chip"><b>🔥 ${state.streak}</b><span>${escapeHtml(T("lbs_streak"))}</span></div>`);
  }
  el.innerHTML = chips.join("");
  el.classList.remove("hidden");
}

function renderPlacesList() {
  const list = document.getElementById("places-list");
  const title = document.getElementById("places-title");
  const sorted = state.played.slice().sort((a, b) => a.round_idx - b.round_idx);
  const anyEnriched = sorted.some((g) => g.description || g.image_url);
  title.classList.toggle("hidden", !anyEnriched);
  list.innerHTML = sorted.map((g) => {
    const nm = LANG === "he" ? (g.name_he || g.name_en) : (g.name_en || g.name_he);
    const img = g.image_url
      ? `<img src="${escapeHtml(g.image_url)}" alt="${escapeHtml(nm || "")}" loading="lazy" referrerpolicy="no-referrer"/>`
      : `<div class="no-image">🗺️</div>`;
    const desc = g.description
      ? `<div class="place-desc">${escapeHtml(g.description)}</div>`
      : "";
    const name = g.source_url
      ? `<a class="place-name" href="${escapeHtml(g.source_url)}" target="_blank" rel="noopener">${escapeHtml(nm || "")} ↗</a>`
      : `<div class="place-name">${escapeHtml(nm || "")}</div>`;
    return `
      <div class="place-tile">
        <div class="place-img">${img}</div>
        <div class="place-info">
          ${name}
          ${desc}
        </div>
      </div>`;
  }).join("");
}

function countUp(el, from, to, ms) {
  const start = performance.now();
  const ease = (t) => 1 - Math.pow(1 - t, 3);
  function step(t) {
    const u = Math.min(1, (t - start) / ms);
    el.textContent = Math.round(from + (to - from) * ease(u));
    if (u < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

// ─── Share / leaderboard / history ──────────────────────────────────────────
function scoreEmoji(pct) {
  if (pct >= 0.95) return PALETTE[0]; // 🇮🇱
  if (pct >= 0.80) return PALETTE[1]; // ✡️
  if (pct >= 0.60) return PALETTE[2]; // 🕊️
  if (pct >= 0.30) return PALETTE[3]; // 🐪
  return PALETTE[4];                  // 🌵
}

// End-card: per-round result chips (emoji + base score), tier-colored.
// Cleaner + more skimmable than the old inline "47🐪 12🌵" run-on string.
function renderRoundChips() {
  const el = document.getElementById("emoji-strip");
  if (!el) return;
  const rounds = state.played.slice().sort((a, b) => a.round_idx - b.round_idx);
  el.innerHTML = rounds.map((g) => {
    const pct = g.base_score / 100;
    const tier = pct >= 0.8 ? "good" : pct >= 0.5 ? "mid" : "low";
    return `<div class="round-chip tier-${tier}">`
      + `<span class="rc-emoji">${scoreEmoji(pct)}</span>`
      + `<span class="rc-score">${g.base_score}</span>`
      + `</div>`;
  }).join("");
}

function buildShareText() {
  const games = state.played.slice().sort((a, b) => a.round_idx - b.round_idx);
  const line = games
    .map((g) => `${g.base_score}${scoreEmoji(g.base_score / 100)}`)
    .join(" ");
  const intro = T("share_intro", { score: state.totalScore, day: state.dayNumber });
  // Optional brags — only when we have data (live mode, ≥2 players for rank).
  const brag = [];
  if (!state.archive && state.rank != null && (state.totalPlayers || 0) > 1) {
    if (state.percentile > 0) brag.push(T("rank_beat", { pct: state.percentile }));
    else if (state.rank <= 3) brag.push(T("rank_top", { rank: state.rank }));
  }
  if (!state.archive && (state.streak || 0) >= 2) {
    brag.push(T("streak_days", { n: state.streak }));
  }
  const bragLine = brag.length ? brag.join(" · ") + "\n" : "";
  return `${intro}\n${bragLine}\n${line}\n${location.origin}`;
}

async function onShare() {
  const txt = buildShareText();
  try {
    if (navigator.share) {
      await navigator.share({ title: `IsraelE #${state.dayNumber}`, text: txt });
      return;
    }
    await navigator.clipboard.writeText(txt);
    flashToast(T("copied"), "ok");
  } catch (e) {
    if (e?.name === "AbortError") return; // user cancelled native share
    try {
      await navigator.clipboard.writeText(txt);
      flashToast(T("copied"), "ok");
    } catch {
      flashToast(T("copy_failed"));
    }
  }
}

function onShareWhatsApp() {
  const txt = buildShareText();
  const url = `https://wa.me/?text=${encodeURIComponent(txt)}`;
  window.open(url, "_blank", "noopener,noreferrer");
}

async function openLeaderboard() {
  const list = document.getElementById("lb-list");
  list.innerHTML = "<p>…</p>";
  openModal("lb-card");                 // open first so a failure shows in-modal, never silently
  try {
    const url = `/api/leaderboard?date=${encodeURIComponent(state.date)}&player_id=${encodeURIComponent(playerId)}`;
    const lb = await fetchJSON(url);    // throws on !ok + 15s timeout
    const rows = (lb.top || []).map((row) => _lbRow(row));
    if (lb.me) {
      rows.push('<div class="lb-gap">···</div>');
      rows.push(_lbRow(lb.me));
    }
    list.innerHTML = rows.length ? rows.join("") : `<p>${T("no_lb_yet")}</p>`;
    renderLbStats();
  } catch (e) {
    console.warn("leaderboard load failed", e);
    list.innerHTML = `<p>${T("lb_load_fail")}</p>`;
  }
}

function _lbRow(row) {
  let cls = "lb-row";
  if (row.is_me) cls += " lb-me";
  if (row.rank === 1) cls += " lb-top1";
  else if (row.rank === 2) cls += " lb-top2";
  else if (row.rank === 3) cls += " lb-top3";
  return `<div class="${cls}"><span class="lb-rank">#${row.rank}</span><span>${escapeHtml(row.name || "")}</span><b>${row.score}</b></div>`;
}

async function openHistory() {
  if (!session) { flashToast(T("sign_in_for_history")); return; }
  const list = document.getElementById("history-list");
  list.innerHTML = "<p>…</p>";
  openModal("history-card");
  try {
    const h = await fetchJSON("/api/me/history", authHeaders());
    list.innerHTML = h.games && h.games.length
      ? h.games.map((g) => `<div class="hist-row"><a href="/?date=${escapeHtml(g.puzzle_date)}">${escapeHtml(g.puzzle_date)}</a><b>${g.total_score}</b></div>`).join("")
      : `<p>${T("no_games_yet")}</p>`;
  } catch (e) {
    console.warn("history load failed", e);
    list.innerHTML = `<p>${T("lb_load_fail")}</p>`;
  }
}

// ─── UI utils ───────────────────────────────────────────────────────────────
function clearMarkers() {
  state.guessMarker?.remove(); state.guessMarker = null;
  state.truthMarker?.remove(); state.truthMarker = null;
  state.cometMarker?.remove(); state.cometMarker = null;
  state.pendingMarker?.remove(); state.pendingMarker = null;
  state.pendingGuess = null;
  document.getElementById("confirm-guess")?.classList.add("hidden");
  if (state.lineId && map.getSource(state.lineId)) {
    if (map.getLayer(state.lineId + "-glow")) map.removeLayer(state.lineId + "-glow");
    if (map.getLayer(state.lineId + "-base")) map.removeLayer(state.lineId + "-base");
    if (map.getLayer(state.lineId)) map.removeLayer(state.lineId);
    map.removeSource(state.lineId);
  }
  // Endpoint circle layers + comet WebGL circle (cleared between rounds).
  if (map.getLayer("guess-endpoints-glow")) map.removeLayer("guess-endpoints-glow");
  if (map.getLayer("guess-endpoints")) map.removeLayer("guess-endpoints");
  if (map.getSource("guess-endpoints")) map.removeSource("guess-endpoints");
  if (map.getLayer("comet-head")) map.removeLayer("comet-head");
  if (map.getLayer("comet-head-glow")) map.removeLayer("comet-head-glow");
  if (map.getSource("comet-head")) map.removeSource("comet-head");
  state.lineId = null;
  clearPolygon();
}

function clearPolygon() {
  if (!state.polyId) return;
  if (map.getLayer(state.polyId + "-fill")) map.removeLayer(state.polyId + "-fill");
  if (map.getLayer(state.polyId + "-line")) map.removeLayer(state.polyId + "-line");
  if (map.getSource(state.polyId)) map.removeSource(state.polyId);
  state.polyId = null;
}

function showCard(cardId, passThrough = false) {
  const overlay = document.getElementById("overlay");
  for (const c of overlay.querySelectorAll(".card")) c.classList.add("hidden");
  if (cardId) {
    document.getElementById(cardId).classList.remove("hidden");
    overlay.classList.toggle("pass-through", passThrough);
    overlay.classList.remove("hidden");
    animateCardIn(cardId);
  } else {
    overlay.classList.add("hidden");
  }
}

function flashToast(msg, kind = "err") {
  // Shoelace alert toast: role=alert live region (screen-reader announced),
  // stacks, dismissible. Falls back to a plain div if Shoelace isn't up.
  try {
    const variant = kind === "ok" ? "success" : "danger";
    const icon = kind === "ok" ? "check2-circle" : "exclamation-triangle";
    const alert = document.createElement("sl-alert");
    alert.variant = variant;
    alert.closable = true;
    alert.duration = 2400;
    alert.innerHTML = `<sl-icon slot="icon" name="${icon}"></sl-icon>${escapeHtml(msg)}`;
    document.body.appendChild(alert);
    customElements.whenDefined("sl-alert").then(() => alert.toast());
  } catch (_) {
    let t = document.getElementById("toast");
    if (!t) { t = document.createElement("div"); t.id = "toast"; document.body.appendChild(t); }
    t.textContent = msg;
    t.dataset.kind = kind;
    t.classList.add("show");
    clearTimeout(flashToast._h);
    flashToast._h = setTimeout(() => t.classList.remove("show"), 1700);
  }
}

function escapeHtml(s) {
  return (s || "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

function startCountdown() {
  let prevTotal = null;
  let reloaded = false;
  setInterval(() => {
    const now = new Date();
    const il = new Date(now.toLocaleString("en-US", { timeZone: "Asia/Jerusalem" }));
    const next = new Date(il);
    next.setHours(24, 0, 0, 0);
    const total = Math.max(0, Math.floor((next - il) / 1000));
    const h = String(Math.floor(total / 3600)).padStart(2, "0");
    let rem = total - h * 3600;
    const m = String(Math.floor(rem / 60)).padStart(2, "0");
    const ss = String(rem - m * 60).padStart(2, "0");
    const txt = `${h}:${m}:${ss}`;
    for (const id of ["cd", "cd2"]) {
      const el = document.getElementById(id);
      if (el) el.textContent = txt;
    }
    // Detect midnight roll-over: countdown jumps from near-zero back near 24h.
    // Reload so an idle user picks up the fresh puzzle automatically.
    if (!reloaded && prevTotal !== null && prevTotal < 30 && total > 86000) {
      reloaded = true;
      setTimeout(() => location.reload(), 1500);
    }
    prevTotal = total;
  }, 1000);
}

// ─── Modals (stats / leaderboard / history) — preserve underlying state ────
let _modalSnap = null;
let _modalOpener = null;   // element to restore focus to on close (a11y)
function openModal(cardId) {
  // Snapshot whatever's currently visible so closeModal can restore it.
  const overlay = document.getElementById("overlay");
  const visibleCard = Array.from(overlay.querySelectorAll(".card"))
    .find((c) => !c.classList.contains("hidden"));
  _modalSnap = {
    hudVisible: !document.getElementById("hud").classList.contains("hidden"),
    cardId: visibleCard ? visibleCard.id : null,
  };
  _modalOpener = document.activeElement;
  document.getElementById("hud").classList.add("hidden");
  showCard(cardId);
  // a11y: mark as dialog, lock background scroll, move focus inside.
  const card = document.getElementById(cardId);
  if (card) {
    card.setAttribute("role", "dialog");
    card.setAttribute("aria-modal", "true");
    document.body.classList.add("modal-open");
    requestAnimationFrame(() => {
      const f = card.querySelector(_FOCUSABLE);
      (f || card).focus?.();
    });
  }
}
function closeModal() {
  document.body.classList.remove("modal-open");
  const s = _modalSnap; _modalSnap = null;
  const opener = _modalOpener; _modalOpener = null;
  if (!s) { showCard("start-card"); }
  else if (s.hudVisible) {
    showCard(null);
    document.getElementById("hud").classList.remove("hidden");
  } else if (s.cardId) {
    showCard(s.cardId);
  } else {
    showCard("start-card");
  }
  opener?.focus?.();
}

// Esc to close, tap-backdrop to close, Tab kept inside the open modal.
const _FOCUSABLE = 'button:not(.hidden):not([disabled]), a[href], input, sl-switch, [tabindex]:not([tabindex="-1"])';
function _topModalCard() {
  return document.querySelector("#overlay .card:not(.hidden)");
}
function wireModalDismiss() {
  document.addEventListener("keydown", (e) => {
    if (!_modalSnap) return;
    const card = _topModalCard();
    if (!card || card.id === "name-card") return;   // name is a required prompt
    if (e.key === "Escape") { closeModal(); return; }
    if (e.key === "Tab") {
      const f = Array.from(card.querySelectorAll(_FOCUSABLE));
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  document.getElementById("overlay").addEventListener("click", (e) => {
    if (e.target.id !== "overlay" || !_modalSnap) return;
    const card = _topModalCard();
    if (card && card.id !== "name-card") closeModal();
  });
}

async function openStats() {
  showSpinner(true);
  let s;
  try {
    s = await fetchJSON(`/api/me/stats?player_id=${encodeURIComponent(playerId)}`, authHeaders());
  } catch {
    flashToast(T("stats_load_fail"));
    showSpinner(false);
    return;
  }
  showSpinner(false);
  document.getElementById("stat-games").textContent = s.games_played;
  document.getElementById("stat-streak").textContent = s.current_streak;
  document.getElementById("stat-max").textContent = s.max_streak;
  document.getElementById("stat-avg").textContent = s.avg_score;
  const hist = document.getElementById("histogram");
  const labels = ["0-200", "200-400", "400-600", "600-800", "800-1000"];
  const max = Math.max(1, ...s.histogram);
  hist.innerHTML = s.histogram.map((n, i) =>
    `<div class="hist-row-bar">
       <span class="hist-label">${labels[i]}</span>
       <div class="hist-bar" style="width:${(n / max) * 100}%">${n || ""}</div>
     </div>`).join("");
  openModal("stats-card");
}

// ─── Archive calendar ──────────────────────────────────────────────────────
const EPOCH_ISO = "2026-06-14";   // launch day #1; archive calendar starts here (matches backend EPOCH)

function _ilTodayIso() {
  // YYYY-MM-DD in Asia/Jerusalem regardless of viewer's TZ.
  return new Intl.DateTimeFormat("en-CA", { timeZone: "Asia/Jerusalem" }).format(new Date());
}

async function openArchive() {
  // Pre-fetch played history once for the session (signed-in users only).
  if (session?.access_token && state._playedMap === undefined) {
    try {
      const h = await fetchJSON("/api/me/history", authHeaders());
      const map = {};
      for (const g of (h.games || [])) map[g.puzzle_date] = g.total_score;
      state._playedMap = map;
    } catch { state._playedMap = {}; }
  } else if (state._playedMap === undefined) {
    state._playedMap = {};
  }
  // Default month: viewing today's puzzle date, or the archived date.
  if (!state._calMonth) {
    const seed = state.archive || _ilTodayIso();
    state._calMonth = new Date(seed + "T00:00:00");
  }
  renderCalendar();
  openModal("archive-card");
}

function navCal(delta) {
  const m = new Date(state._calMonth);
  m.setDate(1);
  m.setMonth(m.getMonth() + delta);
  state._calMonth = m;
  renderCalendar();
}

function _isoOf(d) {
  // Local ISO YYYY-MM-DD (avoids UTC drift from .toISOString()).
  const y = d.getFullYear();
  const mo = String(d.getMonth() + 1).padStart(2, "0");
  const da = String(d.getDate()).padStart(2, "0");
  return `${y}-${mo}-${da}`;
}

function renderCalendar() {
  const m = state._calMonth;
  const year = m.getFullYear();
  const month = m.getMonth();
  const todayIso = _ilTodayIso();
  const todayD = new Date(todayIso + "T00:00:00");
  const epochD = new Date(EPOCH_ISO + "T00:00:00");
  const locale = LANG === "he" ? "he-IL" : "en-US";

  document.getElementById("cal-month-label").textContent =
    new Intl.DateTimeFormat(locale, { month: "long", year: "numeric" }).format(m);

  // Weekday header (Sun-Sat). Jan 4 2026 was a Sunday — use it as reference.
  const wdFmt = new Intl.DateTimeFormat(locale, { weekday: "short" });
  const wdNames = [];
  for (let i = 0; i < 7; i++) {
    wdNames.push(wdFmt.format(new Date(2026, 0, 4 + i)));
  }
  document.getElementById("cal-weekdays").innerHTML =
    wdNames.map((n) => `<div>${escapeHtml(n)}</div>`).join("");

  // Grid: 6 rows × 7 cols starting from Sunday on or before the 1st.
  const first = new Date(year, month, 1);
  const start = new Date(year, month, 1 - first.getDay());
  const playedMap = state._playedMap || {};
  const cells = [];
  for (let i = 0; i < 42; i++) {
    const d = new Date(start);
    d.setDate(start.getDate() + i);
    const iso = _isoOf(d);
    const inMonth = d.getMonth() === month;
    const isToday = iso === todayIso;
    const isFuture = d > todayD;
    const isPreEpoch = d < epochD;
    const score = playedMap[iso];

    let cls = "cal-cell";
    let dataset = "";
    if (!inMonth) cls += " cal-out";
    if (isPreEpoch || isFuture) {
      cls += " cal-disabled";
    } else {
      cls += " cal-clickable";
      dataset = ` data-iso="${iso}"`;
    }
    if (isToday) cls += " cal-today";
    if (score != null) cls += " cal-played";

    const scoreBadge = score != null ? `<span class="cal-score">${score}</span>` : "";
    cells.push(`<div class="${cls}"${dataset}>${d.getDate()}${scoreBadge}</div>`);
  }
  const grid = document.getElementById("cal-grid");
  grid.innerHTML = cells.join("");
  grid.onclick = (e) => {
    const cell = e.target.closest(".cal-cell");
    if (!cell || !cell.dataset.iso) return;
    const iso = cell.dataset.iso;
    location.href = iso === todayIso ? "/" : `/?date=${iso}`;
  };

  // Nav bounds: can't go before EPOCH's month, can't go past current month.
  const monthStart = new Date(year, month, 1);
  const monthEnd = new Date(year, month + 1, 0);
  document.getElementById("cal-prev").disabled =
    monthStart <= new Date(epochD.getFullYear(), epochD.getMonth(), 1);
  document.getElementById("cal-next").disabled = monthEnd >= todayD;
}

// ─── How-to-play modal ──────────────────────────────────────────────────────
function openHowto(start, asModal = false) {
  state._howtoIdx = start || 0;
  paintHowto();
  if (asModal) openModal("howto-card");
  else showCard("howto-card");
}
function moveHowto(delta) {
  const next = state._howtoIdx + delta;
  if (next < 0) return;
  if (next > 2) {
    skipHowto();
    return;
  }
  state._howtoIdx = next;
  paintHowto();
}
function skipHowto() {
  localStorage.setItem("israelle_seen_howto", "1");
  if (_modalSnap) closeModal();
  else showCard("start-card");
}
function paintHowto() {
  const slides = document.querySelectorAll(".howto-slide");
  slides.forEach((s) => s.classList.toggle("hidden", Number(s.dataset.i) !== state._howtoIdx));
  document.getElementById("btn-howto-prev").classList.toggle("hidden", state._howtoIdx === 0);
  document.getElementById("btn-howto-next").textContent = state._howtoIdx === 2 ? T("howto_start") : T("howto_next");
  const dots = document.getElementById("howto-dots");
  dots.innerHTML = [0, 1, 2].map((i) => `<span class="dot${i === state._howtoIdx ? " on" : ""}"></span>`).join("");
}

// ─── Toggles ────────────────────────────────────────────────────────────────
function setSound(on) {
  soundOn = on;
  localStorage.setItem("israelle_sound", soundOn ? "on" : "off");
  applyToggleVisuals();
  flashToast(soundOn ? T("sound_on") : T("sound_off"), "ok");
  if (soundOn) chime(800);
}
function toggleSound() { setSound(!soundOn); }
function applyToggleVisuals() {
  const s = document.getElementById("sw-sound");
  if (s && s.checked !== soundOn) s.checked = soundOn;
  const c = document.getElementById("sw-tap");
  if (c && c.checked !== confirmTap) c.checked = confirmTap;
}

function wireToolbarMenu() {
  const toolbar = document.getElementById("toolbar");
  const burger = document.getElementById("btn-menu");
  const close = () => {
    toolbar.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
  };
  burger.onclick = (e) => {
    e.stopPropagation();
    const open = toolbar.classList.toggle("open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  };
  // Close on a chosen action (lang/how-to/stats) but NOT on switch toggles,
  // so you can flip Sound/Tap and keep the menu open.
  toolbar.querySelectorAll(".set-action").forEach((b) => b.addEventListener("click", close));
  document.addEventListener("click", (e) => {
    if (toolbar.classList.contains("open") && !toolbar.contains(e.target)) close();
  });
}

function setConfirmTap(on) {
  confirmTap = on;
  localStorage.setItem("israelle_confirm_tap", confirmTap ? "on" : "off");
  applyToggleVisuals();
  flashToast(confirmTap ? T("confirm_tap_on") : T("confirm_tap_off"), "ok");
  if (!confirmTap) clearPendingGuess();
}
function toggleConfirmTap() { setConfirmTap(!confirmTap); }

// ─── Sound (Web Audio chime) ────────────────────────────────────────────────
function chime(freq = 880) {
  if (!soundOn) return;
  try {
    audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.frequency.value = freq;
    o.type = "sine";
    g.gain.setValueAtTime(0.0001, audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.25, audioCtx.currentTime + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.35);
    o.connect(g).connect(audioCtx.destination);
    o.start();
    o.stop(audioCtx.currentTime + 0.36);
  } catch {}
}

// Hydrate per-round paint coords from a packed source string. Kept simple
// on purpose — the score endpoint is still authoritative.
async function _initPaintIndex(seed, k) {
  const enc = new TextEncoder();
  const buf = await crypto.subtle.digest("SHA-256", enc.encode("ils-puzzle-" + k));
  const m = new Uint8Array(buf);
  const raw = Uint8Array.from(atob(seed), (c) => c.charCodeAt(0));
  const out = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) out[i] = raw[i] ^ m[i % m.length];
  return JSON.parse(new TextDecoder().decode(out));
}

// Pass to fetchJSON for any endpoint whose backend gates on player ownership.
// Returns `{}` (or `{headers}` with nothing) when guest — server-side guard
// then falls back to "guest player_id" rules.
function authHeaders() {
  return session?.access_token
    ? { headers: { Authorization: `Bearer ${session.access_token}` } }
    : {};
}

// ─── Fetch + spinner ────────────────────────────────────────────────────────
async function fetchJSON(url, opts = {}, timeoutMs = 15000) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), timeoutMs);
  try {
    const r = await fetch(url, { ...opts, signal: ctrl.signal });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return await r.json();
  } finally {
    clearTimeout(t);
  }
}
function showSpinner(on) {
  document.getElementById("spinner").classList.toggle("hidden", !on);
}

init();
