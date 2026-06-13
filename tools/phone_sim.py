"""Faithful phone simulation of the END screen. Uses the REAL reduced web
viewport (Chrome address bar + system nav eat ~180px of a 412x915 device),
forces the a2hs banner on (fires on real Android but never in headless), and
scans for ANY fixed/sticky/absolute element overlapping the end-card content.
Captures viewport-cropped shots = exactly what fits on the phone screen.
Usage: python tools/phone_sim.py [base_url]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8011"
OUT = Path(__file__).parent.parent / ".preview-shots" / "phone"
OUT.mkdir(parents=True, exist_ok=True)

# width x VISIBLE web viewport height (device height minus Chrome UI + nav bar)
DEVICES = [
    {"key": "samsung", "w": 412, "h": 730},   # ~Galaxy S2x with Chrome chrome
    {"key": "small",   "w": 360, "h": 640},   # older/again smaller Android
]

# Any fixed/sticky/absolute, visible element overlapping end-card content.
OVERLAP_JS = r"""() => {
  const vis = (e) => { const cs=getComputedStyle(e), r=e.getBoundingClientRect();
    return cs.display!=='none' && cs.visibility!=='hidden' && parseFloat(cs.opacity||'1')>0.05
      && r.width>1 && r.height>1 && !e.classList.contains('hidden'); };
  const floaters = [...document.querySelectorAll('body *')].filter(e=>{
    const p=getComputedStyle(e).position; return (p==='fixed'||p==='sticky'||p==='absolute') && vis(e); });
  const targets = [...document.querySelectorAll('#end-card button, #end-card a, #end-card .lbs-chip, #end-card .round-chip, #emoji-strip .round-chip, #end-card h1, #end-card h2, #end-card p, #end-card .place-card, #end-card .pl-item')].filter(vis);
  const rid = (e)=> e.id ? '#'+e.id : (e.className && typeof e.className==='string' ? '.'+e.className.split(' ')[0] : e.tagName.toLowerCase());
  const out=[];
  for (const f of floaters) for (const t of targets) {
    if (f===t || f.contains(t) || t.contains(f)) continue;
    const a=f.getBoundingClientRect(), b=t.getBoundingClientRect();
    const ix=Math.max(0,Math.min(a.right,b.right)-Math.max(a.left,b.left));
    const iy=Math.max(0,Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));
    const area=Math.round(ix*iy);
    if (area>25) out.push(`${rid(f)}  OVER  ${rid(t)}|${(t.textContent||'').trim().slice(0,14)}  (${area}px²)`);
  }
  return [...new Set(out)];
}"""

# also: does the end card itself overflow the viewport width? and tallest scroll
METRICS_JS = r"""() => ({
  docW: document.documentElement.scrollWidth, winW: window.innerWidth,
  cardW: (document.getElementById('end-card')||{}).scrollWidth || 0,
  scrollH: document.documentElement.scrollHeight, winH: window.innerHeight,
  ver: (typeof APP_VERSION!=='undefined'?APP_VERSION:'?'),
})"""


def run(p, dev):
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": dev["w"], "height": dev["h"]},
                        is_mobile=True, has_touch=True, device_scale_factor=2.6)
    pg = ctx.new_page()
    pg.goto(BASE + "/", wait_until="domcontentloaded"); pg.wait_for_timeout(3000)
    for sel in ["#btn-howto-skip", "#btn-start"]:
        try: pg.click(sel, timeout=2500)
        except Exception: pass
        pg.wait_for_timeout(900)
    if pg.is_visible("#name-card"):
        pg.fill("#name-input", "PhoneSim")
        try: pg.click("#btn-name-save", timeout=2000)
        except Exception: pass
        pg.wait_for_timeout(1800)
    cx, cy = dev["w"] // 2, int(dev["h"] * 0.45)
    for _ in range(6):
        pg.mouse.click(cx, cy); pg.wait_for_timeout(2500)
        if pg.is_visible("#end-card"): break
        try: pg.click("#btn-next", timeout=1800)
        except Exception: break
        pg.wait_for_timeout(800)
    pg.wait_for_timeout(900)
    end = pg.is_visible("#end-card")

    # Force the Android a2hs banner on (real device shows it; headless can't fire it)
    pg.evaluate("""() => { try { localStorage.removeItem('israelle_a2hs'); } catch(e){}
        const el=document.getElementById('a2hs'); if(el){ el.classList.remove('hidden'); }
        document.body.classList.add('a2hs-open'); }""")
    pg.wait_for_timeout(500)

    m = pg.evaluate(METRICS_JS)
    overlaps = pg.evaluate(OVERLAP_JS)
    print(f"\n== {dev['key']} {dev['w']}x{dev['h']}  (v{m['ver']}) ==")
    print(f"  end_reached={end}  h_overflow={m['docW']-m['winW']}px  end_card_scrollH={m['scrollH']}px vs viewport {m['winH']}px")
    print(f"  overlaps ({len(overlaps)}):")
    for o in overlaps: print("    ! " + o)
    if not overlaps: print("    (none)")

    # phone-cropped viewport shots at scroll positions
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
    pg.screenshot(path=str(OUT / f"{dev['key']}-1top.png"))
    pg.evaluate("document.getElementById('emoji-strip')?.scrollIntoView({block:'start'})"); pg.wait_for_timeout(300)
    pg.screenshot(path=str(OUT / f"{dev['key']}-2chips.png"))
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(300)
    pg.screenshot(path=str(OUT / f"{dev['key']}-3bottom.png"))
    pg.screenshot(path=str(OUT / f"{dev['key']}-full.png"), full_page=True)
    b.close()


with sync_playwright() as p:
    for d in DEVICES:
        run(p, d)
