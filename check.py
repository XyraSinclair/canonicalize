#!/usr/bin/env python3
"""Self-check: this repo's own consistency, enforced (BOOK.md property 2).

Stdlib only, offline, fast. Run: python3 check.py
Also a minimal live example of the templates/consistency-tests.md patterns.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FAILURES: list[str] = []


def check(ok: bool, msg: str) -> None:
    if not ok:
        FAILURES.append(msg)


def md_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


# 3. Links resolve -----------------------------------------------------------
for md in md_files():
    for target in re.findall(r"\]\(([^)]+)\)", md.read_text()):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = target.split("#", 1)[0]
        if path:
            check((md.parent / path).exists(),
                  f"broken link: {md.relative_to(ROOT)} -> {target}")

# 4. Multi-file versions agree ------------------------------------------------
plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
check(plugin["version"] == market["plugins"][0]["version"],
      "version mismatch: plugin.json vs marketplace.json")

# 5. Skill frontmatter contract ----------------------------------------------
for d in sorted((ROOT / "skills").iterdir()):
    if not d.is_dir():
        continue
    text = (d / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check(bool(m), f"{d.name}: missing frontmatter")
    if m:
        nm = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
        check(bool(nm) and nm.group(1) == d.name,
              f"{d.name}: frontmatter name != directory name")
        check("description:" in m.group(1), f"{d.name}: missing description")

# 1. Structural counts derive from source -------------------------------------
# BOOK.md declares seven properties; the count must match its numbered heads.
book = (ROOT / "BOOK.md").read_text()
props = len(re.findall(r"^## \d+\.", book, re.M))
check(props == 7, f"BOOK.md numbered properties: {props} != 7")
check("seven properties" in book,
      "BOOK.md prose count drifted from its numbered sections")
# DRIVE.md declares passes 0-6; verify the ladder is complete and ordered.
drive = (ROOT / "DRIVE.md").read_text()
passes = [int(n) for n in re.findall(r"^## Pass (\d+)", drive, re.M)]
check(passes == list(range(7)), f"DRIVE.md pass ladder broken: {passes}")

# 1b. Named-gap enumerations agree across surfaces ----------------------------
# This class struck four times in the self-drive (a gap row added or changed
# without sweeping the prose that enumerates the gaps). Enforced: every row
# whose label BEGINS with "named-gap" in the denominator must have its id
# named in the README's Status section.
canon = (ROOT / "docs" / "canonicality.md").read_text()
gap_ids = [m.group(1) for m in re.finditer(
    r"^\|\s*([A-E]\d+)\s*\|[^|]*\|\s*named-gap", canon, re.M)]
readme = (ROOT / "README.md").read_text()
check("## Status" in readme, "README lost its Status section; the gap guard needs it")
status = readme.split("## Status", 1)[-1]
for gid in gap_ids:
    check(gid in status,
          f"named-gap row {gid} missing from README Status enumeration")

# standalone-skill (BOOK property 3 / B5): no repo-relative dependencies ------
skill = (ROOT / "skills" / "canonicalize" / "SKILL.md").read_text()
check(not re.search(r"\]\((?!http)[^)]+\)", skill),
      "canonicalize skill carries relative links; it must execute standalone")

if FAILURES:
    print(f"FAIL ({len(FAILURES)}):")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print("OK: all consistency checks pass")
