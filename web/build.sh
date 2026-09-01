#!/bin/bash
# Minify skills-site.html → skills-site.min.html
# Uses sed for basic minification (no external deps needed)

INPUT="skills-site.html"
OUTPUT="skills-site.min.html"

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found"
  exit 1
fi

# Basic minification: remove comments, collapse whitespace, strip newlines
sed \
  -e '/<!--/,/-->/d' \
  -e 's/\/\*.*\*\///g' \
  -e '/^[[:space:]]*$/d' \
  -e 's/^[[:space:]]*//' \
  -e 's/[[:space:]]*$//' \
  -e ':a;N;$!ba;s/\n/ /g' \
  -e 's/  */ /g' \
  -e 's/ >/>/g' \
  -e 's/ </</g' \
  "$INPUT" > "$OUTPUT"

ORIG=$(wc -c < "$INPUT")
MINI=$(wc -c < "$OUTPUT")
PCT=$((100 - MINI * 100 / ORIG))

echo "✅ Minified: $INPUT → $OUTPUT"
echo "   Original: ${ORIG} bytes"
echo "   Minified: ${MINI} bytes"
echo "   Saved:    ${PCT}%"
