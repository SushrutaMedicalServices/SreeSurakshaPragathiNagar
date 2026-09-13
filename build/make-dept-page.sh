#!/bin/sh
# Usage: make-dept-page.sh "<page title>" "<meta title>" "<meta desc>" "/canonical/" "<crumb parent label>" "<crumb parent href>" "<banner img path>" inner-content-file.html output-file.html
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
PAGE_TITLE="$1"; META_TITLE="$2"; DESC="$3"; CANON="$4"; PARENT_LABEL="$5"; PARENT_HREF="$6"; BANNER="$7"; INNER="$8"; OUT="$9"

TMP="$(mktemp)"
{
  echo "  <section class=\"page-header\">"
  echo "    <div class=\"container\">"
  echo "      <h1>${PAGE_TITLE}</h1>"
  if [ -n "$PARENT_HREF" ]; then
    echo "      <div class=\"page-header__crumbs\"><a href=\"/\">Home</a> &rsaquo; <a href=\"${PARENT_HREF}\">${PARENT_LABEL}</a> &rsaquo; <span>${PAGE_TITLE}</span></div>"
  else
    echo "      <div class=\"page-header__crumbs\"><a href=\"/\">Home</a> &rsaquo; <span>${PAGE_TITLE}</span></div>"
  fi
  echo "    </div>"
  echo "  </section>"
  echo "  <section class=\"content-page\">"
  echo "    <div class=\"container content-page__grid\">"
  echo "      <div class=\"content-page__body\">"
  echo "        <img src=\"/assets/original-site/images/${BANNER}\" alt=\"${PAGE_TITLE}\" class=\"content-page__banner\" style=\"margin-bottom:28px;\">"
  cat "$INNER"
  echo "      </div>"
  cat "$DIR/partials/sidebar.html"
  echo "    </div>"
  echo "  </section>"
} > "$TMP"

sh "$DIR/make-page.sh" "$META_TITLE" "$DESC" "$CANON" "$TMP" "$OUT"
rm -f "$TMP"
