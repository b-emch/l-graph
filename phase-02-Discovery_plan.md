# Discovery Plan — Legacio AI Initiative
**Phase:** 2 — Discovery Preparation  
**Previous phase:** `phase-01-understanding.md`  
**Date produced:** 2026-05-06  
**Status:** Illustrative artifact

---

> **Framing note:** This document is what I would have produced on Day 0 of the discovery phase, before any interviews or analysis. It is an illustrative artifact demonstrating the discovery methodology — not a post-hoc reconstruction. All numbers are placeholder hypotheses to be populated and validated through interviews and observation. The panel should read this as: *"here is exactly how I would have set up the discovery, and why."*

---

## 1. Discovery Charter

### Mission
Produce a ranked, evidence-backed shortlist of AI opportunities that directly reduce juriste workflow friction — grounded in measured time loss and expressed willingness to adopt — so that the next investment is targeted, not exploratory.

### In-scope
- Juriste workflows across all file types (wills and inheritance files)
- All 30 juristes and their sub-groups
- Ops and management as business metric sources
- Dev team as a source of technical context and current blockers (not yet scoping builds)

### Out-of-scope
- Build feasibility assessment (that is Phase 4)
- End-client interviews (represented via juriste proxy and support data)
- Workflows outside Legacio (Funeral Manager, Enaos group level)
- Exhaustive prioritisation scoring — the goal is to qualify, not rank with false precision

### Technical Constraints Pre-Hypothesis

> These are working assumptions entering discovery — not commitments. Each is a blocker hypothesis to validate in the dev interview.

**1. Privacy & regulatory stack**
Three regulatory layers constrain any AI architecture on inheritance files:
- **Belgian notarial professional secrecy** (Loi du 25 ventôse an XI, Art. 458 Code pénal): covers all data handled in a notarial capacity, stricter than GDPR alone. May prohibit routing client data through external commercial APIs without explicit consent and a certified data processing agreement.
- **GDPR** (Regulation 2016/679): inheritance files contain special-category data (family relationships, asset values, beneficiary identity). Data minimisation and purpose limitation principles apply to any model training or logging.
- **EU AI Act** (Regulation 2024/1689, in force August 2024): AI systems that influence legal decisions or process personal data in a legal context may qualify as high-risk under Annex III. High-risk designation requires conformity assessment, human oversight mechanisms, and detailed logging before deployment. **Blocker hypothesis:** any AI touching the succession declaration or heir analysis clusters may require a formal risk assessment before going live.

**Implication for model choice:** Commercial cloud APIs (OpenAI, Anthropic, Google) are viable only if data processing agreements comply with all three layers. On-prem or private deployment may be required — validate in the dev interview.

**2. AI approach type varies by cluster**
Not all workflow clusters carry the same AI risk profile. This shapes which clusters enter the shortlist and which require mandatory human-in-the-loop constraints:

| Cluster | Likely AI approach | Risk level | Key concern |
|---|---|---|---|
| 1 — Document collection loop | Gap detection + checklist generation | Low | Output is informational, not legal |
| 2 — Post-death procedures | Structured extraction from standard forms | Low–Medium | Extraction errors cause delays, not harm |
| 3 — Succession declaration | Field extraction + actif/passif structuring | Medium | Errors in tax declaration have legal consequences |
| 4 — Will & heir analysis | Legal reasoning, interpretation | High | AI must not substitute juriste judgment; assist only |
| 5 — Document production | LLM generation (letter drafting) | Medium | Hallucination risk; mandatory review before sending |

Clusters 1–2 are the lowest-risk entry points. Cluster 4 is likely out of scope for autonomous AI action in any Phase 4 build.

### Success criteria for this discovery phase
1. At least 3 distinct workflow bottlenecks confirmed by both qualitative signal (>50% of interviewees cite it) and quantitative measurement (time/cycle data)
2. An economic impact model populated with real or well-argued hypothetical numbers for each shortlisted opportunity
3. A shortlist of 3–5 ranked opportunities, each with: economic impact estimate, adoption risk score (from AI sentiment interviews), and privacy/regulatory flag — ready to enter Phase 4 validation

### Handling the "move fast" pressure
The answer to speed pressure is not a shorter discovery — it is a time-boxed, gate-driven sprint. A 4-week sprint delivers the same urgency signal as "moving fast" while protecting against the exact failure mode we are recovering from: shipping without knowing what to build.

**Explicit commitment to management:** "We will have a ranked opportunity list and a go/no-go recommendation in 4 weeks. Starting now without a validated use case is how we end up where we are today."

### Governance
| Role | Person | Responsibility |
|---|---|---|
| Discovery sponsor | COO | Signs off on charter; approves Week 4 readout |
| Single decision-maker | COO | Go/no-go gate at Week 4 |
| Discovery lead | AI PM (me) | Owns methodology and synthesis |
| Observer/validator | Head of Tech | Reviews technical blocker list; does not scope builds yet |
| Interview coordinator | Team lead or HR | Schedules juriste access; sets expectations with the team |

**Budget envelope:**
- Discovery phase: ~€600 in juriste opportunity cost (see Section 3) + PM time (internal)
- Phase 4 build budget ceiling: **to be named by COO at Week 4 gate** — the go/no-go decision at Week 4 must include a budget commitment, not just a directional approval. The discovery readout will include a cost range for each shortlisted opportunity to enable this decision.

---

## 2. Stakeholder Map

### Tier 1 — Core informants: Juristes

| Sub-group | Hypothesis | Why they matter |
|---|---|---|
| Senior juristes | Handle complex multi-party files; fewer files, more legal judgment | Surface the hardest bottlenecks; most credible voice for AI trust/distrust |
| Junior juristes | Higher volume, more data-entry and letter drafting; less legal judgment | Surface repetitive friction; more open to new tooling |
| Will specialists (Testament) | Focus on Holographic and Notarial wills; document validation heavy | Will-specific workflow (verification of form, registration, heir identification) |
| Inheritance file specialists (Succession) | Focus on succession declaration, actif/passif, tax computation | Declaration-heavy workflow; high document collection loop exposure |

> **Note:** This sub-group split is a hypothesis to be confirmed in Round 1 interviews. If juristes work full-file rather than specialising, the segmentation shifts to seniority only.

**Minimum viable interview set:**
- 15 juriste interviews (mix of seniority and file type: senior will, senior inheritance, junior, mid-level from each)
- Target: 20 if schedule allows

### Tier 2 — Business context: Ops / Management

| Stakeholder | What they provide |
|---|---|
| COO | Volume data, growth trajectory, cost model inputs (hourly cost of juriste), AI initiative history, success definition |
| Team lead(s) | Where errors cluster, informal observations on overload, team morale signals |

### Tier 3 — Technical blockers: Dev team

| Stakeholder | What they provide |
|---|---|
| Dev team lead / tech lead | Current tooling landscape, where data is structured vs. locked in PDFs, integration points, known technical walls |

> **Scope constraint:** The dev interview is explicitly not a feasibility scoping session. The question is: "what technical blockers exist today that any AI project would need to account for?" — not "how long would it take to build X?"

### End clients (indirect)
Families using Legacio are represented via juriste proxy (what do juristes tell us about client behaviour, missing documents, and emotional context?) and any available support/complaint data. No direct client interviews in this phase.

---

## 3. Metrics Framework — Baseline Workflow Measurement

### The 5 Workflow Clusters

The juriste's work is not a linear pipeline. It contains a critical non-linear loop (Cluster 1) that is invisible in any process map but likely accounts for the majority of hidden time waste.

```
[File opened]
     │
     ▼
┌─────────────────────────────────────────────┐
│  CLUSTER 1 — Document Collection Loop       │  ← NON-LINEAR, repeats per missing doc
│  Request docs → Check completeness →        │
│  Chase family → Verify → Re-check           │
└─────────────────────────────────────────────┘
     │  (once complete)
     ▼
[Cluster 2] Post-death procedures & Certificate
     │
     ▼
[Cluster 3] Succession Declaration Filing
     │
     ▼
[Cluster 4] Will & Heir Analysis
     │
     ▼
[Cluster 5] Document Production (letters, forms)
     │
     ▼
[File closed]
```

---

### Universal Metrics (all clusters)

| Metric | What it measures | How to collect |
|---|---|---|
| Volume | Files/year × occurrences per file | Management interview + CRM data |
| Time per task | Min / typical / max (hours or minutes) | Time-diary + interview estimation |
| Tool switches | # of systems touched per task | Shadow observation |
| Satisfaction | 1-5 self-reported frustration | Interview rating |

---

### Cluster-Specific Bottleneck Metrics

#### Cluster 1 — Document Collection & Verification Loop

> This is the hypothesis-0 bottleneck. Every inheritance file requires documents from the family (asset lists, will originals, Article 108 evidence, matrimonial regime documents, bank statements). Families frequently submit incomplete or incorrect documents. The juriste must verify, identify gaps, re-contact the family, and restart the check. This loop can repeat 3-5 times per file.

| Metric | Placeholder hypothesis | Source |
|---|---|---|
| Avg # of contact cycles before full document set | 3 cycles / file | Interview estimation |
| % of files requiring at least 1 re-contact | ~80% | Interview estimation |
| Avg waiting time for missing documents | 5-10 calendar days / cycle | Time-diary |
| % of files where a legal deadline was at risk | ~30% | Management / CRM |
| Time per contact cycle (call + email + follow-up) | 30-45 min / cycle | Shadow observation |
| **Implied annual cost of this loop** | `3,000 files × 3 cycles × 37.5 min × [hourly rate]` | Formula |

#### Cluster 2 — Post-Death Procedures & Certificate

| Metric | Placeholder | Source |
|---|---|---|
| Avg time to obtain Certificat d'Hérédité | [X days from file opening] | CRM data |
| % of certificate requests triggering additional verification | [X%] | Dev/CRM logs |
| Time spent on bank account unlocking per file | [X min] | Interview |

#### Cluster 3 — Succession Declaration Filing

| Metric | Placeholder | Source |
|---|---|---|
| Avg time to compile actif/passif inventory | [X hours] | Interview + time-diary |
| # of PDF documents manually re-keyed per file | [X docs] | Shadow observation |
| % of declarations requiring amendment after submission | [X%] | CRM / dev logs |
| Time to compute succession tax (droits de succession) | [X min] | Interview |

#### Cluster 4 — Will & Heir Analysis

| Metric | Placeholder | Source |
|---|---|---|
| Avg time to identify all heirs and their shares | [X hours] | Interview |
| % of cases with contested réserve héréditaire | [X%] | Management |
| Time spent on legal research per file (réserve, quotité) | [X min] | Time-diary |

#### Cluster 5 — Document Production

| Metric | Placeholder | Source |
|---|---|---|
| Avg # of standard letters per file | [X letters] | Interview |
| Avg time per letter (template to send) | [X min] | Shadow observation |
| % of letters requiring significant juriste customisation | [X%] | Interview |
| Time spent re-keying data from PDFs into letter templates | [X min/file] | Shadow observation |

---

### Economic Impact Formula

```
Annual cost of pain = Volume × Frequency per file × Time per occurrence × Hourly cost
                    = 3,000 files × [F] × [T hours] × [€C/hour]

Potential annual saving = Annual cost × Time saved ratio × Adoption rate
                        = Annual cost × [S%] × [A%]

Net ROI = (Potential annual saving − Annual AI run cost) / (Build cost + Annual run cost)
        ≈ Potential annual saving / Build cost  [Annual AI run cost is negligible at this scale — see below]
```

**Placeholder inputs (to populate from interviews):**
- Files per year: ~3,000 (to confirm with management)
- Hourly cost of a juriste: **€60 fully loaded** (working estimate; Belgian notarial/legal sector benchmarks: gross salary ~€3,000–4,000/month for juriste niveau bachelor/master, × 1.4–1.5 employer charges, ÷ 1,700 productive hours/year ≈ €55–70/hour — confirm precise figure with COO in Week 1)
- Adoption rate: conservative 50% for sizing, validated with pilot group in Phase 4
- Build cost: rough estimate from dev team in Phase 4 (not this phase)

**Discovery phase cost estimate:**

The COO's implicit first question is: "what does this 4-week sprint cost me?"

| Cost item | Estimate | Basis |
|---|---|---|
| PM time (4 weeks) | Internal cost (salaried) | Discovery is within existing AI PM mandate |
| Juriste interview time (15 × 30 min) | ~7.5h × €60 = **€450** | At €60/h fully loaded |
| Shadow observation (3 × 120 min) | PM time only — **€0 juriste cost** | Juristes work normally; PM observes |
| Time-diary pilot (5 juristes × 3 days) | Passive — no dedicated session time | Self-logged asynchronously |
| Async friction log (30 juristes × 5 min) | ~2.5h × €60 = **€150** | Minimal per-person commitment |
| **Total juriste opportunity cost** | **~€600** | Conservative estimate |

**Implication:** A discovery sprint that costs under €1,000 in juriste time to produce a validated opportunity shortlist is a low-cost gate before committing Phase 4 build budget. The argument for skipping discovery does not survive this comparison.

---

**AI operational cost benchmark (provider pricing, May 2026):**

| Provider | Model | Input (per 1M tokens) | Output (per 1M tokens) | Best for |
|---|---|---|---|---|
| Anthropic | Claude Haiku 4.5 | $1.00 | $5.00 | Extraction, classification |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $15.00 | Drafting, reasoning |
| OpenAI | GPT-4o-mini | $0.15 | $0.60 | High-volume extraction |
| OpenAI | GPT-4o | $2.50 | $10.00 | Drafting, complex reasoning |
| Google | Gemini 2.5 Flash | $0.30 | $2.50 | Extraction, high volume |
| Google | Gemini 3.1 Pro | $2.00 | $12.00 | Complex reasoning |
| Azure OpenAI | GPT-4o (EU hosted) | ~$3.25 | ~$13.00 | GDPR-compliant EU region deployment |

**Working cost estimate for 3,000 files/year:**
- Average file: ~75 pages ≈ 50,000 input tokens → 3,000 files = ~150M input tokens/year
- Extraction pass (Haiku/Flash rates): ~$150–450/year
- Letter drafting: 3 letters × 600 output tokens × 3,000 files = 5.4M output tokens → ~$27–80/year
- **Total AI inference cost: well under €1,000/year** — the cost driver is engineering, not inference

> Implication for ROI: the denominator is build cost, not run cost. Any use case that saves >50h/year of juriste time pays back at €55/h × 50h = €2,750/year — far exceeding inference costs.

---

### Bottleneck Confirmation Protocol

> A metric alone is not a bottleneck signal. An affinity cluster alone is not enough either.

**A bottleneck is confirmed when all three of the following are true:**
1. The task is cited as a top-3 pain by >50% of interviewees
2. The measured or estimated time/cycle data shows material impact (e.g., >1h/file or >30% of files affected)
3. The signal appears across both senior and junior groups (not a role-specific quirk)

Only confirmed bottlenecks enter the opportunity qualification stage.

---

## 4. Interview Guide — Per Persona

### Template A — Juriste (core interview, 30 min)

**Opening (2 min)**
> "I'm here to understand your work, not to evaluate you or pitch a tool. There are no right answers. Everything you share stays within the discovery process."

**Section 1 — Warm-up (5 min)**
- Walk me through a typical week. What does a Monday look like?
- Describe the last complex file you closed. What made it hard?

**Section 2 — Workflow mapping (8 min)**
- Describe a file from the moment it lands on your desk to the moment it's closed. Where does it tend to get stuck?
- When you open a new file, what documents do you need to get started? How often do you have everything at first contact?
- What happens when something is missing? Walk me through the steps.
- How many times, on average, do you need to go back to the family before the file is complete?

**Section 3 — Pain surfacing (7 min)**
- Where do you lose the most time in a week? (Probe: is it waiting? searching? re-doing something? explaining?)
- What task do you dread the most? Why?
- Which tool do you use most? Which one frustrates you the most?
- What do you copy-paste or re-type most often?

**Section 4 — Time estimation (3 min)**
- For your top 2-3 most time-consuming tasks: how long does each take on a good day? On a hard day?
- How many files are you managing at once right now?

**Section 5 — AI sentiment probe (5 min)**

> ⚠️ **Interviewer note:** This is a trust diagnostic, not a feature wishlist. Listen for: privacy fears, fear of legal errors caused by AI, distrust of opaque outputs, fear of being held responsible for AI mistakes, or discomfort with AI accessing sensitive client data. These are first-class signals — they must appear in the opportunity qualification, not be filtered out.

- When you think about AI being used on client files — files that contain very personal family information — what comes to mind?
- What would concern you most about an AI assistant in your workflow?
- What would it need to do to actually earn your trust? What would "safe" look like?
- If there was one task where you'd be comfortable with AI helping — what would it be?

**Closing (1 min)**
- Is there anything I didn't ask that you think I should know?

---

### Template B — Ops / Management (COO / team lead, 30 min)

**Section 1 — Volume & cost**
- How many files does the team manage per year, across all file types? What's the growth trajectory?
- What is the fully-loaded cost of a juriste hour (salary + charges)? Do you have that figure, or is it something we need to model?
- How many files does a typical juriste handle simultaneously?

**Section 2 — Quality & friction signals**
- Where do errors or complaints cluster in the current workflow?
- Have you seen delays or near-misses on legal deadlines? What caused them?
- What is your biggest fear about the team's current workload trajectory?

**Section 3 — AI ambition**
- Has the team explored AI tooling before, or would this be a first? (Do not probe further — the goal is to understand openness, not diagnose past projects.)
- What would "AI working" look like for this team in 12 months?
- What would make you confident enough to commit a production budget to an AI project?

---

### Template C — Dev team (technical blockers only, 30 min)

> **Framing for the dev team:** "I'm not here to scope a build. I'm in discovery. I want to understand the technical landscape so I can avoid building a roadmap that hits invisible walls."

**Section 1 — Current tooling**
- What systems do juristes use today? (DMS, CRM, email client, internal tools?)
- Which of these talk to each other? Which require manual data transfer?
- What are the 2-3 technical pain points you hear about most from the team?

**Section 2 — Data availability**
- Where does structured data exist today (databases, APIs)?
- What proportion of the juriste's relevant information is locked in PDFs or unstructured documents?
- What types of documents make up a typical inheritance file? What formats?

**Section 3 — AI readiness**
- Has the team built or evaluated any AI tooling before? If so, what approach, and what was the outcome?
- What would need to be true technically before an AI project could be attempted here?

**Section 4 — Known blockers**
- If we were to build an AI tool that touches juriste files, what are the 2-3 technical walls we'd hit first?
- Are there data privacy or GDPR constraints that would shape any AI architecture on this data? (Probe: Belgian professional secrecy, EU AI Act high-risk classification)
- What integrations exist today that we could leverage vs. what would need to be built?

---

## 5. Raw Feedback Collection Process

### Method 1 — Shadow Observation (mandatory, run first)

**What:** Sit with 2-3 juristes for 90-120 min each, watching them work on a live file. No questions during the session — only observe.

**What to log (observation sheet):**
- Tool switches: which app → which app, how often
- Moments of hesitation: re-reading, searching, scrolling through documents
- Copy-paste / re-keying actions: what data, from where, to where
- Document formats encountered: PDF (native digital vs. scanned/image), Word, email attachments — note which are machine-readable and which would require OCR
- Interruptions: phone calls to families, incoming emails requiring immediate response
- Visible friction: sighs, comments under breath, "this again"-type moments
- Any workarounds: sticky notes, personal spreadsheets, shortcuts that are not part of the official workflow

**Why first:** Juristes often cannot articulate their own workflow — they automate it. Observation catches what interviews miss. It also arms the interviewer with specific observations to probe ("I noticed you re-typed the address three times in one session — is that common?").

**Schedule:** 2-3 sessions in Days 1-3 of Week 1, before any formal interviews begin.

---

### Method 2 — 1:1 Interviews

**Schedule:** Days 3-5 of Week 1 (after shadow sessions)  
**Duration:** 30 min per session  
**Templates:** See Section 4

**Minimum viable set:**
- 15 juriste interviews (mix of seniority and file type)
- 2 management interviews (COO + 1 team lead)
- 1 dev interview (tech lead)

**Target set:**
- 20 juriste interviews
- 3 management interviews
- 1 dev interview

**Session note template (one per interview):**
```
Interviewee: [role, seniority, file type specialty]
Date:
Top pains cited (verbatim quotes preferred):
  1.
  2.
  3.
Time estimates given:
  - [Task]: [min/max]
AI sentiment: [1=very sceptical / 5=open to trying]
  Key concerns:
  Conditions for trust:
Tool frustrations:
Surprise observations (things not in the guide):
```

**Storage:** All notes in a shared Notion page, access restricted to PM + sponsor.

---

### Method 3 — Time-Diary (3-day pilot, 5 juristes)

**What:** A 5-person pilot (mix of senior and junior) self-logs their time for 3 consecutive working days.

**Format:** Simple shared Notion table, pre-labelled with the 5 workflow clusters as categories:

| Date | Task cluster | Specific task | Time started | Time ended | Notes / friction |
|---|---|---|---|---|---|
| | Cluster 1 — Document loop | Chase family for missing docs | | | |
| | Cluster 3 — Declaration | Re-key actif list from PDF | | | |

**Purpose:** Validate the time estimates from interviews with behavioral data. If interviewees say "20 minutes per letter" but time-diaries show 45 minutes, the diary wins.

**Launch:** Day 3 of Week 1, run concurrently with interviews.

---

### Method 4 — Async Friction Log

**What:** A single-question Notion form sent to all 30 juristes.

> *"What was the most frustrating or time-consuming task you did this week — and why? (2-3 sentences max)"*

**Duration:** Open for 5 business days (Week 1)

**Purpose:** Capture pain signals from juristes who won't speak up in a 1:1, or whose experience differs from the interview sample. Low friction to respond. Anonymised.

---

### How to handle "move fast" pressure

- All data collection runs in Week 1 only — hard stop
- Synthesis begins mid-Week 1 as the first interview notes come in (rolling synthesis, not batch)
- No interview exceeds 30 min — respecting juriste time is both practical and a trust signal
- If fewer than 6 juriste interviews are completed by end of Week 1: extend by 3 business days maximum, then proceed with available data

---

## 6. Feedback Triage, Clustering & Qualification

### Step 1 — Affinity Clustering (end of Week 1)

For each pain point surfaced across all methods, tag:
- **Workflow cluster** (1-5 from Section 3)
- **Frequency signal:** "every file" / "weekly" / "occasional"
- **Severity signal:** time-consuming / error-prone / emotionally draining / deadline risk
- **Population affected:** senior only / junior only / all

Group into themes on an affinity map (Notion table or FigJam). Look for clusters that span both seniority levels and both file types — those are the highest-priority candidates.

---

### Step 2 — Bottleneck Confirmation

For each theme from Step 1, apply the three-gate confirmation test:

| Gate | Question | Pass threshold |
|---|---|---|
| Gate 1 — Breadth | Is this cited by enough people? | >50% of interviewees mention it |
| Gate 2 — Magnitude | Is the time/cycle data material? | >1h/file OR >30% of files affected |
| Gate 3 — Universality | Does it appear across groups? | Present in both senior and junior groups |

Only themes that pass all three gates advance to opportunity qualification.

---

### Step 3 — Opportunity Qualification (Week 2)

For each confirmed bottleneck, complete one qualification card:

| Dimension | Score / value | Evidence |
|---|---|---|
| **Impact** | Annual cost of pain (€) | Economic formula with measured time data |
| **Reach** | % of juristes affected × frequency | Interview + time-diary |
| **Confidence** | 1-5 (how well can we measure/prove this?) | Data quality assessment |
| **Technical effort signal** | Blocker / feasible / unknown | Dev interview flags |
| **Adoption risk** | 1-5 (1 = high risk of non-adoption) | AI sentiment from interviews |
| **Privacy constraint** | Yes/No + description | Dev + juriste interviews |
| **Human presence required?** | Yes/No | Juriste interviews (some client touchpoints must remain human — flag these as out of scope for AI) |

**Output:** A shortlist of 3-5 candidate opportunities, ranked by (Impact × Reach) adjusted downward for adoption risk.

---

### Step 4 — Hypothesis Cards

One card per shortlisted opportunity. These become the inputs to Phase 4 (validation + POC).

**Format:**
```
Opportunity: [Name]

We believe that [AI action]
for [persona]
during [workflow step]
will save [X hours per week / per file]
because [evidence from interviews + time data].

We'll know we're right if [measurable signal: time reduction, error rate, adoption rate].

Adoption risk: [key concern from AI sentiment interviews]
Condition for trust: [what juristes said would make them comfortable]
Privacy constraint: [flag if client data is involved and what mitigations are needed]
```

---

## 7. 4-Week Discovery Sprint

### Sprint Overview

| Week | Focus | Key activities | Deliverables |
|---|---|---|---|
| **Week 1** | Data collection | Shadow sessions (Days 1-3), interviews (Days 3-5), time-diary launch, async friction log | Raw notes in Notion; time-diaries running; all interviews scheduled |
| **Week 2** | Synthesis | Rolling synthesis continues; affinity map; bottleneck confirmation; metrics compilation | Pain taxonomy; confirmed bottleneck list; baseline metrics with placeholders filled |
| **Week 3** | Qualification | Opportunity qualification cards; economic model populated; hypothesis cards drafted | 3-5 ranked opportunities; impact estimates; adoption risk scores |
| **Week 4** | Readout | Discovery readout prepared; go/no-go presentation to COO + Head of Tech | Discovery readout deck; ranked opportunity list; Phase 4 brief |

---

### Milestone Gates

| Gate | When | Question | If no → |
|---|---|---|---|
| **Gate 1** | End of Week 1 | Do we have enough signal from ≥6 juriste interviews + observation? | Extend data collection by 3 days max |
| **Gate 2** | End of Week 2 | Are the top pains distinct, confirmed by data, and not redundant? | Re-cluster; broaden interview set |
| **Gate 3** | End of Week 3 | Is there at least one opportunity with ROI > 3x and manageable adoption risk? | Reframe scope; escalate to COO for decision |
| **Gate 4** | End of Week 4 | Does the COO + Head of Tech approve the go/no-go recommendation? | Pivot or re-scope before Phase 4 |

---

### Pivot Signals

> These are the conditions under which I would stop, reframe, or escalate — rather than proceed:

| Signal | What it means | Response |
|---|---|---|
| Juristes report different pains than management assumed | Management's informal perception was projection, not data | Re-scope around actual juriste pain; update COO |
| Time-diary data shows tasks take <10 min each | Automation ROI may not justify AI build cost | Shift to UX/process improvement framing; flag to COO |
| AI sentiment is universally negative across all groups | Adoption is a prerequisite for impact — without it, ROI is zero | Prioritise trust-building before any build; flag as Phase 4 input |
| Dev interview reveals data is too unstructured for reliable extraction | Technical foundation for AI extraction doesn't exist yet | Flag as Phase 3 blocker; recommend data structuring as precondition |
| EU AI Act high-risk classification confirmed on shortlisted clusters | Conformity assessment required before any pilot | Escalate to COO; include compliance timeline in Phase 4 brief |
| Fewer than 3 bottlenecks pass the three-gate confirmation | Discovery was under-powered | Extend discovery by 1 week; broaden interview scope |

---

## Appendix — Artefact Checklist

| Artefact | Status | Location |
|---|---|---|
| Discovery Charter | ✅ Section 1 | This document |
| Stakeholder map | ✅ Section 2 | This document |
| Metrics framework | ✅ Section 3 | This document |
| Juriste interview template | ✅ Section 4 — Template A | This document |
| Management interview template | ✅ Section 4 — Template B | This document |
| Dev interview template | ✅ Section 4 — Template C | This document |
| Shadow observation guide | ✅ Section 5 — Method 1 | This document |
| Bottleneck confirmation protocol | ✅ Section 6 — Step 2 | This document |
| Opportunity qualification card | ✅ Section 6 — Step 3 | This document |
| Hypothesis card template | ✅ Section 6 — Step 4 | This document |
| 4-week sprint plan | ✅ Section 7 | This document |
| Economic impact model | ✅ Section 3 (formula + placeholders) | This document |
| Discovery readout | Phase 3 input | To be produced in Phase 3 |
