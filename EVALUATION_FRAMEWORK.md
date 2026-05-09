# Evaluation Framework — Enaos AI PM Case Study

**Purpose:** A structured evaluation protocol that mirrors what your panel (COO, CTO, Product Owner) actually assesses. Use this after completing each phase to validate your work and flag issues early.

**Last Updated:** 2026-05-06  
**Status:** Active (used at end of each phase)

---

## Core Principle

Your case study presentation succeeds if it demonstrates:
1. **Rigorous problem diagnosis** (not guessing, measuring)
2. **High-impact opportunity identification** (tied to business economics)
3. **Realistic execution strategy** (technical grounding + user validation)
4. **Clear thinking** (shows how you'd actually operate as an AI PM)

The three panelists evaluate you through overlapping but distinct lenses.

---

## The Three Evaluation Lenses

### LENS 1: COO Perspective — Business Impact & Economics

**The COO asks:** "Does this person understand how to tie AI initiatives to business value? Can they quantify impact and make a case that justifies investment?"

**Evaluation Checklist:**

- [ ] **Current-state economics quantified**
  - What does the status quo cost? (time/FTE/error rates/revenue loss)
  - How is this measured? (hours per task, salary loaded, operational risk)
  - Is the number credible? (not a guess — grounded in discovery or reasonable assumption)
  - RED FLAG: "Lawyers are busy" without numbers

- [ ] **Problem scope tied to business metrics**
  - Which workflow costs the most? (time × salary × volume)
  - How does this affect revenue? (client acquisition, retention, margin)
  - Why should AI solve this *first* vs. other problems?
  - RED FLAG: Picking a problem because "AI is trendy," not because it's the biggest economic lever

- [ ] **Solution impact forecasted realistically**
  - For each use case: time saved per task × tasks per year × loaded cost
  - For each use case: confidence level (high/medium/low) and reasoning
  - Are you inflating numbers? (COO will smell it)
  - RED FLAG: "Time per task will drop 50%" without pilot data or comparable precedent

- [ ] **Budget & timeline constraints named**
  - What's the 6-month budget? (was it stated, or do you infer?)
  - Team capacity: 12 devs, 30 lawyers — how will they participate in discovery/pilot?
  - What's the go/no-go decision point?
  - RED FLAG: Ignoring constraints or treating them as "not my problem"

- [ ] **Risk acknowledgment**
  - What could cause this to fail? (adoption risk, technical risk, regulatory risk)
  - How would you know early? (which signals matter?)
  - Pivot readiness: when would you kill this and try something else?
  - RED FLAG: Over-confidence; no contingency thinking

- [ ] **Success criteria are measurable**
  - How do you know if a use case is "working"? (user adoption, time savings, cost reduction)
  - Who measures? (you, the CFO, the ops team?)
  - RED FLAG: Vague metrics like "user satisfaction" without specificity

**COO's Silent Question:** "Is this person someone I'd trust to make a go/no-go call on the next $500K investment?"

---

### LENS 2: Head of Tech (CTO) Perspective — Technical Grounding & Feasibility

**The CTO asks:** "Does this person understand what we're actually building? Have they thought about the technical constraints? Would this AI initiative actually work on our stack?"

**Evaluation Checklist:**

- [ ] **Problem is technically tractable**
  - What kind of AI solves this? (LLM, retrieval-augmented generation, classification, extraction)
  - Why that approach? (is there a simpler non-AI solution they missed?)
  - Are there known hard parts? (structured data from unstructured PDFs, hallucination risk, domain knowledge gap)
  - RED FLAG: "We'll use ChatGPT" without thinking about data privacy, cost, or domain specificity

- [ ] **Data & integration realities named**
  - What data exists? (formats, volume, quality, structure)
  - What data is missing? (discovery gap to close in Phase 2)
  - Integration touch points: how does this plug into the current workflow? (email, web UI, internal tool)
  - RED FLAG: Assuming clean data; underestimating data pipeline work

- [ ] **Privacy, compliance, security are considered**
  - Legal documents + AI = sensitive. What regulations apply? (GDPR, legal privilege, client data confidentiality)
  - Model choice: can you use commercial APIs, or do you need on-prem?
  - Audit trail: do you need to log what the AI suggested vs. what the lawyer actually sent?
  - RED FLAG: Glossing over privacy; assuming you can just throw data at OpenAI

- [ ] **Prototype feasibility is realistic**
  - What's the minimum viable prototype? (one use case, one workflow step)
  - Could you build it in 2–4 weeks with 2 engineers? (or is it a 3-month project?)
  - What's the learning curve? (is this a known pattern for your team, or new tech?)
  - RED FLAG: Scope creep disguised as "MVP"; underestimating integration work

- [ ] **Cost model exists**
  - API costs (tokens, model pricing) vs. FTE savings
  - Does AI save money, or just shift cost to engineering?
  - Scaling costs: if this works, how much does it cost to roll out to other use cases?
  - RED FLAG: Ignoring operational costs; assuming AI is free

- [ ] **Tech roadmap is credible**
  - Phase 2: discovery + prototype (timeline, team size)
  - Phase 3–4: validation + scaled rollout (realistic?)
  - Dependencies: what blockers might slow you down? (data clean-up, API access, internal tooling)
  - RED FLAG: Wishful timeline; ignoring dependencies

**CTO's Silent Question:** "Is this person someone who understands technical reality, or are they going to ask us to build magic?"

---

### LENS 3: Product Owner Perspective — Customer Insight & Execution Clarity

**The Product Owner asks:** "Is the discovery actually rigorous? Do they understand the user deeply, or are they guessing? Can they run this discovery well?"

**Evaluation Checklist:**

- [ ] **User segmentation is specific**
  - Who are the 30 lawyers? (roles, seniority, task profiles)
  - Do they all do the same work, or are there distinct personas?
  - Example: junior lawyer (procedural, lower autonomy) vs. partner (high judgment, client-facing) — different needs
  - RED FLAG: Treating "lawyers" as a monolith; not thinking about variance within the group

- [ ] **Current workflow is mapped with evidence**
  - What does a lawyer actually do hour-by-hour? (not assumptions, actual observations)
  - Where are the bottlenecks? (search, writing, verification, rekeying — ranked by time/frequency/pain)
  - What workarounds exist? (do they already use templates, copy/paste, external tools?)
  - RED FLAG: Guessing workflows; not having observed users actually work

- [ ] **Problem validation is grounded**
  - Is the problem real, or a manager's hunch? (Have you talked to lawyers directly?)
  - How would you know if you were wrong? (what evidence would disprove your hypothesis?)
  - Competing problems: why are you solving *this* first?
  - RED FLAG: Building on a manager's assumption without user validation

- [ ] **Discovery method is sound**
  - Who will you interview? (which personas, how many, which office locations?)
  - Interview guide: what are you actually asking? (probing for workflows, not just opinions)
  - Metrics collection: how do you measure time-per-task? (observation, self-report, time tracking)
  - RED FLAG: Vague; "we'll talk to some lawyers" without structure

- [ ] **Use case qualification framework is clear**
  - How do you rank use cases? (RICE, Weighted Shortest Job First, custom framework?)
  - Inputs to the framework: time saved, effort to build, user impact, strategic fit
  - How do you validate before building? (prototype, user feedback, pilot)
  - RED FLAG: No framework; picking based on gut feel

- [ ] **Pilot & iteration approach is realistic**
  - Will you build → test → iterate, or build once and launch?
  - Who are your pilot users? (early adopters, or random sample?)
  - What's the feedback loop? (how often, what signals matter?)
  - RED FLAG: No pilot; going straight to full rollout

- [ ] **Success definition is testable**
  - For each use case: what does success look like? (adoption rate, time saved, cost reduction)
  - How do you measure it? (logging, surveys, time tracking)
  - When do you decide to expand or kill it?
  - RED FLAG: Vague success criteria that can't be measured

**Product Owner's Silent Question:** "Would I trust this person to run discovery and make the right call on what to build?"

---

## Red Flags Summary (Across All Lenses)

If you see ANY of these in your work, fix it before presenting:

1. **Unquantified claims** — "Lawyers are busy" without data
2. **Guessed workflows** — You haven't actually watched someone work
3. **Technical hand-waving** — "We'll use AI" without specifying which approach or thinking through integration
4. **Privacy/compliance glossed over** — You haven't named the regulatory constraints
5. **Vague discovery plan** — You don't have a specific interview guide or sampling strategy
6. **No qualification framework** — You can't explain how you'll rank use cases
7. **Wishful timeline** — Your phases assume zero integration work, no blockers, perfect execution
8. **Ignoring the 1-year failure** — You haven't explained why your approach would succeed where the last initiative failed
9. **No contingency** — You have one idea and no plan B
10. **Overconfidence in AI solving everything** — You haven't named realistic limitations or manual handoff points

---

## How to Use This Framework

### At the End of Each Phase:

1. **Read your artifact** (phase-0X-*.md) against each lens
2. **Check the boxes** — be honest about what you've done and what you've skipped
3. **Note gaps** — which checkboxes are unchecked? Why?
4. **Identify which panel member would most disagree** — that's where to focus next
5. **List your top 3 risks** — what would each panelist push back on?
6. **Plan your next iteration** — which gaps must close before the next phase?

### Scoring (Optional):

For each lens, count checked boxes:
- **10/10 boxes checked** = Strong (panelist would be impressed)
- **7–9 boxes checked** = Solid (panelist has minor questions)
- **5–6 boxes checked** = Weak (panelist will push back)
- **<5 boxes checked** = Red flag (panelist won't buy your logic)

If any lens scores <6, you have work to do before moving forward.

---

## Example Application

**Scenario:** You finish Phase 2 (Discovery Preparation) and produce a Discovery Charter + Interview Guide.

**You run the evaluation:**
- COO lens: ✓ Economics quantified, ✓ Problem scope clear, ✗ Budget constraints not named, ✗ Risk framework missing
- CTO lens: ✓ Problem is tractable, ✗ Data sources not inventoried, ✓ Privacy constraints named, ✗ Prototype feasibility unclear
- PO lens: ✓ Personas segmented, ✗ Workflows not yet observed, ✓ Discovery method is sound, ✓ Use case framework is clear

**Diagnosis:** You're strong on strategy and discovery method, but weak on technical grounding and budget/risk framing.

**Action:** Before moving to Phase 3, spend 1–2 hours on:
1. Inventory data sources with the CTO
2. Define budget envelope and kill criteria with the COO
3. Build a risk matrix (what could go wrong, how would you know)

---

## Integration with Your Workflow

This framework should be **your internal quality gate before any external review**. After each phase:
1. **Self-evaluate** (use this framework)
2. **Fix the gaps** (iterate on your artifact)
3. **Then present** to get feedback

This way, when you're in the real interview, you've already heard and answered every critical question.

