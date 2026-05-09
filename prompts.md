# Prompt & Response Log — Enaos AI PM Case Study

**Purpose:** Track every user prompt and AI response produced in this folder, across all phases.  
**Requirement:** Every prompt written in `00-Enaos/` must be logged here, in chronological order, with the full AI response. This file is a key input to the Bonus section of the presentation (AI workflow transparency).

---

## Session 1 — 2026-05-05

---

### Prompt 1 — Case Study Brief & Phase Kickoff

**Role:** User  
**Phase:** Phase 1 — Understanding the Case Study

> Act as a Senior AI Product Manager with strong skills in customer discovery in a blurry AI context.
>
> Brainstorm with me on the AI Product Manager Case Study from Enaos, Legacio and Funeral Manager.
>
> The three brands have merged into one group. Legacio offers a platform to manage will and inheritance files, with a team of 30 law experts. The team manages thousands of projects per year and it's growing. A team of 12 devs with a modern tech stack.
>
> Here is some context in French about the case study:
>
> **La situation, il y a un an:**
> - Les juristes remontaient informellement être surchargés : recherches dans dossiers volumineux, rédaction de courriers standards, vérifications de cohérence, ressaisies depuis PDFs
> - La direction voyait une opportunité dans l'IA générative, sans use case identifié
> - Un budget exploratoire était alloué pour ~6 mois, sans métriques précises sur le temps passé par tâche
> - Pression interne pour "faire quelque chose en IA" rapidement, dans un contexte concurrentiel
>
> Une initiative IA a été lancée — ses bénéfices restent ponctuels et limités. C'est pourquoi nous recrutons un AI PM capable de mieux structurer cette phase de discovery.
>
> The phases: 1. Understanding of the case study / 2. Discovery preparation / 3. Discovery analysis / 4. Execution preparation.
>
> Using the skill AskUserQuestions, interview me to perfectly understand the business case before thinking or writing anything. Then, produce the output of phase 1.

**AI Response:**  
Conducted a 3-round structured interview using `AskUserQuestion` (6 questions total). Produced `phase-01-understanding.md`.

**Key decisions made:**
- Sequenced questions: audience → initiative → positioning → format/timeline
- Identified central narrative: "recovering from a discovery that never happened"
- Chose not to write anything before completing the interview

---

### Prompt 2 — PM Assessment of the Plan

**Role:** User  
**Phase:** Phase 1 (review)

> As Senior Product Manager, what do you think of this plan?

**AI Response:**  
Delivered a critical PM assessment with 6 points:

1. **Phases simulate a real discovery but the output is a presentation** — key structural issue: phases 2–4 must produce *illustrative artefacts*, not real discovery outputs.
2. **RAG diagnosis is a list of maybes** — need one clear, confident diagnosis: the RAG was built on qualitative signals rather than workflow-anchored, quantified use cases.
3. **"Thousands of projects" is the key economic lever, underused** — build a cost model from the volume and time-per-task data.
4. **30 juristes ≠ one persona** — segment at minimum by seniority and task profile.
5. **AI workflow bonus is underrated** — should be a deliberate asset, not an afterthought.
6. **Open questions should become discovery hypotheses** — avoid presenting gaps, present structured curiosity.
7. **Missing: Day 0 artefact** — Discovery Charter before any interview.

---

### Prompt 3 — Selective Agreement & New Requirements

**Role:** User  
**Phase:** Phase 1 (revision)

> I agree with 1, edit Phase 1 understanding accordingly.
> I agree with 3 that we must evaluate the economic impact of the status quo and if we suggest ideas the economic impact of each solution. Edit Phase 1 understanding accordingly (add expected outputs or framework).
> I agree with 4, that's just part of phase 2 the discovery preparation.
> I agree with 5, that's why I need you to save all my prompts to you in a file prompts.md. You must save my prompt to you and your answer. Write this in Phase 1 so that it's known as a key requirement while working on other phases. Basically, all prompts written in the current folder 00-Enaos must be tracked and saved.
> Day 0 artefact will be produced during phase 2.

**AI Response:**  
- Created this file (`prompts.md`) as the canonical prompt/response log for the project.
- Edited `phase-01-understanding.md` to:
  - Clarify the "presentation mode vs. discovery mode" distinction in the Brainstorming Phases section
  - Add an economic impact framework to the Expected Outputs section
  - Add a `prompts.md` tracking requirement as a standing key requirement
  - Note that the Day 0 artefact (Discovery Charter) is a Phase 2 deliverable

---

## Session 2 — 2026-05-05

**Purpose of this session:** Build the raw knowledge base for the case study by scraping all content from legacio.be — blog articles and all chapters from the three guides. This is preparatory material for phases 2–4.

---

### Prompt 4 — Scrape Legacio Blog & All Guide Chapters

**Role:** User  
**Phase:** Raw content acquisition (pre-Phase 2)

> Search, Find and Save original raw content from https://www.legacio.be/blog. Search for content related to the will and inheritance process. For instance 'Remplir sa déclaration de succession par soi-même et sans notaire : Region wallonne et Bruxelles Capitales' must be downloaded. Search and save similar content. Also in this page, you'll find 'Nos Guides'. There are 3 guides: [Préparer son Testament, Succession après Décès, Anticiper Déclarations de Volonté]. Save all the sub chapters of these guides.

**AI Response:**  
Fetched the legacio.be blog and all three guide index pages. Identified ~22 blog articles and 39 chapters across 3 guides. Saved all content as individual HTML files to `/raw/`. Encountered a path typo in a prior run (wrong username); corrected and re-saved the 5 affected chapters (35–39).

**Files produced:**
- `raw/Blog_*.html` — 22+ blog articles on succession, wills, and Belgian inheritance law
- `raw/Guide_*.html` — 3 guide overview files
- `raw/Chapitre_01.html` through `raw/Chapitre_39.html` — all 39 chapters:
  - Chapters 1–12: *Préparer son Testament* guide
  - Chapters 13–17: *Anticiper Déclarations de Volonté* guide
  - Chapters 18–39: *Succession après Décès* guide
- 7 regulatory PDF files (Belgian succession law references)

**Key decisions made:**
- Fetched guide index pages to extract authoritative chapter URLs rather than guessing slugs (prevented 404 errors for chapters 36 and 38)
- Saved minimal but faithful HTML structure — original headings, paragraphs, and lists preserved for downstream LLM processing
- Files named with sequential chapter numbers for easy ordering

---

## Session 3 — 2026-05-06

**Purpose of this session:** Build the structured knowledge base with semantic/domain connections for the case study based on inheritance law and best practices.

---

### Prompt 5 — Build the knowledge graph

**Role:** User  
**Phase:** Raw content analysis (pre-Phase 2)

> /graphify ./raw --mode deep --obsidian --svg

**AI Response:**  
Fetched the legacio.be blog and all three guide index pages. Identified ~22 blog articles and 39 chapters across 3 guides. Saved all content as individual HTML files to `/raw/`. Encountered a path typo in a prior run (wrong username); corrected and re-saved the 5 affected chapters (35–39).

**Files produced:**
- `graphify-out/` — Knowledge Graph with an Obsidian Vault and SVG file


---

## Session 2 — 2026-05-06

---

### Prompt 2 — Phase 2 Discovery Plan

**Role:** User  
**Phase:** Phase 2 — Discovery Preparation

> Act as a Senior Product Manager, with a strong expertise in user discovery in a blurry environment.
>
> **CONTEXT:**
> I am preparing an AI PM case study for Legacio/Enaos as described in @phase-01-understanding.md
> I am starting phase 2 "Discovery preparation"
> As I am not an expert in inheritance or will redaction, I scrapped Legacio content and official regulation on the web and I have built a knowledge graph around the concepts: Succession Tax & Costs, Wills & Intestate Distribution, Asset Liability, and others. Use the skill /graphify to interact with the knowledge graph @graphify-out/
>
> **TASK:**
> Prepare a plan for my discovery phase including all the artifacts that must be prepared, such as but not exclusively:
> - List of metrics to implement and measure how the current workflows work
> - List of stakeholders that must be involved in the discovery (Juristes - inc sub-group of juristes, Dev, Ops)
> - Interview templates
> - Raw feedback collection process
> - Feedback triage/clustering and qualification process
> - Discovery plan divided in phases
>
> **OBJECTIVES:**
> The objectives of the customer discovery are:
> - Collect raw feedback
> - Know precisely the key workflows of the juristes when managing will redaction or inheritance files, including the business metrics (inc cost/revenue)
> - Identify the bottlenecks in these workflows
> - Being able to quantify and qualify these bottlenecks and the cost of inaction
> - Define the personas
>
> **OUTPUT:**
> A markdown file Discovery_plan.md
>
> Use AskUserQuestions to better define this prompt and the objectives before starting planning and writing the plan

**AI workflow decisions:**
- Used `/graphify query` on existing knowledge graph (graphify-out/) to orient in the domain before planning — identified 5 workflow clusters from the graph's community structure
- Used `AskUserQuestion` (4 questions) to clarify: purpose of the artifact (illustrative), stakeholder scope (juristes + ops + dev for technical blockers only), economic model depth (full with placeholders), and timeline (4-week sprint)
- User mid-plan corrections incorporated: (1) document collection loop added as Cluster 1 with non-linear metrics; (2) bottleneck confirmation protocol requiring both qualitative + quantitative signals; (3) AI sentiment probe added to juriste interview as a trust diagnostic; (4) shadow observation promoted to mandatory Method 1, run before interviews
- Domain grounded in graph communities: Declaration Filing & Notary Services, Post-Death Procedures & Certificate, Wills & Intestate Distribution, Succession Tax & Costs, Asset Liability & Property

**Key decisions made:**
- 5 workflow clusters (not 4) — the document collection loop is a distinct non-linear cluster
- Shadow sessions are mandatory and run before interviews, not after
- AI adoption risk is a first-class qualification dimension, not a footnote
- Dev interview is scoped to technical blockers only (not build feasibility)

**Output:** `Discovery_plan.md` — 7 sections covering charter, stakeholder map, metrics framework, 3 interview templates, 4 feedback collection methods, triage/qualification process, and 4-week sprint with milestone gates and pivot signals.

---

*This log will be updated at the start of each new prompt/response exchange across all phases.*

---

## Session 4 — 2026-05-06 — Persona Design

**Purpose of this session:** Design three AI agent personas (juriste, dev, ops) grounded in the knowledge graph, to simulate discovery interviews for Phase 3. Serve as both a methodology demonstration and a live AI workflow showcase for the presentation.

---

### Prompt 6 — Persona Agent Strategy

**Role:** User  
**Phase:** Phase 3 — Discovery Simulation

> For Phase 3, I wanted to define 3 agents one for each persona (jurist, dev, ops) based on the knowledge graph.
> These agents will act as the persona and answer to the interviews.
> It will help me gather feedback, identify bottleneck in the processes to apply the validation methodology, priotitisation framework and plan the execution.
>
> What suprises me is that they say "Ce que nous n'attendons pas: Une priorisation détaillée avec scoring — l'objet est d'identifier et de qualifier"
>
> It will also show my AI workflow and demonstrate my skills.
>
> What's your opinion?

**Task conducted:**  
Strategic assessment of the approach — identified the misread concern (scoring ≠ qualification), confirmed the idea is strong, named the one real risk (synthetic agents confirm what you built into them), and prescribed how to neutralize it (frame outputs as hypotheses to validate, not findings).

**Key points delivered:**
- The "pas de priorisation" line is about false-precision scoring matrices, not about the qualification process — no conflict with the agent approach
- The knowledge graph anchors the agents in real domain knowledge (god nodes, workflow clusters), which is the key differentiator vs. generic ChatGPT prompts
- The real risk: synthetic agents reflect their training, not ethnographic reality — the panel has interviewed real juristes and will notice if outputs are too clean
- Mitigation: frame agent outputs as "hypotheses to validate," name the epistemological limits explicitly in the presentation

---

### Prompt 7 — Design the Three Personas

**Role:** User  
**Phase:** Phase 3 — Persona Design

> As a senior AI PM, guide me into designing the three agent personas.
> I want this config to be easily reusable to show the panel during the presentation and even maybe run the three persona live during the presentation.

**Task conducted:**  
Delivered the full persona design framework (5 layers: Identity, Domain knowledge, Pain profile, AI sentiment, Hidden signals) plus behavioral constraints. Drafted all three persona profiles with calibrated AI sentiment scores and hidden signals. Recommended a Python CLI runner (`interview_agent.py --persona [juriste|dev|ops]`) as the live demo vehicle.

**Personas drafted:**
- **Sophie** — Senior Juriste, Succession Specialist — AI sentiment 3/5 (initial draft)
- **Thomas** — Dev Team Lead, ex-fintech — AI sentiment 4/5, built a RAG once
- **Claire** (later renamed Marc) — COO — AI sentiment 4/5, pressuring for AI implementation

---

### Prompt 8 — Persona Corrections

**Role:** User  
**Phase:** Phase 3 — Persona Design (revision)

> Use the following information to better define Sophie:
> "surchargés : recherches dans dossiers volumineux, rédaction de courriers standards, vérifications de cohérence, ressaisies depuis PDFs"
> Thomas has already built a RAG once.
> To the COO, add that he's pressuring for AI to be implemented to improve the processes.
> Write the Design framework in 'persona-design.md'

**User correction mid-write:** Sophie's AI sentiment corrected from 3/5 to 2/5 — she has direct legal liability exposure, making her the most resistant persona.

**Task conducted:**
- Updated Sophie's pain profile to include all four specific overload signals from the case brief (recherches dans dossiers volumineux, rédaction de courriers standards, vérifications de cohérence, ressaisies depuis PDFs)
- Updated Thomas's identity to reflect that he has built a RAG once (on a structured knowledge base; it broke on real scanned production documents)
- Updated COO (renamed Marc, male) to reflect active AI implementation pressure as a strategic imperative
- Recalibrated Sophie's AI sentiment to 2/5 — sharpest resistance of the three
- Created `persona-design.md` with the full 5-layer design framework, all three persona profiles, interview sequencing protocol, live demo guidance, and epistemological limits section

**File produced:** `persona-design.md`

---

## Session 5 — 2026-05-07 — Discovery Synthesis

**Purpose of this session:** Synthesize the 12 discovery interviews into a structured signal analysis with economic impact, ahead of opportunity mapping.

---

### Prompt 9 — Generate Discovery Synthesis

**Role:** User  
**Phase:** Phase 3 — Discovery Analysis

> Act as a Senior AI PM, expert in customer discovery.
>
> Generate the Discovery synthesis based on the @interviews-recap.md and you're early knowledge of the field @01-graphify-out/GRAPH_REPORT.md.
>
> The synthesis must:
> - identify key recurring signals (bottlenecks, pain points, error prone), with their occurences in the interviews compared to the number of interviews (in %)
> - attach these signals to a cluster (document collection loop, Post-death procedures, Succession declaration, Will & heir analysis, Document production)
> - evaluate the economic impact based on interview data: time spent on tasks, cost of juristes 70€/h, volume of the tasks (considering 2500-3000 files per year, ie ~80 per juristes per year, ie ~25 simultaneous files/juristes -due to the 4 months deadline)
> - evaluate the level of pain from 1 to 5 (qualitative, based on the interviews)
>
> We'll identify the opportunities in a second time based on this analysis.
>
> Write the synthesis in discovery-synthesis.md

**AI Response (v1):**  
Read all 12 interviews in full. Cross-referenced with GRAPH_REPORT.md god nodes and community structure. Produced `discovery-synthesis.md` with:
- Volume assumptions table (2,750 files/year, 34 juristes, €70/h, 1,920h/year)
- 11 signals with occurrence counts, cluster tags, and pain levels
- Deep-dives per signal with representative quotes and time estimates
- Economic impact table: ~€11.7M total annual cost, ~€3.8–4.0M annual savings potential

**Key decisions made:**
- Used file-based time estimates (hours/file) from interview self-reports for chasing, declaration, verification, and templates rather than percentage-of-time estimates, which were more reliable
- S9 (Shadow AI) counted at 12/12 — all interviewees including COO and Tech Lead admitted unprompted use of public AI with client data
- Article 108 surfaced as a cross-cutting complexity driver confirmed by the graph (God Node, 6 edges, central to Asset Liability and Succession Declaration communities)

---

### Prompt 10 — Corrections & Rewrite

**Role:** User  
**Phase:** Phase 3 — Discovery Analysis (revision)

> marc and thomas are not juristes. Marc is COO and Thomas is a tech lead.
> Count 38h/week. 52 week in a year, minus 5 week of holidays.
> We are not really considering Will redaction in this analysis. I agree that this represents a small share of the revenue (15% according to marc) but worth be mentioned.
> Rename S5 - Obsolete templates into something closer to the fact that they have to write a large part of their email before sending them. Deprioritise the fragmented tool, I'll consider it as a technical constraint, but it won't be addressed. Why the economic impact summary only consider 1 to 7? Add them all, even by putting 0€ next to it if no direct economic impact.

**Corrections applied:**
- **Marc = COO, Thomas = Tech Lead** — recounted juriste-specific signals as n=10; Marc and Thomas credited separately as strategic/technical perspectives
- **Working hours** corrected to 38h × 47 weeks = **1,786h/year** → total payroll revised to **~€4.25M/year**
- **Will redaction** added as a named-but-excluded service line (~15% revenue per Marc, COO); explicitly out of scope for this analysis
- **S5 renamed** to "Manual communication drafting — minimal template value" to reflect that the core pain is rewriting most of each email/letter before sending, not just template staleness
- **S2 (Fragmented tools)** deprioritized throughout — labelled "Technical constraint — not being addressed," savings set to €0 in economic table
- **Economic summary** expanded to cover all 11 signals — S3, S6, S9, S10, S11 each get an explicit €0 row with stated reason (captured elsewhere, risk/unquantified, or inherent to job)
- **Total addressable savings revised** to **~€3.1M/year** (excluding S2)

**File produced:** `discovery-synthesis.md` (full rewrite)

---

## Session 6 — 2026-05-07 — AI Opportunity Mapping

**Purpose of this session:** Translate the discovery synthesis into a ranked AI opportunity map with a qualification framework and validation protocol.

---

### Prompt 11 — Generate AI Opportunity Map

**Role:** User  
**Phase:** Phase 3 — Opportunity Identification

> Act as a senior AI Product Manager, expert in applying AI technology in sceptical environment.
>
> Suggest opportunities where AI could improve internal processes at Legacio based on @discovery-synthesis.md and @01-graphify-out/GRAPH_REPORT.md.
>
> Key constraints:
> - Family are griefing, meaning that they will always prefer talking to a human to explain their personal situation, ask their questions about the procedures, and be guided in this challenge by human.
> - Solution must be GDPR, Belgian notarial law and AI act compliant (high risk)
>
> Output:
> The output must be a list of opportunities with the following information:
> - Task it impacts
> - Frequency of the task
> - Estimated volume (number of juristes, number of files) (Reach)
> - current time spent and current pain level
> - type of AI task: generation, extraction, vérification, research)
> - technical complexity as a teach lead (to be confirmed by Enaos tech team) (effort)
> - Risk (low, medium, low)
>
> The opportunities must be then represented using a qualification framework based on the impact (frequency, reach and pain) and the feasibility x risk
>
> The output must also contain a validation protocol that can be applied to each opportunities. Below is a non-exhaustive list of protocol steps:
> - Identify early adopters in the potential users
> - Validation with information from the discovery-synthesis
> - Manual test of a prototype with the early adopters and analyse the impact on the metrics
> - Error rate/Early-stage quality
> - First feeling about the solution from early adopters
> - Prototyping
> - Pilot phase with early adopters + a few users - success based on the metric, go/nogo decision
> - Technical assessment (technical blockers, feasibility, current workload)
> Metrics have been defined in @phase-02-Discovery_plan.md

**AI Response (v1 — rejected before write):**  
Identified 6 opportunities: O1 Document Gap Detection, O2 PDF Data Extraction, O3 Communication Drafting, O4 Pre-Submission Verification, O5 Article 108 Mapper, O6 Secure AI Workspace. Drafted opportunity cards with qualification 2×2 and 7-step validation protocol.

---

### Prompt 12 — First Round of Corrections

**Role:** User  
**Phase:** Phase 3 — Opportunity Mapping (revision 1)

> for O1, is there any risk depending on the type of document, for instance a form that has been filled by hand, scanned and sent to Legacio?
> O3 is partially based on O1 (dynamic document checklist), it must be acknowledged. O3 should pull data from CRM and the documents. O4 depends on O2 (data extraction from unstructured and unclear pdf file) it must be acknowledged too.

**Corrections applied:**
- **O1 — scanned/handwritten document risk** added as a named sub-section with an OCR accuracy table by document type (native digital vs. clean scan vs. handwritten vs. low-DPI). False gap alerts (document received but not parsed) identified as the key failure mode. Four required mitigations: confidence score, unknown document bucket, manual override, and % of handwritten documents to validate with Thomas.
- **O3 dependency on O1** acknowledged: O3 pulls (1) O1 gap view for dynamic document checklist and (2) CRM structured data (family details, contact history, file stage). O3 without O1 = partial value only; noted that O3 should launch after O1 is in production.
- **O4 dependency on O2** acknowledged: O4 without O2 = document presence check only; O4 with O2 = full content verification including figure cross-referencing. Full value requires O2 in production.
- **Dependency map** added at the top of the document showing the full O6 → O1 → O3 and O6 → O2 → O4 → O5 chain.

**Write attempt rejected by user for further corrections.**

---

### Prompt 13 — Second Round of Corrections

**Role:** User  
**Phase:** Phase 3 — Opportunity Mapping (revision 2)

> merge O5 with O4, they are very similar. In O4, just add that the development will be phased, one phase per output. In Phase B, prioritise on 01 - highest impact and feed 03, otherwise 03 will have to involve once 01 is done.
> A metric for 01 is also the document is received and SEEMS complete. A lot of document might be forms that can't be empty. Why the EU AI Act conformity is only Step 7 and not directly in Step 0? Can we run the pilot with AI act conformity?

**Corrections applied:**
- **O5 merged into O4** as a phased product: Phase 1 (document presence check), Phase 2 (Article 108 temporal logic), Phase 3 (figure cross-reference requiring O2). Each phase has its own savings estimate, complexity level, and build prerequisite.
- **Phase B reordered**: O1 launches first (highest impact, feeds O3). O3 is explicitly sequenced after O1 is in production — building O3 before O1 would require re-engineering it when O1 lands.
- **O1 completeness metric** added: AI flags documents that are *received but appear incomplete* (blank mandatory fields, unsigned, undated forms). Distinct from the missing-document signal. Added to quality thresholds (Step 4: ≥75% of incomplete forms correctly flagged) and pilot metrics (% of incomplete forms caught before declaration stage).
- **EU AI Act classification moved to Step 0** (not Step 7): classification takes days and shapes the entire product design (confidence scores, override mechanics, audit trail); discovering high-risk status at Step 6 means rebuilding. The conformity *assessment* is opened at Step 0 and runs in parallel through the pilot. Step 7 becomes a pre-GA completion gate, not a starting point. Answer to "can we run the pilot?": yes — a controlled named-cohort pilot with enhanced logging and informed consent is compatible with an in-progress conformity assessment, and the pilot evidence feeds the assessment.

**File produced:** `phase-03-AI-opportunities.md`

---

## Session 7 — 2026-05-07 — AI Workflow Retrospective

**Purpose of this session:** Generate a structured retrospective of the AI-assisted workflow across all phases of the case study, for inclusion in the Bonus section of the presentation.

---

### Prompt 14 — AI Workflow Retrospective

**Role:** User  
**Phase:** Bonus — AI Workflow Transparency

> Act as a Senior AI Product Manager.
>
> Generate an AI Workflow retrospective, explaining how AI helped and where human judgment is necessary.
>
> I have used AI to produce all the content in the current folder.
> I have tracked the most important prompt in @prompts.md.
>
> Some Pros, you can suggest more:
> - Domain grounding via graphify - identified Article 108 as a God Node before any interview
> - Persona calibration from knowledge graph - testing the interview workflow
> - Economic model scaffolding in 1 pass
>
> Cons:
> - Persona interviews are limited even if asked to slightly differ - it doesn't replace the real interviews and the ground sentiment
> - Couldn't evaluate the reach because all interviews are similar
> - Couldn't confirm if the hypothesis of fragmented tools is true - Head of tech validation needed
>
> The output must be a file ai-workflow-retro.md

**AI Response:**
Read `prompts.md` in full and cross-referenced with project structure. Produced `ai-workflow-retro.md` with:
- 5 AI strengths with "human judgment applied" callouts per section
- 5 structural limitations with named manifestations and mitigations
- Full phase-by-phase summary table (AI contribution vs. human judgment)
- Honest assessment section with the key insight: AI compresses preparation, real interviews generate surprise

**Additional pros surfaced beyond user prompt:**
- Discovery plan architecture from graph clusters (document collection loop identified as non-linear before any interview)
- Iterative precision via human correction — the correction loop is itself a PM skill demonstration
- Regulatory design response (O4 scoped as "flagging, not deciding") derived from recognizing Article 108 interpretation limits

**File produced:** `ai-workflow-retro.md`

---

### Prompt 15 — WYSIATI Con Addition

**Role:** User  
**Phase:** Bonus — AI Workflow Transparency (revision)

> Add in the cons the WYSIATI concept: "What you see is all there is". If you give 60% of the picture, it builds a thorough, confident analysis from that 60%. It won't say "You haven't mentioned this." It means that it's currently biased by the information I gave in the graph.

**Corrections applied:**
- Added **3.5 WYSIATI — the knowledge graph is also the knowledge ceiling** to the limitations section
- Named the Kahneman concept explicitly with a plain-language definition
- Grounded the risk in this specific project: public Legacio content defines the graph ceiling; unpublished workflows (heir disputes, informal notary coordination) have no node and generate no hypotheses
- Named confirmation bias as structurally embedded in the methodology, with shadow sessions as the only corrective
- Prior 3.5 renumbered to 3.7

---

### Prompt 16 — Three QA Fixes to ai-workflow-retro.md

**Role:** User  
**Phase:** Bonus — AI Workflow Transparency (QA)

> 1. Numbering gap — Section 3.6 is missing (3.5 → 3.7). Fix: renumber 3.7 to 3.6.
> 2. Summary table organized by phase — too broad for a slide. Rewrite as decision-point rows showing specific moments of PM override.
> 3. Section 2.5 title undersells the claim. Rename to "The PM as quality gate — AI generates, the PM steers."

**Corrections applied:**
- **3.6 renumbered** — 3.7 (AI sentiment) corrected to 3.6; no section was missing, just a numbering error from the prior insertion
- **Section 4 table rewritten** — phase-level rows replaced with 6 specific decision-point rows: Article 108 prioritization, Sophie's sentiment correction, S2 exclusion from roadmap, economic model assumption corrections, O4+O5 merge, EU AI Act Step 0 move
- **Section 2.5 renamed** to "The PM as quality gate — AI generates, the PM steers"

---

## Session 8 — 2026-05-08 — WYSIATI Audit & Gap Closure

**Purpose of this session:** Apply the WYSIATI cognitive bias framework to audit what is missing from the case study materials before building the presentation. Two audit rounds, followed by targeted gap closure.

---

### Prompt 17 — WYSIATI Audit Round 1

**Role:** User  
**Phase:** Pre-presentation QA

> Before building the deck for my presentation, I'll like to ensure that I am not missing anything.
> In "Thinking, Fast and Slow", Nobel Prize winning psychologist Daniel Kahneman identified a cognitive bias called WYSIATI: What you See is All there is. It means the brain builds the most coherent story it can from whatever information is available and never asks what's missing. The result is that decisions feel complete even when they're built on incomplete information.
>
> I need you to act as WYSIATI auditor for my next business decision. Do not evaluate whether my plan is good. Instead, surface every category of information that is completely absent from my thinking. What data haven't I gathered? What assumptions am I treating as facts? What customer segments, competitors, risk, or market dynamics am I not considering at all? What questions haven't I even thought to ask?
>
> For each gap, tell me how critical it is, what could go wrong if I proceed without it, and exactly how I can get that information quickly.
>
> Here's my current content that should cover the case study requirements: [referenced all phase files, discovery-synthesis, personas, opportunity map, ai-workflow-retro]

**AI Response:**
Read all referenced files in full before auditing. Produced a 9-gap WYSIATI audit ranked by criticality:

| Gap | Criticality |
|---|---|
| The failed RAG — inoculate, not analyze | CRITICAL |
| Non-AI alternatives not considered | CRITICAL |
| Presentation structure/narrative absent | CRITICAL |
| Budget/build cost estimates missing | HIGH |
| Competitive landscape absent | HIGH |
| Change management / HR / Belgian social consultation | HIGH |
| Build vs. buy not addressed | HIGH |
| Revenue upside / capacity model absent | MEDIUM |
| Juriste attrition unmentioned | MEDIUM |

**Key decisions surfaced:** The three cannot-ignore gaps before building the deck are the RAG narrative, non-AI alternatives, and the presentation structure itself.

---

### Prompt 18 — Gap Triage & Competitive Landscape Research

**Role:** User  
**Phase:** Gap closure — Round 1

> Ignore the failed RAG, the case study clearly says that "Tu rejoins Enaos il y a un an, juste avant le démarrage de la discovery."
> For the competitive landscape, let's consider the partnership between Fednot & ML6 and Heriwise https://konsultia.be/en/agent/notaire-patri-patrimoine-succession and https://www.ml6.eu/en/customers/cases/ai-powered-extraction-transforming-succession-workflows-at-fednot
> Presentation structure and narrative will be done in a second time.
> Build Vs Buy is interesting but should just be mentioned in the rollout phase within the validation protocol. The case study is about discovery, analysis, validation before the delivery.
> Jurist attribution must be mentioned in the problem framing @phase-01-understanding.md
> Ignore for now Gap 5
> I agree that timeline must be designed for both the discovery phase and also for the validation phase

**AI Response:**
Fetched both URLs via subagent. Results:
- **Konsultia (konsultia.be):** HTTP 403 on all pages — fully blocked to crawlers, no indexed content. Inferred from URL: Konsultia is the company, "Notaire Patri" is the product name, scope is patrimoine/succession.
- **ML6/Fednot:** Full case study retrieved. Key facts: AI-powered PDF extraction for fiscal lists (bank statements) → eSuccession integration. Tech stack: Gemini (Google Vertex AI). Results: **40% time reduction, 15 min saved per declaration, 4× fewer errors**. Scale: 1,600+ Belgian notary offices.

**Files modified:**
- `phase-01-understanding.md` — added juriste attrition row to "Situation One Year Ago" table; added new Competitive Landscape section with Fednot × ML6 data and Konsultia/Heriwise placeholder
- `phase-03-AI-opportunities-and-rollout.md` — added ML6/Fednot market validation paragraph to O2 card; added build-vs-buy row to Step 0 Track A; added full Validation Phase Timeline section (week-by-week table mapping Steps 0–7 per opportunity)

**Key decisions made:**
- Failed RAG gap correctly dismissed — candidate joins before discovery, not after
- Konsultia TBC pending user-provided details
- Validation timeline shows O1 as critical path blocking O3; O2 has longest arc due to EU AI Act classification + build-vs-buy

---

### Prompt 19 — Heriwise Product Assessment

**Role:** User  
**Phase:** Gap closure — Competitive landscape

> Here are info about Heriwise:
> [12 areas of expertise: succession planning, donations, wills, matrimonial regimes, inheritance tax, asset companies, usufruct, real estate, life insurance, succession pacts, estate taxation, asset protection]
> [Use cases: Plan succession, Donation to children, Draft a will, Matrimonial regime, Inheritance & usufruct, Succession declaration]
> I don't know what's work and what's bullshit

**AI Response:**
Assessment: Heriwise is a **B2C AI advisory agent** for individuals and families — not an internal tool for juristes or a workflow automation layer. It operates at the planning phase (pre-death or early succession), not at the execution phase (post-death file management). It is not a direct competitor to Legacio's juriste tooling.

Heriwise's 12 domains are credible for a Belgian succession advisory chatbot (LLM + law knowledge base). The product appears real but is in a different segment and customer journey stage.

**File modified:** `phase-01-understanding.md` — replaced Konsultia/Heriwise TBC placeholder with accurate B2C characterization, added competitive interpretation table distinguishing Fednot × ML6 (direct/active threat) from Heriwise (indirect signal), added three "why this matters" bullets anchoring competitive urgency in specific numbers.

**Key decision:** Heriwise is a market signal (AI entering succession from the client side), not a threat. The Fednot × ML6 benchmark (40%, 15 min, 4×) is the only number that matters competitively.

---

### Prompt 20 — WYSIATI Audit Round 2

**Role:** User  
**Phase:** Pre-presentation QA — second pass

> Apply again the WYSIATI principle

**AI Response:**
Fresh audit pass — only gaps genuinely absent after Round 1 updates. Produced 8 new gaps:

| Gap | Criticality |
|---|---|
| Legacio revenue model absent — no capacity expansion argument | CRITICAL |
| Discovery synthesis not labeled as illustrative in the file itself | CRITICAL |
| BSJ filing integration reality unknown — could halve O2's ROI | HIGH |
| Dev team capacity and AI/ML skills assumed | HIGH |
| Active GDPR exposure (shadow AI) has no interim response | HIGH |
| No Day 0 / first week plan in the charter | MEDIUM |
| Pilot overlap: O1 and O4 Ph.1 running simultaneously, same cohort | MEDIUM |
| Adoption rate not explicitly stated in annual savings figures | MEDIUM |

**Key insight surfaced:** The two CRITICAL gaps (revenue model, illustrative labeling) are fast to fix and high-stakes to miss. The BSJ integration unknown is the single most important technical question for O2's business case.

---

### Prompt 21 — Apply Round 2 Fixes

**Role:** User  
**Phase:** Gap closure — Round 2

> Add Gap 3 in @phase-03-AI-opportunities-and-rollout.md as a risk, something to consider before building for O2.
> I fill Gap 4, I've already built an OCR and I can code products with AI.
> I'll consider that revenue model is per file, depending on the size of the project. Legacio team define the price for each customer.

**Corrections applied:**
- **Gap 3 — BSJ integration risk** added to O2 card in `phase-03-AI-opportunities-and-rollout.md` as `⚠️ BSJ Filing Integration — Critical Unknown Before Build`. Three-scenario table: API (full value) → web portal (partial) → paper (minimum). Specific Step 0 validation question for Thomas added. Fednot benchmark explicitly conditioned on BSJ API access.
- **Gap 4 — Dev capacity/skills:** Closed by user — existing OCR experience + AI coding capability fills this gap. No document change required. Worth naming explicitly in the presentation when the Head of Tech is in the room.
- **Gap 1 — Revenue model / capacity expansion:** Added revenue upside note to both `phase-03-AI-opportunities-and-rollout.md` (Summary Scorecard section) and `discovery-synthesis.md` (economic impact summary). Formula: O1 frees ~27,500h/year → ~344 additional files at current throughput → revenue upside at per-file pricing, likely exceeding the €1.9M cost saving. Framed as a COO argument ("how many more files at the same headcount?") rather than a cost model.

**Key decision:** The capacity expansion argument reframes the entire ROI case — from "we save cost" to "we grow revenue without hiring." Stronger at every stage of the company's growth trajectory.
