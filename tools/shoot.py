"""Dev-only: headless phone screenshots + functional checks of the local app.
Bypasses the managed-Chrome org policy by driving our own Chromium.
Usage: python tools/shoot.py [base_url]   (default http://127.0.0.1:8000)
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"
OUT = Path(__file__).parent.parent / ".preview-shots"
OUT.mkdir(exist_ok=True)
checks = []


def shot(page, name):
    page.screenshot(path=str(OUT / name))
    print("  +", name)


def check(name, ok):
    checks.append((name, ok))
    print(("  PASS " if ok else "  FAIL ") + name)


def click_if(page, sel, timeout=1500):
    try:
        page.click(sel, timeout=timeout)
        return True
    except Exception:
        return False


def main():
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"]
        browser = p.chromium.launch()
        ctx = browser.new_context(**iphone)
        page = ctx.new_page()

        # Archive mode: guesses are stateless (no leaderboard writes), so test
        # runs don't pollute today's real board. Use a past in-range date.
        page.goto(BASE + "/?date=2026-06-05", wait_until="domcontentloaded")
        page.wait_for_timeout(3500)
        click_if(page, "#btn-howto-skip")
        page.wait_for_timeout(400)
        shot(page, "01-start.png")

        # start a guest game (name prompt first)
        click_if(page, "#btn-start")
        page.wait_for_timeout(1500)
        if page.is_visible("#name-card"):
            shot(page, "08-name.png")
            page.fill("#name-input", "רואי")
            click_if(page, "#btn-name-save")
            page.wait_for_timeout(2000)
        page.wait_for_timeout(1200)
        shot(page, "05-hud-round1.png")

        # ---- settings menu (Shoelace switches) ----
        click_if(page, "#btn-menu")
        page.wait_for_timeout(400)
        shot(page, "02-settings.png")
        before = page.evaluate("localStorage.getItem('israelle_sound')")
        click_if(page, "#sw-sound")       # toggle Sound switch
        page.wait_for_timeout(700)
        after = page.evaluate("localStorage.getItem('israelle_sound')")
        check("sound switch flips localStorage", before != after)
        check("sound switch reflects state",
              page.evaluate("document.getElementById('sw-sound').checked") == (after != "off"))
        shot(page, "11-settings-toast.png")
        # menu stays open after a switch toggle
        check("menu stays open on switch toggle",
              page.evaluate("document.getElementById('toolbar').classList.contains('open')"))
        click_if(page, "#btn-menu")        # close
        page.wait_for_timeout(300)

        # ---- play through ----
        for rnd in range(6):
            page.mouse.click(195, 430)
            page.wait_for_timeout(700)
            if rnd == 0:
                shot(page, "06-pending-guess.png")
            click_if(page, "#btn-confirm-guess", timeout=1000)
            page.wait_for_timeout(1600)
            if rnd == 0:
                shot(page, "07-reveal.png")
            if not click_if(page, "#btn-next", timeout=1500):
                break
            page.wait_for_timeout(900)

        page.wait_for_timeout(1500)
        if page.is_visible("#end-card"):
            shot(page, "09-end.png")
            page.evaluate("window.flashToast && window.flashToast('צליל: פעיל', 'ok')")
            page.wait_for_timeout(700)
            shot(page, "10-toast.png")

        # ---- leaderboard + ESC-to-close a11y ----
        if click_if(page, "#btn-leaderboard"):
            page.wait_for_timeout(1200)
            shot(page, "03-leaderboard.png")
            check("leaderboard open", page.is_visible("#lb-card"))
            page.keyboard.press("Escape")
            page.wait_for_timeout(600)
            check("Escape closes leaderboard", not page.is_visible("#lb-card"))

        browser.close()

    print("\nchecks:", sum(1 for _, ok in checks if ok), "/", len(checks), "passed")
    for name, ok in checks:
        if not ok:
            print("  FAILED:", name)


if __name__ == "__main__":
    main()
