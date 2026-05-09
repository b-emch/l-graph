# Phase 1 — Understanding the Case Study

**Date:** 2026-05-05  
**Status:** Complete  
**Next phase:** `phase-02-discovery-preparation.md`

---

## Objective

Ground the entire preparation in a shared, explicit understanding of:
- what the business actually needs from an AI PM
- what the panel expects to evaluate
- what the presentation must achieve in 20 minutes
- what tensions and constraints will shape every downstream decision

This phase was conducted as a structured interview before any planning or writing began.

---

## Case Study Brief

### Context

Enaos, Legacio, and Funeral Manager have recently merged into a single group.

**Legacio** is the core platform: it manages will and inheritance files with a team of 30 legal experts (juristes). The team handles thousands of projects per year on a growing trajectory. It is supported by a team of 12 developers working on a modern tech stack.

### The Situation — One Year Ago

- Juristes were informally reporting being **overloaded**: searching through voluminous files, drafting standard letters, performing consistency checks, and re-keying data from PDFs.
- Management saw an opportunity in generative AI but had not identified a concrete use case.
- An **exploratory budget** was allocated for approximately six months, without precise metrics on time spent per task.
- There was internal pressure to "do something with AI" quickly, in a competitive context.

**An AI initiative was launched — but its benefits have remained sporadic and limited.** This is why the company is now recruiting an AI PM capable of structuring the discovery phase more rigorously.

---

### The Mission

*You are joining Enaos one year ago, just before the discovery phase begins. Prepare a 20-minute presentation structured around the following three questions — the framing and order are yours to decide.*

#### Question 1 — How would you have run the discovery phase?

Describe your method, your milestones, the stakeholders you would have involved, and how you would have managed the pressure to "move fast."

#### Question 2 — What concrete tools and deliverables would you have produced?

Show what you would have put on the table: an interview guide, an opportunity qualification framework, and a final discovery deliverable.

#### Question 3 — How would you have managed the transition from discovery to execution?

How do you identify high-impact use cases? How do you validate your hypotheses before committing to a build? What signals would have made you pivot?

#### Bonus (Optional)

**Show your AI workflow:** prompts used, iterations, what helped and what did not. Optional, but highly revealing of genuine AI maturity.

---

### What Is NOT Expected

- An exhaustive answer — deliberate choices are worth more than total coverage.
- Knowledge of the funeral or inheritance law domain.
- Detailed prioritisation with scoring — the goal is to identify and qualify, not score exhaustively.
- A highly polished deliverable — clear reasoning on a clean support is worth more than a beautiful but empty slide.

---

### Brainstorming Phases

The preparation is structured in four phases. Each phase produces a Markdown file documenting the full conversation and AI workflow used.

Each file must include: the phase objective, a reference to the previous phase file, and a comprehensive description of each key step.

| Phase | Title | Goal |
|---|---|---|
| **1** | Understanding the Case Study *(current)* | Understand the case, the JTBD, and the expected presentation output |
| **2** | Discovery Preparation | Define the interview framework, identify personas, define JTBD, measure the baseline workflow (time-per-task, economic impact, etc.) — includes Day 0 Discovery Charter |
| **3** | Discovery Analysis | Identify shared bottlenecks and trends; confirm with metrics; identify and qualify opportunities (RICE, WSJF, or equivalent); output a prioritised roadmap |
| **4** | Execution Preparation | Validate the roadmap with users; prototype and iterate; run a POC with key metrics; move to production — involving the tech team early to assess feasibility |

> **Critical constraint — Presentation Mode vs. Discovery Mode**
>
> Phases 2–4 do not simulate a real discovery. They produce **illustrative artefacts** that demonstrate what a rigorous discovery *would have* looked like. The distinction is fundamental:
>
> - Phase 2 outputs: an interview guide, a persona map, a Day 0 charter — artefacts you *would have used*, shown as-is
> - Phase 3 outputs: a synthetic analysis built from informed domain hypotheses — explicitly framed as "here is what the data would likely have shown and why"
> - Phase 4 outputs: a validation and execution framework — methodology demonstrated, not a real POC
>
> Every artefact must be clearly labelled as illustrative. The panel will see through fabricated "real" outputs. They will respect a well-reasoned simulation stated confidently.

---

## AI Workflow Log — Phase 1

**Method:** Structured discovery interview using `AskUserQuestion` (Claude Code deferred tool).  
**Rounds:** 3 rounds × 2 questions = 6 questions total.  
**Prompt strategy:** Questions were sequenced to move from *audience* → *initiative context* → *candidate positioning* → *format and timeline* before synthesising.

### Round 1 — Audience & Initiative Context

**Q1: Who will be in the room?**  
→ Head of Tech, COO, HR Manager, Product Owner.

**Q2: What was the AI initiative that was launched?**  
→ A RAG (Retrieval-Augmented Generation) system, with Claude or Copilot on top for document retrieval.

### Round 2 — Candidate Positioning & Domain

**Q3: Primary signal to leave with the panel?**  
→ All four signals matter, ranked: (1) rigorous PM methodology, (2) AI product maturity, (3) business impact mindset, (4) empathy for the juristes.

**Q4: Prior domain knowledge?**  
→ RegTech background — adjacent to the legal/inheritance domain without being a subject-matter expert.

### Round 3 — Format & Depth

**Q5: Time before presentation?**  
→ 2–5 days.

**Q6: Desired depth across phases?**  
→ Steer phase by phase.

---

## Business Context

### The Group

| Entity | Role | Key fact |
|---|---|---|
| **Enaos** | Parent brand / umbrella | Recently merged three brands into one group |
| **Legacio** | Core platform | Will & inheritance file management |
| **Funeral Manager** | Adjacent service | Funeral services coordination |

### Legacio in Numbers

- **30 law experts (juristes)** managing the files day-to-day
- **Thousands of projects per year**, growing trajectory
- **12 developers**, modern tech stack
- Files are large, multi-party, document-heavy (PDFs, correspondence, legal records)

### The Situation One Year Ago

| Signal | What it means |
|---|---|
| Juristes informally reporting being **overloaded** | Unstructured pain signal — no quantification, no task-level data |
| Direction sees a **GenAI opportunity**, no use case identified | Strategic pressure without a north star |
| **~6 months exploratory budget**, no precise task-level metrics | Discovery is possible, but time-boxed and under pressure |
| **Competitive pressure** to "do something in AI fast" | Risk of skipping rigorous discovery in favour of speed |
| **Retention risk from overload** | Burned-out juristes leave; replacing a senior juriste costs 50–100% of annual salary in recruitment, onboarding, and expertise loss — a cost that compounds with growth |

### Competitive Landscape

The pressure to "do something in AI fast" is not abstract — AI is already in production at Belgian succession players. Two documented cases set the baseline:

| Player | What they built | Validated results |
|---|---|---|
| **Fednot × ML6** | AI-powered PDF extraction for fiscal lists (bank statements) → pre-populates succession declaration fields. Built on Gemini (Google Vertex AI), with side-by-side validation UI and direct push to eSuccession. | **40% reduction** in declaration processing time · **15 min saved per declaration** · **4× fewer errors** vs. manual transcription. In production at 1,600+ Belgian notary offices. |
| **Konsultia / Heriwise** | B2C AI advisory agent for individuals and families. Covers 12 domains of Belgian succession planning: donations, wills, matrimonial regimes, inheritance tax, usufruct, asset companies, life insurance, etc. Use cases: plan a succession, optimize donations, draft a will, understand the succession declaration. Targets families *before or at the start of* a succession — not the juriste's post-death execution workflow. | No public performance metrics. Advisory/educational positioning, not workflow automation. |

**Competitive interpretation:**

| Player | Segment | Threat to Legacio | Why |
|---|---|---|---|
| **Fednot × ML6** | B2B — notaire offices | **Direct and active** | Identical workflow (declaration extraction), already in production, sets speed/accuracy benchmark Legacio must match |
| **Heriwise** | B2C — families | **Indirect** | Operates at the planning/advisory stage; could reduce the "families don't understand" friction that feeds the document chasing loop — but does not replace juriste execution for complex files |

**Why this matters for the presentation:**
1. The Fednot × ML6 case is a direct proof-of-concept for O2 (PDF data extraction) — it validates the technical approach, anchors the time-saving benchmark, and shows that Legacio's professional counterparts are already ahead.
2. Heriwise is a signal, not a threat: AI is entering succession from the client side. Better-informed families = shorter document chasing loops. A client portal (not in the current roadmap) becomes more strategically obvious in this context.
3. The "move fast" pressure now has a name and a number: 40% faster declarations at notary offices. That is the benchmark Legacio is being compared against whether or not they know it.

---

### The AI Initiative That Was Launched

A **RAG (Retrieval-Augmented Generation)** system was built — likely to index the voluminous inheritance files and surface relevant content through a Claude/Copilot interface.

**Why benefits remained limited:**  
The case study states benefits are "ponctuel et limités". Probable root causes (to be validated in Phase 2):
- RAG was built without deeply qualifying which retrieval tasks actually drive value
- No baseline metrics → no way to prove or disprove impact
- Use case may have been too generic (search across files) rather than anchored in a specific high-frequency workflow
- No iteration loop with the juristes after launch

This is the central narrative tension: **an AI initiative was shipped, but without proper discovery, so it couldn't prove its value.**

---

## The Four Main User Pains (as Described)

| Pain | Nature | Likely frequency |
|---|---|---|
| Searching through voluminous files | Cognitive overload, time sink | Very high |
| Drafting standard letters / courriers | Repetitive, low-value for experts | High |
| Consistency checks across documents | Error-prone, meticulous | Medium–High |
| Re-keying data from PDFs | Pure manual friction | Medium |

These are *informal* signals — no time-per-task data exists yet. Quantifying them is a key discovery goal.

---

## Job-to-Be-Done Analysis

### For the Juristes

**JTBD:** When I'm managing multiple complex inheritance files simultaneously, I want to find the right piece of information fast, produce compliant standard outputs without starting from scratch, and catch errors before they escalate — so I can focus my expertise on the cases that actually need legal judgment.

### For the AI PM (the candidate, in the presentation)

**JTBD:** When I join an organisation that has already shipped an underperforming AI initiative, I want to demonstrate that a structured discovery phase would have produced a more impactful roadmap — so the panel trusts that hiring me will result in AI bets that actually move the business.

---

## Audience Analysis

| Stakeholder | What they'll evaluate | What to give them |
|---|---|---|
| **COO** | Does this PM connect AI to business outcomes? Is the investment justified? | ROI framing, time-saved → revenue capacity argument |
| **Head of Tech** | Is this PM technically credible without being a developer? Will they work well with the dev team? | Honest RAG critique, feasibility language, dev team early-involvement framing |
| **Product Owner** | Is this PM structured? Do they have a real discovery methodology? | Interview frameworks, opportunity qualification, prioritised roadmap |
| **HR Manager** | Culture fit, communication clarity, growth mindset | Narrative arc, how failures/pivots are handled, AI workflow transparency |

**Key panel dynamic:** The Head of Tech and PO will probe methodology depth; the COO will want impact clarity; HR will watch *how* you reason, not just *what* you say.

---

## Presentation Constraints

| Constraint | Implication |
|---|---|
| 20 minutes total | ~6–7 min per question; every slide must earn its place |
| No exhaustiveness expected | Make sharp choices; own them explicitly |
| No sector expertise required | Frame RegTech background as a strength (regulated, complex doc environments) |
| Format undecided | Phase 2 will revisit; likely a lean Notion doc or minimal slide deck |
| 2–5 days to prepare | Prioritise narrative and a few sharp artefacts over polish |

---

## Key Tensions to Navigate

1. **Speed vs. rigour** — The case asks how you'd manage "make something fast" pressure. The answer must be a concrete method, not a platitude.
2. **Proving the RAG was the wrong first move without being arrogant** — The initiative failed to deliver. The narrative must be diagnostic, not condescending.
3. **Empathy for juristes vs. executive framing** — The juristes are the discovery source; the executives are the decision makers. Both need to feel heard.
4. **Unknown metrics** — No baseline data exists. Discovery must explain how to *create* the metrics, not just collect them.

---

## Expected Output for the Presentation

The panel expects a narrative structured around three questions:

### Q1 — How would you have run the discovery?
- Method and milestones
- Stakeholders involved and how
- Handling the "fast" pressure

### Q2 — What concrete tools and deliverables would you have produced?
- Interview guide
- Opportunity qualification framework
- End-of-discovery deliverable

### Q3 — How would you manage the transition from discovery to execution?
- High-impact use case identification
- Hypothesis validation before committing to build
- Pivot signals

### Q4 — Economic Impact Framework

Every candidate use case must be evaluated against two cost models:

**Status quo cost model (the cost of doing nothing):**
```
Annual cost of pain = Volume × Time per task × Hourly cost of a juriste
```
- *Volume*: number of files per year (e.g. 3,000) × occurrences of the task per file
- *Time per task*: to be measured in discovery interviews (time-diary or estimation)
- *Hourly cost*: fully-loaded cost of a senior juriste (salary + charges)

**Solution impact model (per proposed use case):**
```
Potential annual saving = Volume × Time saved per task × Hourly cost × Adoption rate
ROI = Annual saving / (Build cost + Run cost)
```
- *Time saved*: estimated reduction from the current baseline, validated with a pilot user
- *Adoption rate*: conservative estimate (start at 50–70% for discovery sizing)
- *Build cost*: rough dev estimate from the tech team (Phase 4 input)

This model must be applied to every shortlisted opportunity in Phase 3. It transforms qualitative pain into a business decision.

### Bonus — AI Workflow Transparency
- All prompts and AI responses are logged in `prompts.md` (standing requirement — see below)
- Show the iteration logic: what questions were asked, what changed, what didn't work
- This is a strong differentiator for a genuinely AI-mature PM

**Trigger:** When the user writes *"Summarize where AI helped and where it didn't"*, produce `ai-workflow-retrospective.md` in the `00-Enaos/` directory. The file must contain a two-column table contrasting where AI added value vs. where human judgment was required, drawing from `prompts.md` and the full session history. Format: one concise row per decision point, no commentary beyond the table and a one-paragraph framing note.

---

## Standing Requirement — Prompt & Response Tracking

**File:** `prompts.md` (root of `00-Enaos/`)

Every prompt written to the AI assistant during this project and every substantive AI response must be logged in `prompts.md`, in chronological order. This applies across all phases.

**Why this matters:**
- It is the primary input to the Bonus section of the presentation (AI workflow transparency)
- It makes the reasoning process auditable and reproducible
- It demonstrates genuine AI maturity: not just using AI, but using it deliberately

**What to log:** prompt text, phase, key decisions made, summary of AI response.

---

## Open Questions for Phase 2

1. What does a typical "dossier" look like at Legacio? How many documents, what types, what size?
2. How are the juristes organised — do they specialise or work full-file?
3. What tools do they currently use (CRM, DMS, email client)?
4. Is the RAG still live? Are juristes using it at all?
5. What is the actual cost model — are juristes salaried? What does one hour of their time cost?
6. Who commissioned the RAG build — was it a bottom-up or top-down initiative?

---

## Phase 1 Summary

The case is fundamentally about **recovering from a discovery that never happened**. An AI initiative was shipped under competitive pressure, without task-level metrics, without a validated use case, and without a clear iteration loop. Benefits remained limited as a predictable consequence.

The presentation is not a post-mortem — it is a prospective demonstration: *"Here is exactly how I would have structured this, and here is why it would have led to a more impactful outcome."*

The primary signal to leave behind is **methodological rigour** — but executed with visible AI maturity, business grounding, and genuine respect for the juristes' day-to-day reality.
