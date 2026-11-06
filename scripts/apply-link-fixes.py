#!/usr/bin/env python3
"""Fold link fixes from an exported build into the catalog.

Usage:
    python3 scripts/apply-link-fixes.py my-type65-build.json [--dry-run]

The hub's "fix link" dialog saves a replacement product page, source link and
any extra links with the build (localStorage on the free site, the state
collection in the Claude version). "Export my build" writes that to a JSON
file. This script reads the file, finds every part with a fix, and writes the
new url / srcUrl / links into data/parts-*.json so the catalog carries the fix
for everyone. Run scripts/build.py afterwards.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')


def dump(path, parts):
    s = json.dumps(parts, ensure_ascii=False, indent=1)
    s = re.sub(r'^ +', '', s, flags=re.M)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s + '\n')


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    dry = '--dry-run' in argv
    with open(argv[1], encoding='utf-8') as f:
        export = json.load(f)
    state = export.get('state') or {}
    fixes = {k: v for k, v in state.items() if v and (v.get('url') or v.get('srcUrl') or v.get('links'))}
    if not fixes:
        print('No link fixes in that export.')
        return 0
    changed = 0
    for path in sorted(glob.glob(os.path.join(DATA, 'parts-*.json'))):
        with open(path, encoding='utf-8') as f:
            parts = json.load(f)
        touched = False
        for p in parts:
            fx = fixes.get(p['id'])
            if not fx:
                continue
            before = (p.get('url'), p.get('srcUrl'), p.get('links'))
            if fx.get('url'):
                p['url'] = fx['url']
            if fx.get('srcUrl'):
                p['srcUrl'] = fx['srcUrl']
            if fx.get('links'):
                have = {l['url'] for l in p.get('links', [])}
                p['links'] = p.get('links', []) + [l for l in fx['links'] if l.get('url') and l['url'] not in have]
            if (p.get('url'), p.get('srcUrl'), p.get('links')) != before:
                print(f"{p['id']} {p['name']}")
                for k in ('url', 'srcUrl'):
                    if fx.get(k) and fx[k] != before[('url', 'srcUrl').index(k)]:
                        print(f"   {k}: {before[('url', 'srcUrl').index(k)] or '(none)'} -> {fx[k]}")
                if fx.get('links'):
                    print(f"   links: +{len(fx['links'])}")
                changed += 1
                touched = True
        if touched and not dry:
            dump(path, parts)
    print(f"{changed} part(s) {'would be' if dry else ''} updated. {'' if dry else 'Now run: python3 scripts/build.py'}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
