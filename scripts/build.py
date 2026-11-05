#!/usr/bin/env python3
"""Rebuild hub-data.json from data/*.json and index.html from head.html + body.html."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = {"stages": json.load(open(root/"data/stages.json"))}
parts = []
for f in sorted((root/"data").glob("parts-*.json")):
    parts += json.load(open(f))
d["parts"] = parts
d.update(json.load(open(root/"data/refs.json")))
json.dump(d, open(root/"hub-data.json", "w"), ensure_ascii=False, separators=(",", ":"))
(root/"index.html").write_text((root/"head.html").read_text() + (root/"body.html").read_text())
print(f"{len(parts)} parts, {len(d['stages'])} stages")
