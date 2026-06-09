#!/usr/bin/env python3
"""
🗝️  gather-reliquaries.py — the Rite of Gathering

Reads the grimoires named in spellbook.toml and summons each into temp-repos/.
A vault already gathered is renewed (git pull); one never seen is cloned afresh
(--depth 1 — we read the relic as it lies today, not the full archaeology of its
making). The wards of .gitignore keep temp-repos/ unseen by our own book.

This is the gathering half of the rite; transcribe-spells.py is the transcribing
half. Both read the same spellbook.toml, so the Book has a single source of truth.
"""

from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULTS = ROOT / "temp-repos"
CONFIG = ROOT / "spellbook.toml"


def git(*args: str, cwd: Path | None = None) -> int:
    return subprocess.run(["git", *args], cwd=cwd).returncode


def gather() -> int:
    if not CONFIG.exists():
        print(f"🕯️  no spellbook.toml found at {CONFIG}")
        return 1

    sources = tomllib.loads(CONFIG.read_text(encoding="utf-8")).get("source", [])
    if not sources:
        print("🕯️  spellbook.toml names no [[source]] — nothing to gather")
        return 1

    VAULTS.mkdir(exist_ok=True)
    tended = 0

    for src in sources:
        url = src.get("url")
        if not url:
            print(f"⚠  {src.get('name', '?')}: no url — skipping")
            continue
        repo = src.get("repo") or url.rstrip("/").rsplit("/", 1)[-1]
        dest = VAULTS / repo

        if (dest / ".git").is_dir():
            print(f"🜂  renewing relic: {repo}")
            rc = git("-C", str(dest), "pull", "--ff-only", "--quiet")
            print("    ✦ up to date" if rc == 0 else "    ✗ could not renew")
        else:
            print(f"🗝️  summoning relic: {repo}")
            rc = git("clone", "--depth", "1", "--quiet", url, str(dest))
            print("    ✦ gathered" if rc == 0 else "    ✗ could not gather")
        if rc == 0:
            tended += 1

    print(f"🔮  the rite is complete — {tended} reliquaries tended in temp-repos/")
    return 0


if __name__ == "__main__":
    sys.exit(gather())
