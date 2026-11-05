# Type 65 Coupe Build Hub

Source for the Factory Five Gen 3 Type 65 Coupe build hub: a stage-by-stage parts and resources database with picks, progress, notes, an order sheet and builder suggestions.

The live page is a Claude artifact. This repo is the versioned copy of its data and page source.

## Layout

- `data/stages.json` — the 14 build stages in manual order: window, hours, summary, read-first links, challenges, ideas, default checklist.
- `data/parts-*.json` — the parts catalog (FFR options and aftermarket alternatives). Each part: stage, category, name, model/part number, vendor, product URL, price (tagged vendor/forum/est), who runs it, source thread or video, notes, Gen 3 fit, decision `group`, engine `family`, popularity rating.
- `data/refs.json` — build threads, video series, vendor directory, Northwest community, FFR order-form verdicts, decision groups (with decide-by deadline and trade-off text), engine families, compatibility warnings, WSP receipt checklist, order-up-front list, open questions.
- `head.html` + `body.html` — the page; `scripts/build.py` concatenates them into `index.html` and rebuilds `hub-data.json`.

Runtime state (picks, percent complete, notes, photos, receipts, checklist ticks, builder suggestions, what's-new) lives in the artifact's database, not here.

## Rebuild

    python3 scripts/build.py

Then republish `index.html` with `hub-data.json` as a supporting file.

## Make your own copy

The live hub is a Claude artifact. To run your own, with your own picks, notes, photos and progress, open the Claude app and paste:

> Publish the Factory Five Type 65 Coupe Build Hub from the GitHub repo nathanjparker/type65-hub as my own artifact: publish index.html with hub-data.json as a supporting file, and declare these capabilities: db with rules [{path:"",read:"view",write:"owner"},{path:"private",read:"owner",write:"owner"},{path:"data/users/{self}",write:"interact"},{path:"suggestions",read:"view",write:"owner"},{path:"suggestions/{self}",read:"view",write:"interact"},{path:"references",read:"view",write:"owner"},{path:"references/{self}",read:"view",write:"interact"}], user, sample, assets. Then tell me the link.

You get the full catalog with an empty database: no picks, notes or progress carried over. Edit `data/*.json` and rerun `scripts/build.py` to change the catalog; republish the same two files to update your copy.

### What the access rules mean

- Everyone who can open the artifact reads the catalog, the owner's picks and progress, checklists, stage notes and what's new.
- `private/` (per-part notes, photos, receipts) is readable and writable by the owner only.
- `data/users/{self}` is each visitor's own sandbox (their picks, percentages, ticks); only they can read or write it, and the owner cannot see it either.
- `suggestions/` and `references/` are builder submissions: each person writes only their own, everyone reads them, the owner can remove any.
- Visitors need Contributor access on the share link to write a sandbox or submit; Viewer access is read-only.
