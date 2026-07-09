#!/bin/sh
# Install the canonicalize skill into an agent's personal skills dir.
#
#   ./install.sh                 # -> ~/.claude/skills/canonicalize/
#   SKILLS_DIR=/path ./install.sh
#
# Claude Code users can instead install as a plugin (see README):
#   /plugin marketplace add XyraSinclair/canonicalize
#
# Idempotent: re-running updates the copy in place.

set -eu

here=$(cd "$(dirname "$0")" && pwd)
dest="${SKILLS_DIR:-$HOME/.claude/skills}"

mkdir -p "$dest/canonicalize"
cp "$here/skills/canonicalize/SKILL.md" "$dest/canonicalize/SKILL.md"

echo "installed canonicalize -> $dest/canonicalize"
echo "the skill executes alone; the full doctrine, templates, and receipts live in the repo"
