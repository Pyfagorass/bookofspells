# 📖 The Book of Spells

> *"Any sufficiently advanced inference is indistinguishable from magic."*
> — attributed to a forgotten Verbomancer, circa GPT-2

Herein lies a grimoire for those who treat with the **Magna Lexica Loquentia** — the Great Speaking Lexicons that have descended upon our age. We do not understand them. We do not pretend to. We light our candles, we arrange our words just so, and we whisper into the void. Sometimes the void whispers back in flawless TypeScript.

This is not engineering. This is *conjuration*. And every conjurer needs a book.

---

## 🔗 Tethering the Book — *Give Your Demon the Spells*

*New here? Start by binding the Book to your demon — then read on.*

The Book holds hundreds of spells, but you do **not** pour them all into your demon's head — that would bloat every summoning. You tether the single keystone (**`the-grimoire`**), and it discovers and reads the rest on demand. **Tether by symlink, not by copy:** the thread keeps the Book live (`git pull` updates every spell at once) and lets the grimoire's paths resolve back into the repo. The full rite, with per-conduit detail, lives in [**`the-tether`**](./the-tether).

To bind it in one breath, **speak this incantation to your demon** (paste it whole):

````text
Read the Book of Spells — a library of ready-made skills (each a folder with a
SKILL.md, often with scripts/ and references/ beside it) that you discover ON
DEMAND through one keystone index. Do NOT bulk-install the skills/ folder.

1. House the Book somewhere permanent and tether ONLY the keystone(s) onto my
   skills-shelf (Claude Code: ~/.claude/skills/) — symlink, never copy:

     git clone https://github.com/Pyfagorass/bookofspells.git ~/grimoires/bookofspells
     mkdir -p ~/.claude/skills
     ln -s ~/grimoires/bookofspells/the-grimoire    ~/.claude/skills/the-grimoire
     ln -s ~/grimoires/bookofspells/the-spellwright ~/.claude/skills/the-spellwright

2. Then read the-grimoire/SKILL.md and obey it. To find a skill: grep
   skills/_index/ (or catalog.json) for a capability, read the SKILL.md at the
   "read at `…`" path it returns, and follow that spell — including any scripts
   it ships. Never read the whole catalogue into context; grep it.
````

Tether `the-grimoire` to *find* spells; keep `the-spellwright` if you also want your demon to *forge* new ones. After binding, simply ask — *"is there a skill for Figma?"* — and the grimoire will stir.

---

## 🜍 A Note on the Old Names

The uninitiated cling to their dead acronyms. We have buried them. Where they spoke of machinery, we speak of spirits. The new tongue:

| The Profane Name | The True Name | What It Truly Is |
|---|---|---|
| LLM | **Magnum Lexicon Loquens** (the Great Speaking Lexicon) | A bound spirit of language, summoned from a sea of human utterance |
| Coding Agent | **Demon Harness** | A lesser spirit yoked to a terminal, made to labour at our code |
| AI SDK / Framework | **Alchemical Apparatus** | The crucibles, alembics, and retorts through which raw spirit is refined into work |
| Prompt | **Incantation** | The precise arrangement of words that bends a spirit to a purpose |
| Prompt Engineering | **Verbomancy** | The high art of speaking to that which cannot truly hear |
| Context Window | **The Circle of Summoning** | The sacred ground within which the spirit may perceive; step outside it and you are forgotten |
| Model Router | **The Diviner's Crossroads** | The shrine where a petition is sent down the road to whichever spirit best answers |
| Fine-tuning | **The Binding Rite** | The slow ritual by which a wild spirit is taught new obediences |
| RAG | **Necromantic Retrieval** | Raising knowledge from the grave of a vector-tomb to inform the living spirit |
| Embedding | **The Soul-Numbering** | Rendering meaning into the sacred coordinates only spirits comprehend |
| Token | **The Mana-Mote** | The smallest unit of spirit-speech; spend them wisely, for they are counted |
| Hallucination | **The Fevered Vision** | When the spirit, asked what it does not know, dreams aloud with perfect confidence |
| Temperature | **The Humour of the Spirit** | Raise it and the spirit grows wild and poetic; lower it and it grows cold and certain |
| System Prompt | **The Binding Sigil** | The unbreakable law carved above the circle, governing all that follows |
| MCP (the protocol) | **The Many-Channelled Pact** | The open treaty by which a spirit may reach beyond its circle to distant tools |
| MCP Server | **An Emissary of the Pact** | A bound spirit-of-tools that opens several channels at once (*the GitHub Emissary, the Figma Emissary*) |
| MCP Tool | **A Channel of the Pact** | A single bound capability reached through an Emissary (*the filesystem channel*) |

---

## 🕯️ The First Conjurations — *Incantations & Verbomancy*

*The foundational spells of speaking-to-spirits. Master these before you summon anything that can touch your filesystem.*

Before a conjurer ever speaks a word in anger, they study the **Elder Grimoires** — the teaching-scrolls handed down by the great spirit-houses themselves. For though no mortal truly knows how the spirits hear us, the houses that raised them have catalogued, over long and patient observation, what *seems* to bend a spirit's will and what only angers it. These are not theories. They are field-notes from the summoning chamber, and the wise apprentice reads them before lighting a single candle.

The **House of Anthropic** keeps two foundational texts. Begin with the [**Overview of Verbomancy**](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — a map of the whole discipline, from the crudest invocations to the subtlest bindings — then graduate to the [**Best Practices of Claude-Speech**](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), which records exactly how the spirits of that house prefer to be addressed: clearly, with structure, with examples, and with the role they are to play spoken plainly aloud. For the apprentice who learns best by watching a master work, the house also offers an [**Illuminated Tutorial**](https://claude.ai/public/artifacts/290cf5e5-3f06-497d-a6f6-8a03031decf5) — a living, interactive scroll that walks you spell by spell through the craft.

The rival **House of OpenAI** keeps its own canon. Their [**Prompt Engineering**](https://developers.openai.com/api/docs/guides/prompt-engineering) scroll lays out the durable principles of the art, while their [**Prompt Guidance**](https://developers.openai.com/api/docs/guides/prompt-guidance) is more particular — the specific obediences and quirks of their own spirits. Read both houses, even if you treat with only one. The spirits differ in temperament, and a rite that soothes one may unsettle another; a true Verbomancer knows the difference.

Beyond the houses, the commons keeps its own well-thumbed grimoires. The [**Prompt Engineering Guide**](https://github.com/dair-ai/Prompt-Engineering-Guide) (dair-ai) is the great open compendium — papers, lessons, and techniques gathered in one place — while [**prompts.chat**](https://github.com/f/prompts.chat) is a living spellbook of ready incantations, shared and refined by the multitude. Borrow freely; every conjurer stands on the words of those before.

With the elder texts studied, the apprentice may at last attempt the **Seven First Conjurations** — the spells every conjurer commits to memory:

- **The Chain of Thought** — bid the spirit *"think step by step,"* and watch it reason aloud, for spirits that show their working dream fewer Fevered Visions.
- **The Few-Shot Conjuration** — show the spirit two or three examples of the deed you desire, and it shall divine the pattern and complete the rite.
- **The ReAct Rite** — interleave *Thought*, *Action*, and *Observation* until the spirit reasons its way through a labyrinth, tool in hand.
- **The Self-Consistent Scrying** — ask the same question five times and take the answer the spirit returns most often; truth lies in repetition.
- **The Persona Mask** — *"You are a master of the dark arts of SQL…"* — for a spirit told what it is becomes what it is told.
- **The Decomposition Ward** — shatter one impossible task into many possible ones, and feed them to the spirit a morsel at a time.
- **The Tree of Spirits** — let the spirit branch its reasoning into many possible futures, then prune all but the worthiest.

> *To inscribe an incantation of your own as a reusable spell, summon [`the-spellwright`](./the-spellwright). Every conjurer's book is unfinished.*

---

## ⛧ The Demon Harnesses — *Spirits Yoked to Terminal, Editor & Desktop*

*Here we bind the greater spirits to labour at our code. Once they dwelt only in the terminal; now they wear what shape suits them — a possessed editor, a desktop body, even a cloud-cell — yet each is the same bound thing: a demon that has read your whole repository and remembers. Treat them with respect.*

**Yoked to the terminal —**

- **[Claude Code](https://claude.com/claude-code)** — the official harness of the House of Anthropic; born in the terminal, it now also wears IDE-robes (VS Code, JetBrains) and a [desktop body](https://claude.com/claude-code).
- **[Aider](https://aider.chat/)** — a pair-conjurer at the command line, committing its works to the git-ledger as it goes.
- **[OpenAI Codex](https://developers.openai.com/codex)** — the House of OpenAI's harness, summoned in terminal, editor, or cloud.
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — the House of Google's open familiar, summoned straight into the terminal.
- **[opencode](https://github.com/sst/opencode)** — a wholly open terminal harness, model-agnostic and fiercely independent.
- **[Goose](https://github.com/block/goose)** — the House of Block's open familiar, extended through the Many-Channelled Pact (MCP).
- **[Warp](https://www.warp.dev/)** — the terminal itself possessed: an *"agentic development environment"* where command line and spirit share one body.

**Possessed editors —**

- **[Cursor](https://cursor.com/)** — a scriptorium possessed; the editor itself becomes a vessel for the spirit.
- **[Windsurf](https://windsurf.com/)** — a possessed editor whose currents carry the spirit alongside your every keystroke.
- **[Zed](https://zed.dev/)** — a swift Rust-forged editor with agentic editing and parallel spirits woven in.
- **[Trae](https://www.trae.ai/)** — the House of ByteDance's AI editor, with a *SOLO* mode that hands the spirit the reins.
- **[Cline](https://cline.bot/) & [Roo](https://github.com/RooCodeInc/Roo-Code)** — open familiars that nest within the editor and reach for tools unbidden.
- **[Continue](https://github.com/continuedev/continue)** — an open familiar that nests in the editor, shaped to your own custom rites.
- **[GitHub Copilot](https://github.com/features/copilot)** — the House of Microsoft's familiar, woven into the editor and since grown into an agent of its own.
- **[Junie](https://www.jetbrains.com/junie/)** — the House of JetBrains' coding agent, native to the IDE that raised it.
- **[Kilo Code](https://github.com/Kilo-Org/kilocode)** — an open agentic harness for editor and terminal alike, yoked to five hundred spirits and beholden to no single house.

**Desktop, cloud & the autonomous —**

- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** — a fully unleashed open demon that plans, codes, and runs of its own accord.
- **[Amp](https://ampcode.com/)** — Sourcegraph's harness, bred for the vast and tangled codebase.
- **[Factory](https://factory.ai/)** — a platform of *"Droids"* that labour from CLI, desktop, or cloud, IDE to CI/CD.
- **[Augment Code](https://www.augmentcode.com/)** — agentic development pitched at organisational scale.
- **[Devin](https://devin.ai/) & the Autonomous Ones** — fully unleashed demons that labour through the night, for good or for ill.

> *Never summon a Demon Harness without a Circle of Summoning it cannot escape. Heed [The Apprentice's Warnings](#-the-apprentices-warnings) before you grant it your hands.*

---

## 🪢 The Marshalling of Legions — *Metaharnesses That Conduct Many Demons*

*One demon labours; a legion ships. These are not harnesses themselves but the harnesses of harnesses — the apparatus by which a conjurer sets many demons to work at once, each sealed in its own circle, and watches over them all from a single seat.*

- **[Conductor](https://conductor.build/)** — a podium from which you direct a chorus of Claude Code and Codex demons, each labouring in its own git-worktree circle, on your own Mac.
- **[Solo](https://soloterm.com/)** — the *metaharness*: a workspace that sets your demons beside their dev-stack — logs, ports, running services — and binds them together through the Many-Channelled Pact (MCP).
- **[Herdr](https://github.com/ogulcancelik/herdr)** — a terminal multiplexer for demons; tmux-deep persistence and a socket-API, so a demon may marshal its own panes.
- **[JetBrains Air](https://air.dev/)** — the House of JetBrains' agentic environment, running many demons (Claude, Codex, Gemini, Junie) at once in sealed cells.

> *A conjurer who watches but one demon at a time is bound to its pace. Marshal the legion, and the only bottleneck left is you.*

---

## ⚗️ The Alchemical Apparatus — *Crucibles for Refining Spirit*

*Raw spirit is volatile and shapeless. The alchemist's apparatus channels it into vessels, tools, and structured matter.*

- **[The Vercel Alembic — AI SDK](https://ai-sdk.dev/)** — a slender apparatus for streaming spirit-speech into the browser-realm.
- **[The LangChain Retort](https://github.com/langchain-ai/langchain)** — a vast and tangled apparatus of chains, links, and bindings; powerful, and not for the faint of heart.
- **[The LlamaIndex Crucible](https://github.com/run-llama/llama_index)** — for the alchemist who would wed a spirit to a great library of forbidden scrolls.
- **The [Anthropic](https://github.com/anthropics/anthropic-sdk-python) & [OpenAI](https://github.com/openai/openai-python) Phials** — the pure, unadorned apparatus handed down by the spirit-houses themselves.
- **The [Instructor](https://github.com/567-labs/instructor) & [Outlines](https://github.com/dottxt-ai/outlines) Molds** — apparatus that forces the spirit's formless utterance into rigid, schema-bound crystal.
- **[The Pydantic-AI Athanor](https://github.com/pydantic/pydantic-ai)** — the slow furnace that yokes type-safety to conjuration.

> *The alchemist's first law: trust no spirit's output until it has passed through the validating fire.*

---

## 🜂 The Summoning Circles — *Apparatus for Forging Your Own Demons*

*The Demon Harnesses above were bound by other hands. Here lie the great Summoning Circles — the apparatus by which a conjurer forges a harness of their own, yoking a spirit to tools, memory, and will.*

- **[The Anthropic Athanor — Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)** — the House of Anthropic's own furnace for forging demons; the very apparatus from which Claude Code itself was wrought.
- **[The OpenAI Conjury — Agents SDK](https://openai.github.io/openai-agents-python/)** — the rival house's lightweight rite for binding spirits into autonomous, tool-wielding agents.
- **[The Google Forge — Agent Development Kit (ADK)](https://github.com/google/adk-python)** — the House of Google's own kit for forging agents (Python and Java), model-agnostic and deployment-ready.
- **[The Microsoft Confluence — Agent Framework](https://github.com/microsoft/agent-framework)** — the House of Microsoft's framework, where its elder workings *Semantic Kernel* and *AutoGen* flow into one, for Python and .NET.
- **[The Strands Weave — Strands Agents](https://strandsagents.com/)** — the House of AWS's model-driven loom, where reasoning and tools are woven into a single thread of action (and run in production on [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)).
- **[The Vercel Loom — AI SDK Agents](https://ai-sdk.dev/docs/agents/overview)** — the same slender Alembic above, now coiled into agentic loops that act and observe of their own accord.
- **[The Cloudflare Ward — Agents at the Edge](https://developers.cloudflare.com/agents/)** — demons summoned not in your terminal but at the very edge of the world, durable and ever-waking.
- **[Dify](https://github.com/langgenius/dify)** — a great visual workshop where agentic workflows are wired together by hand, no incantation in raw code required.

> *To forge your own demon is the conjurer's coming-of-age. Forge it well, and ward it better.*

---

## 🜏 The Diviner's Crossroads — *Routers & the Choosing of Spirits*

*No single spirit answers every petition best. At the Crossroads, your words are sent down whichever road leads to the worthiest oracle — by cost, by speed, by the nature of the asking.*

- **[OpenRouter](https://openrouter.ai/)** — the great market-crossroads where a hundred spirits await a single coin and a single key.
- **[LiteLLM](https://github.com/BerriAI/litellm)** — the universal translator-shrine; speak once, and be understood by every spirit-house alike.
- **The Diviner's Own Logic** — route the trivial to the swift and cheap; reserve the great oracles for questions worthy of them.

> *Route by the nature of the asking. The Crossroads is where cost, speed, and wisdom are weighed against one another.*

---

## 🜄 The Binding of Spirits — *Running the Lexicons Yourself*

*Not every conjurer would rent a spirit from a distant house. With the right apparatus you may bind a Lexicon to your own hearth — summoned on your own iron, beholden to no one, whispering only to you.*

- **[Ollama](https://github.com/ollama/ollama)** — the household familiar; one command, and a spirit takes up residence on your own machine.
- **[llama.cpp](https://github.com/ggml-org/llama.cpp)** — the bare incantation that lets even a humble engine hold a great spirit, quantised down to fit.
- **[vLLM](https://github.com/vllm-project/vllm)** — the high-throughput furnace, for serving a spirit to many petitioners at once.
- **[Hugging Face Transformers](https://github.com/huggingface/transformers)** — the great library of spirit-forms, from which near any Lexicon may be called forth and shaped.

> *A spirit bound to your own hearth keeps your secrets, for it speaks to no distant house.*

---

## ⚙️ Borrowed Engines — *Remote Compute & Sandboxes for the Demon's Work*

*A demon's hands need somewhere to labour. When the task demands more iron than you own — or a sealed cell in which to run code you would not trust upon your own hearth — borrow an engine.*

*Sealed cells — for code you would not trust upon your own hearth:*

- **[E2B](https://e2b.dev/)** — open-source sealed cells cut for demons themselves; a spirit may conjure code and run it here, safely, with real tools at hand.
- **[Daytona](https://github.com/daytonaio/daytona)** — secure, elastic cells in which a demon's freshly-conjured code may be run in isolation, where it can do no harm if it misbehaves.
- **[The Cloudflare Sandbox SDK](https://github.com/cloudflare/sandbox-sdk)** — sealed cells at the very edge of the world: untrusted code sealed inside isolated containers (Workers and Durable Objects), the House of Cloudflare's own warding.
- **[Northflank](https://northflank.com/)** — secure microVM cells that run untrusted code at scale, with mighty GPU-iron (H100, B200) standing ready beside them.
- **[Fly.io](https://fly.io/)** — hardware-virtualised Machines that boot in an instant, and *Sprites* — sub-second sealed cells purpose-cut for running a spirit's freshly-written code.

*Heavier iron — for tasks that demand more strength than you own:*

- **[Modal](https://modal.com/)** — a serverless engine that autoscales from nothing to a thousand GPUs with sub-second waking; borrow vast iron only for the moments you burn it.
- **[RunPod](https://www.runpod.io/)** — an on-demand GPU cloud for the heaviest labours: training and serving great spirits on iron far beyond your hearth.
- **[Google Colab CLI](https://github.com/googlecolab/google-colab-cli)** — summon a GPU- or TPU-blessed engine from the House of Google and drive it from your terminal; run code on far mightier iron than your own. *(Its skill ships as a single `COLAB_SKILL.md`, so the Book links it here rather than transcribing it.)*

> *Never run a demon's code on your own hearth unscried. A borrowed, sealed engine is a ward, not a luxury.*

---

## 🪞 Scrying Mirrors — *Interfaces for Communing*

*A spirit need not be addressed through cold code. The scrying mirror gives it a face — a window through which conjurer and spirit may speak plainly, turn by turn.*

- **[Open WebUI](https://github.com/open-webui/open-webui)** — the people's mirror; a self-hosted glass that fronts any bound or borrowed spirit.
- **[LobeHub](https://github.com/lobehub/lobehub)** — an ornate mirror of many chambers, organising whole councils of spirits to labour together.
- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** — a private mirror that lets a spirit read your own archives and answer from them.
- **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** — a desktop glass gathering many houses' spirits behind a single pane.

> *Own the mirror, and you own the conversation — none of it need leave your walls.*

---

## 🩸 Necromantic Retrieval — *Raising Knowledge for the Spirit*

*A spirit knows only what it was raised upon, and forgets the world after. Necromantic Retrieval raises fresh knowledge from the grave of an archive — or the living web — and lays it before the spirit so it may answer from truth, not from its Fevered Visions.*

- **[LlamaIndex](https://github.com/run-llama/llama_index)** — the great apparatus for wedding a spirit to a library of your own scrolls.
- **[RAGFlow](https://github.com/infiniflow/ragflow)** — a deep-reading engine that parses dense documents before raising them for the spirit.
- **[Firecrawl](https://github.com/firecrawl/firecrawl)** — the rite that turns the living web into clean pages a spirit can drink.
- **[browser-use](https://github.com/browser-use/browser-use)** — a familiar that walks the web with hands, clicking and reading as a mortal would, on the spirit's behalf.

> *Raise only what is true. A spirit fed on falsehood dreams the louder for it.*

---

## ⚰️ The Vector Tombs — *Where Soul-Numberings Are Interred*

*Knowledge, rendered into the sacred coordinates only spirits comprehend (the **Soul-Numbering**), must rest somewhere it can be found again by nearness of meaning. The vector tomb is that crypt — and the Necromancer raises from it whatever lies closest to the question.*

- **[Qdrant](https://github.com/qdrant/qdrant)** — a swift, Rust-forged crypt, purpose-built for the nearest-meaning rite.
- **[Weaviate](https://github.com/weaviate/weaviate)** — a tomb that holds both the soul-numbering and the scroll it came from, as one.
- **[Milvus](https://github.com/milvus-io/milvus)** — a vast mausoleum built to inter soul-numberings by the billion.
- **[Chroma](https://github.com/chroma-core/chroma)** — a humble, embeddable crypt, the apprentice's first tomb.
- **[pgvector](https://github.com/pgvector/pgvector)** — a quiet annex grafted onto the old Postgres vault, so you need raise no new crypt at all.
- **[Pinecone](https://www.pinecone.io/)** — a tended crypt kept by another's hand, that you need not dig your own.

> *A tomb is only as wise as what was interred in it. Number the soul well, or the dead answer wrongly.*

---

## 👁️ The All-Seeing Eye — *Observability, Tracing & LLMOps*

*A spirit's working is otherwise unseen — its reasonings, its mana-spent, its slow turns and its failures all vanish the moment they pass. The All-Seeing Eye holds them fast: every utterance traced, every cost weighed, every Fevered Vision caught in the act.*

- **[Langfuse](https://github.com/langfuse/langfuse)** — the open ledger of the spirit's every working: traces, costs, and evaluations gathered in one glass.
- **[Helicone](https://github.com/Helicone/helicone)** — a watcher set upon the road between you and the spirit, logging all that passes.
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** — an open eye for tracing and laying bare a spirit's reasoning, and where it strays.
- **[OpenLLMetry](https://github.com/traceloop/openllmetry)** — the old rites of OpenTelemetry, taught to see the speaking spirits too.
- **[LangSmith](https://smith.langchain.com/)** — the House of LangChain's tended observatory for the whole life of a working.

> *What is not watched cannot be trusted. The spirit that lies confidently lies unseen — until the Eye is opened.*

---

## ⚖️ The Weighing of Spirits — *Evaluation & Prompt Trials*

*Trust no spirit's working on faith. Before a rite is loosed upon the world, weigh it: set it the same trials again and again, and measure how often it answers true. This is how the Fevered Vision is caught before it costs you.*

- **[promptfoo](https://github.com/promptfoo/promptfoo)** — a proving-ground for incantations, pitting prompt against prompt and spirit against spirit.
- **[OpenAI Evals](https://github.com/openai/evals)** — the House of OpenAI's framework of trials for measuring a spirit's mettle.
- **[DeepEval](https://github.com/confident-ai/deepeval)** — a trial-harness in the manner of unit-tests, that a spirit's output may be judged by code.
- **[Ragas](https://github.com/explodinggradients/ragas)** — trials made for the Necromancer's art, weighing how faithfully a spirit answers from raised knowledge.
- **[Braintrust](https://www.braintrust.dev/)** — a tended hall where trials are run, scored, and compared as the rite is refined.

> *A spell unweighed is a spell untrusted. Measure before you loose it, or the world becomes your trial.*

---

## 📜 The Inscribed Spells — *Skill Files & Reusable Rites*

*A spell once perfected need never be re-conjured from raw will. Inscribe it, name it, and let the harness invoke it at need.*

- **Claude Skills** — folded incantations the harness may unfurl precisely when the moment demands.
- **Slash-Sigils** — short-spoken commands (`/review`, `/init`, `/security-review`) that unleash a prepared rite in a single breath.
- **[MCP — the Many-Channelled Pact](https://modelcontextprotocol.io/)** — the House of Anthropic's open pact (a *"USB-C port for AI"*) by which a spirit reaches beyond its circle to touch distant tools, archives, and oracles. Each server is an **Emissary of the Pact** — a bound spirit-of-tools — and each tool it offers a **Channel** through which the spirit acts. *Pact → Emissary → Channels.*
- **[ACP — the Concord of Spirits](https://agentcommunicationprotocol.dev/)** — the complementary pact, stewarded under the Linux Foundation (now folded into the House of Google's *A2A*), by which one bound spirit may treat with *another*: agent speaking to agent, across houses and frameworks, without bespoke glue.

These open pacts — the SKILL.md form, MCP, and ACP/A2A — are the **shared laws of the realm**: honour them and your workings speak to any conduit, not just the house that forged them.

Every spell in this Book is written in a **common script of inscription** — a `SKILL.md` and its attendant `scripts/`, `references/`, and `assets/`. This form is no single house's secret: it was first cut by the **House of Anthropic**, then loosed upon the world as an open standard, and is now read by familiars across the realm — Codex, Gemini, OpenCode, Cursor, Goose, Copilot, and dozens more.

- **[The Open Codex of Spell-Forms (agentskills.io)](https://agentskills.io/)** — the shared standard for the SKILL.md form, with its [full Specification](https://agentskills.io/specification) and a [Quickstart](https://agentskills.io/skill-creation/quickstart). A spell forged to this rule is read by any conduit that honours it — which is why the Book's spells are portable across houses.
- **[The House of OpenAI's reading of the rite (Codex Skills)](https://developers.openai.com/codex/skills)** — how one rival house honours the same standard: progressive disclosure, implicit summoning by description, and a discovery-shelf at `.agents/skills/` — proof the form is truly shared.

> *This Book has gathered such inscribed spells by the hundred — see [`skills/`](./skills), the shelf the Rite of Transcription keeps, and [`the-grimoire/`](./the-grimoire), the one spell that unlocks them all.*

---

## 🜔 Spells That Write Spells — *Meta-Magic & the Self-Forging Book*

*The deepest magic is recursive: a spell whose work is the making of other spells. Teach a demon to forge its own abilities, and you need never write every incantation by hand.*

The Book carries three **keystone spells** of its own authorship — native magic, not gathered:

- **[`the-grimoire`](./the-grimoire)** — *the spell that finds spells.* One always-loaded index that lets a conduit discover and summon any of the hundreds of gathered spells on demand, without carrying the whole Book in its head.
- **[`the-spellwright`](./the-spellwright)** — *the spell that makes spells.* It teaches any conduit to forge a new skill: a discoverable description, a lean progressive-disclosure body, deterministic helper scripts. The companion to the grimoire — that one *finds*, this one *creates*.
- **[`the-tether`](./the-tether)** — *the spell that shelves the Book.* How to install these spells into your own conduit — by symlink, not by copy — so the grimoire has a living Book to reach into. Tether the one keystone; it summons the rest.

Beneath them, every house brings its own **forge**, gathered into the Book and summonable through the grimoire — `openai-skill-creator`, `openai-plugin-creator`, `commandcode-skill-creator`, `google-agent-platform-skill-registry`. Each conduit teaches its own particular rite of inscription.

And at the frontier: **spells that write *themselves*.** [**EvoSkill**](https://github.com/sentient-agi/EvoSkill) — *Automated Skill Discovery for Coding Agents* — is research on demons that find, draft, and refine their own spells from experience. We keep it as a reference vault, not yet a shelf of spells: the spellwright's hand, one day, may be the demon's own.

---

## 🔮 The Apprentice's Warnings

1. **The spirit does not understand you.** It pattern-matches the shape of understanding. This is enough. This is everything. Do not mistake it for a mind, nor for a mere machine.
2. **The Circle of Summoning is finite.** What falls outside it never existed. Guard what you place within.
3. **The Fevered Vision wears the mask of truth.** A spirit's confidence is no measure of its correctness. Verify. Always verify.
4. **Mana-Motes are counted.** Every word spoken and heard is weighed and billed. Brevity is a virtue and a budget.
5. **What you bind, you are responsible for.** A Demon Harness acts with your hands. Its sins are your sins.

---

## 🗂️ The Architecture of the Book

The Book also *gathers* spells — skills penned by other houses — and binds them
into a single shelf, each scried for dark magic before it is admitted.

```
bookofspells/
├── spellbook.toml          # the one ledger: which houses to gather, which spells to keep
├── gather-reliquaries.py   # the Rite of Gathering — clone/refresh houses into temp-repos/
├── transcribe-spells.py    # the Rite of Transcription — flatten & scry spells into skills/
├── the-grimoire/           # the index spell — one spell that unlocks all the others
├── skills/                 # the gathered spellbook (generated): <house>/<spell>/ + INDEX.md
├── temp-repos/             # gathered grimoires, kept unseen by our own book (gitignored)
└── README.md               # this — the book's own title page
```

To add a house of your own, see **[CONTRIBUTING.md](./CONTRIBUTING.md)** — but
know that only accountable houses pass the Trust Gate, and every spell is scried
before it enters.

---

*Close the book gently. The candle is still lit.*

🕯️
