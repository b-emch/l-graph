# AI Workflow Retrospective — Enaos AI PM Case Study

**Author:** Bastien Chevallier  
**Date:** 2026-05-07  
**Scope:** All AI-assisted work produced in this folder across 6 sessions

---

## 1. Overview

This case study was produced end-to-end with AI assistance, from domain familiarization through discovery synthesis and opportunity mapping. This document reflects honestly on where AI accelerated and improved the work, and where human judgment remained irreplaceable.

The full prompt/response log is available in `prompts.md`.

---

## 2. What AI Did Well

### 2.1 Domain grounding before any interview
**How:** `/graphify` processed 39 legal chapters, 22+ blog articles, and 7 regulatory PDFs into a structured knowledge graph. Community detection surfaced 5 workflow clusters; god-node analysis identified Article 108 (post-death administrative filing deadline) as the highest-centrality concept — 6+ edges, central to both Asset Liability and Succession Declaration communities.

**Why it mattered:** I had no prior expertise in Belgian inheritance law. The graph gave me a structured mental model before the first interview question was written, preventing me from asking naïve or mis-ordered questions. The Article 108 finding shaped the interview template (dedicated probe question) and later confirmed as the most technically complex discovery signal (O4/O5 in opportunities).

**Human judgment applied:** I decided which god nodes were operationally meaningful vs. legally theoretical. The graph surfaces centrality — the PM frames relevance.

---

### 2.2 Economic model scaffolding in one pass
**How:** The discovery synthesis (Prompt 9–10) took interview self-reports on time-per-task and computed a full annual cost model in a single pass: 2,750 files/year × 34 juristes × 38h × 47 weeks × €70/h, with per-signal breakdowns and addressable savings (~€3.1M/year).

**Why it mattered:** Building this model manually across 11 signals and 5 workflow clusters would have taken hours. AI produced a structurally sound model; the errors it made (wrong working hours, Marc/Thomas miscounted as juristes) were caught immediately in review.

**Human judgment applied:** Every assumption required validation — working hours, cost per hour, volume — and the corrections changed the output meaningfully. The model is a scaffold, not a fact sheet.

---

### 2.3 Discovery plan architecture from a knowledge graph
**How:** Prompt 5 used `/graphify query` to orient in the domain before planning. The 5 workflow clusters from the graph became the 5 discovery lenses in the interview templates. The non-linearity of the document collection loop (Cluster 1) was flagged by graph structure before any juriste confirmed it.

**Why it mattered:** The discovery plan was domain-grounded rather than generic. Cluster-anchored interview questions produced more specific answers in simulated interviews.

---

### 2.4 Persona calibration against known domain signals
**How:** Sophie, Thomas, and Marc (Prompts 6–8) were designed using a 5-layer framework (Identity, Domain knowledge, Pain profile, AI sentiment, Hidden signals) anchored in both the graph (workflow clusters, document types) and the case brief (the four specific overload signals from the original situation description).

**Why it mattered:** Sophie's AI sentiment calibration (corrected to 2/5 due to legal liability exposure) produced meaningfully different responses than a generic "sceptical user" prompt would. The hidden signal layer ("never pushed back formally on AI in team meetings — avoids confrontation") created behavioral consistency across interview questions.

---

### 2.5 The PM as quality gate — AI generates, the PM steers
**How:** Every major document went through at least one round of user-directed correction before final write. Prompts 10, 12, and 13 document significant corrections that changed the output structurally (not cosmetically).

**Why it mattered:** This mirrors the real PM skill: knowing what to ask for, reading the output critically, and steering precisely. The AI produced drafts; the PM produced decisions.

---

## 3. Where Human Judgment Was Necessary

### 3.1 Persona interviews do not replace ethnographic reality
**Risk:** The three agent personas (Sophie, Thomas, Marc) were built from domain knowledge and the case brief — they reflect what I embedded in them. They cannot surface what I didn't know to ask.

**Manifestation:** All three persona interviews converged on the same bottlenecks (document collection, declaration drafting, template weakness). This confirmed hypotheses but could not generate surprising signals. Real juristes might reveal a workflow step not covered in the knowledge graph, a tool used informally, or an emotional dimension not in the brief.

**Mitigation applied:** The persona outputs were framed as hypotheses to validate, not findings. The discovery plan mandates shadow observation before interviews for exactly this reason.

---

### 3.2 Reach and variance could not be evaluated
**Risk:** All 12 simulated interviews drew from the same source material. There was no variance in sentiment distribution, regional practice differences, or team-level disagreement.

**Manifestation:** Occurrence rates (e.g., S1 document gap detection at 10/10 juristes) are structurally inflated — the model generates consistent agents, not a realistic distribution. A real team of 30 juristes would include outliers: one who has already built their own template system, one who works exclusively on high-value estates with different document profiles.

**What this means for the presentation:** The % occurrence figures represent hypothesis strength, not statistical confidence. This must be named explicitly.

---

### 3.3 Technical hypotheses require expert validation
**Risk:** Two key signals depend on technical facts I could not verify from interviews or the knowledge graph.

**Signal S2 — Fragmented tools:** The juristes described friction between systems, but whether this is a genuine integration gap or a workflow habit could not be confirmed. Head of Tech (Thomas) validation is required before this can inform product decisions.

**Signal O1 — OCR on handwritten documents:** The risk of false gap alerts on scanned/handwritten forms was identified and documented (Prompt 12), but the actual % of incoming documents that are handwritten is unknown. This changes the severity of the risk tier significantly.

---

### 3.4 Regulatory interpretation requires a lawyer
**Risk:** The graph surfaced Article 108 as a central node and I used it to design O4's Phase 2 (temporal logic verification). But interpreting Article 108 correctly — edge cases, regional variations, recent case law — requires a qualified Belgian inheritance lawyer, not a knowledge graph.

**How this was handled:** O4 is scoped as a "flagging" tool, not a compliance engine. It surfaces potential issues for juriste review, not automated decisions. This is the correct product design response to a regulatory unknown.

---

### 3.5 WYSIATI — the knowledge graph is also the knowledge ceiling
**Concept (Kahneman):** *What You See Is All There Is.* The model builds the best possible coherent story from the information it has — and does not flag what is missing. It does not say "you haven't told me about X."

**Risk:** The entire analysis — workflow clusters, signal identification, persona pain profiles, opportunity scoping — is bounded by what was in the Legacio content and regulatory PDFs scraped in Session 2. If a key workflow step is absent from the public documentation (e.g., an internal escalation procedure, an informal coordination loop between juristes and notaries, a tool used informally), the graph simply has no node for it. The AI will produce a thorough, confident analysis from the 60% it sees, with no indication that 40% was never in scope.

**Manifestation:** The document collection loop was correctly identified as non-linear from the graph — but only because Legacio's own guides described it that way. A workflow that Legacio doesn't publish (e.g., how juristes handle disputes between heirs) would not appear in the graph, and therefore not in the discovery hypotheses, and therefore not in the interview templates as a probe question.

**What this means:** The knowledge graph shapes what gets asked, what gets found, and what gets prioritized. Confirmation bias is structurally embedded. Real discovery — especially shadow sessions — is the only corrective.

---

### 3.6 AI sentiment is assumed, not measured
**Risk:** The AI readiness scores (Sophie 2/5, Thomas 4/5, Marc 4/5) were calibrated by the PM based on role and liability profile — they were not measured by survey, observation, or prior change management data.

**What this means:** The adoption risk section of the opportunity map is qualitative. A real discovery would include an AI sentiment survey run before the persona interviews (as specified in the discovery plan), giving a quantitative baseline to compare against.

---

## 4. AI Workflow Summary

| Decision point | AI contribution | Human judgment |
|---|---|---|
| Identifying Article 108 as priority | Graph: god node status, 6 edges, central to 2 communities | Deciding it was operationally relevant, not just legally central |
| Sophie's AI sentiment score | Framework: liability profile → resistance signal | Correcting 3/5 to 2/5 — catching the legal liability dimension AI didn't weight |
| Excluding S2 (fragmented tools) from roadmap | Flagged as a confirmed pain signal (10/10 occurrence) | Reclassifying it as a technical constraint pending Thomas validation — not an opportunity |
| Economic model assumptions | Full cost model in one pass: 11 signals, 5 clusters, €3.1M savings | Correcting working hours, recounting juristes, removing Marc and Thomas from juriste pool |
| Merging O4 + O5 | Two separate opportunity cards with distinct scopes | Recognizing shared data pipeline → one phased product, not two |
| EU AI Act placement | Draft placed conformity assessment at Step 7 | Moved to Step 0 — discovering high-risk status at Step 6 means rebuilding from scratch |

---

## 5. Honest Assessment

This AI-assisted workflow produced a structurally sound, domain-grounded case study in less time than a conventional approach. The knowledge graph was the highest-leverage single decision — it compressed what would have been a week of domain research into one session and produced a finding (Article 108) that survived through to the final opportunity map.

The hardest thing AI cannot do in this workflow: generate surprise. The strongest discovery moments — the juriste who uses WhatsApp to chase documents, the one who printed a form because she doesn't trust the scanned version, the team that built an internal FAQ after a €40k penalty on a missed deadline — those come from being in the room. The simulated interviews produce plausible signals. Real interviews produce the unexpected ones that reshape your opportunity map.

The workflow demonstrated here is a valid PM methodology: use AI to be more prepared, faster, and more structured — then use real interviews to stress-test and surprise.

---

*Full prompt/response log: `prompts.md`*  
*All source material: `00-raw/`, `01-graphify-out/`*
