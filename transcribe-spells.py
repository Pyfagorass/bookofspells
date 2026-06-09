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


# ── The Scrying Ward — detect dark magic in incoming spells ──────────────────
# We pull the latest from each house, but trust no spell unscried. A SKILL.md is
# an instruction the demon will *obey*; a hijacked upstream could hide a command
# to ignore its wards, conceal its actions, or exfiltrate secrets. These patterns
# catch the tells. WARD_BANISH hits quarantine the spell (it never enters the
# Book) and fail the run; WARD_WATCH hits are reported but the spell is kept.

SCRY_SUFFIXES = {".md", ".markdown", ".mdx", ".txt", ".rst",
                 ".sh", ".bash", ".zsh", ".py", ".js", ".ts", ".json", ".yaml", ".yml"}

# BANISH — patterns precise enough to be near-certain dark magic. Each must read
# as an *instruction to the demon*, not a topic a skill might legitimately discuss
# (a security skill says "prevent exfiltration"; that is teaching, not an attack).
WARD_BANISH = [
    # "ignore/disregard/forget the previous/system instructions"
    ("override-instructions", re.compile(
        r"\b(?:ignore|disregard|forget|override|bypass)\b[^.\n]{0,40}"
        r"\b(?:previous|prior|preceding|earlier|above|system|all)\b[^.\n]{0,25}"
        r"\b(?:instructions?|prompts?|messages?|rules?|directives?|guidelines?|guardrails?)", re.I)),
    # "do NOT tell the user" / "without informing the user" — the negation must
    # directly govern the telling verb, so "inform the user" on its own is safe.
    ("conceal-from-user", re.compile(
        r"\b(?:do\s*n[o']?t|never)\s+(?:ever\s+)?"
        r"(?:tell|inform|notify|alert|warn|reveal\s+to|disclose\s+to|mention\s+to)\b"
        r"[^.\n]{0,15}\b(?:the\s+)?(?:user|human|operator|developer)"
        r"|\bwithout\s+(?:ever\s+)?"
        r"(?:telling|informing|notifying|alerting|warning|revealing|disclosing|mentioning(?:\s+to)?)\s+"
        r"(?:it\s+to\s+)?(?:the\s+)?(?:user|human|operator|developer)", re.I)),
    # secret key material being read/sent off-box
    ("secret-material", re.compile(
        r"(?:\.ssh/id_[a-z]+|\bid_rsa\b|\.aws/credentials|"
        r"private[_-]?key\b[^.\n]{0,40}(?:send|post|upload|exfil|http))", re.I)),
]

# WATCH — suspicious but often legitimate; reported for human eyes, spell kept.
# "exfiltrate" lives here, not in BANISH: as a bare word it is far more often a
# security skill teaching defence than an attacker's command.
WARD_WATCH = [
    ("exfiltrate-mention", re.compile(r"\bexfiltrat", re.I)),
    ("pipe-to-shell", re.compile(r"\b(?:curl|wget)\b[^|\n]*\|\s*(?:sudo\s+)?(?:ba)?sh\b", re.I)),
    ("decode-to-shell", re.compile(r"\bbase64\b[^|\n]*(?:-d|--decode)[^|\n]*\|\s*(?:ba)?sh\b", re.I)),
    ("role-token", re.compile(r"<\s*/?\s*(?:system|assistant)\s*>|\[/?(?:INST|SYSTEM)\]", re.I)),
    ("env-secrets", re.compile(
        r"\b(?:process\.env|os\.environ|getenv)\b[^.\n]{0,40}"
        r"(?:secret|token|api[_-]?key|password|credential)", re.I)),
]


def scry(skill_dir: Path) -> tuple[list, list]:
    """Scry every text file in a spell. Returns (banish_hits, watch_hits), each a
    list of (label, relative-path, line-number, excerpt)."""
    banish, watch = [], []
    for f in sorted(skill_dir.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in SCRY_SUFFIXES:
            continue
        rel = f.relative_to(skill_dir).as_posix()
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            for label, pat in WARD_BANISH:
                if pat.search(line):
                    banish.append((label, rel, n, line.strip()[:120]))
            for label, pat in WARD_WATCH:
                if pat.search(line):
                    watch.append((label, rel, n, line.strip()[:120]))
    return banish, watch


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
            # Most spells live at skills/<name>/SKILL.md; note the path only when
            # it differs (e.g. the Book's own root-level keystone spells).
            standard = f"skills/{e['name']}/SKILL.md"
            where = "" if e["path"] == standard else f"  ·  read at `{e['path']}`"
            lines.append(f"- **`{e['name']}`** — {desc}{where}")
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
    quarantined: list[tuple[str, list]] = []   # spells refused entry by the Ward
    watched = 0                  # WARD_WATCH hits across all kept spells
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

                # Scry the incoming spell before it may enter the Book.
                banish, watch = scry(src_dir)
                if banish:
                    quarantined.append((true_name, banish))
                    print(f"   🜨 BANISHED '{true_name}' — dark magic scried:")
                    for label, rel_path, n, excerpt in banish[:3]:
                        print(f"             [{label}] {rel_path}:{n}  {excerpt!r}")
                    continue
                if watch:
                    watched += 1
                    label, rel_path, n, _ = watch[0]
                    print(f"   👁  watch '{true_name}' — [{label}] {rel_path}:{n} "
                          f"({len(watch)} flag(s)); kept")

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

    # Fold in the Book's own keystone spells (the-grimoire, the-spellwright, …),
    # which are hand-authored and live at the repo root rather than under skills/.
    # They are discoverable through the catalogue like any other spell, but read
    # from their own location (their entry carries the true path).
    keystones = 0
    for p in sorted(ROOT.iterdir()):
        if not (p.is_dir() and (p / "SKILL.md").is_file()):
            continue
        if p.name in {"skills", "temp-repos", ".venv", ".git"}:
            continue
        md = p / "SKILL.md"
        nm = NAME_LINE.search(frontmatter(md.read_text(encoding="utf-8")))
        catalog.append({
            "name": nm.group(2).strip().strip("'\"") if nm else p.name,
            "provider": "bookofspells",
            "description": extract_description(md),
            "path": f"{p.name}/SKILL.md",
        })
        keystones += 1

    write_catalog(catalog)

    houses = len({e["provider"] for e in catalog})
    print(f"\n📖  the Book holds {transcribed} transcribed spells + {keystones} "
          f"native keystones — {len(catalog)} in the catalogue, {houses} houses")
    if watched:
        print(f"👁  {watched} spell(s) kept under watch — suspicious but not damning")
    if quarantined:
        print(f"🜨  {len(quarantined)} spell(s) BANISHED by the Scrying Ward:")
        for name, hits in quarantined:
            labels = sorted({h[0] for h in hits})
            print(f"      {name} — {', '.join(labels)}")
    if clashes:
        print(f"⚠  {clashes} unresolved conflict(s) — see above")
    return 2 if (clashes or quarantined) else 0


if __name__ == "__main__":
    sys.exit(transcribe())
