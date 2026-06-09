#!/usr/bin/env python3
"""
find-emissary.py — search the official MCP Registry for an Emissary (MCP server).

A deliberately tiny, dependency-free helper for the `the-emissary` spell. You can
run it directly — OR just read it: it is simple enough to re-express in bash
(curl + jq), PowerShell, or JavaScript if that suits your harness better. Nothing
here is magic; it is one HTTP GET and a little printing.

It only DISCOVERS and prints. Binding an Emissary — running it, handing it
secrets — is always the conjurer's deliberate act. Propose; never auto-connect.

Usage:
    python3 find-emissary.py <keyword> [more words...]
    python3 find-emissary.py notion
    python3 find-emissary.py github issues

Equivalent raw call (port me to anything):
    curl -s "https://registry.modelcontextprotocol.io/v0/servers?search=<kw>&version=latest"
"""
import json
import sys
import urllib.parse
import urllib.request

API = "https://registry.modelcontextprotocol.io/v0/servers"


def search(keyword, limit=20):
    """One GET against the live Registry. Server-side search keeps it fast."""
    query = urllib.parse.urlencode({"search": keyword, "version": "latest", "limit": limit})
    req = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": "book-of-spells/the-emissary"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return [entry["server"] for entry in json.load(resp).get("servers", [])]


def connection(server):
    """One readable line per way this Emissary can be reached."""
    lines = []
    for remote in server.get("remotes", []) or []:
        lines.append(f"remote — {remote.get('type', '?')}: {remote.get('url', '')}".rstrip())
    for pkg in server.get("packages", []) or []:
        registry = pkg.get("registryType") or pkg.get("registry_type") or "?"
        identifier = pkg.get("identifier") or pkg.get("name") or "?"
        lines.append(f"package — {registry}: {identifier}")
    return lines or ["(no connection metadata listed)"]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    keyword = " ".join(sys.argv[1:])
    try:
        servers = search(keyword)
    except Exception as err:  # offline, or the Registry is unreachable
        print(f"Could not reach the MCP Registry ({err}).")
        print("Browse the directories in references/sources.md instead.")
        sys.exit(1)

    if not servers:
        print(f"No Emissary found for '{keyword}'. Try a broader word, or browse "
              f"the directories in references/sources.md.")
        return

    print(f"{len(servers)} Emissary candidate(s) for '{keyword}':\n")
    for server in servers:
        print(f"• {server.get('name', '?')}  (v{server.get('version', '?')})")
        desc = (server.get("description") or "").strip()
        if desc:
            print(f"    {desc}")
        for line in connection(server):
            print(f"    ↳ {line}")
        repo = (server.get("repository") or {}).get("url")
        if repo:
            print(f"    repo: {repo}")
        print()
    print("Discovery only — propose the chosen Emissary's connection to the user; "
          "let THEM add it and supply any secrets. Never auto-connect.")


if __name__ == "__main__":
    main()
