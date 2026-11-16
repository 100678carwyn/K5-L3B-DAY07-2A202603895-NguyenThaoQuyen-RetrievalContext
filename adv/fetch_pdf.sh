#!/bin/bash
# Download the source PDF (NOT committed: third-party copyright) and verify its SHA-256 against adv/manifest.json.
set -e; cd "$(dirname "$0")/.."
mkdir -p adv/raw
URL="https://www.ifc.org/content/dam/ifc/doc/mgrt/ccdr-full-report-vie-1107.pdf"
[ -f adv/raw/ccdr_vi.pdf ] || curl -sSL -o adv/raw/ccdr_vi.pdf "$URL"
EXPECT=$(python3 -c "import json;print(json.load(open('adv/manifest.json'))['sha256'])")
GOT=$(shasum -a 256 adv/raw/ccdr_vi.pdf | cut -d' ' -f1)
[ "$EXPECT" = "$GOT" ] && echo "SHA-256 OK ($GOT)" || { echo "SHA-256 MISMATCH: expected $EXPECT got $GOT"; exit 1; }
