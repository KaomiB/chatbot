#!/usr/bin/env bash
# Local-only: full-page screenshot of Streamlit HSA app in dark embed mode.
# Output: screenshots/dark-streamlit-hsa.png (gitignored)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/screenshots"
URL="${STREAMLIT_DARK_URL:-https://chatbot-37tx6ldxlh6gzz4od3t5oa.streamlit.app/?embed=true&embed_options=show_toolbar&embed_options=dark_theme&embed_options=show_colored_line&embed_options=show_padding&embed_options=show_footer}"
echo "Capturing (first load may take 60s+)..."
npx --yes playwright@1.49.1 screenshot --full-page --timeout=180000 --wait-for-timeout=45000 "$URL" "$ROOT/screenshots/dark-streamlit-hsa.png"
echo "Wrote $ROOT/screenshots/dark-streamlit-hsa.png"
