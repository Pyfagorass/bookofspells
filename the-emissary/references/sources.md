# Where to Seek Emissaries of the Pact (MCP servers)

Search these in order of trust. We **link** to them and **query** them live; we
never vendor or run a server from here. Discovery only — the binding is the
conjurer's.

## Canonical — the official MCP Registry

The source of truth, and **searchable server-side** (so one call, not a crawl):

```bash
# search by capability; version=latest collapses an Emissary's versions to one
curl -s "https://registry.modelcontextprotocol.io/v0/servers?search=<keyword>&version=latest"
```

Each result is a `server` object: `name`, `description`, `version`, `repository`,
and how to connect — `remotes[]` (a `streamable-http`/`sse` URL) and/or
`packages[]` (an `npm`/`pypi`/`oci` identifier to launch locally). The bundled
`scripts/find-emissary.py` wraps exactly this call; read it and port it freely.

- Registry home: https://registry.modelcontextprotocol.io/
- The list that used to live in `modelcontextprotocol/servers` now lives here.

## Official reference servers

- **modelcontextprotocol/servers** — https://github.com/modelcontextprotocol/servers
  The steering group's reference implementations (filesystem, fetch, git, memory,
  time, sequential-thinking, …). Good, vetted starting points.

## Reputable directories (breadth + reviews)

- **Awesome MCP Servers** — https://github.com/punkpeye/awesome-mcp-servers
  Large community list, organised by category with links to each server's repo.
  Browse freely, but apply the Trust Gate — **prefer the first-party Emissary**
  (the service's own official server) over a viral community one.
- **PulseMCP** — https://www.pulsemcp.com/ — servers, clients, and use-cases,
  with a newsletter.
- **Smithery** — https://smithery.ai/ — directory plus hosted/remote connections.

## How to choose

1. Look for the **first-party** server first (the house that makes the service).
2. Query the Registry (`scripts/find-emissary.py <keyword>`), or `jq`/grep the raw
   JSON for your capability.
3. Before proposing one, open its repo and read **what tools it exposes** and
   **what secrets it needs** — then hand the conjurer the connection to approve.
   Never connect it yourself.
