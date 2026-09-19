# freelance-ops-kit (marketplace listing kit)

> **Repo slug:** `freelance-ops-kit` · **Product focus:** Etsy + Gumroad listing copy (not invoices/proposals).
> GitHub description still mentions invoices — treat the README as source of truth until the description is updated.

Copy + SEO helpers for listing a digital product on **Etsy** and **Gumroad**: titles, tags, descriptions, and a simple launch checklist.

Re-aimed so it does not compete with the Solo Freelancer Cashflow Kit — this is the *distribution* layer, not another finance template.

## Quick start

```bash
python3 listing.py --product "Solo Freelancer Cashflow Kit" --price 19 --platform both
```

Writes draft listing fields under `./out/` (gitignored).

## What's inside

| Path | Purpose |
| --- | --- |
| `listing.py` | Generates title options, tags, short/long description drafts |
| `templates/etsy.md` | Etsy listing skeleton |
| `templates/gumroad.md` | Gumroad listing skeleton |
| `checklists/launch.md` | Ship checklist for first sale |
| `LICENSE` | MIT |

## Roadmap toward revenue-ready

1. Update the GitHub repo description to match this marketplace focus (or rename the repo to `marketplace-listing-kit`).
2. Add 2–3 niche-specific prompt packs (e.g. Notion templates, spreadsheet kits) under `templates/`.
3. Pair one real SKU + cover images, run `listing.py`, complete `checklists/launch.md`, and publish on Gumroad or Etsy.

## Money angle

Distribution layer for whatever digital SKU you're selling. Pair with the Cashflow Kit (or any PDF/sheet product) instead of being another finance template.

## License

MIT — see [LICENSE](LICENSE).
