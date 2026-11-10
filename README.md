# Type 65 Coupe Build Hub

Source for the Factory Five Gen 3 Type 65 Coupe build hub: a stage-by-stage parts and resources database with picks, progress, notes, a build estimator and builder suggestions.

The live page is a Claude artifact. This repo is the versioned copy of its data and page source.

## About

I'm Nate, a first-time kit builder in Washington State putting together a Gen 3 Type 65 Coupe as a street car (no donor, BluePrint 347 EFI + Tremec TKX, 2015 IRS, A/C, side windows, wipers) with my daughter, target finish September 2029. Researching the build meant reading the same forty threads and videos over and over, so I had the parts, prices, who-runs-what and the gotchas filed into one page in the order the FFR manual builds the car. This is that page, shared so you don't have to redo the reading.

What's in it:

- **14 build stages** in manual order, each with what to read first, what goes wrong, ideas worth stealing and a checklist.
- **201 parts and ideas**: FFR part numbers next to the aftermarket alternatives, list price, who runs it (with the thread or video it came from), Gen 3 fit, and dots for how many documented coupes chose it.
- **Kit builder**: pick one option per decision, compare every option side by side, see which decisions lock at the kit order, and get warnings when two picks don't go together.
- **Build estimator** generated from your picks: one compact table grouped by vendor (tick this on the FFR form, buy this elsewhere), a low-to-high total, a sales tax estimate by state, and an Excel copy. **Export schedule of values** downloads an .xlsx for whoever handles the money: one line per purchase with low/high/budget, the month it lands (from the Schedule), funding source (cash, 0% card, Affirm), paid-to-date and balance, plus a month-by-month cash flow tab that spreads card and Affirm purchases into level payments. No library; the file is written in the page.
- **Shop & tools**: right under the Kit builder; tick Buy or Skip on each tool and garage build-out item, and what you mark Buy lands in the estimator as its own line.
- **Build calculator and schedule**: hours per week in, go-kart / title / done dates out, on an editable Gantt with gates and order-by dates for long-lead parts.
- **Fold and focus**: fold any section to a one-line summary (it stays folded), mark the stage you're working on and it moves to the top under a "You are here" strip with progress, hours, the next step and parts still to arrive; mark stages done as you go. Contents has Fold all / Open all.
- **Two themes**: Race program '65 (light: program paper, press black, team blue, spot red) and Midnight blue (dark: blue-black shop, bare aluminum plate, team blue). The button next to search switches; it follows your device until you pick. Every section has its own line icon and every build stage a two-tone number-and-icon pill.
- **Gearing calculator**: rear axle ratio, TKX gear set and tire in; rpm at 60/70/80 mph and speed at redline in each gear out. Lives in the rear-suspension stage, linked from Contents.
- **Plans that cross stages**: cabin comfort, driver fit at 6'2", and Washington rain. Pick what you want the car to be and it tells you the fewest and the cheapest changes that get you there.

Nothing here is FFR-official and prices go stale; every figure is tagged with where it came from. Found something wrong or have a part that should be in it? Open an issue or post in the forum thread linked from the page.

## Layout

- `data/stages.json` — the 14 build stages in manual order: window, hours, summary, read-first links, challenges, ideas, default checklist.
- `data/parts-*.json` — the parts catalog (FFR options and aftermarket alternatives). Each part: stage, category, name, model/part number, vendor, product URL, price (tagged vendor/forum/est), who runs it, source thread or video, notes, Gen 3 fit, decision `group`, engine `family`, popularity rating.
- `data/refs.json` — build threads, video series, vendor directory, Northwest community, FFR order-form verdicts, decision groups (with decide-by deadline and trade-off text), engine families, compatibility warnings, WSP receipt checklist, order-up-front list, open questions.
- `head.html` + `body.html` — the page; `scripts/build.py` concatenates them into `index.html` and rebuilds `hub-data.json`.

Runtime state (picks, percent complete, notes, photos, receipts, checklist ticks, builder suggestions, what's-new) lives in the artifact's database, not here.

## Rebuild

    python3 scripts/build.py

Then republish `index.html` with `hub-data.json` as a supporting file.

## Use it

- **Free web version:** https://nathanjparker.github.io/type65-hub/ — the whole hub, no account. Your picks, progress, checklist ticks and notes save in your browser; use Export / Import at the top to back them up or move them between devices.
- **Nate's live copy** is a Claude artifact with cloud features on top (photos, receipts, builder submissions, a weekly research pass that files what builders post). The public link to it is read-only.

To change the catalog, edit `data/*.json`, run `python3 scripts/build.py`, and commit; GitHub Pages serves `docs/`.

### Fixing a dead link, or adding more

Vendors move pages. You don't need the repo to fix one:

1. On the part's card, click **fix link** (bottom-right of the links row; it's there on your own copy and for the owner on the Claude version).
2. Paste the working product page and/or source, add any extra links worth a click (an install video, a review thread, a PDF) with a short label, and Save. The card, the compare view, the build estimator and Ask the hub all use your links from then on. **Back to catalog link** undoes it.

To get a fix into the shared catalog so every copy carries it, do one of:

- Click **Export my build** at the top, then run `python3 scripts/apply-link-fixes.py my-type65-build.json` in this repo (add `--dry-run` to preview), then `python3 scripts/build.py` and commit. The script copies only the links; your picks and notes stay out of the catalog.
- Or post the part and the new link in the forum thread linked from the page; the weekly pass reads it.

Parts can also carry extra links in the catalog itself: an optional `links: [{"label": "...", "url": "..."}]` array on any part in `data/parts-*.json`.

### Access rules on the Claude copy

- Everyone with the link reads the catalog, the owner's picks and progress, checklists, stage notes and what's new.
- `private/` (per-part notes, photos, receipts) is readable and writable by the owner only.
- `data/users/{self}` is each invited builder's own sandbox; only they can read or write it.
- `suggestions/` and `references/` are builder submissions: each person writes only their own, everyone reads them, the owner can remove any.
