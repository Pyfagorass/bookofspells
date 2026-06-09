#!/usr/bin/env python3
"""
🔮  divine-spells.py — the Rite of Divination

We gaze into the aether (GitHub) to discover new magic: spell repos to import,
and the wider tools, agents, and frameworks of the craft. Search finds
*everything* — houses and street magic alike — so each candidate skill-repo is
passed through the same Trust Gate we curate by, and labelled:

    HOUSE    — an accountable organization; promote into spellbook.toml
    REVIEW   — a borderline org, or an allowlisted individual; judge by hand
    STREET   — an unaccountable individual; popular maybe, but street magic

Nothing is imported automatically. The Rite writes a report
(divined-candidates.md); you skim it and paste the worthy HOUSE rows into
spellbook.toml, where the gather → scry → transcribe pipeline takes over.

Requires the `gh` CLI, authenticated. Run with: uv run divine-spells.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "spellbook.toml"
REPORT = ROOT / "divined-candidates.md"

# Topics that tend to mark a repo of skills ("spells") …
HOUSE_TOPICS = ["claude-skills", "agent-skills", "agent-skill",
                "claude-code-skills", "ai-skills", "skills"]
# … and topics for the wider craft — tools, agents, frameworks (README fodder).
TOOL_TOPICS = ["llm", "ai-agents", "llm-agents", "agent-framework",
               "llmops", "llm-tools", "rag", "llm-framework"]

PER_TOPIC = 15
THIS_YEAR = datetime.now(timezone.utc).year


def gh_json(args: list[str]):
    try:
        out = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=90)
    except FileNotFoundError:
        sys.exit("🕯️  the `gh` CLI is not installed — the aether is unreachable")
    if out.returncode != 0:
        return []
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return []


def search_topic(topic: str):
    return gh_json(["search", "repos", f"--topic={topic}", "--sort=stars",
                    f"--limit={PER_TOPIC}", "--json",
                    "fullName,stargazersCount,owner,pushedAt,description"])


_owner_cache: dict[str, dict] = {}


def owner_info(login: str) -> dict:
    """Fetch (and cache) an owner's accountability signals."""
    if login in _owner_cache:
        return _owner_cache[login]
    u = gh_json(["api", f"users/{login}"]) or {}
    info = {
        "login": login,
        "type": u.get("type", "?"),
        "year": (u.get("created_at") or "????")[:4],
        "repos": u.get("public_repos", 0),
        "verified": False,
    }
    if info["type"] == "Organization":
        o = gh_json(["api", f"orgs/{login}"]) or {}
        info["verified"] = bool(o.get("is_verified"))
    _owner_cache[login] = info
    return info


def verdict(info: dict, allowlist: set[str]) -> str:
    if info["type"] != "Organization":
        return "REVIEW" if info["login"].lower() in allowlist else "STREET"
    if info["verified"]:
        return "HOUSE"
    try:
        age = THIS_YEAR - int(info["year"])
    except ValueError:
        age = 0
    if age >= 5 and info["repos"] >= 30:
        return "HOUSE"
    return "REVIEW"


def load_known() -> tuple[set[str], set[str]]:
    """Return (slugs we already import, owners on the individual allowlist)."""
    have, allow = set(), set()
    for src in tomllib.loads(CONFIG.read_text(encoding="utf-8")).get("source", []):
        url = src.get("url", "")
        slug = url.split("github.com/", 1)[-1].rstrip("/").lower() if "github.com/" in url else ""
        if slug:
            have.add(slug)
            if src.get("trust") == "individual-allowlisted":
                allow.add(slug.split("/", 1)[0])
    return have, allow


def collect(topics: list[str]) -> dict[str, dict]:
    """Dedupe candidate repos across topics, keyed by full name."""
    found: dict[str, dict] = {}
    for topic in topics:
        for r in search_topic(topic):
            name = r.get("fullName")
            if name and name not in found:
                found[name] = r
    return found


def short(text: str | None, n: int = 90) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def main() -> int:
    if not CONFIG.exists():
        sys.exit(f"🕯️  no spellbook.toml at {CONFIG}")
    have, allowlist = load_known()
    print("🔮  scrying the aether for spell repos…")

    # ── Candidate houses (skill repos), gated ───────────────────────────────
    houses = []
    for name, r in collect(HOUSE_TOPICS).items():
        if name.lower() in have:
            continue  # already in the Book
        login = (r.get("owner") or {}).get("login") or name.split("/", 1)[0]
        info = owner_info(login)
        houses.append({
            "verdict": verdict(info, allowlist),
            "name": name,
            "stars": r.get("stargazersCount", 0),
            "type": info["type"],
            "age": (THIS_YEAR - int(info["year"])) if info["year"].isdigit() else "?",
            "repos": info["repos"],
            "verified": info["verified"],
            "push": (r.get("pushedAt") or "")[:7],
            "desc": short(r.get("description")),
        })
    order = {"HOUSE": 0, "REVIEW": 1, "STREET": 2}
    houses.sort(key=lambda h: (order.get(h["verdict"], 9), -h["stars"]))

    print("🔮  scrying for tools, agents & frameworks…")
    tools = []
    for name, r in collect(TOOL_TOPICS).items():
        tools.append({
            "name": name,
            "stars": r.get("stargazersCount", 0),
            "push": (r.get("pushedAt") or "")[:7],
            "desc": short(r.get("description")),
        })
    tools.sort(key=lambda t: -t["stars"])
    tools = tools[:30]

    # ── Write the report ────────────────────────────────────────────────────
    n_house = sum(1 for h in houses if h["verdict"] == "HOUSE")
    n_review = sum(1 for h in houses if h["verdict"] == "REVIEW")
    lines = [
        "# 🔮 Divined Candidates",
        "",
        "*Scryed from GitHub by topic, then gated by accountability. Nothing here "
        "is imported — promote worthy **HOUSE** rows into `spellbook.toml`, judge "
        "**REVIEW** by hand, ignore **STREET** magic however many stars it has.*",
        "",
        f"Found **{len(houses)}** new candidate houses "
        f"({n_house} HOUSE, {n_review} REVIEW) and **{len(tools)}** tools/frameworks.",
        "",
        "## 🏛️ Candidate Houses — *skill repos not yet in the Book*",
        "",
        "| Verdict | Repo | ⭐ | Type | Age | Repos | ✓ | Last push | What |",
        "| --- | --- | --: | --- | --: | --: | :-: | --- | --- |",
    ]
    badge = {"HOUSE": "✅ HOUSE", "REVIEW": "🟡 REVIEW", "STREET": "⛔ STREET"}
    for h in houses:
        v = "✓" if h["verified"] else ""
        lines.append(
            f"| {badge.get(h['verdict'], h['verdict'])} "
            f"| [`{h['name']}`](https://github.com/{h['name']}) | {h['stars']} "
            f"| {h['type']} | {h['age']} | {h['repos']} | {v} | {h['push']} | {h['desc']} |"
        )
    lines += [
        "",
        "## ⚗️ Candidate Tools & Frameworks — *for the prose grimoire (README)*",
        "",
        "| Repo | ⭐ | Last push | What |",
        "| --- | --: | --- | --- |",
    ]
    for t in tools:
        lines.append(
            f"| [`{t['name']}`](https://github.com/{t['name']}) | {t['stars']} "
            f"| {t['push']} | {t['desc']} |"
        )
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"\n📜  {len(houses)} candidate houses ({n_house} HOUSE, {n_review} REVIEW), "
          f"{len(tools)} tools → {REPORT.name}")
    if n_house:
        print("   Top houses to consider:")
        for h in [h for h in houses if h["verdict"] == "HOUSE"][:5]:
            print(f"     ✅ {h['name']}  ({h['stars']}⭐)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
