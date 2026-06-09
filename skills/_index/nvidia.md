# 📖 Spells of the House of Nvidia — *11*

*Grep this file for a capability, then read the chosen spell's own `SKILL.md` in full.*

- **`nvidia-aiq-deploy`** — Use when asked to install, deploy, run, validate, troubleshoot, or stop NVIDIA AI-Q Blueprint infrastructure.
- **`nvidia-aiq-research`** — Use when asked to run deep research or AI-Q research through a reachable NVIDIA AI-Q Blueprint backend.
- **`nvidia-cuopt-user-rules`** — Base rules for end users calling NVIDIA cuOpt (routing/LP/MILP/QP/install/server). Not for cuOpt internals — use cuopt-developer for those.
- **`nvidia-dynamo-interconnect-check`** — Validate that a Dynamo deployment's NIXL/UCX/NCCL interconnect is ready for disaggregated serving over RDMA/NVLink. Use after recipe-runner brings a deployment up (especially disagg/multi-node) to confirm the KV transport is correct; use…
- **`nvidia-dynamo-router-starter`** — Start or patch Dynamo router modes and run router endpoint smoke checks. Use for round-robin, KV-aware, least-loaded, or device-aware routing setup; use recipe-runner for recipe deployment and troubleshoot for failure diagnosis.
- **`nvidia-nemoclaw-user-get-started`** — Installs NemoClaw, launches a sandbox, and runs the first agent prompt. Use when onboarding, installing, or launching a NemoClaw sandbox for the first time. Trigger keywords - nemoclaw quickstart, install nemoclaw openclaw sandbox, nemoh…
- **`nvidia-omniverse-cad-to-simready`** — Coordinate the end-to-end CAD/source-asset to SimReady workflow. Use for broad requests such as CAD to SimReady, source asset to simulation-ready USD, or prop packaging that require conversion, material/physics assignment, SimReady confo…
- **`nvidia-omniverse-realtime-viewer`** — Use as the top-level router for Omniverse Realtime Viewer USD app requests and focused viewer reference documents.
- **`nvidia-omniverse-usd-performance-tuning`** — Top-level workflow skill for USD performance diagnosis and optimization. Use for slow loading, high memory, low FPS, or 'optimize my scene' requests; delegates auth/runtime setup to Phase 0 owners.
- **`nvidia-physical-ai-infrastructure-setup-and-resilient-scaling`** — Use when the user wants to set up, scale, validate, or harden NVIDIA physical AI infrastructure for synthetic data generation workflows across local MicroK8s or Azure AKS, including Kubernetes clusters, inference endpoint deployment, OSM…
- **`nvidia-physical-ai-neural-reconstruction`** — Router for NVIDIA NuRec/NRE: USDZ rendering, NCore conversion, 3DGS, gRPC sensor sim, PhysicalAI HF datasets. Do NOT use for SimReady or infra setup.
