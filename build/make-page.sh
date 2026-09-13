#!/bin/sh
# Usage: make-page.sh "<title>" "<description>" "/canonical/path/" body-file.html output-file.html
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
TITLE="$1"
DESC="$2"
CANON="$3"
BODY="$4"
OUT="$5"

mkdir -p "$(dirname "$OUT")"

esc() { printf '%s' "$1" | sed -e 's/[&#\]/\\&/g'; }
ETITLE=$(esc "$TITLE")
EDESC=$(esc "$DESC")
ECANON=$(esc "$CANON")

sed -e "s#__TITLE__#${ETITLE}#" -e "s#__DESC__#${EDESC}#" -e "s#__CANONICAL__#${ECANON}#" "$DIR/partials/head-template.html" > "$OUT"
cat "$DIR/partials/nav.html" >> "$OUT"
printf '\n<main>\n' >> "$OUT"
cat "$BODY" >> "$OUT"
printf '\n</main>\n' >> "$OUT"
cat "$DIR/partials/footer.html" >> "$OUT"
