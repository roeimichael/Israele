#!/usr/bin/env bash
set -e
mkdir -p public/docs
cp frontend/index.html public/index.html
cp frontend/app.js public/app.js
cp frontend/style.css public/style.css
cp frontend/style-v2.css public/style-v2.css
cp frontend/manifest.json public/manifest.json
cp frontend/privacy.html public/privacy.html
cp frontend/terms.html public/terms.html
cp frontend/robots.txt public/robots.txt
cp frontend/googlea45400d763791cc6.html public/googlea45400d763791cc6.html
cp docs/flag.png public/docs/flag.png
cp docs/icon-192.png public/docs/icon-192.png
cp docs/icon-512.png public/docs/icon-512.png
cp docs/icon-maskable-512.png public/docs/icon-maskable-512.png
cp docs/homepage.png public/docs/homepage.png
cp docs/share.png public/docs/share.png
if [ -f docs/share.jpg ]; then cp docs/share.jpg public/docs/share.jpg; fi
