# freelance-ops-kit → marketplace listing kit

**Re-aim:** this repo is no longer an invoice/ops/finance-template product. It is a **marketplace listing kit** — copy + SEO helpers for listing a digital product on **Etsy** and **Gumroad** (titles, tags, descriptions, launch checklist).

It **complements** the Solo Freelancer Cashflow Kit (and similar SKUs). Do not treat this repo as a competing cashflow/finance spreadsheet product.

**New:** [BUYER_README.md](BUYER_README.md) (listing ↔ download alignment) · [HOW_TO_SELL.md](HOW_TO_SELL.md) (short sell path)

## Quick start

```bash
python3 listing.py --product "Solo Freelancer Cashflow Kit" --price 19 --platform both
```

Writes draft listing fields under `./out/` (gitignored). A committed sample lives in `examples/`.

Smoke / regenerate the Cashflow Kit listing drafts:

```bash
./scripts/demo.sh
# or
make demo
```

## What's inside

| Path | Role |
| --- | --- |
| `listing.py` | Generates title options, tags, short/long description drafts |
| `templates/` | Etsy + Gumroad prompt skeletons |
| `checklists/launch.md` | Ship checklist for first sale |
| `examples/` | Sample listing draft for Solo Freelancer Cashflow Kit @ $19 |
| `BUYER_README.md` | Keep marketplace claims honest vs the buyer zip |
| `HOW_TO_SELL.md` | Short how-to-sell path for this kit |
| `scripts/demo.sh` | Runs `listing.py` for that product and prints output paths |

## Example: Solo Freelancer Cashflow Kit @ $19

```bash
python3 listing.py \
  --product "Solo Freelancer Cashflow Kit" \
  --price 19 \
  --platform both \
  --out out
```

See `examples/solo-freelancer-cashflow-kit-listing.md` for a checked-in draft you can paste into Etsy/Gumroad and edit.

## Money angle

Distribution layer for whatever digital SKU you're selling. Pair with the Cashflow Kit (or any PDF/sheet product) instead of being another finance template.
