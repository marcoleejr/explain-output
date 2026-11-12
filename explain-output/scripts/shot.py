#!/usr/bin/env python3
"""HTML -> PNG at a real mobile viewport (Playwright, own headless browser).
  shot.py in.html out.png [width=390] -> prints out path and the page scrollWidth (must equal width)."""
import os, sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 390
with sync_playwright() as p:
    b = p.chromium.launch()
    try:
        pg = b.new_page(viewport={"width": w, "height": 844}, color_scheme=os.environ.get("SCHEME", "light"))
        pg.goto("file://" + os.path.abspath(src))
        sw = pg.evaluate("document.documentElement.scrollWidth")
        pg.screenshot(path=out, full_page=True)
    finally:
        b.close()
print(out, "scrollWidth=%d" % sw)
