#!/usr/bin/env bash
# Rung 2/3 renders in ~5 s with the system Chrome (own headless instance). Set CHROME to override the path.
#   render.sh mmd  in.mmd  out.png    # Mermaid -> PNG (for clients that cannot show Mermaid)
#   render.sh mmd3b in.mmd out.png    # Mermaid -> PNG, 3Blue1Brown style (dark background, blue/yellow)
#   render.sh shot in.html out.png [width]   # HTML -> PNG preview for the review pass
set -euo pipefail
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
mode="${1:?mode: mmd|mmd3b|shot}"; in="${2:?input}"; out="${3:?output}"
case "$mode" in
  mmd|mmd3b)
    cfg="$(mktemp -t eo-pp).json"
    printf '{"executablePath":"%s","args":["--no-sandbox","--headless=new"]}' "$CHROME" > "$cfg"
    if command -v mmdc >/dev/null; then run=(mmdc); else run=(pnpm dlx @mermaid-js/mermaid-cli); fi
    if [ "$mode" = mmd3b ]; then
      "${run[@]}" -i "$in" -o "$out" -p "$cfg" -c "$(dirname "$0")/3b1b.json" -b '#1c1c1c' -s 2 -q
    else
      "${run[@]}" -i "$in" -o "$out" -p "$cfg" -b white -s 2 -q
    fi
    rm -f "$cfg" ;;
  shot)
    python3 "$(dirname "$0")/shot.py" "$in" "$out" "${4:-390}"; exit 0 ;;
  *) echo "unknown mode $mode" >&2; exit 2 ;;
esac
echo "$out"
