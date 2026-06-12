"""One-off: dump the maplibre attribution element so we can fix its CSS."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone = p.devices["iPhone 13"]
    b = p.chromium.launch()
    pg = b.new_context(**iphone).new_page()
    pg.goto("http://127.0.0.1:8000/", wait_until="domcontentloaded")
    pg.wait_for_timeout(4000)
    html = pg.evaluate("""() => {
      const el = document.querySelector('.maplibregl-ctrl-attrib');
      return el ? { cls: el.className, html: el.outerHTML.slice(0, 400) } : 'none';
    }""")
    print(html)
    b.close()
