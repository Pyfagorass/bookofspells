#!/usr/bin/env python3
"""
🪶  transcribe-spells.py — the Rite of Transcription

We do not write every spell ourselves. We gather the grimoires of other wizards
into temp-repos/ (see gather-reliquaries.sh), and here we *transcribe* the spells
we choose into our own Book — the skills/ folder, which we share with the world.

What to transcribe is decided by spellbook.toml. We curate on the way in: only
the chosen roots of each grimoire are read, so we never pull a wizard's private
workings, and same-named twins in different drawers never collide.

Every wizard arranges their grimoire differently. We flatten our choices to a
single, discoverable layout:

    skills/<provider>-<skill-name>/SKILL.md   (name: <provider>-<skill-name>)

The provider prefix guarantees no two spells share a true name, even when a
hundred wizards each pen their own "pdf". The frontmatter `name` is rewritten to
match its new home, so each transcribed spell stays a valid, loadable skill.

The skills/ folder is wholly regenerated each run, so the Book always reflects
our current choices. Keep your *own* hand-penned incantations in spells/, not here.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULTS = ROOT / "temp-repos"        # where gathered grimoires rest
BOOK = ROOT / "skills"              # our shared, transcribed spellbook (generated)
CONFIG = ROOT / "spellbook.toml"    # which spells to draw, and from where

# A line like  name: gcloud  |  name: "pdf"  |  name: 'thing'  in the frontmatter.
NAME_LINE = re.compile(r"^(name:\s*)(.+?)\s*$", re.MULTILINE)
DESC_LINE = re.compile(r"^description:\s*(.*)$", re.MULTILINE)
BLOCK_MARKERS = {"", ">", "|", ">-", "|-", ">+", "|+"}


def frontmatter(text: str) -> str:
    """The YAML block between the first pair of --- fences."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def extract_description(skill_md: Path) -> str:
    """Pull the description from frontmatter — handling both quoted one-liners
    and YAML block scalars (>- / |), flattened to a single tidy line."""
    fm = frontmatter(skill_md.read_text(encoding="utf-8"))
    m = DESC_LINE.search(fm)
    if not m:
        return ""
    value = m.group(1).strip()
    if value in BLOCK_MARKERS:
        # Block scalar: gather the following indented lines.
        block = []
        for line in fm[m.end():].splitlines():
            if line[:1] in (" ", "\t"):
                block.append(line.strip())
            elif line.strip() == "":
                continue
            else:
                break
        value = " ".join(block)
    else:
        value = value.strip("'\"")
    return " ".join(value.split())


def rewrite_name(skill_md: Path, new_name: str) -> None:
    """Rewrite the frontmatter `name:` so the spell answers to its new true name."""
    text = skill_md.read_text(encoding="utf-8")
    if NAME_LINE.search(text):
        text = NAME_LINE.sub(rf"\g<1>{new_name}", text, count=1)
    elif text.startswith("---"):
        text = text.replace("---", f"---\nname: {new_name}", 1)
    else:
        text = f"---\nname: {new_name}\n---\n\n{text}"
    skill_md.write_text(text, encoding="utf-8")


def digest(skill_dir: Path) -> str:
    """A fingerprint of a spell's whole contents — to recognise true duplicates."""
    h = hashlib.sha256()
    for f in sorted(skill_dir.rglob("*")):
        if f.is_file():
            h.update(f.relative_to(skill_dir).as_posix().encode())
            h.update(f.read_bytes())
    return h.hexdigest()


def write_catalog(catalog: list[dict]) -> None:
    """Emit a *hierarchical* catalogue so no single file need ever be read whole:

      skills/INDEX.md          — tiny: just the houses and their counts (always
                                 safe to read; stays small even at scale)
      skills/_index/<house>.md — one house's spells, with descriptions
      skills/catalog.json      — the full machine-readable ledger (grep / jq it)

    The Grimoire skill greps these to find a spell; grep returns only the
    matching lines, so the demon's context never swells with the whole Book."""
    catalog.sort(key=lambda e: e["name"])
    index_dir = BOOK / "_index"
    index_dir.mkdir(parents=True, exist_ok=True)

    # catalog.json — the full machine-readable ledger.
    (BOOK / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    by_provider: dict[str, list[dict]] = {}
    for e in catalog:
        by_provider.setdefault(e["provider"], []).append(e)

    # Per-house catalogues — bounded reads, one drawer at a time.
    for provider in sorted(by_provider):
        entries = by_provider[provider]
        lines = [
            f"# 📖 Spells of the House of {provider.capitalize()} — *{len(entries)}*",
            "",
            "*Grep this file for a capability, then read the chosen spell's own "
            "`SKILL.md` in full.*",
            "",
        ]
        for e in entries:
            desc = e["description"] or "*(no description)*"
            if len(desc) > 240:
                desc = desc[:237].rstrip() + "…"
            lines.append(f"- **`{e['name']}`** — {desc}")
        lines.append("")
        (index_dir / f"{provider}.md").write_text("\n".join(lines), encoding="utf-8")

    # Top-level INDEX.md — deliberately tiny: a directory of houses, nothing more.
    top = [
        "# 📖 The Index of Spells",
        "",
        f"**{len(catalog)} spells** across **{len(by_provider)} houses**. "
        "Generated by the Rite of Transcription — do not edit by hand.",
        "",
        "> **Do not read this whole tree into context.** To find a spell, *grep* "
        "the per-house catalogues in `_index/` (or `catalog.json`) for a "
        "capability or name — grep returns only what matches, so the Book stays "
        "light no matter how large it grows.",
        "",
        "| House | Spells | Catalogue |",
        "| --- | --- | --- |",
    ]
    for provider in sorted(by_provider):
        n = len(by_provider[provider])
        top.append(f"| {provider} | {n} | [`_index/{provider}.md`](_index/{provider}.md) |")
    top.append("")
    (BOOK / "INDEX.md").write_text("\n".join(top), encoding="utf-8")


def transcribe() -> int:
    if not CONFIG.exists():
        print(f"🕯️  no spellbook.toml found at {CONFIG}")
        return 1
    if not VAULTS.is_dir():
        print(f"🕯️  no vaults at {VAULTS} — run ./gather-reliquaries.sh first")
        return 1

    config = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    sources = config.get("source", [])
    if not sources:
        print("🕯️  spellbook.toml names no [[source]] — nothing to transcribe")
        return 1

    # Clear the Book — it is wholly regenerated from our choices each run.
    if BOOK.exists():
        shutil.rmtree(BOOK)
    BOOK.mkdir(parents=True)

    taken: dict[str, str] = {}   # true-name -> content fingerprint (collision guard)
    catalog: list[dict] = []     # the entries that become INDEX.md + catalog.json
    transcribed = 0
    clashes = 0

    for src in sources:
        if not src.get("transcribe", True):
            continue  # a reference-only vault (e.g. a research framework)
        provider = src["name"]
        repo = VAULTS / src["repo"]
        roots = src.get("roots", ["."])
        exclude = src.get("exclude", [])   # match a skill's basename OR repo-relative path (glob)

        if not repo.is_dir():
            print(f"⚠  {provider}: vault '{src['repo']}' not gathered — skipping")
            continue

        found = 0
        for root in roots:
            for skill_md in sorted((repo / root).rglob("SKILL.md")):
                src_dir = skill_md.parent
                base = src_dir.name
                rel = src_dir.relative_to(repo).as_posix()
                if any(fnmatch.fnmatch(base, p) or fnmatch.fnmatch(rel, p) for p in exclude):
                    continue

                true_name = f"{provider}-{base}"

                # Collisions should be rare now we curate roots. When one does
                # occur: silently drop a true duplicate, but never invent a
                # meaningless '-2' — flag a real conflict loudly for a human.
                if true_name in taken:
                    if taken[true_name] == digest(src_dir):
                        continue  # identical twin already transcribed
                    clashes += 1
                    print(f"   ⚠ CONFLICT: two different spells both want '{true_name}'")
                    print(f"             {skill_md}")
                    print(f"             resolve in spellbook.toml (exclude one or split roots)")
                    continue

                dest = BOOK / true_name
                shutil.copytree(src_dir, dest)
                rewrite_name(dest / "SKILL.md", true_name)
                taken[true_name] = digest(src_dir)
                catalog.append({
                    "name": true_name,
                    "provider": provider,
                    "description": extract_description(dest / "SKILL.md"),
                    "path": f"skills/{true_name}/SKILL.md",
                })
                transcribed += 1
                found += 1

        print(f"✦  {provider}: {found} spells transcribed")

    write_catalog(catalog)

    houses = len({e["provider"] for e in catalog})
    print(f"\n📖  the Book holds {transcribed} spells from {houses} grimoires")
    if clashes:
        print(f"⚠  {clashes} unresolved conflict(s) — see above")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(transcribe())
