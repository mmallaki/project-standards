#!/usr/bin/env bash
# Copy the documentation skeleton into a repo. Never overwrites: prints what it skipped.
# usage: new-project.sh <project-name> [destination]
set -euo pipefail

NAME="${1:?usage: new-project.sh <project-name> [destination]}"
DEST="${2:-$PWD/$NAME}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$DEST"

copy() {
  local src="$1" dst="$2"
  if [ -e "$dst" ]; then
    echo "skip  ${dst#./}"
    return
  fi
  mkdir -p "$(dirname "$dst")"
  sed "s/{{PROJECT}}/${NAME}/g" "$src" > "$dst"
  echo "add   ${dst#./}"
}

copy "$ROOT/templates/README.en.md"    "$DEST/README.md"
copy "$ROOT/templates/README.fa.md"    "$DEST/README.fa.md"
copy "$ROOT/templates/AGENTS.md"       "$DEST/AGENTS.md"
copy "$ROOT/templates/HANDOFF.md"      "$DEST/HANDOFF.md"
copy "$ROOT/templates/DECISIONS.md"    "$DEST/docs/DECISIONS.md"
copy "$ROOT/templates/OPEN-ITEMS.md"   "$DEST/docs/OPEN-ITEMS.md"
copy "$ROOT/templates/ARCHITECTURE.md" "$DEST/docs/ARCHITECTURE.md"
copy "$ROOT/templates/gitignore"       "$DEST/.gitignore"

mkdir -p "$DEST/docs/images"
[ -e "$DEST/docs/images/.gitkeep" ] || : > "$DEST/docs/images/.gitkeep"

echo
echo "next:"
echo "  1. fill README.md and README.fa.md with what is true TODAY"
echo "  2. git init && git add . && git commit -m 'docs: scaffold'"
echo "  3. python3 $ROOT/scripts/check-docs.py $DEST"
