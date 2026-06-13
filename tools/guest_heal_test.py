"""Verify the guest-id self-heal: a legacy non-UUID player_id (as produced in
in-app browsers lacking crypto.randomUUID) must be regenerated to a valid UUID
on load, and a guest guess must then save (200, round advances) — no freeze.
Usage: python tools/guest_heal_test.py [base_url]
"""
import sys
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8011"
UA_INAPP = ("Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS]")  # Facebook in-app webview

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True,
                              has_touch=True, user_agent=UA_INAPP)
    # Runs before any page script: plant a stale bad id + simulate missing randomUUID.
    ctx.add_init_script("""
      try { Object.defineProperty(window.crypto, 'randomUUID', {value: undefined, configurable: true}); } catch(e) {}
      localStorage.setItem('israelle_player_id', 'p_stalebad123');
      localStorage.setItem('israelle_player_name', 'HealTest');
    """)
    page = ctx.new_page()
    guess_status = []
    page.on("response", lambda r: guess_status.append(r.status) if "/api/today/guess" in r.url else None)
    errs = []
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)

    page.goto(BASE + "/", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)

    has_randomuuid = page.evaluate("typeof (window.crypto && window.crypto.randomUUID)")
    uuidv4_sample = page.evaluate("uuidv4()")
    healed_id = page.evaluate("localStorage.getItem('israelle_player_id')")
    import re
    UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)

    print("randomUUID present in page:", has_randomuuid, "(simulated absent)")
    print("uuidv4() sample          :", uuidv4_sample, "valid:", bool(UUID_RE.match(uuidv4_sample)))
    print("stale id 'p_stalebad123' healed to:", healed_id, "valid:", bool(UUID_RE.match(healed_id or "")))

    # play round 1 as guest
    try: page.click("#btn-howto-skip", timeout=2500)
    except Exception: pass
    page.wait_for_timeout(400)
    try: page.click("#btn-start", timeout=2500)
    except Exception: pass
    page.wait_for_timeout(1000)
    if page.is_visible("#name-card"):
        page.fill("#name-input", "HealTest")
        try: page.click("#btn-name-save", timeout=2000)
        except Exception: pass
        page.wait_for_timeout(1800)
    page.mouse.click(195, 422)        # center → on land
    page.wait_for_timeout(4200)       # reveal line animation is ~2500ms + render
    advanced = page.is_visible("#btn-next") or page.is_visible("#end-card")
    save_fail = page.evaluate(
        "[...document.querySelectorAll('.toast,#toast')].some(t=>/שמירת|save/i.test(t.textContent||''))")

    print("guess HTTP statuses      :", guess_status)
    print("round advanced (next/end):", advanced)
    print("save-fail toast visible  :", save_fail)
    print("console errors           :", len(errs), errs[:3])

    ok = (bool(UUID_RE.match(healed_id or "")) and bool(UUID_RE.match(uuidv4_sample))
          and guess_status == [s for s in guess_status if s == 200] and 200 in guess_status
          and advanced and not save_fail)
    print("\nSELF-HEAL OK:", ok)
    browser.close()
