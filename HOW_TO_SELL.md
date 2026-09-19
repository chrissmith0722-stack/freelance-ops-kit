# How to sell this kit

Short path: use **freelance-ops-kit** as your listing/copy layer, pair it with a real digital SKU zip, publish on Gumroad or Etsy.

## 1. Pick one SKU

Example: Solo Freelancer Cashflow Kit @ **$19**. Do not list this repo itself as a finance spreadsheet — it is listing helpers only.

## 2. Draft the listing

```bash
python3 listing.py --product "Solo Freelancer Cashflow Kit" --price 19 --platform both
```

Or start from `examples/solo-freelancer-cashflow-kit-listing.md` and edit.

Fill `templates/gumroad.md` or `templates/etsy.md` with the chosen title, tags, and description.

## 3. Align buyer delivery

Follow [BUYER_README.md](BUYER_README.md): every listing bullet must exist in the download (or be removed from the listing).

## 4. Ship checklist

Complete [checklists/launch.md](checklists/launch.md) — covers, test purchase, thank-you note, one distribution push.

## 5. Publish

| Channel | Action |
| --- | --- |
| **Gumroad** | New digital product → upload zip → paste listing → set price → Publish |
| **Etsy** | Digital download listing → same copy + tags → Publish |

Save the public URL. First-dollar stop condition: live listing with price &gt; $0.

## 6. After first sale

- Reply fast to support email
- Note which title/tag won the click
- Optionally mirror the other marketplace with the same aligned copy

## What not to do

- Do not market this GitHub repo as invoices/proposals/client tracking (legacy slug noise)
- Do not invent features in the listing that are not in the zip
- Do not wait for a perfect funnel — one live paid listing beats a polished draft
