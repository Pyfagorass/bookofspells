# 📖 Spells of the House of Montecarlo — *17*

*Grep this file for a capability, then read the chosen spell's own `SKILL.md` in full.*

- **`montecarlo-analyze-root-cause`** — Investigate data incidents and find root causes using Monte Carlo's observability data. Guides the agent through systematic investigation: alert lookup, lineage tracing, ETL checks, query analysis, and data profiling. Activates when a us…
- **`montecarlo-asset-health`** — Check the health of a data table/asset using Monte Carlo. Activates on "how is table X", "check health of X", "is X healthy", "status of X", "check on X table", or any health/status question about a data asset.
- **`montecarlo-automated-triage`** — Triage Monte Carlo alerts interactively or build an automated workflow. Fetch, score, and troubleshoot alerts using MCP tools now, or design a reusable workflow that runs on a schedule.
- **`montecarlo-connection-auth-rules`** — Build a Connection Auth Rules for a Monte Carlo connection type. Fetches live connector schemas and transform steps from the apollo-agent repo.
- **`montecarlo-context-detection`** — Route data-related requests to the right Monte Carlo skill or workflow. USE WHEN alerts, incidents, data broken, stale, coverage gaps, data quality, or any ambiguous data observability request.
- **`montecarlo-generate-validation-notebook`** — Generate SQL validation notebooks for dbt changes. Pass a GitHub PR URL or local dbt repo path.
- **`montecarlo-incident-response`** — Orchestrate incident response — triage, root cause, remediate, prevent recurrence. USE WHEN active alerts, data broken, stale, pipeline failure, or investigate and fix a data incident.
- **`montecarlo-instrument-agent`** — Instrument a new AI agent in a Python codebase for Monte Carlo Agent Observability. Detects AI libraries, installs the Monte Carlo OpenTelemetry SDK, and proposes tracing setup and decorator placements as diffs. Asks before editing any f…
- **`montecarlo-manage-mac`** — Create, edit, validate, and import Monitors-as-Code YAML files. CLI-first; falls back to MC MCP tools, then manual validation.
- **`montecarlo-monitoring-advisor`** — Analyze data coverage, create monitors for warehouse tables and AI agents. Covers coverage gaps, use-case analysis, data monitor creation, and agent observability.
- **`montecarlo-performance-diagnosis`** — Diagnoses pipeline performance issues -- slow jobs, expensive queries, latency trends -- using Monte Carlo's cross-platform observability. Uses a tiered investigation approach: discover problems, bridge to affected tables, then drill int…
- **`montecarlo-prevent`** — Shift-left safety net for dbt/SQL model edits. Runs change impact assessment before edits, generates SQL validation queries after, and executes them via `/mc-validate run`. Delegates health and monitor creation to peer skills.
- **`montecarlo-proactive-monitoring`** — Guide users from coverage analysis to monitor creation. USE WHEN user asks what should I monitor, where are my gaps, improve coverage, or wants a systematic approach to monitoring across their data estate.
- **`montecarlo-push-ingestion`** — Expert guide for Monte Carlo's push ingestion model. Use this skill whenever a customer or engineer mentions: pushing data to Monte Carlo, the IngestionService, pycarlo push APIs, build me a collection script, push metadata/lineage/query…
- **`montecarlo-remediation`** — Investigate and remediate data quality alerts using Monte Carlo MCP tools. Runs root cause analysis, assesses blast radius, discovers available tools (MCP/CLI/API), proposes and executes fixes, or escalates with full context when uncertain.
- **`montecarlo-storage-cost-analysis`** — Analyze a warehouse for stale, unused, or redundant tables via the analyze_storage_costs MCP tool. Classifies waste patterns and table categories, computes safety tiers, and handles category drill-downs and lineage follow-ups.
- **`montecarlo-tune-monitor`** — Analyze a Monte Carlo monitor and recommend config changes to reduce alert noise. Supports metric, custom SQL, validation, and table monitors. Fetches the report, identifies patterns, and suggests tuning.
