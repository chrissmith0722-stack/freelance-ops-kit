#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT_DIR="${OUT_DIR:-out}"
rm -rf "$OUT_DIR"
python3 listing.py \
  --product "Solo Freelancer Cashflow Kit" \
  --price 19 \
  --platform both \
  --out "$OUT_DIR"

echo "demo outputs:"
ls -1 "$OUT_DIR"
echo "demo ok: listing drafts for Solo Freelancer Cashflow Kit @ \$19"
