# CLAUDE.md — Smart Data AI Training Modules

## Project Overview

This is Smart Data's open-source internal AI training curriculum. It lives at `github.com/Smart-Data-Ohio/AI-Training-Modules` and serves as the async education pillar of Smart Data's Developer Advocacy-led AI Training Program.

The program has three pillars (async modules, live sessions, open-source projects). This repo covers the first: self-paced training modules that any Smart Data developer — or external contributor — can work through independently.

**Owner:** Riel St. Amand (Developer Advocate, Smart Data)
**License:** MIT
**Audience:** Software developers with varying AI/ML experience levels. Assume strong programming fundamentals but zero ML background unless specified otherwise.

---

## Repository Structure

```text
AI-Training-Modules/
├── CLAUDE.md
├── README.md
├── LICENSE
│
├── 01-foundations/
│   ├── 01-llm-fundamentals/
│   │   ├── README.md          # Lesson content
│   │   ├── exercises/         # Hands-on work
│   │   └── resources/         # Supplementary links, diagrams
│   ├── 02-prompt-engineering/
│   ├── 03-ai-assisted-coding/
│   └── 04-ethics-and-liability/
│
├── 02-applied/
│   ├── 01-building-with-llm-apis/
│   ├── 02-evaluating-ai-tools/
│   ├── 03-ai-in-the-sales-cycle/
│   └── 04-agent-patterns-and-mcp/
│
├── 03-classical-ml/
│   ├── 01-problem-type-recognition/
│   ├── 02-sklearn-essentials/
│   ├── 03-neural-nets-with-keras/
│   ├── 04-decision-framework/
│   └── 05-capstone-cost-comparison/
│
├── 04-ai-security/
│   ├── 01-securing-ai-applications/
│   └── 02-ai-powered-security-tools/
│
├── 05-specialized/
│   ├── 01-databricks-ml-workflows/
│   ├── 02-fine-tuning-vs-rag/
│   └── 03-ai-infrastructure-and-cost/
│
├── 06-projects/
│   ├── 01-client-intake-simulator/
│   ├── 02-rag-system-build/
│   ├── 03-ml-pipeline-comparison/
│   └── 04-ai-security-audit/
│
└── resources/
    └── datasets/              # Shared datasets across modules
```

Each module folder follows the same internal pattern:

```text
module-name/
├── README.md          # The lesson itself — explanation, context, theory
├── exercises/         # Hands-on code, notebooks, or challenges
│   ├── starter/       # Skeleton code or starter notebooks
│   └── solutions/     # Completed reference solutions
└── resources/         # Links, diagrams, supplementary reading
```

---

## Prior Art: KCDC 2022 Workshop

Riel delivered a 4-hour ML Foundations workshop at KCDC (Kansas City Developer Conference) in 2022. The materials live at `github.com/CanadaApollo6/KCDC-2022-Materials` and should be referenced and adapted — not copy-pasted — when building modules in the `03-classical-ml/` category.

### What the KCDC workshop covers

- **Part 0:** Environment setup (Google Colab)
- **Part 1:** ML fundamentals & terminology (AI vs ML vs DL, supervised/unsupervised/reinforcement, the ML framework, overfitting/underfitting)
- **Part 2:** Data wrangling with Pandas & NumPy
- **Part 3:** Regression with scikit-learn (MAE, MSE, RMSE)
- **Part 4:** Classification with scikit-learn (accuracy, precision, recall)
- **Part 5:** Neural networks with TensorFlow

### Datasets available from KCDC repo

- `car-sales-extended.csv` / `car-sales-extended-missing-data.csv` — regression exercises
- `car_sales_dropped.csv` — data cleaning exercises
- `heart-disease.csv` — classification exercises

### How to adapt KCDC content

1. The KCDC workshop was a single monolithic Jupyter notebook. Break it into discrete, focused modules.
2. Update library references: the KCDC workshop used TensorFlow. The training modules should use **Keras** (which is now standalone, not just `tf.keras`). sklearn remains the same.
3. The KCDC content is aimed at conference attendees with zero ML experience. That's the right baseline for `03-classical-ml/` modules too.
4. Preserve Riel's teaching voice — conversational, builds intuition before formalism, uses analogies. Don't make it read like a textbook.
5. Add a consulting angle the KCDC workshop didn't have: each module should include a "Why This Matters for Consulting" section that connects the technical skill to client-facing work.
6. Add new datasets where appropriate. Don't rely solely on the car sales and heart disease data — variety keeps it engaging.

---

## Module Curriculum

### 01 — Foundations (4 modules)

The on-ramp. Assumes developers know how to code but have never worked with AI/ML beyond casual use of ChatGPT.

| #   | Module             | Core Concept                                                                            | Hands-On Exercise                                                                                        |
| --- | ------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 01  | LLM Fundamentals   | Tokens, context windows, temperature, embeddings, why models hallucinate                | Compare outputs across temperature settings; token counting exercise; demonstrate hallucination patterns |
| 02  | Prompt Engineering | Structured prompts, few-shot, chain-of-thought, system prompts, output formatting       | Build a prompt library for common consulting tasks; A/B test prompt strategies                           |
| 03  | AI-Assisted Coding | Copilot, Claude Code, Cursor — capabilities, limitations, when to trust/distrust        | Solve a real bug using three different AI coding tools; document where each fails                        |
| 04  | Ethics & Liability | Client data handling, IP concerns, what can/can't go into an API, bias, responsible use | Audit a sample prompt for PII leakage; draft a client-facing AI data policy                              |

### 02 — Applied (4 modules)

Building things with AI. Assumes completion of Foundations or equivalent experience.

| #   | Module                 | Core Concept                                                                                   | Hands-On Exercise                                          |
| --- | ---------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 01  | Building with LLM APIs | REST calls, function calling/tool use, RAG basics, structured outputs, streaming               | Build a simple RAG pipeline over a local document set      |
| 02  | Evaluating AI Tools    | Framework for assessing AI tools: accuracy, cost, latency, maintenance, vendor lock-in         | Score 3 real AI tools using a structured evaluation rubric |
| 03  | AI in the Sales Cycle  | Demos, proof-of-concepts, how to talk about AI to non-technical clients, managing expectations | Build a 15-minute AI demo for a hypothetical client brief  |
| 04  | Agent Patterns & MCP   | Agentic workflows, tool use, orchestration, Model Context Protocol                             | Build a simple MCP server; connect it to Claude Code       |

### 03 — Classical ML for Consultants (5 modules)

The differentiator. Teaches developers to recognize when a client doesn't need an LLM and to prototype the right solution. **Heavily informed by KCDC 2022 workshop materials.**

| #   | Module                    | Core Concept                                                                                         | Hands-On Exercise                                                        | KCDC Reference                                      |
| --- | ------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------- |
| 01  | Problem Type Recognition  | Classification, regression, clustering, anomaly detection — spotting them in the wild                | Given 10 business scenarios, identify the problem type and justify       | KCDC Part 1 (ML Framework)                          |
| 02  | sklearn Essentials        | Training, evaluation, cross-validation, random forest, logistic regression, SVM, k-means             | Train and evaluate models on provided datasets; compare performance      | KCDC Parts 2-4 (Pandas, regression, classification) |
| 03  | Neural Nets with Keras    | When to graduate from sklearn, basic architectures, training loop, callbacks                         | Build a simple feedforward network; compare to sklearn on same dataset   | KCDC Part 5 (TensorFlow → update to Keras)          |
| 04  | Decision Framework        | Given a problem: classical ML vs fine-tuning vs RAG vs raw LLM? Cost, latency, accuracy, maintenance | Decision tree exercise; map 5 client scenarios to recommended approaches | New — not in KCDC                                   |
| 05  | Capstone: Cost Comparison | Same business problem solved with sklearn, Keras, and an LLM API — full cost/performance analysis    | End-to-end project with written cost justification                       | New — not in KCDC                                   |

### 04 — AI Security (2 modules)

Non-negotiable for consulting. If you're building AI features for clients, you must understand the attack surface.

| #   | Module                    | Core Concept                                                                                         | Hands-On Exercise                                                               |
| --- | ------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 01  | Securing AI Applications  | Prompt injection, jailbreaking, data exfiltration, PII leakage, OWASP Top 10 for LLMs                | Attack/defend exercise: exploit a deliberately vulnerable AI app, then patch it |
| 02  | AI-Powered Security Tools | AI in threat detection, anomaly detection for security (ties to sklearn), security tooling landscape | Build a simple anomaly detection model for log analysis                         |

### 05 — Specialized (3 modules)

Deeper dives for developers working on specific technology tracks. These will evolve as Smart Data's AI practice matures.

| #   | Module                   | Core Concept                                                                                    | Hands-On Exercise                                                    |
| --- | ------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 01  | Databricks ML Workflows  | MLflow, Unity Catalog, Feature Store, medallion architecture for ML pipelines                   | Build an ML pipeline in Databricks Community Edition                 |
| 02  | Fine-tuning vs RAG       | When to customize a model vs augment at inference, cost/quality tradeoffs, dataset requirements | Fine-tune a small model on a domain-specific dataset; compare to RAG |
| 03  | AI Infrastructure & Cost | GPU costs, API pricing tiers, self-hosting vs managed services, build vs buy decision framework | Build a cost model spreadsheet for a hypothetical AI deployment      |

### 06 — Projects (3–4 capstone projects)

Multi-module integration. Designed for bench developers or anyone who wants to go deeper. These simulate real consulting scenarios.

| #   | Project                 | Modules Used                               | Deliverable                                  |
| --- | ----------------------- | ------------------------------------------ | -------------------------------------------- |
| 01  | Client Intake Simulator | Foundations + Applied + Decision Framework | Written recommendation + working prototype   |
| 02  | RAG System Build        | Applied (APIs, Agents) + Security          | Deployed RAG system with security review     |
| 03  | ML Pipeline Comparison  | Classical ML (all) + Cost Modeling         | Three implementations + cost analysis report |
| 04  | AI Security Audit       | Security + Applied                         | Vulnerability report + remediation PR        |

---

## Writing & Style Guide

### Voice

Riel's teaching voice — adapted from the KCDC workshop and Smart Data blog content:

- **Conversational, not academic.** Write like you're explaining to a smart colleague at a whiteboard, not writing a textbook. Think TED Talk energy, not lecture hall.
- **Build intuition before formalism.** Start with "here's why this matters" and an analogy before diving into the technical details.
- **Authority through experience, not tone.** Share real-world context (consulting scenarios, production gotchas) rather than using authoritative-sounding language.
- **Opinionated when it helps.** "Use random forest first, it's almost always good enough to validate the idea" is more useful than "there are many algorithms to choose from."
- **Honest about limitations.** If something is hard, say it's hard. If a tool has downsides, name them. Developers smell hedging.

### Structure (per module README)

Each module README should follow this structure:

```markdown
# Module Title

> One-sentence summary of what this module teaches and why it matters.

## Prerequisites

- What modules or knowledge are assumed

## What You'll Learn

- 3-5 bullet points, specific and measurable

## The Concept

- Main lesson content
- Use analogies, diagrams, code snippets
- Break into logical subsections

## Why This Matters for Consulting

- How does this skill translate to client work?
- Real or realistic scenarios
- What does this let you do that competitors can't?

## Exercises

- Link to exercises/ directory
- Brief description of each exercise
- Estimated time

## Take It Further

- Optional deeper dives
- External resources
- Related modules
```

### Code Standards

- **Python** for all ML/data science content (sklearn, Keras, pandas, numpy)
- **TypeScript/JavaScript** for API integration and tooling modules
- **Jupyter notebooks** (`.ipynb`) for exploratory/educational content in the Classical ML and Applied tiers
- **Standalone scripts** for exercises that should be run locally
- All code should run without paid services or API keys where possible. Use free tiers, local models, or mock data.
- Pin dependency versions in any requirements files.
- Include a `requirements.txt` or `package.json` at the module level if dependencies differ from the repo root.

### Datasets

- Store shared datasets in `resources/datasets/`
- Module-specific datasets go in the module's `exercises/` directory
- Prefer real-ish data over toy data. The KCDC car sales and heart disease datasets are good starting points.
- Always include a data dictionary (column descriptions, types, source)
- Never include client data, PII, or anything proprietary

---

## Brand

- **Company:** Smart Data (Dayton, OH based IT consulting)
- **Primary color:** `#5bb131` (green)
- **Secondary color:** `#1c212f` (dark navy)
- **Use brand colors** in any diagrams, slide decks, or visual materials produced for this repo

---

## Contributing

This repo is open source (MIT) but primarily maintained by Riel. Contributions from Smart Data developers (especially bench devs) are encouraged. External contributions are welcome.

### Before contributing

1. Check if there's an existing issue for the module or improvement you want to work on
2. If not, open one describing what you plan to do
3. Fork the repo, create a branch, make your changes
4. Ensure any code runs cleanly and any notebooks execute top-to-bottom
5. Submit a PR with a clear description of what changed and why

### PR standards

- Module READMEs should follow the structure defined in the Writing & Style Guide above
- Exercise code must include a working solution in `solutions/`
- Starter code must be functional (no syntax errors) with clear TODO comments
- No hardcoded API keys, tokens, or secrets

---

## Relationship to Other Repos

| Repo                                     | Relationship                                                                                                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CanadaApollo6/KCDC-2022-Materials`      | Prior art. 4-hour ML workshop (2022). Adapt concepts and datasets for `03-classical-ml/` modules. Do not copy-paste — update, restructure, and expand. |
| `Smart-Data-Ohio/Snowflake-CortexAI-Lab` | Reference for Applied modules — demonstrates a real AI-integrated lab environment                                                                      |
| `Smart-Data-Ohio/sd-harvest`             | Reference implementation for Agent Patterns & MCP module — a production MCP server                                                                     |

---

## Development Priorities

### Phase 1 — Foundation (Current)

- Scaffold all module directories (done)
- Write `01-foundations/` modules (high priority — this is the on-ramp)
- Adapt KCDC materials into `03-classical-ml/01-problem-type-recognition` and `03-classical-ml/02-sklearn-essentials`

### Phase 2 — Core Curriculum

- Complete `02-applied/` modules
- Complete remaining `03-classical-ml/` modules (neural nets, decision framework, capstone)
- Write `04-ai-security/01-securing-ai-applications`

### Phase 3 — Advanced & Projects

- `05-specialized/` modules (align with Databricks certification timeline)
- `06-projects/` capstone projects
- `04-ai-security/02-ai-powered-security-tools`

### Ongoing

- Update modules as tools and APIs evolve (this space moves fast)
- Add new datasets and exercises based on real consulting scenarios
- Incorporate feedback from live session participants
