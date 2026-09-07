#!/bin/bash
# Minify skills-site.html to skills-site.min.html.
# Keep this recipe aligned with .github/workflows/build-site.yml.
set -euo pipefail

INPUT="skills-site.html"
OUTPUT="skills-site.min.html"

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found" >&2
  exit 1
fi

npx --yes html-minifier-terser \
  --collapse-whitespace \
  --remove-comments \
  --remove-redundant-attributes \
  --remove-script-type-attributes \
  --remove-style-link-type-attributes \
  --minify-css true \
  --minify-js true \
  -o "$OUTPUT" \
  "$INPUT"

ORIG=$(wc -c < "$INPUT")
MINI=$(wc -c < "$OUTPUT")
PCT=$((100 - MINI * 100 / ORIG))

echo "Minified: $INPUT -> $OUTPUT"
echo "Original: ${ORIG} bytes"
echo "Minified: ${MINI} bytes"
echo "Saved:    ${PCT}%"
