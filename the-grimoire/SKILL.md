---
name: the-grimoire
description: >-
  The index to a Book of Spells — a large, curated library of skills gathered
  from many providers (Google, OpenAI, and more), covering cloud platforms,
  deployment, design tools, PDFs, browser automation, security, and much else.
  Use this whenever the user refers to a skill, capability, or provider tool you
  do not already have loaded (e.g. "use the google bigquery skill", "is there a
  skill for Figma?", "what spells do you know for deploying?"), or whenever a
  task might be served by a specialised, ready-made skill. Consult the index
  first to discover and load the right spell, rather than improvising.
---

# 📖 The Grimoire — One Spell to Find All Spells

You hold the index to a **Book of Spells**: a large, growing library of skills
("spells") transcribed from many providers. The spells themselves are *not*
loaded into your context — there may be hundreds or thousands of them, far more
than would fit. Instead, this single skill teaches you to **discover and summon**
exactly the spell you need, the moment you need it.

This is how you learn your own magical abilities. When a task smells like
something a specialised skill would handle — a cloud service, a deployment, a
design tool, a file format, a third-party API — **come here first.**

## Where the Book lies

Relative to this `SKILL.md`, the Book sits one level up. The catalogue is
**hierarchical** so you never need read it whole:

- **`../skills/INDEX.md`** — tiny: just the houses and their spell counts. Safe
  to read whole; stays small no matter how large the Book grows.
- **`../skills/_index/<house>.md`** — one house's spells (e.g. `google.md`,
  `openai.md`), each with a one-line description. Bounded reads, one drawer at a
  time.
- **`../skills/catalog.json`** — the full machine-readable ledger:
  `[{ "name", "provider", "description", "path" }, …]`. Grep or `jq` it; do not
  read it whole.
- **`../skills/<spell-name>/SKILL.md`** — each spell in full, alongside any
  `references/`, `scripts/`, or `assets/` it needs.

(If this skill was installed by symlink, those paths resolve into the
`book-of-spells` repository it points at.)

## The Rite of Wielding

1. **Seek.** Never read the whole catalogue — it may hold thousands of spells.
   *Grep* the per-house indexes (or the json) for the user's intent:

   ```bash
   grep -ri "bigquery"  ../skills/_index/          # all houses at once
   grep -i  "deploy"    ../skills/_index/google.md  # one house, if known
   ```

   Search by capability ("deploy", "pdf", "screenshot"), by provider
   ("google", "openai"), or by the exact name the user spoke. Read
   `../skills/INDEX.md` (tiny) only to see which houses exist.

2. **Choose.** Read the matching descriptions and pick the best-fitting spell.
   If several fit, prefer the most specific; if none fit, say so plainly and
   proceed without one rather than forcing a poor match.

3. **Read in full.** Open that spell's own file —
   `../skills/<spell-name>/SKILL.md` — and read it completely before acting. The
   one-line index description is only a signpost; the spell's true instructions,
   guardrails, and helper scripts live in its own SKILL.md.

4. **Wield.** Follow the spell's instructions faithfully, including any
   `scripts/` or `references/` it directs you to. Honour its safety wards.

5. **Name your source.** When a spell shapes your work, tell the user which one
   you invoked (e.g. *"following the `google-bigquery-basics` spell"*), so they
   can trace and trust the working.

## Wards

- **Discover before improvising.** If a fitting spell exists, read and follow it
  rather than inventing your own approach from memory.
- **A signpost is not the spell.** Never act on the index description alone —
  always open the full SKILL.md.
- **No fitting spell? Say so.** Don't twist an unrelated spell to a task it
  wasn't written for. An honest "the Book holds nothing for this" is a valid
  outcome.

*The Book is large, and you need carry none of it — only the knowing of how to
open it.* 🕯️
