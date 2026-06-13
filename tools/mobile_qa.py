"""Mobile QA masterclass: multi-device live playthrough + overlap/overflow/error audit.
Drives our own Chromium (org policy blocks managed Chrome). Live mode (no ?date) because
EPOCH moved to launch day so archive dates are out of range. QA games on today's board get
wiped by the launch reset.
Usage: python tools/mobile_qa.py [base_url]   (default http://127.0.0.1:8011)
"""
import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8011"
OUT = Path(__file__).parent.parent / ".preview-shots" / "qa2"
OUT.mkdir(parents=True, exist_ok=True)

UA_IOS = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
          "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
UA_ANDROID = ("Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/124.0.0.0 Mobile Safari/537.36")

DEVICES = [
    {"key": "se",     "label": "iPhone SE",  "w": 320, "h": 568, "ios": True,  "ua": UA_IOS},
    {"key": "ip13",   "label": "iPhone 13",  "w": 390, "h": 844, "ios": True,  "ua": UA_IOS},
    {"key": "pixel7", "label": "Pixel 7",    "w": 412, "h": 915, "ios": False, "ua": UA_ANDROID},
]

OVERFLOW_JS = "(() => ({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth}))()"

# bounding-box intersection of two selectors (null if either missing/hidden)
RECT_JS = """(sel) => { const e = document.querySelector(sel);
  if (!e) return null; const r = e.getBoundingClientRect();
  const cs = getComputedStyle(e);
  if (cs.display==='none' || cs.visibility==='hidden' || r.width===0 || r.height===0) return null;
  return {x:r.x,y:r.y,w:r.width,h:r.height,bottom:r.bottom,right:r.right}; }"""

# tiny / hard-to-read text scan: visible elements with own text < 11px
TINY_TEXT_JS = """(() => {
  const out=[];
  for (const e of document.querySelectorAll('body *')) {
    const own = [...e.childNodes].some(n=>n.nodeType===3 && n.textContent.trim());
    if (!own) continue;
    const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
    if (cs.display==='none'||cs.visibility==='hidden'||r.width===0||r.height===0) continue;
    const fs = parseFloat(cs.fontSize);
    if (fs < 11) out.push({tag:e.tagName.toLowerCase(), id:e.id||null, fs:Math.round(fs*10)/10,
       txt:(e.textContent||'').trim().slice(0,30)});
  }
  return out.slice(0,12);
})()"""


def intersect(a, b):
    if not a or not b:
        return 0.0
    ix = max(0, min(a["right"], b["right"]) - max(a["x"], b["x"]))
    iy = max(0, min(a["bottom"], b["bottom"]) - max(a["y"], b["y"]))
    return ix * iy


def run_device(p, dev):
    res = {"device": dev["label"], "console_errors": [], "page_errors": [],
           "failed_requests": [], "bad_responses": [], "overflow": {}, "tiny_text": {},
           "rounds_played": 0, "end_reached": False, "a2hs": {}, "leaderboard_ok": False,
           "notes": []}
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": dev["w"], "height": dev["h"]},
                              device_scale_factor=3, is_mobile=True, has_touch=True,
                              user_agent=dev["ua"])
    page = ctx.new_page()
    page.on("console", lambda m: res["console_errors"].append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: res["page_errors"].append(str(e)))
    page.on("requestfailed", lambda r: res["failed_requests"].append(
        f"{r.url} :: {r.failure}") if "favicon" not in r.url else None)
    page.on("response", lambda r: res["bad_responses"].append(f"{r.status} {r.url}")
            if r.status >= 400 and "favicon" not in r.url else None)

    def ovf(state):
        d = page.evaluate(OVERFLOW_JS)
        res["overflow"][state] = {"scroll": d["sw"], "client": d["cw"],
                                  "overflow": d["sw"] - d["cw"]}

    def click_if(sel, t=1500):
        try:
            page.click(sel, timeout=t); return True
        except Exception:
            return False

    def shot(name):
        page.screenshot(path=str(OUT / f"{dev['key']}-{name}.png"))

    page.goto(BASE + "/", wait_until="domcontentloaded")
    page.wait_for_timeout(3500)
    click_if("#btn-howto-skip", 2500)
    page.wait_for_timeout(500)
    ovf("start"); shot("1start")
    res["tiny_text"]["start"] = page.evaluate(TINY_TEXT_JS)

    # start guest game
    click_if("#btn-start", 2500)
    page.wait_for_timeout(1200)
    if page.is_visible("#name-card"):
        page.fill("#name-input", "QA רואי")
        click_if("#btn-name-save")
        page.wait_for_timeout(2000)
    page.wait_for_timeout(1200)
    ovf("hud"); shot("2hud")
    res["tiny_text"]["hud"] = page.evaluate(TINY_TEXT_JS)

    # play through (live, confirmTap off → click submits)
    cx, cy = dev["w"] // 2, int(dev["h"] * 0.5)
    for rnd in range(6):
        page.mouse.click(cx, cy)
        page.wait_for_timeout(800)
        click_if("#btn-confirm-guess", 900)   # no-op if confirmTap off
        page.wait_for_timeout(1500)
        if rnd == 0:
            ovf("reveal"); shot("3reveal")
            res["tiny_text"]["reveal"] = page.evaluate(TINY_TEXT_JS)
        res["rounds_played"] = rnd + 1
        if page.is_visible("#end-card"):
            break
        if not click_if("#btn-next", 1800):
            res["notes"].append(f"no #btn-next after round {rnd+1} (click may have missed land)")
            break
        page.wait_for_timeout(900)

    page.wait_for_timeout(1500)
    res["end_reached"] = page.is_visible("#end-card")
    if res["end_reached"]:
        ovf("end"); shot("4end")
        res["tiny_text"]["end"] = page.evaluate(TINY_TEXT_JS)
        res["end_round_chips"] = page.eval_on_selector_all("#emoji-strip .round-chip", "els => els.length")

        # force-show a2hs (iOS variant needs no beforeinstallprompt) and test overlap vs CTAs
        page.evaluate("localStorage.removeItem('israelle_a2hs')")
        shown = page.evaluate("(() => { try { maybeShowA2HS(); } catch(e){ return 'err:'+e.message; } "
                              "return !document.getElementById('a2hs').classList.contains('hidden'); })()")
        page.wait_for_timeout(700)
        a2 = page.evaluate(RECT_JS, "#a2hs")
        res["a2hs"]["shown"] = shown
        res["a2hs"]["visible_box"] = bool(a2)
        if a2:
            for sel in ["#btn-share-wa", "#btn-share", "#btn-leaderboard"]:
                box = page.evaluate(RECT_JS, sel)
                res["a2hs"].setdefault("overlaps", {})[sel] = round(intersect(a2, box), 1)
            shot("5end-a2hs")
    else:
        res["notes"].append("END NOT REACHED")

    # leaderboard
    page.evaluate("document.getElementById('a2hs')?.classList.add('hidden')")
    if click_if("#btn-leaderboard", 2500):
        page.wait_for_timeout(1500)
        res["leaderboard_ok"] = page.is_visible("#lb-card")
        ovf("leaderboard"); shot("6leaderboard")
        res["tiny_text"]["leaderboard"] = page.evaluate(TINY_TEXT_JS)

    browser.close()
    return res


def main():
    with sync_playwright() as p:
        allres = [run_device(p, d) for d in DEVICES]
    (OUT / "summary.json").write_text(json.dumps(allres, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(allres, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
