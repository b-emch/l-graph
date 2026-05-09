# AI Opportunity Map — Legacio Juristes
**Date:** 2026-05-07  
**Author:** Bastien Chevallier, AI PM  
**Inputs:** discovery-synthesis.md · GRAPH_REPORT.md · phase-02-Discovery_plan.md  
**Status:** Draft — pending tech team feasibility review

---

## Design Constraints (non-negotiable)

| Constraint | Implication |
|---|---|
| **Grieving families → human contact only** | No client-facing AI. AI supports juriste back-office work exclusively. |
| **"C'est moi qui signe"** | Every AI output is advisory. Human review and approval before any document is sent or filed. |
| **GDPR + Belgian notarial professional secrecy** | All data must remain on Legacio-controlled infrastructure. No routing through external commercial APIs without a certified DPA. |
| **EU AI Act — high-risk flag** | Any AI touching succession declarations or heir analysis likely qualifies as high-risk (Annex III). Classification must happen before any build begins. Conformity assessment must complete before production GA. |
| **Shadow AI paradox** | Demand is latent and universal. The barrier is infrastructure, not behaviour. A secure internal deployment unlocks adoption for all other opportunities. |

---

## Decision Register

> One place to read every choice made in this document — what was prioritized, what was sequenced, and what was ruled out, with rationale and validation status.

| Decision | What it rules out | Rationale | Validation status |
|---|---|---|---|
| **S2 — Tool fragmentation excluded from roadmap** | Fixing the DMS/CRM/email integration gap | Juristes and Marc (COO) confirmed this is a structural platform constraint, not a workflow fix addressable by a feature team | ⚠️ **Pending** — must validate with Thomas (Tech Lead) in Step 0. If integration is technically feasible within a 12-month horizon, this decision should be revisited before Phase C is locked. |
| **Will redaction out of scope** | Wills-specific AI features in this roadmap | Marc confirmed 15% of revenue, distinct workflows, and a separate opportunity landscape — mixing scopes would dilute the succession roadmap | ✅ Confirmed by COO in discovery interview |
| **No client-facing AI** | Chatbots, AI-response portals for families | All 10 juristes confirmed families in grief need human guidance; replacing or mediating that contact with AI was universally rejected | ✅ Confirmed across all juriste interviews |
| **O3 sequenced after O1** | Building the drafting assistant before the gap tracker | O3 without O1 requires manual document list input and would need re-engineering once O1 lands — building it first means doing the work twice | PM decision |
| **O4 built in phases, not monolithic** | Waiting for O2 before delivering any pre-submission value | Phase 1 (document presence check) delivers value with O6 only — blocking on O2 delays a low-risk, high-value feature by ~12 weeks | PM decision |

---

## Dependency Map

```
O6 — Secure Infrastructure  ←  prerequisite for all features
        │
        ├── O1 — Document Gap Detection & Completeness Check
        │        └── feeds context into ──► O3 — Communication Drafting
        │                                        (gap view + CRM data)
        │                                        [O3 launched after O1 in production]
        │
        └── O2 — PDF Data Extraction
                 └── enables full version of ──► O4 — Pre-Submission Verification
                                                      + Article 108 Mapper (integrated)
```

**O3 without O1:** Document checklist in letters must be populated manually. Partial value only. Launch O3 only after O1 is in production — otherwise O3 will need to be re-engineered when O1 lands.  
**O4 without O2:** Verification limited to document *presence* (did we receive X?). Cannot verify figures or cross-reference declaration content. Full value requires O2 in production.

---

## Opportunity Cards

---

### O1 — Document Gap Detection & Completeness Check
**Signals: S1 (chasing loop), S3 (no real-time visibility)**

| Dimension | Value |
|---|---|
| **Task impacted** | Document collection: identifying missing and incomplete documents across all active files; surfacing a structured per-file gap view |
| **Frequency** | Daily — continuous across all active files throughout the 4-month window |
| **Reach** | 34 juristes · 2,750 files/year · **100% of juristes** |
| **Current time spent** | ~40h/file total chasing · ~3.5h/day per juriste |
| **Current pain level** | 4/5 |
| **AI task type** | **Extraction** (parse received documents from DMS) + **Verification** (cross-check against expected checklist per file type + completeness of each received document) |
| **What AI does** | Reads DMS document metadata and content → maps to a dynamic per-file checklist (tailored by file type: standard succession, Article 108 flag, minors present, etc.) → surfaces two types of alerts: **(1) Missing documents** — not yet received; **(2) Incomplete documents** — received but appear blank, partially filled, or missing required fields (e.g., undated form, unsigned declaration, empty balance column) |
| **What human does** | Reviews the gap view · decides on follow-up action · makes the family call (human contact preserved entirely) |
| **Technical complexity** | **Medium** (see scanned document risk below) |
| **Effort estimate** | 5–8 weeks engineering (gap view + reminder queue + completeness flag + scan quality indicator) |
| **Risk** | **Low–Medium** |
| **Annual savings potential** | **~€1.9M/year** (25% reduction in chasing cycles) |

#### Completeness Check — Why It Matters
Many documents in a succession file are structured forms (heir declarations, bank release authorisations, asset inventories) that cannot legally be empty. A document that arrives but is unsigned, undated, or has blank mandatory fields is functionally equivalent to a missing document — yet it would not appear as a gap in a presence-only tracker.

AI adds value here by flagging: "Document received — appears incomplete: signature field empty / balance column not filled." This is a distinct signal from "document not received."

#### ⚠️ Scanned & Handwritten Document Risk
Succession files regularly include hand-filled forms and scanned documents. OCR accuracy varies significantly:

| Document type | OCR accuracy | Gap/completeness detection reliability |
|---|---|---|
| Native digital PDF (bank statement, notary act) | 95–99% | High |
| Clean scan of typed document | 85–95% | Medium–High |
| Scanned handwritten form | 50–80% | Low–Medium |
| Poor quality scan (faxed, low DPI) | <50% | Unreliable |

**Consequences of failure:** The system may fail to recognise a received document (false gap alert) or fail to detect a blank field in a scan (false completeness pass). Both produce the problem O1 is trying to solve: unnecessary relances, or a missed incomplete document reaching the declaration stage.

**Required mitigations:**
1. **Confidence score per document:** Every parsed document displays a confidence rating. Low-confidence = flagged for manual review: "Document received but could not be read reliably."
2. **Unknown document bucket:** Documents the model cannot classify are surfaced separately, never silently ignored.
3. **Manual override:** Juriste can mark any document as "received and verified" regardless of AI result.
4. **Validate with Thomas:** Confirm the proportion of inbound documents that are scanned handwritten forms. This determines whether the standard OCR pipeline is sufficient or a higher-quality model is needed before MVP.

---

### O2 — PDF Data Extraction for Succession Declaration
**Signals: S4 (manual filling), S6 (deadline + liability)**

| Dimension | Value |
|---|---|
| **Task impacted** | Extracting actif/passif figures from bank statements, property valuations, debt records → pre-populating BSJ declaration form fields |
| **Frequency** | Once per file at declaration stage (~month 3–4) |
| **Reach** | 34 juristes · 2,750 files/year · **100% of juristes** |
| **Current time spent** | ~4h/file total declaration · ~2h/file on mechanical extraction |
| **Current pain level** | **5/5** (highest across all signals) |
| **AI task type** | **Extraction** — OCR + named entity recognition + structured field mapping |
| **What AI does** | Reads PDF documents → extracts monetary figures, dates, asset identifiers → maps to BSJ form fields with a source citation for every figure ("€X extracted from document Y, page 3, line 8") |
| **What human does** | Reviews every extracted figure against the source document · corrects errors · signs the declaration. Full professional and legal liability remains with the juriste. |
| **Technical complexity** | **Medium.** Heterogeneous PDF formats (same scanned document risk as O1, amplified because errors here feed a tax declaration). Confidence scoring per field is mandatory. Validate on a representative sample of real Legacio files before any pilot. |
| **Effort estimate** | 8–12 weeks engineering (OCR pipeline + extraction model + form pre-fill UI + confidence display + source citation) |
| **Risk** | **Medium.** Extraction errors feed tax declarations with direct legal and fiscal consequences. Mitigated by: mandatory human review, confidence score on every field, source citation for every figure, explicit "I have verified this figure" confirmation before any field is accepted. **EU AI Act high-risk — see Step 0 of validation protocol.** |
| **Annual savings potential** | **~€385K/year** direct + unquantified risk reduction |

**Critical design principle:** Every pre-filled field must display its source document and page. Field confidence below threshold → highlighted, left blank, filled manually by juriste. A plausible-looking wrong figure with no uncertainty flag is a disqualifying failure mode.

**Market validation:** Fednot (the Belgian notary federation) and ML6 deployed an identical approach in production — multimodal AI (Gemini on Google Cloud) extracts figures from bank-issued fiscal lists into a side-by-side validation UI, then pushes directly to the eSuccession platform. Results: **40% time reduction, 15 min saved per declaration, 4× fewer errors**. Scale: 1,600+ notary offices. This validates O2's technical feasibility and sets the competitive benchmark: the professional counterparts to Legacio's juristes are already using this in production.

**⚠️ BSJ Filing Integration — Critical Unknown Before Build**

O2's ROI depends entirely on how the pre-populated fields reach the BSJ. Fednot × ML6 achieves maximum value because eSuccession has a direct system integration — the juriste approves and the data pushes automatically. Whether Legacio has equivalent access to the BSJ is the single most important technical question for O2's business case.

| Scenario | O2 value |
|---|---|
| BSJ accepts structured import / has an API | **Full value** — juriste reviews, approves, system pushes |
| BSJ has a digital web portal (manual form entry) | **Partial value** — juriste reviews AI output, copy-pastes verified figures into the portal |
| BSJ filing is paper or PDF-based | **Minimum value** — juriste reviews AI output, then re-types into a physical or PDF form |

**Validate in Step 0 with Thomas:** "How does the declaration currently reach the BSJ? Is there a digital submission portal? Does it accept structured data or XML import?" This answer changes O2's annual savings estimate and its position in the build sequence. If BSJ is paper-based, O2 still reduces time (from ~2h extraction to ~30min review) but the Fednot benchmark no longer applies directly.

---

### O3 — AI Communication Drafting Assistant
**Signals: S5 (manual drafting), S9 (shadow AI)**  
**Dependency: O1 (dynamic document checklist) + CRM integration**  
**Launch sequence: after O1 is in production**

| Dimension | Value |
|---|---|
| **Task impacted** | Drafting client-facing letters and emails: initial document checklist, follow-up relances, bank letters, BSJ cover letter, notaire transmission cover |
| **Frequency** | 6–8 letters/emails per file · ~20,000 letters/year |
| **Reach** | 34 juristes · 2,750 files/year · **100% of juristes** |
| **Current time spent** | ~3.5h/file on drafting (70–80% rewrite of unusable templates) |
| **Current pain level** | 3/5 |
| **AI task type** | **Generation** — LLM drafts letter from structured file context |
| **What AI does** | Pulls two data sources: **(1) CRM structured data** — family name, heir list, file stage, last contact date, previous communication history; **(2) O1 gap view output** — current missing document list, completeness flags, follow-up history. Generates a complete draft letter in the appropriate register: empathetic, plain-language, legally accurate, personalised. |
| **What human does** | Reviews and edits the draft · approves and sends. No AI output is ever sent without juriste review. |
| **Why O3 launches after O1** | O3 with O1 live: document checklist in letters is populated dynamically from the gap view — accurate, current, no manual input. O3 without O1: the juriste must specify missing documents manually, and the drafting assistant will need to be re-engineered when O1 lands. Building O3 before O1 means doing the work twice. |
| **CRM integration requirement** | Drafting assistant must read family details, contact history, and file stage from CRM. Validate API access with Thomas before build. |
| **Technical complexity** | **Low–Medium.** Standard LLM generation with system prompt for legal register and tone. CRM integration and O1 data injection are the main engineering dependencies. Template governance: a designated senior juriste (Michèle, J11) reviews and approves the system prompt quarterly. |
| **Effort estimate** | 4–6 weeks engineering after O1 is in production |
| **Risk** | **Low.** Letters are communications, not legal decisions. Hallucination risk mitigated by mandatory human review. No AI Act high-risk trigger for routine correspondence. |
| **Annual savings potential** | **~€471K/year** + elimination of shadow template debt and junior juriste quality inconsistency |

**Note on S9:** Juristes are already using external AI tools for drafting. O3 redirects an existing behaviour onto compliant infrastructure. Adoption friction is minimal.

---

### O4 — Pre-Submission Verification Copilot (includes Article 108 Mapper)
**Signals: S8 (verification anxiety), S4 (declaration), S6 (liability), S7 (Article 108)**  
**Dependency: O2 (for full content verification) · Phased development**

This opportunity merges the pre-submission checklist (S8) and the Article 108 evidence mapping (S7). Both tasks occur at the same moment in the workflow — final review before submission — and share the same data sources (financial documents, declaration draft, heir list). Building them as a single product avoids duplicate data pipelines and delivers a unified "pre-flight" experience.

#### Phased Development

| Phase | Output | Prerequisite | Savings unlocked |
|---|---|---|---|
| **Phase 1** | Document presence checklist: are all required documents in the file? | O6 only | Partial — catches missing documents before submission |
| **Phase 2** | Article 108 coverage check: are all transactions within the presumption window documented? | O6 + date-of-death parsing | Adds ~€80K/year (Article 108 files) + reduces S7 complexity |
| **Phase 3** | Figure cross-reference: do declared figures match extracted figures from source documents? | O2 in production | Full value — catches declaration inconsistencies |

#### Full Card

| Dimension | Value |
|---|---|
| **Task impacted** | Pre-submission completeness check before filing with notaire or BSJ: documents present, figures consistent, heirs accounted for, Article 108 coverage verified |
| **Frequency** | Once per file — highest-stakes moment in the workflow |
| **Reach** | 34 juristes · 2,750 files/year · **90% of juristes** |
| **Current time spent** | ~2.5h/file (1h simple, 3–4h complex); Article 108 adds ~3h on ~30% of files |
| **Current pain level** | 4/5 (verification) · 3/5 (Article 108) |
| **AI task type** | **Verification** (presence + consistency) + **Research** (Article 108 temporal cross-reference) |
| **What AI does** | Runs a structured pre-flight checklist: document presence, heir completeness, Article 108 window coverage (date-of-death → 3 or 5 years by region → transactions → missing proof documents), and — in Phase 3 — figure cross-reference against O2 extracted data. Surfaces a pre-flight report: "Document X ✓ / Article 108: ⚠️ Missing donation records for 2023 / Actif total: ✓ matches extracted figures" |
| **What human does** | Reviews the pre-flight report · investigates flagged items · makes the final go/no-go submission decision. AI cannot approve a submission. |
| **Technical complexity** | **Medium (Phase 1–2) → Medium–High (Phase 3).** Phase 1 is straightforward rule-based logic. Phase 2 adds temporal reasoning over financial documents and Belgian fiscal code rules (3-year / 5-year window by region). Phase 3 requires O2 extraction output and cross-reference logic. GRAPH_REPORT confirms Article 108 is a God Node with 6 edges connecting Asset Liability and Declaration Filing communities — the Phase 2 logic must handle both dimensions. |
| **Effort estimate** | Phase 1: 4–6 weeks · Phase 2: +4–6 weeks · Phase 3: +4–6 weeks after O2 in production |
| **Risk** | **Medium.** Primary risk: false confidence — a juriste treats a green checklist as definitive. Mitigation: explicit "this tool does not replace your review" on every pre-flight report; all items marked ✓ remain the juriste's legal responsibility. **EU AI Act high-risk applies from Phase 2 onward — see Step 0 of validation protocol.** |
| **Annual savings potential** | Phase 1: ~€80K/year · Phase 1+2: ~€160K/year · Full (Phase 1+2+3): **~€240K + ~€80K = ~€320K/year** |

---

### O6 — Secure Internal AI Workspace (Platform Prerequisite)
**Signal: S9 (shadow AI / data privacy)**

| Dimension | Value |
|---|---|
| **Task impacted** | All AI-assisted tasks — this is the infrastructure layer that makes O1–O4 legally deployable |
| **Frequency** | Continuous — infrastructure |
| **Reach** | 34 juristes · 12/12 interviews confirmed latent demand · **100% of all staff** |
| **Current pain level** | 4/5 (active compliance risk — 12 people have already sent client PII to external servers) |
| **AI task type** | **Platform** — private LLM deployment + data isolation + audit logging |
| **What it provides** | A secure, Legacio-hosted environment where all AI inference stays within the organisation's perimeter. No client data leaves controlled infrastructure. All interactions logged for compliance and EU AI Act audit trail requirements. |
| **Technical complexity** | **High.** Requires: private cloud or on-prem LLM deployment (Azure EU OpenAI with certified DPA is the fastest compliant path; self-hosted via Ollama/vLLM is lower cost but higher ops burden), SSO integration, per-request audit logging, data retention policy aligned with GDPR and Belgian notarial secrecy. Thomas must assess current infra capacity. |
| **Effort estimate** | 6–10 weeks infrastructure before any feature builds on top |
| **Risk** | **Low once deployed.** Eliminates the current active compliance risk. |
| **Annual savings potential** | **€0 direct** — enables all other opportunities; eliminates current unquantified GDPR liability |

**This is a prerequisite, not an option.** O1–O4 cannot be deployed compliantly without this layer. The current shadow AI behaviour is an active, unmitigated GDPR and notarial secrecy exposure.

---

## Qualification Framework

### Scoring Rubrics

**Impact** = equal-weighted average of frequency, reach, and pain (each 1–5). Equal weights chosen because each dimension is an independent axis of impact: how often the pain occurs, how broadly it affects the team, and how severely it is felt. Weighting one dimension above another would require stronger comparative evidence than available at this stage.

**Frequency rubric:**

| Score | Definition |
|---|---|
| 5 | Continuous / multiple times per day |
| 4 | Several times per file (~6–8 occurrences spread across weeks) |
| 3 | Once per file (concentrated single task) |
| 2 | ~30% of files (conditional occurrence) |
| 1 | Rare / edge case |

**Reach:** direct mapping from discovery occurrence rate — 100% → 5, 90% → 4.5, 80% → 4, 60% → 3.  
**Pain:** directly from discovery interview ratings (1–5, per signal).

**Impact calculation:**

| Opportunity | Frequency | Reach | Pain | Impact = (F+R+P)/3 |
|---|---|---|---|---|
| O1 Doc Gap + Completeness | 5 — daily, continuous | 5 — 100% | 4 | **(5+5+4)/3 = 4.7** |
| O2 PDF Extraction | 3 — once/file | 5 — 100% | 5 | **(3+5+5)/3 = 4.3** |
| O3 Communication Drafting | 4 — 6–8/file | 5 — 100% | 3 | **(4+5+3)/3 = 4.0** |
| O4 Ph.1 Pre-Submit (presence) | 3 — once/file | 4.5 — 90% | 4 | **(3+4.5+4)/3 = 3.8** |
| O4 Ph.2–3 (full) | 3 — once/file | 4.5 — 90% | 4–5 | 3.8–4.3 (scales with phase) |

> **O1 vs O2:** O2 has maximum pain (5/5, unanimous, highest-stakes liability) but is a concentrated once-per-file task. O1 is a daily, continuous drain across every active file. Equal weights give O1 a higher impact score — consistent with its higher economic savings (€1.9M vs €385K/year).

**Feasibility** = equal-weighted average of (technical simplicity + safety). Complexity converted: Low→5, Low-Medium→4, Medium→3, Medium-High→2, High→1. Risk converted: Low→5, Low-Medium→4, Medium→3, High→1.

| Opportunity | Complexity → score | Risk → score | Feasibility = avg |
|---|---|---|---|
| O3 Communication Drafting | Low–Medium → 4 | Low → 5 | **4.5** |
| O4 Ph.1 Pre-Submit (presence) | Low–Medium → 4 | Low → 4 | **4.0** |
| O1 Doc Gap + Completeness | Medium → 3 | Low–Medium → 4 | **3.5** |
| O2 PDF Extraction | Medium → 3 | Medium → 3 | **3.0** |
| O4 Ph.2 + Art.108 | Medium → 3 | Medium → 3 | **3.0** |
| O4 Ph.3 + figures | Medium–High → 2 | Medium → 3 | **2.5** |

### Summary Table

| # | Opportunity | Impact | Feasibility | Savings/year | Risk | Phase |
|---|---|---|---|---|---|---|
| O6 | Secure AI Workspace | Prerequisite | Medium | — | Low | **A — First** |
| O1 | Document Gap + Completeness | **4.7/5** | 3.5/5 | €1.9M | Low–Med | **B — First** |
| O3 | Communication Drafting | 4.0/5 | **4.5/5** | €471K | Low | B — After O1 |
| O4 Ph.1 | Pre-Submit (presence) | 3.8/5 | 4.0/5 | ~€80K | Low | B–C |
| O2 | PDF Data Extraction | 4.3/5 | 3.0/5 | €385K | Medium | C |
| O4 Ph.2 | Pre-Submit + Art.108 | 4.0/5 | 3.0/5 | ~€160K | Medium | C |
| O4 Ph.3 | Pre-Submit + figures | 4.3/5 | 2.5/5 | ~€320K | Medium | D |

### 2×2 Positioning

```
HIGH IMPACT  (≥4.0)
    │
    │   [O2 4.3]  [O4 Ph.2-3 4.0-4.3]      [O1 4.7]  [O3 4.0]
    │
    │   [O6 Platform*]
    │
    │                            [O4 Ph.1 3.8]
    │
LOW IMPACT  (<4.0)
    └──────────────────────────────────────────────────────────
         LOW FEASIBILITY (<3.0)              HIGH FEASIBILITY (≥4.0)
              2.0    2.5    3.0    3.5    4.0    4.5    5.0

  * O6 is a prerequisite — position reflects build effort, not relative impact.
  Scores derived from rubric tables above.
```

### Recommended Build Sequence

```
Phase A (Weeks 0–10)
└── O6 — Secure Infrastructure + EU AI Act classification for O2/O4

Phase B (Weeks 6–16, overlapping with A once architecture confirmed)
├── O1 — Document Gap + Completeness  [start here: highest impact, feeds O3]
└── O4 Ph.1 — Pre-Submit document presence  [low complexity, immediate value]

Phase B+ (after O1 in production)
└── O3 — Communication Drafting  [O1 gap view + CRM injection; builds on O1 output]

Phase C (Weeks 16–28, EU AI Act conformity running in parallel)
├── O2 — PDF Data Extraction
└── O4 Ph.2 — Article 108 temporal logic added to pre-flight report

Phase D (Weeks 28+, after conformity assessment complete)
└── O4 Ph.3 — Figure cross-reference (requires O2 in production + conformity sign-off)
```

**Total addressable savings (O1+O2+O3+O4 full): ~€3.1M/year on ~€4.25M juriste payroll.**

---

## Validation Protocol

> One protocol for all opportunities. Opportunity-specific metrics are noted at each step.

---

### Step 0 — Technical & Regulatory Readiness Gate
**Owner:** Thomas (Tech Lead) + Legal + AI PM · *Before any build or prototype begins*

This step has two parallel tracks that must both pass before work proceeds.

**Track A — Technical readiness:**

| Check | Pass condition |
|---|---|
| Infrastructure path confirmed (Azure EU OpenAI DPA or self-hosted) | Written confirmation from Tech Lead |
| DMS document metadata queryable | API or structured export available |
| CRM data accessible for O3 | API or structured export confirmed |
| % of inbound documents that are scanned handwritten assessed | Needed to calibrate O1 OCR pipeline choice |
| **Build vs. buy assessment for O2** | Confirm whether an off-the-shelf PDF extraction vendor (e.g., similar architecture to ML6/Fednot × Gemini) can be licensed and integrated faster than building the OCR pipeline from scratch. Decision criterion: if a vendor covers ≥80% of Legacio's document formats and has a compliant EU data residency option, buy accelerates Phase C by 4–6 weeks vs. build. |

**Track B — EU AI Act classification (for O2 and O4):**

| Check | Pass condition |
|---|---|
| AI Act risk classification completed for each opportunity | Legal + AI PM confirm high-risk / limited-risk status |
| If high-risk: conformity assessment process formally opened | Documented start, owner assigned, timeline to completion |
| Human oversight mechanism designed | Review step, approval gate, liability chain documented |
| Audit logging architecture defined | Every AI-assisted action on a succession file must be traceable |

**Why classification belongs in Step 0, not later:** You cannot responsibly design a product whose regulatory status is unknown. If O2 or O4 are classified high-risk, this shapes the UI design (confidence scores, override mechanics, audit trail), the pilot conditions, and the production GA gate. Discovering this at Step 6 means rebuilding. The conformity *assessment* takes weeks to complete — but the *classification* takes days and must happen first.

**Can we run a pilot while conformity assessment is ongoing?**  
Yes — a controlled pilot with a named cohort, enhanced logging, and explicit informed consent from participants is compatible with an in-progress conformity assessment. The pilot itself generates evidence that feeds the assessment (real-world performance data, error rates, human override frequency). What you cannot do is launch to all 34 juristes before the assessment is complete.

**Gate:** Both tracks must pass before any prototype or build begins on O2 or O4. O1 and O3 (limited-risk) can proceed on Track A alone.

---

### Step 1 — Early Adopter Identification
**Owner:** AI PM + Team Lead

Identify 3–5 juristes meeting all three criteria:
1. **Pain intensity:** cited the target signal as a top-2 pain in discovery
2. **AI sentiment:** rated ≥3/5 in discovery (open to trying)
3. **File volume:** manages ≥25 simultaneous files

**Candidate signals from discovery:**
- **O1:** Sophie (J1), Denis (J12), Philippe (J6) — chasing/visibility as top pain; Denis has tech background
- **O2/O4:** Nathalie (J5), Carole (J2), Valérie (J4) — pre-submission anxiety and extraction burden explicitly named
- **O3:** Sophie (J1), Michèle (J11 — mentor, template quality owner)

---

### Step 2 — Discovery Signal Confirmation
**Owner:** AI PM · *Before any prototype is built*

| Check | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| Signal frequency ≥50% of juristes | ✓ 100% | ✓ 100% | ✓ 100% | ✓ 90% |
| Time estimate validated (midpoint) | 40h/file | 2h/file | 3.5h/file | 2.5h/file |
| Pain level ≥3/5 | 4/5 | 5/5 | 3/5 | 4/5 |
| Not client-facing | ✓ | ✓ | ✓ | ✓ |

---

### Step 3 — Prototype (lowest fidelity that demonstrates the core AI action)
**Owner:** AI PM + Tech Lead · *1–2 weeks*

| Opportunity | Prototype form | What to test |
|---|---|---|
| O1 | Figma mockup of gap view + completeness flags; static walkthrough on one anonymised file | Does the juriste understand the view? Does the completeness flag (e.g., "form appears empty") feel useful or noisy? |
| O2 | Manual OCR + LLM extraction on 5 anonymised files; results in a spreadsheet with source citations | Extraction accuracy on real Legacio documents before any UI is built |
| O3 | LLM drafts 3 letter types using real anonymised file data (CRM export + O1 gap view) | Quality vs. juriste's own draft; time to review and approve |
| O4 Ph.1 | Paper pre-flight checklist generated from a real file | Does it catch what the juriste would have checked? Does it feel like a useful second pair of eyes? |

**Key question every session:** "Would you actually use this? What would stop you?"

---

### Step 4 — Early-Stage Quality Assessment
**Owner:** AI PM + Tech Lead · *Before showing to juristes*

| Opportunity | Quality metric | Minimum threshold | Hard stop condition |
|---|---|---|---|
| O1 — gap detection | % of missing documents correctly flagged across 20 test files | ≥85% recall | Silent failure: document received but dropped from gap view → false chase generated |
| O1 — completeness | % of incomplete forms correctly flagged (blank/unsigned) | ≥75%; remainder flagged for manual review | Incomplete form passes as complete and reaches declaration stage |
| O1 — scanned docs | % of scanned handwritten docs correctly classified as received | ≥70%; remainder flagged for manual review | Received document silently not recognised → false gap alert to family |
| O2 | % of figures correctly extracted across 20 test PDFs | ≥90% field accuracy | Plausible-looking wrong figure with no uncertainty flag → disqualifying failure |
| O3 | % of letters rated "usable with minor edits" by 2 senior juristes | ≥70% usable | Legally outdated clause in draft sent without detection |
| O4 Ph.1 | % of known missing documents caught on 10 retrospective closed files | ≥80% recall | All-green checklist on a file known to have had a missing document at submission |

---

### Step 5 — Early Adopter Feedback Sessions
**Owner:** AI PM · *2 × 30-min sessions per early adopter*

**Session 1 (before using):** Show prototype without coaching.
- "Walk me through what you see."
- "What would you trust? What would you check anyway?"
- "What would make you uncomfortable using this on a real file?"

**Session 2 (after using on a real anonymised file):**
- "Did it save you time?"
- "Did it catch something you might have missed?"
- "Did it make a mistake? How did you feel about that?"
- "Would you use this tomorrow if it were live?"

**Target:** ≥3.5/5 average sentiment across early adopter cohort (1 = would not use; 5 = would use immediately).

---

### Step 6 — Pilot Phase
**Owner:** AI PM + Tech Lead + Team Lead  
**Duration:** 4 weeks · **Cohort:** early adopters (3–5) + 3–5 additional juristes  
**Prerequisite:** O6 secure infrastructure live. GDPR compliance active. For O2/O4: EU AI Act conformity assessment in progress (pilot runs in parallel — see Step 0).

**Success metrics:**

| Opportunity | Primary metric | Target vs. discovery baseline | Secondary metric |
|---|---|---|---|
| O1 | Avg follow-up rounds per file | ≤2 (baseline: 3–5) | % of juristes actively using the gap view daily |
| O1 | % of incomplete forms caught before declaration stage | ≥60% of previously missed incomplete documents surfaced | 0 incomplete forms reaching BSJ submission |
| O2 | Time on extraction step per file | ≤1h (baseline: ~2h) | Zero serious errors in submitted declarations |
| O3 | Time on letter drafting per file | ≤1.5h (baseline: 3.5h) | % of letters sent with only minor edits (quality signal) |
| O4 Ph.1 | Time on pre-submission review per file | ≤2h (baseline: 2.5h) | % of flagged items confirmed as real issues by juriste (precision) |

**Measurement:** Time-diary self-logging (format from phase-02-Discovery_plan.md) for all pilot juristes. Debrief at Week 2 and Week 4.

**Decision-maker: COO (Marc) + Head of Tech (Thomas).** This is a production budget commitment and a risk sign-off — it requires both business authorization and technical confirmation. The AI PM prepares the evidence pack and a written recommendation; the go/no-go decision is made by COO + Head of Tech jointly.

**Go/No-Go at Week 4:**
- **Go:** primary metric at target AND sentiment ≥3.5/5 AND zero serious uncaught errors
- **Conditional go:** metric partially met, errors caught by human review, juristes want to continue
- **No-go:** primary metric not met OR serious uncaught error (incorrect figure filed, critical document missed without flag) OR sentiment <2.5/5

---

### Step 7 — EU AI Act Conformity Assessment Completion Gate (O2 and O4 only)
**Owner:** Legal + Tech Lead + AI PM · *Must complete before production GA*

The assessment was opened in Step 0 and has been running in parallel with Steps 1–6. This gate confirms it is complete before any rollout beyond the named pilot cohort.

1. Risk classification confirmed and documented
2. Human oversight mechanisms validated in pilot (review step, approval gate, override logging)
3. Technical documentation complete (model behaviour, accuracy limits, failure modes)
4. Audit trail for every AI-assisted declaration operational
5. COO sign-off on risk documentation

**This gate cannot be bypassed.** General availability of O2 or O4 without completed conformity assessment exposes Legacio to EU AI Act liability.

---

## Summary Scorecard

| # | Opportunity | Impact | Feasibility | Savings/year | Risk | Phase |
|---|---|---|---|---|---|---|
| O6 | Secure AI Workspace | Prerequisite | Medium | — | Low | **A — First** |
| O1 | Document Gap + Completeness | **4.7/5** | 3.5/5 | €1.9M | Low–Med | **B — First** |
| O4 Ph.1 | Pre-Submit presence check | 3.8/5 | 4.0/5 | ~€80K | Low | B–C |
| O3 | Communication Drafting | 4.0/5 | **4.5/5** | €471K | Low | B — After O1 |
| O2 | PDF Data Extraction | 4.3/5 | 3.0/5 | €385K | Medium | C |
| O4 Ph.2 | Pre-Submit + Article 108 | 4.0/5 | 3.0/5 | ~€160K | Medium | C |
| O4 Ph.3 | Pre-Submit + figures | 4.3/5 | 2.5/5 | ~€320K | Medium | D |

**Phase B combined (O1 + O3 + O4 Ph.1): ~€2.5M/year at lowest technical risk.**  
**Full programme (O1 + O2 + O3 + O4 Ph.1–3): ~€3.1M/year on €4.25M juriste payroll.**

> **Revenue upside (capacity expansion) — not captured in the cost model above.**  
> Legacio's revenue model is per-file, with pricing defined per engagement by the team. This means saved time translates directly into file capacity. O1 alone frees ~10h/file across 2,750 files = 27,500h/year — equivalent to capacity for ~344 additional files without hiring (at 80 files/juriste/year). At Legacio's average revenue per file, this capacity upside likely exceeds the €1.9M cost saving. The COO's question is not just "what do we save?" but "how many more files can we handle at the same headcount?" — a stronger investment argument, and one that scales with growth.

---

---

## Validation Phase Timeline

> Maps the 7-step validation protocol to calendar weeks. The build sequence (Phase A → D) runs in parallel — validation gates are the go/no-go checkpoints within each build phase.

### Per-Opportunity Validation Timeline

| Week | O1 — Doc Gap | O3 — Drafting | O4 Ph.1 — Pre-Submit | O2 — PDF Extraction | O4 Ph.2–3 |
|---|---|---|---|---|---|
| **0–2** | Step 0: infra + data access gate | Step 0: CRM API gate | Step 0: infra gate | Step 0: infra + EU AI Act classification + **build vs. buy decision** | Step 0 (blocked until O2 done) |
| **2–3** | Step 1–2: Early adopters ID'd; signal confirmed | Step 1–2: Sophie + Michèle confirmed | Step 1–2: Carole + Valérie confirmed | Step 1–2: Nathalie + Denis confirmed | — |
| **3–6** | Step 3: Figma gap view mockup on 1 anonymised file | Step 3: LLM drafts 3 letter types on real CRM export | Step 3: Paper pre-flight checklist on a real closed file | Step 3: Manual OCR + LLM on 5 anonymised files → spreadsheet with source citations | — |
| **6–8** | Step 4: ≥85% gap recall, ≥75% completeness flag on 20 files | Step 4: ≥70% letters rated "usable with minor edits" | Step 4: ≥80% missing docs caught on 10 closed files | Step 4: ≥90% field accuracy on 20 test PDFs | — |
| **8–10** | Step 5: 2 × 30-min sessions per early adopter | Step 5: Same | Step 5: Same | Step 5: Same | — |
| **10–14** | **Step 6: Pilot** (4 weeks, 6–8 juristes, O6 live) | Step 6: Pilot (after O1 in production) | Step 6: Pilot alongside O1 | **Step 6: Pilot** (EU AI Act conformity ongoing in parallel) | — |
| **14** | **Go/No-Go:** COO + Head of Tech | Go/No-Go | Go/No-Go | Go/No-Go | — |
| **14+** | Production rollout | Production | Production | Step 7: Conformity assessment completion gate | Step 0 begins |
| **28+** | — | — | — | — | Step 3–7, then GA after conformity |

### Key Observations

- **O1 is the critical path**: it must reach production before O3 can deliver full value (O3 needs the live gap view as input). O1 pilot starting at Week 10 → production by Week 16 is the target.
- **O2 is the longest validation arc**: Step 0 includes both the build-vs-buy decision and EU AI Act classification. If build-vs-buy goes to "buy," Phase C accelerates by 4–6 weeks.
- **Total time to first production feature (O4 Ph.1 or O1)**: 10–14 weeks from discovery readout — which is why Step 0 must begin the week the discovery readout is approved, not after.
- **Discovery readout to production GA (full programme)**: ~32–36 weeks. Communicating this at Week 4 of discovery sets accurate expectations with the COO before any build budget is committed.

---

*Next step: present to COO (Marc) and Tech Lead (Thomas) for go/no-go on O6 infrastructure and Phase B scope commitment.*
