#!/usr/bin/env python3
"""Generate Etsy/Gumroad listing drafts for a digital product."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

STOP = {"a", "an", "the", "and", "or", "for", "of", "to", "in", "on", "with"}


def slug_words(product: str) -> list[str]:
    parts = [w.lower() for w in product.replace("/", " ").split() if w]
    return [w for w in parts if w not in STOP][:6]


def titles(product: str, price: str) -> list[str]:
    return [
        f"{product} | Instant Download Digital Template",
        f"{product} — Printable & Editable (${price})",
        f"Digital {product} for Solopreneurs | Instant Download",
    ]


def tags(product: str) -> list[str]:
    base = slug_words(product)
    extras = [
        "instant download",
        "digital download",
        "printable",
        "template",
        "solopreneur",
        "small business",
        "planner",
        "spreadsheet",
        "etsy digital",
        "gumroad",
    ]
    out: list[str] = []
    for t in base + extras:
        if t not in out:
            out.append(t)
    return out[:13]  # Etsy soft cap habit


def description(product: str, price: str, platform: str) -> str:
    return f"""{product}

What you get:
- Instant digital download
- Ready to use the same day
- Clear instructions included

Price: ${price}
Platform draft: {platform}

Who it's for:
Solopreneurs and freelancers who want a simple system without building it from scratch.

How it works:
1. Purchase
2. Download instantly
3. Duplicate / open and customize

Support: reply to your purchase email if anything's unclear.
""".strip()


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--product", required=True)
    p.add_argument("--price", default="19")
    p.add_argument("--platform", choices=["etsy", "gumroad", "both"], default="both")
    p.add_argument("--out", type=Path, default=Path("out"))
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    platforms = ["etsy", "gumroad"] if args.platform == "both" else [args.platform]

    for platform in platforms:
        path = args.out / f"{stamp}-{platform}-listing.md"
        body = [
            f"# {args.product} — {platform} listing draft",
            "",
            "## Title options",
            *[f"- {t}" for t in titles(args.product, args.price)],
            "",
            "## Tags",
            ", ".join(tags(args.product)),
            "",
            "## Description",
            description(args.product, args.price, platform),
            "",
        ]
        path.write_text("\n".join(body) + "\n", encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
