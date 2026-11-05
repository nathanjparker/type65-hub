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
