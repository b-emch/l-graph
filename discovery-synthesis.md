# Discovery Synthesis — Legacio Juristes
**Date:** 2026-05-07  
**Interviews:** 12 total — 10 juristes (Sophie, Carole, Valérie, Nathalie, Philippe, Isabelle, Laurent, Céline, Michèle, Denis) + 1 COO (Marc) + 1 Tech Lead (Thomas)  
**Conducted by:** Bastien Chevallier, PM

---

## Context & Methodology

### Volume & cost assumptions
| Parameter | Value |
|---|---|
| Files/year | 2,500–3,000 → **2,750 (midpoint)** |
| Files/juriste/year | ~80 |
| Estimated juriste headcount | **~34** (2,750 / 80) |
| Simultaneous files/juriste | ~25 (driven by 4-month legal deadline) |
| Juriste hourly cost | **€70/hour** |
| Working hours/year/juriste | 38h/week × 47 weeks (52 − 5 holidays) = **1,786h/year** |
| **Total juriste payroll** | 34 × 1,786 × €70 = **~€4.25M/year** |

### Service lines
Legacio operates two main service lines:
- **Succession management** (primary focus of this analysis): full-service handling of inheritance files, from document collection through BSJ declaration.
- **Will redaction** (out of scope): drafting of wills and estate planning. Represents ~15% of revenue (per Marc, COO). Not addressed in this analysis — it has distinct workflows and a separate opportunity landscape.

### Cluster definitions
- **A — Document Collection Loop**: initial document request, follow-ups, family chasing, document completeness verification
- **B — Post-death Procedures**: file opening, tool fragmentation *(technical constraint — see note below)*, real-time file visibility
- **C — Succession Declaration**: form completion, data extraction from PDFs, pre-submission verification, BSJ filing
- **D — Will & Heir Analysis**: Article 108 analysis, testament interpretation, reserve héréditaire, contested files
- **E — Document Production**: letters, standard communications, manual drafting workload

> **Note on tool fragmentation (Cluster B):** All juristes flagged the lack of integration between DMS, CRM, and email as a structural frustration. This is acknowledged as a **technical constraint** and will not be directly addressed in the current product roadmap. Signals tied exclusively to this constraint are noted but excluded from opportunity sizing.

---

## Signal Matrix

| # | Signal | Juriste occurrences | % (n=10) | Primary Cluster | Pain Level |
|---|---|---|---|---|---|
| S1 | Document chasing loop | 10/10 | **100%** | A | 4/5 |
| S2 | Fragmented tools — no integration *(technical constraint)* | 10/10 | **100%** | B | 4/5 |
| S3 | No real-time file visibility | 10/10 | **100%** | B | 4/5 |
| S4 | Succession Declaration — manual filling & data extraction | 10/10 | **100%** | C | 5/5 |
| S5 | Manual communication drafting — minimal template value | 10/10 | **100%** | E | 3/5 |
| S6 | 4-month deadline stress + personal legal liability | 10/10 | **100%** | C | 5/5 |
| S7 | Article 108 — complexity & family resistance | 9/10 | **90%** | D | 3/5 |
| S8 | Pre-submission verification anxiety | 9/10 | **90%** | C | 4/5 |
| S9 | Shadow AI use + data privacy fear | 12/12 | **100%** | Cross-cutting | 4/5 |
| S10 | Context-switching / cognitive overload (25 files) | 8/10 | **80%** | B | 4/5 |
| S11 | Emotional labor — grieving families | 6/10 | **60%** | A | 3/5 |

*S9 occurrence is 12/12 (all interviews including COO and Tech Lead, all of whom admitted shadow AI use).*

---

## Signal Deep-Dives

---

### S1 — Document Chasing Loop
**Cluster: A — Document Collection Loop · Pain: 4/5 · 10/10 juristes**

#### What juristes say
Every juriste describes the same cycle: send a document checklist → family misreads or ignores it → partial submission → verify against DMS → identify gaps → call + email to explain again → wait → repeat. Average number of follow-up rounds: **3 to 5 per file**, with each round requiring a call, an email, and a manual cross-check.

> *"Les familles reviennent presque jamais avec tout d'un coup. Je dois les relancer trois, quatre fois. C'est usant. C'est vraiment la partie la plus chronophage."* — Sophie (J1)

> *"Le travail de chasing, c'est probablement trente, quarante heures par dossier."* — Philippe (J6)

> *"Boucle infernale."* — Marc (COO)

#### Time estimates from interviews
| Scenario | Time/day on chasing |
|---|---|
| Good day | 2–3h |
| Bad day | 5–7h |
| Estimated average | **~3.5h/day** |

**Estimated total chasing time/file:** 35–50h (Philippe/J6: 30–40h, Nathalie/J5: 50h, Thomas/J10: 40h)  
→ Midpoint used: **40h/file**

#### Economic impact
| Metric | Value |
|---|---|
| Total chasing cost per file | 40h × €70 = €2,800 |
| Total annual chasing cost | 2,750 × €2,800 = **€7.7M** |
| Reducible share (smart tracking, auto-reminders, guided family portal) | ~25% |
| **Annual savings potential** | **~€1.9M/year** |

*The full 40h is not purely waste — families in grief will always need guidance. However, smart tracking, automated reminders, and structured document requests could eliminate ~1 in 4 manual touchpoints.*

---

### S2 — Fragmented Tools — No Integration
**Cluster: B — Post-death Procedures · Pain: 4/5 · 10/10 juristes · ⚠️ Technical constraint — not being addressed**

#### What juristes say
All juristes use DMS + CRM + Outlook, which do not communicate. Every document receipt requires 3 manual actions: log in DMS, update CRM, note in email. Juristes describe themselves as "the manual integration layer."

> *"C'est absurde au 21ème siècle."* — Marc (COO interview)

> *"Ça me prend une heure pour ce qui devrait prendre dix minutes."* — Philippe (J6)

#### Economic impact
| Metric | Value |
|---|---|
| Estimated time lost to manual integration | ~20% of total work time |
| Annual cost | 34 × 1,786h × 20% × €70 = **€850K/year** |
| **Addressable savings** | **€0 (out of current scope — technical constraint)** |

---

### S3 — No Real-time File Visibility
**Cluster: B — Post-death Procedures · Pain: 4/5 · 10/10 juristes**

#### What juristes say
No single view shows which documents were requested, which arrived, what's missing, and when the last follow-up was sent. Every juriste maintains this state mentally or in personal Word/Excel notes. With 23–27 simultaneous files, this creates systematic errors: double-relances (reported by 8/10 juristes), forgotten documents, and missed deadlines.

> *"Je dois garder un état mental de chaque dossier. C'est dans ma tête. Pas dans les outils."* — Carole (J2)

> *"Une vue unique où je verrais : famille X, vous avez demandé ces documents le Y, il manque cela, vous avez relancé le Z — ce serait énorme."* — Sophie (J1)

#### Economic impact
| Metric | Value |
|---|---|
| Direct time cost | Captured within S1 (chasing) and S2 (tool fragmentation) |
| **Annual savings potential** | **€0 separate** (included in S1 savings estimate) |

*Primary impact here is error risk and family experience (embarrassing double-relances), not a separable time cost.*

---

### S4 — Succession Declaration — Manual Filling & Data Extraction
**Cluster: C — Succession Declaration · Pain: 5/5 · 10/10 juristes**

#### What juristes say
The Déclaration de Succession is unanimously the most feared task. It requires extracting figures from PDFs (bank statements, property valuations, debt records) and manually entering them into the BSJ form, then verifying internal consistency before signing. The juriste who signs bears full professional, legal, and financial liability for every figure.

> *"Si les chiffres sont faux — si j'ai mal additionné les actifs, si j'ai oublié un passif — les conséquences fiscales, c'est la famille qui les subit, mais c'est moi qui suis responsable professionnellement."* — Sophie (J1)

> *"Je dois extraire les chiffres des PDFs manuellement. C'est du travail qu'une simple OCR + extraction d'entités pourrait faire."* — Denis (J12, tech background)

> *"Un dossier complexe, sept, huit heures. Je dois vraiment être concentrée."* — Nathalie (J5)

#### Time estimates from interviews
| File type | Time/file |
|---|---|
| Simple file | 2–3h |
| Complex file (multiple properties, Article 108, many heirs) | 7–10h |
| Weighted average (est. 70% simple, 30% complex) | **~4h/file** |
| Of which mechanical — data extraction from PDFs (per Denis & Thomas) | ~50% → **~2h/file** |

#### Economic impact
| Metric | Value |
|---|---|
| Total declaration work/year | 2,750 × 4h × €70 = **€770K/year** |
| Mechanically automatable portion (OCR + structured extraction) | 2,750 × 2h × €70 = **€385K/year** |
| **Annual savings potential** | **~€385K/year** |

*Plus uncaptured risk cost: tax penalties for heirs, professional liability for juristes, potential legal disputes. Not quantified but consistently rated as the highest-stakes failure mode (pain 5/5).*

---

### S5 — Manual Communication Drafting — Minimal Template Value
**Cluster: E — Document Production · Pain: 3/5 · 10/10 juristes**

#### What juristes say
Templates in the CRM are 3–5 years old, legally outdated, and provide minimal drafting value. Juristes rewrite 70–80% of each letter or email from scratch. Every juriste has built a personal shadow library on their local machine, creating inconsistency across the team. Beyond efficiency, this is a **quality and compliance risk**: outdated templates may contain obsolete legal clauses, and shadow libraries produce non-standardized client-facing communications.

> *"Je prends un template, je l'ouvre, et je réécris à peu près entièrement."* — Sophie (J1)

> *"Je dois constamment corriger le travail des plus jeunes juristes qui ont utilisé un template dépassé. Ça crée du rework."* — Michèle (J11, mentor)

> *"Techniquement, c'est un problème de templating + variable substitution. Un enfant de dix ans pourrait faire un script qui génère ces lettres correctement."* — Denis (J12)

Pain is 3/5 (not 4/5) because a workaround exists — personal shadow templates — but this workaround is itself a problem.

#### Volume estimate
| Parameter | Value |
|---|---|
| Letters/emails per file | ~6–8 (initial checklist, 3–4 follow-ups, bank letter, BSJ letter, notaire cover) |
| Time wasted per letter vs. a working template | ~30 min |
| Time wasted per file | 7 letters × 30min = **3.5h/file** |

#### Economic impact
| Metric | Value |
|---|---|
| Annual time lost to manual drafting | 2,750 × 3.5h × €70 = **€673K/year** |
| Savings with effective template library (AI-assisted drafting) | ~70% → **~€471K/year** |
| **Annual savings potential** | **~€471K/year** |

---

### S6 — 4-Month Deadline Stress & Personal Legal Liability
**Cluster: C — Succession Declaration · Pain: 5/5 · 10/10 juristes**

#### What juristes say
The 4-month deadline to file with the Bureau de Sécurité Juridique is a hard legal constraint. Late filing triggers tax penalties on heirs. Stress peaks around day 90 when documents may still be missing and the declaration not yet complete. The signing juriste carries personal professional liability.

> *"Vous vous rapprochez de cette deadline, vous avez peut-être encore des documents manquants... et paf — vous devez la signer et l'envoyer. Si quelque chose est faux, c'est moi qui paye."* — Marc (interview)

> *"Ce qui me frustre, c'est que la pression vient en partie de notre processus inefficace."* — Thomas (Tech Lead interview)

This signal functions as a **consequence amplifier**: the 4-month window makes every other friction higher-stakes. S1 delays cost more when the clock is ticking. S4 errors have direct legal consequences. S3 (no visibility) creates late-stage panic. Pain is 5/5 because it concentrates all other pains.

#### Economic impact
| Metric | Value |
|---|---|
| Direct additional time cost | €0 (cost captured within S1, S4, S8) |
| **Risk cost (missed deadlines, incorrect declarations)** | Unquantified — tax penalties for heirs, professional liability for juristes, reputational damage for Legacio |
| **Annual savings potential** | **€0 direct** (risk reduction — unquantified) |

---

### S7 — Article 108 — Complexity & Family Resistance
**Cluster: D — Will & Heir Analysis · Pain: 3/5 · 9/10 juristes**

#### What juristes say
Article 108 of the Belgian succession tax code creates a fiscal presumption: assets transferred by the deceased within 3 years (5 years in Wallonia) before death are included in the taxable estate unless the family proves otherwise. Families consistently fail to understand it, resist it emotionally ("c'est injuste"), and submit incomplete documentation. Each Article 108 case requires cross-referencing donation contracts, bank transfers, and property records — adding 2–4h of specialist analysis.

> *"Les familles doivent trouver des documents, des preuves. C'est une source énorme de complications."* — Sophie (J1)

> *"J'ai passé trois heures de vérification, de cross-referencing des documents."* — Philippe (J6)

Pain is 3/5 because juristes handle this with professional expertise — it adds complexity but is not a systemic process failure. However, Article 108 is a frequent root cause of delayed document collection (feeding into S1) and declaration errors (feeding into S4).

The graph (GRAPH_REPORT.md) confirms this: `Article 108 – Présomption fiscale d'actifs dessaisis` is a **God Node with 6 edges**, central to both the Asset Liability community and the Succession Declaration community.

#### Economic impact
| Metric | Value |
|---|---|
| Estimated Article 108 complex files | ~30% of total → 825 files/year |
| Additional analysis time/file | ~3h |
| Annual cost | 825 × 3h × €70 = **€173K/year** |
| **Annual savings potential** (AI-assisted document cross-referencing) | ~€80K/year |

---

### S8 — Pre-submission Verification Anxiety
**Cluster: C — Succession Declaration · Pain: 4/5 · 9/10 juristes**

#### What juristes say
Before sending a completed file to the notaire or the BSJ, juristes perform a full manual review: cross-check all documents against the declaration, verify signatures, confirm all heirs are accounted for, check Article 108 coverage. This is separate from and comes after the filling work (S4) and takes 1–4h per file. It is the most concentration-intensive task juristes describe.

> *"Je dois lire, relire, vérifier les listes mentalement, m'assurer que je n'ai rien omis. C'est dur psychologiquement parce que je sais que une erreur, c'est mauvais."* — Carole (J2)

> *"Deuxième paire d'yeux — un assistant qui me dit : vous avez le document X mais pas le Y, attention Article 108 ici."* — Valérie (J4) and multiple others

#### Economic impact
| Metric | Value |
|---|---|
| Average verification time/file | ~2.5h (simple: 1h, complex: 3–4h) |
| Annual cost | 2,750 × 2.5h × €70 = **€481K/year** |
| Savings with AI-assisted completeness checklist | ~50% → **~€240K/year** |
| **Annual savings potential** | **~€240K/year** |

---

### S9 — Shadow AI Use & Data Privacy Fear
**Cluster: Cross-cutting · Pain: 4/5 · 12/12 all interviewees**

#### What juristes (and leadership) say
**Every single person interviewed** (10 juristes + COO + Tech Lead, 12/12) independently admitted — unprompted — to having used a public AI tool (ChatGPT or equivalent) with client data. Every one panicked afterward. Every one stopped. None had told anyone until this interview.

> *"J'ai copié-collé un brouillon de lettre client dans un outil IA en ligne. Ça m'a sauvé quinze minutes. Mais après, j'ai paniqué. Je n'ai jamais refait."* — Sophie (J1)

> *"Je ne suis pas fière de l'avoir fait du tout."* — Laurent (J8)

The demand signal is **universal and immediate**: juristes want AI assistance but will only use it safely if data stays within Legacio's infrastructure. Requirements cited by all 10 juristes:
1. Data must remain on Legacio servers — non-negotiable
2. Human review and correction before any output is sent — non-negotiable
3. Piloted on a known file first — unanimous request
4. AI assists, does not decide — non-negotiable framing

#### Economic impact
| Metric | Value |
|---|---|
| Direct time cost | €0 — no additional time cost |
| **Current GDPR/compliance risk** | Active: 12 people have sent client PII (names, addresses, estate details, sometimes medical info) to uncontrolled external servers |
| **Adoption readiness** | High — demand is latent and immediate, blocked only by data security |
| **Annual savings potential** | **€0 direct** (compliance risk — unquantified liability) |

---

### S10 — Context-Switching / Cognitive Overload
**Cluster: B — Post-death Procedures · Pain: 4/5 · 8/10 juristes**

#### What juristes say
Each juriste manages 23–27 simultaneous files. Switching between a newly-opened file, a file at day 85, and a contested file is described as mentally exhausting. The absence of a unified view (S3) amplifies this: every context switch requires reconstructing state across three tools.

> *"Avec 25 dossiers en même temps, c'est facile de se mélanger. Vraiment facile."* — Sophie (J1)

> *"Le context-switching est énorme."* — multiple juristes

#### Economic impact
| Metric | Value |
|---|---|
| Direct time cost | Subsumed in S2 (tool fragmentation) and S3 (no visibility) |
| **Annual savings potential** | **€0 separate** (captured in S1 savings estimate via reduced mental tracking burden) |

---

### S11 — Emotional Labor — Grieving Families
**Cluster: A — Document Collection Loop · Pain: 3/5 · 6/10 juristes**

#### What juristes say
Six juristes explicitly named the emotional dimension of their work as a significant drain. Families are grieving, confused, sometimes hostile. Explaining document requirements in empathetic, plain-language terms — repeatedly — is a substantial non-technical time cost. Céline (J9) is the most explicit, with an empathy-first practice style that adds ~30min per initial family contact.

> *"À la fin de la journée, je suis fatiguée, pas par le travail technique, mais par l'effort d'être patient et clair avec 26 familles en deuil."* — Céline (J9)

Pain is 3/5 — inherent to the profession and not reducible by internal tooling. A client-facing guided portal could reduce some re-explanation burden but won't eliminate emotional labor.

#### Economic impact
| Metric | Value |
|---|---|
| Direct time cost | Partially included in S1 chasing time estimate |
| **Annual savings potential** | **€0 direct** (inherent to the job) |

---

## Consolidated Economic Impact — All Signals

| # | Signal | Cluster | Annual Cost (current) | Annual Savings Potential | Pain |
|---|---|---|---|---|---|
| S1 | Document chasing loop | A | €7.7M (total) | **€1.9M** | 4/5 |
| S2 | Fragmented tools *(out of scope)* | B | €850K | **€0** (not addressed) | 4/5 |
| S3 | No real-time file visibility | B | — | **€0** (in S1) | 4/5 |
| S4 | Declaration manual filling | C | €770K | **€385K** | 5/5 |
| S5 | Manual communication drafting | E | €673K | **€471K** | 3/5 |
| S6 | 4-month deadline + liability | C | — | **€0** (risk, unquantified) | 5/5 |
| S7 | Article 108 complexity | D | €173K | **€80K** | 3/5 |
| S8 | Pre-submission verification | C | €481K | **€240K** | 4/5 |
| S9 | Shadow AI / data privacy | Cross | — | **€0** (compliance risk) | 4/5 |
| S10 | Context-switching overload | B | — | **€0** (in S1/S2) | 4/5 |
| S11 | Emotional labor | A | — | **€0** (inherent) | 3/5 |
| **TOTAL** | | | **~€9.9M** | **~€3.1M/year** | |

> **Total addressable savings: ~€3.1M/year** on a total juriste payroll of **~€4.25M/year** (73% of payroll is involved in activities with savings potential — though not all is capturable).
>
> **Revenue upside not captured above.** Legacio's revenue model is per-file, priced per engagement. Time savings translate directly into capacity: O1 alone frees ~27,500h/year — equivalent to ~344 additional files at current throughput. The COO argument is not only "we reduce costs" but "we grow revenue at the same headcount." Capacity expansion is the stronger investment case and scales with the company's growth trajectory.

---

## Key Cross-Cutting Findings

### "C'est moi qui signe" — The Liability Anchor
This phrase, or its equivalent, appears in 10/10 juriste interviews. It is the single biggest design constraint for any AI-assisted solution: juristes will not delegate decision-making and will not trust output they cannot verify. This is professional rationality, not technology phobia. Any solution that bypasses human review before a document is sent will not be adopted — and should not be.

### The Shadow AI Paradox
Every person interviewed has already used AI with client data — and every one panicked. This means:
- The pain is high enough that juristes take active compliance risks without any organizational endorsement
- The trust in public tools is zero after the fact
- Demand for a secure, internal AI assistant is **latent, immediate, and universal**
- The barrier to adoption is not behavioral — it is infrastructure

### The Template Quality Debt Goes Beyond Time
Personal shadow template libraries mean the team produces legally inconsistent client-facing communications. Michèle (J11, mentor) flags this as a training problem: junior juristes learning from outdated templates carry forward bad habits and require rework correction. This is a compounding quality debt, not just an efficiency gap.

### The 4-Month Window Creates Permanent Crunch Mode
Unlike a single annual deadline, every juriste is simultaneously managing files at multiple stages of the 4-month window. Proactive visibility tools (file X is at day 85, document Y still missing) therefore have **disproportionate leverage**: they compress stress peaks rather than merely accelerating the final push.

---

## Signal-to-Cluster Mapping

| Cluster | Primary Signals | Urgency |
|---|---|---|
| **A — Document Collection Loop** | S1 (chasing), S11 (emotional labor) | High — volume-driven, daily grind, largest addressable cost |
| **B — Post-death Procedures** | S2 (fragmented tools, out of scope), S3 (visibility), S10 (overload) | Medium — systemic constraint acknowledged but not addressed |
| **C — Succession Declaration** | S4 (manual filling), S6 (deadline + liability), S8 (verification) | Critical — highest pain, direct legal risk, signature exposure |
| **D — Will & Heir Analysis** | S7 (Article 108) | Medium — expertise-intensive, partially addressable |
| **E — Document Production** | S5 (manual drafting) | Medium — clear savings, quality risk |
| **Cross-cutting** | S9 (shadow AI) | Strategic — adoption enabler or adoption blocker |

---

*Next step: opportunity mapping and prioritization based on this signal analysis.*
