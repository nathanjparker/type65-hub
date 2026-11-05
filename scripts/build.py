#!/usr/bin/env python3
"""Rebuild hub-data.json and index.html from data/ and head/body, and the standalone site in docs/."""
import json, pathlib, shutil
root = pathlib.Path(__file__).resolve().parent.parent
d = {"stages": json.load(open(root/"data/stages.json"))}
parts = []
for f in sorted((root/"data").glob("parts-*.json")):
    parts += json.load(open(f))
d["parts"] = parts
d.update(json.load(open(root/"data/refs.json")))
json.dump(d, open(root/"hub-data.json", "w"), ensure_ascii=False, separators=(",", ":"))
page = (root/"head.html").read_text() + (root/"body.html").read_text()
(root/"index.html").write_text(page)
# standalone site (GitHub Pages serves docs/)
skeleton = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
            'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
(root/"docs").mkdir(exist_ok=True)
(root/"docs/index.html").write_text(skeleton + page + "</body></html>")
shutil.copy(root/"hub-data.json", root/"docs/hub-data.json")
(root/"docs/.nojekyll").write_text("")
print(f"{len(parts)} parts, {len(d['stages'])} stages; docs/ rebuilt")
