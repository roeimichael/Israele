"""Verify the end screen on a phone viewport: top bar (burger) hidden, end card
fits width, and the round chips aren't overlapped by anything fixed. Screenshots
the end card scrolled to the chips so we can eyeball it. Pixel 7 (412) + SE (320).
Usage: python tools/end_overlap_test.py [base_url]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8011"
OUT = Path(__file__).parent.parent / ".preview-shots" / "qa2"
OUT.mkdir(parents=True, exist_ok=True)
DEVICES = [{"key": "pixel7", "w": 412, "h": 915}, {"key": "se", "w": 320, "h": 568}]


def run(p, dev):
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": dev["w"], "height": dev["h"]}, is_mobile=True,
                        has_touch=True, device_scale_factor=3)
    pg = ctx.new_page()
    pg.goto(BASE + "/", wait_until="domcontentloaded"); pg.wait_for_timeout(3000)
    for sel in ["#btn-howto-skip", "#btn-start"]:
        try: pg.click(sel, timeout=2500)
        except Exception: pass
        pg.wait_for_timeout(900)
    if pg.is_visible("#name-card"):
        pg.fill("#name-input", "EndTest")
        try: pg.click("#btn-name-save", timeout=2000)
        except Exception: pass
        pg.wait_for_timeout(1800)
    cx, cy = dev["w"] // 2, int(dev["h"] * 0.5)
    for _ in range(6):
        pg.mouse.click(cx, cy); pg.wait_for_timeout(2600)
        if pg.is_visible("#end-card"): break
        if not _click(pg, "#btn-next"): break
        pg.wait_for_timeout(800)
    pg.wait_for_timeout(800)
    end = pg.is_visible("#end-card")
    topbar_hidden = pg.evaluate("document.getElementById('topbar')?.classList.contains('hidden')")
    # horizontal overflow + burger-vs-chip overlap after scrolling to chips
    pg.evaluate("document.getElementById('emoji-strip')?.scrollIntoView({block:'center'})")
    pg.wait_for_timeout(500)
    ov = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    overlap = pg.evaluate("""() => {
      const tb=document.getElementById('topbar'), strip=document.getElementById('emoji-strip');
      if(!tb||!strip) return 'n/a';
      const cs=getComputedStyle(tb);
      if(cs.display==='none'||tb.classList.contains('hidden')) return 0;
      const a=tb.getBoundingClientRect(), b=strip.getBoundingClientRect();
      const ix=Math.max(0,Math.min(a.right,b.right)-Math.max(a.left,b.left));
      const iy=Math.max(0,Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));
      return Math.round(ix*iy);
    }""")
    pg.screenshot(path=str(OUT / f"{dev['key']}-end-fixed.png"))
    print(f"{dev['key']}: end={end} topbar_hidden={topbar_hidden} h_overflow={ov} burger_x_chips={overlap}")
    b.close()


def _click(pg, sel, t=1800):
    try: pg.click(sel, timeout=t); return True
    except Exception: return False


with sync_playwright() as p:
    for d in DEVICES:
        run(p, d)
