# Buyer README — marketplace listing alignment

**Who this is for:** You bought (or are packaging) a digital product and want the **storefront promise** to match what the buyer downloads.

**What this repo is:** A **marketplace listing kit** (Etsy + Gumroad copy helpers) — not a cashflow spreadsheet and not a client-ops template pack. Use it to draft titles, tags, and descriptions; then keep those claims honest in the zip the buyer receives.

---

## Promise ↔ delivery map

| Marketplace claim (listing) | Must be true in the download |
| --- | --- |
| Instant digital download | Zip/file attaches and opens without a login wall |
| Editable / printable / template | Files open in the apps you named (Sheets, Docs, PDF, etc.) |
| "What's included" bullet list | Same filenames (or clear README map) inside the zip |
| Price / platform | Matches Gumroad or Etsy listing; no surprise upsells in the zip |
| Support line | Real reply path (purchase email or stated channel) |

If a bullet is on the listing, it belongs in the zip **or** the buyer-facing README must say why it is not.

---

## Suggested buyer-facing README (paste into the product zip)

Keep this short. Buyers skim.

```text
# Start here

Thanks for buying [PRODUCT NAME].

## Open these first
1. [main file] — duplicate before editing
2. This README — 5-minute setup

## What's in this download
- …list every deliverable that appeared on the listing…

## How to use (≤10 minutes)
1. Unzip
2. Duplicate the folder as MASTER
3. Replace [YOUR_NAME] / placeholders
4. Export or share as needed

## Support
Reply to your purchase receipt email.

## License (plain language)
Personal use for your business. Do not resell or redistribute the files.

## Disclaimer
Templates / organizational tools only — not legal, tax, or financial advice.
```

---

## Align listing drafts from this repo

1. Generate drafts:

```bash
python3 listing.py --product "Your Product Name" --price 19 --platform both
```

2. Compare `out/*-listing.md` (or `examples/`) to the zip contents.
3. Edit the listing **or** the zip until every title/description claim is true.
4. Run `checklists/launch.md` before publish.

---

## Related docs

- [HOW_TO_SELL.md](HOW_TO_SELL.md) — short path to list and sell with this kit
- [checklists/launch.md](checklists/launch.md) — first-sale checklist
- [templates/etsy.md](templates/etsy.md) / [templates/gumroad.md](templates/gumroad.md) — skeletons
