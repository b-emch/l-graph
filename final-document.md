# Legacio × AI — Discovery to Execution : A PM Case Study

> **Note de cadrage :** Ce document est un artefact illustratif. Il démontre la méthodologie que j'aurais appliquée si j'avais rejoint Legacio avant le lancement de toute initiative AI. Les données (temps, volumes, coûts) sont des hypothèses étayées, destinées à valider en interviews. Le panel doit lire ce document comme : *« voici exactement comment j'aurais structuré cette découverte, et pourquoi elle aurait produit un résultat plus ciblé. »*

---

## 1 — Reframing du problème

### Ce que ce cas n'est pas

Ce cas n'est pas « comment ajouter de l'IA ». C'est **comment éviter de reproduire une initiative qui n'a pas tenu ses promesses faute de discovery rigoureuse.**

La pression compétitive est réelle. L'IA est déjà en production chez des acteurs comparables (Fednot × ML6 : 40% de réduction du temps de déclaration, 15 min économisées par dossier, déployé dans 1 600 études notariales belges). La question n'est donc pas *si* — c'est *quoi*, *pour qui*, et *dans quel ordre*.

### Posture PM

| Dimension | Ce que ça implique |
|---|---|
| **Juriste-first** | Les juristes sont la source de vérité. Leur quotidien prime sur les hypothèses managériales. |
| **Diagnostic, pas prescriptif** | Je n'arrive pas avec une solution. J'arrive avec des questions et une méthode. |
| **Cadré côté business** | Chaque opportunité se traduit en coût annuel du statu quo et en potentiel de libération de capacité. |
| **Honnête sur les risques** | RGPD, secret professionnel notarial belge, EU AI Act — ces contraintes sont nommées dès le départ, pas découvertes en production. |

### JTBD — Le juriste

> *"Quand je gère simultanément plusieurs dossiers de succession complexes, je veux trouver rapidement la bonne information, produire des sorties standard conformes sans repartir de zéro, et détecter les erreurs avant qu'elles s'aggravent — pour concentrer mon expertise sur les dossiers qui nécessitent vraiment un jugement juridique."*

### Tensions à naviguer

| Tension | Réponse |
|---|---|
| **Vitesse vs. rigueur** | Un sprint time-boxé de 4 semaines donne le même signal d'urgence que "aller vite" — sans reproduire l'échec de bâtir sans savoir quoi construire. |
| **Empathie juristes vs. cadrage exécutif** | Les juristes sont la source de discovery ; les exécutifs sont les décideurs. Les deux besoins sont adressés, pas choisis. |
| **Métriques inconnues** | La discovery ne collecte pas des métriques — elle les *crée*. Pas de données de départ = première tâche de la semaine 1. |

---

## 2 — Méthode de discovery

### Charter de discovery

> **Mission :** Produire une shortlist d'opportunités AI classées et étayées par des preuves, qui réduisent directement la friction dans les workflows des juristes — ancrées dans des pertes de temps mesurées et une volonté d'adoption exprimée — pour que le prochain investissement soit ciblé, pas exploratoire.

**In-scope :** workflows juristes (succession), 30 juristes, ops/management comme sources de métriques business, équipe dev pour contexte technique.

**Out-of-scope :** rédaction de testaments (15% du CA, workflows distincts), interfaces client directes, workflows hors Legacio.

**Critère de succès :** ≥3 bottlenecks confirmés · modèle d'impact économique populé · shortlist de 3–5 opportunités avec estimation ROI et score d'adoption.

---

### Cartographie des parties prenantes

| Tier | Qui | Ce qu'ils apportent |
|---|---|---|
| **1 — Juristes seniors** | Dossiers complexes, multi-parties | Bottlenecks les plus durs ; voix la plus crédible sur la confiance AI |
| **1 — Juristes juniors** | Volume élevé, saisie + rédaction | Friction répétitive ; plus ouverts aux nouveaux outils |
| **1 — Spécialistes succession** | Déclaration BSJ, actif/passif | Exposition maximale à la boucle de collecte et à la déclaration |
| **2 — COO** | Volume, trajectoire, coût horaire | Définition du succès, budget, contexte de l'initiative AI |
| **2 — Chef d'équipe** | Où se concentrent les erreurs, signaux de surcharge | Observations informelles sur la réalité terrain |
| **3 — Tech Lead** | Outils actuels, structure des données, contraintes techniques | Murs invisibles à ne pas découvrir en production |

---

### Méthodes de collecte — Semaine 1

| Méthode | Qui | Durée | Objectif |
|---|---|---|---|
| **Shadow observation** | 2–3 juristes | 90–120 min / session | Voir ce que les interviews ne diront pas : automatismes, outils informels, copy-paste silencieux |
| **Interviews 1:1** | 15–20 juristes + 2 management + 1 dev | 30 min | Cartographier les douleurs, estimer les temps, sonder le sentiment AI |
| **Time-diary** | 5 juristes (mix senior/junior) | 3 jours consécutifs | Valider les estimations d'interviews avec des données comportementales |
| **Friction log async** | 30 juristes | 5 min/semaine | Capter les signaux des juristes qui ne parleront pas en 1:1 |

---

### Mesure de la baseline — Indispensable avant tout build

> **Principe :** Sans baseline, il est impossible de prouver que l'AI a fonctionné. La discovery ne se contente pas de collecter des douleurs — elle crée les métriques qui serviront à mesurer le succès du pilote.

**Métriques à collecter en Semaine 1 :**

| Métrique | Cluster | Comment la mesurer |
|---|---|---|
| Nb de cycles de relance / dossier | A — Collecte documents | Interview estimation + time-diary |
| Temps total de chasing / dossier (h) | A | Time-diary + shadow session |
| Temps d'extraction manuelle / déclaration (h) | C — Déclaration | Interview + shadow session |
| Temps de vérification pré-soumission (h) | C | Interview estimation |
| Nb de lettres / courriels rédigés / dossier | E — Production | Shadow session |
| Temps moyen de rédaction / lettre (min) | E | Time-diary |

Ces mêmes métriques deviennent les **critères de succès du pilote** en Étape 6. Si le pilote ne les déplace pas, le produit n'a pas fonctionné.

---

### Sprint de 4 semaines

| Semaine | Focus | Activités clés | Livrable |
|---|---|---|---|
| **S1** | Collecte + baseline | Shadow (J1–3), interviews (J3–5), time-diary lancé, friction log ouvert, **métriques baseline enregistrées** | Notes brutes Notion ; diaries actifs ; baseline documentée |
| **S2** | Synthèse | Affinity mapping, confirmation des bottlenecks (3 gates), compilation métriques | Taxonomie des douleurs ; liste bottlenecks confirmés |
| **S3** | Qualification | Cartes d'opportunités, modèle économique populé, cartes hypothèse rédigées | 3–5 opportunités classées avec ROI estimé |
| **S4** | Readout | Présentation COO + Head of Tech, go/no-go, brief Phase 4 | Deck readout ; liste opportunités ; brief build |

**Engagement COO :** *"Nous aurons une liste d'opportunités classées et une recommandation go/no-go dans 4 semaines. Démarrer sans use case validé, c'est reproduire exactement le problème que nous essayons de résoudre."*

---

### Gates de confirmation bottleneck

| Gate | Question | Seuil |
|---|---|---|
| **G1 — Breadth** | Cité par assez de personnes ? | >50% des interviewés |
| **G2 — Magnitude** | Impact temps/cycle matériel ? | >1h/dossier OU >30% des dossiers affectés |
| **G3 — Universalité** | Présent senior ET junior ? | Les deux groupes confirment |

Seuls les bottlenecks passant les 3 gates entrent en qualification d'opportunités.

---

### Signaux de pivot

| Signal | Ce que ça signifie | Réponse |
|---|---|---|
| Juristes citent des douleurs différentes des hypothèses management | La perception informelle était une projection | Re-scoper autour des vraies douleurs ; informer le COO |
| Time-diary : tâches <10 min chacune | ROI automatisation ne justifie pas un build AI | Rebasculer vers amélioration UX/process |
| Sentiment AI universellement négatif | L'adoption est un prérequis à l'impact | Prioriser le travail de confiance avant tout build |
| Data trop non-structurée pour extraction fiable | Foundation technique inexistante | Recommander structuration des données en précondition |
| EU AI Act : classification high-risk confirmée sur cluster C/D | Assessment de conformité obligatoire avant pilote | Escalader au COO ; intégrer la timeline compliance dans le brief Phase 4 |

---

## 3 — Guide d'entretien

### Template A — Juriste (30 min)

**Ouverture (2 min)**
> *"Je suis là pour comprendre votre travail, pas pour vous évaluer ni vendre un outil. Il n'y a pas de bonnes réponses. Tout ce que vous partagez reste dans le processus de discovery."*

**Section 1 — Warm-up (5 min)**
- Décrivez-moi une semaine type. À quoi ressemblait votre lundi dernier ?
- Quel est le dernier dossier complexe que vous avez clôturé ? Qu'est-ce qui l'a rendu difficile ?

**Section 2 — Cartographie workflow (8 min)**
- Décrivez un dossier depuis son ouverture jusqu'à sa clôture. Où a-t-il tendance à se bloquer ?
- Quand vous ouvrez un nouveau dossier, quels documents avez-vous besoin ? Vous les avez tous au premier contact ?
- Que se passe-t-il quand il manque quelque chose ? Walk me through les étapes.
- Combien de fois, en moyenne, devez-vous relancer la famille avant que le dossier soit complet ?

**Section 3 — Surfacing des douleurs (7 min)**
- Où perdez-vous le plus de temps dans une semaine ?
- Quelle tâche redoutez-vous le plus ? Pourquoi ?
- Quel outil utilisez-vous le plus ? Lequel vous frustre le plus ?
- Qu'est-ce que vous copiez-collez ou ressaisissez le plus souvent ?
- Pour vos 2–3 tâches les plus longues : combien de temps prennent-elles un bon jour ? Un mauvais jour ?

**Section 4 — Estimation du temps (3 min)**
- Combien de dossiers gérez-vous simultanément en ce moment ?
- Pour vos tâches les plus chronophages, pouvez-vous estimer le temps ?

**Section 5 — Sonde sentiment AI (5 min)**

> ⚠️ **Note interviewer :** Diagnostic de confiance, pas liste de souhaits. Écouter : peur de la vie privée, peur d'erreurs légales causées par l'AI, méfiance des sorties opaques, peur d'être tenu responsable des erreurs de l'AI.

- Quand vous pensez à l'AI utilisée sur des dossiers clients — données familiales très personnelles — qu'est-ce qui vous vient à l'esprit ?
- Qu'est-ce qui vous préoccuperait le plus dans un assistant AI sur votre workflow ?
- Qu'est-ce qu'il faudrait pour que vous fassiez confiance à un tel outil ?
- S'il y avait une tâche où vous seriez à l'aise avec une aide AI — laquelle serait-ce ?

---

### Template B — Management / COO (30 min)

**Volume & coût**
- Combien de dossiers l'équipe gère-t-elle par an ? Trajectoire de croissance ?
- Quel est le coût plein d'une heure juriste (salaire + charges) ?
- Combien de dossiers un juriste typique gère-t-il simultanément ?

**Qualité & signaux de friction**
- Où les erreurs ou plaintes se concentrent-elles dans le workflow actuel ?
- Avez-vous vu des retards ou quasi-ratés sur des délais légaux ? Causes ?
- Quelle est votre plus grande crainte concernant la trajectoire de charge actuelle de l'équipe ?

**Ambition AI**
- Qu'est-ce que "l'AI qui fonctionne" ressemblerait pour cette équipe dans 12 mois ?
- Qu'est-ce qui vous rendrait assez confiant pour engager un budget de production sur un projet AI ?

---

### Template C — Dev team (30 min)

> *"Je ne suis pas là pour scoper un build. Je suis en discovery. Je veux comprendre le paysage technique pour éviter de construire une roadmap qui heurte des murs invisibles."*

**Outillage actuel :** Quels systèmes les juristes utilisent-ils ? Lesquels se parlent ? Lesquels nécessitent transfert manuel ?

**Disponibilité des données :** Où les données structurées existent-elles ? Quelle proportion de l'information est dans des PDFs non-structurés ? Types de documents dans un dossier type ?

**Murs techniques :** Si on construisait un outil AI touchant les dossiers juristes, quels sont les 2–3 premiers murs que l'on heurterait ? Contraintes RGPD / secret professionnel ? Intégrations exploitables vs. à construire ?

---

### Grille d'observation (shadow session)

À logger silencieusement — sans questions pendant la session :
- Changements d'outil : quelle app → quelle app, fréquence
- Moments d'hésitation : re-lecture, scroll, recherche
- Actions copy-paste / ressaisie : quoi, d'où, vers où
- Formats documents rencontrés : PDF natif / scan / formulaire manuscrit
- Workarounds informels : post-it, Excel perso, templates personnels

---

## 4 — Carte des opportunités AI

### Les 5 clusters de workflow

```
[Dossier ouvert]
     │
     ▼
┌──────────────────────────────────────────────┐
│  CLUSTER A — Boucle collecte documents       │  ← NON-LINÉAIRE, se répète
│  Demande → Vérification → Relance → Recheck  │
└──────────────────────────────────────────────┘
     │  (une fois complet)
     ▼
[Cluster B] Procédures post-décès & Certificat
     │
     ▼
[Cluster C] Déclaration de Succession (BSJ)
     │
     ▼
[Cluster D] Analyse testament & héritiers
     │
     ▼
[Cluster E] Production documents (lettres, formulaires)
     │
     ▼
[Dossier clôturé]
```

---

### Matrice des signaux

| # | Signal | % juristes | Cluster | Douleur | Éco. annuel actuel | Savings potentiels |
|---|---|---|---|---|---|---|
| S1 | Boucle de chasing documents | **100%** | A | 4/5 | €7.7M | **€1.9M** |
| S2 | Outils fragmentés *(contrainte technique, hors scope)* | 100% | B | 4/5 | €850K | €0 |
| S3 | Pas de visibilité temps réel | 100% | B | 4/5 | — | €0 (dans S1) |
| S4 | Déclaration — saisie manuelle & extraction PDF | **100%** | C | **5/5** | €770K | **€385K** |
| S5 | Rédaction communications — templates inutilisables | 100% | E | 3/5 | €673K | **€471K** |
| S6 | Deadline 4 mois + responsabilité personnelle | 100% | C | **5/5** | — | €0 (amplificateur de risque) |
| S7 | Article 108 — complexité & résistance famille | 90% | D | 3/5 | €173K | **€80K** |
| S8 | Anxiété de vérification pré-soumission | 90% | C | 4/5 | €481K | **€240K** |
| S9 | Usage shadow AI + peur données privées | **100%** (12/12) | Transversal | 4/5 | — | Risque RGPD actif |

> **"C'est moi qui signe."** Cette phrase — ou son équivalent — apparaît dans 10/10 interviews juristes. C'est la contrainte de design non-négociable : toute sortie AI est advisory. Validation humaine obligatoire avant envoi ou dépôt.

---

### Cartes d'opportunités

> ### O6 — Workspace AI sécurisé (infrastructure)
>
> **Tâche concernée :** *"J'ai utilisé ChatGPT pour rédiger un brouillon de lettre. Après, j'ai paniqué."* — 12/12 interviewés, non-sollicité
>
> **Fréquence :** Continu — infrastructure
>
> **Volume estimé :** 34 juristes × 2 750 dossiers/an · 100% du personnel
>
> **Temps perdu estimé :** €0 direct · risque de conformité actif et non-mitigé
>
> **Niveau de douleur exprimée :** 4/5 (exposition compliance active — 12 personnes ont déjà envoyé des données client PII vers des serveurs externes)
>
> **Type de tâche IA :** Plateforme — déploiement LLM privé + isolation des données + audit logging
>
> **Complexité technique estimée :** Élevée (déploiement cloud privé ou on-prem, SSO, logging par requête, politique de rétention RGPD + secret notarial)
>
> **Risque métier / juridique :** Faible une fois déployé · Élimine le risque RGPD actif
>
> **Signal de validation disponible :** Aveux spontanés en interview (12/12) · Aucun juriste n'a signalé l'incident — risque silencieux
>
> **→ Prérequis. O1–O4 ne peuvent pas être déployés de façon conforme sans cette couche.**

---

> ### O1 — Détection des lacunes documentaires & vérification de complétude
>
> **Tâche concernée :** *"Je dois garder un état mental de chaque dossier. C'est dans ma tête. Pas dans les outils."* — Carole (J2)
>
> **Fréquence :** Quotidien — continu sur tous les dossiers actifs sur la fenêtre de 4 mois
>
> **Volume estimé :** 34 juristes × 2 750 dossiers/an · 3–5 cycles de relance/dossier en moyenne
>
> **Temps perdu estimé :** 30–50h de chasing total / dossier (fourchette interviews : J6 = "30–40h", J5 = "50h") · ~3,5h/jour/juriste
>
> **Niveau de douleur exprimée :** 4/5 · *"Boucle infernale."* — Marc (COO)
>
> **Type de tâche IA :** Extraction (parse documents DMS) + Vérification (cross-check vs. checklist dynamique par type de dossier)
>
> **Complexité technique estimée :** Moyenne · Risque OCR sur documents manuscrits/scannés à valider avec Thomas
>
> **Risque métier / juridique :** Faible–Moyen · Fausses alertes = relances inutiles ; documents incomplets non-détectés = risque déclaration · *Hallucinations :* tout item flaggé sous le seuil de confiance du modèle s'affiche en "à vérifier" — jamais confirmé silencieusement absent ; le juriste conserve l'override manuel.
>
> **Signal de validation disponible :** Logs DMS (historique de réception) · Emails de relance dans Outlook · Time-diaries baseline Semaine 1
>
> **→ Phase B · Savings : ~€1.9M/an · Impact 4.7/5 · Alimente O3**

---

> ### O3 — Assistant de rédaction des communications
>
> **Tâche concernée :** *"Je prends un template, je l'ouvre, et je réécris à peu près entièrement."* — Sophie (J1)
>
> **Fréquence :** 6–8 lettres/emails par dossier · ~20 000 lettres/an
>
> **Volume estimé :** 34 juristes × 2 750 dossiers/an × 7 lettres moyennes
>
> **Temps perdu estimé :** 3–4h/dossier en rédaction (70–80% de réécriture de templates obsolètes)
>
> **Niveau de douleur exprimée :** 3/5 · Workaround existant (templates perso) mais lui-même source de dette qualité
>
> **Type de tâche IA :** Génération — LLM génère un brouillon depuis le contexte structuré du dossier (CRM + vue lacunes O1)
>
> **Complexité technique estimée :** Faible–Moyenne · Génération LLM standard + injection CRM + données O1
>
> **Risque métier / juridique :** Faible · Lettres = communications, pas décisions légales · Validation humaine obligatoire · *Hallucinations :* tout brouillon contenant un champ non-résolu (prénom manquant, montant absent) est flaggé en surbrillance avant présentation au juriste — jamais envoyé en l'état.
>
> **Signal de validation disponible :** Exemples de lettres existantes (shadow session) · Templates actuels du CRM · Validation par Michèle (J11, mentor qualité)
>
> **→ Phase B (après O1 en prod) · Savings : ~€471K/an · Redirige l'usage shadow AI vers infrastructure conforme**

---

> ### O4 Phase 1 — Copilote de vérification pré-soumission
>
> **Tâche concernée :** *"Je dois lire, relire, vérifier les listes mentalement. C'est dur psychologiquement parce que je sais qu'une erreur, c'est mauvais."* — Carole (J2)
>
> **Fréquence :** Une fois par dossier — moment le plus critique du workflow
>
> **Volume estimé :** 34 juristes × 2 750 dossiers/an · 90% des juristes concernés
>
> **Temps perdu estimé :** 1–4h/dossier (simple : 1h, complexe : 3–4h) · ~2,5h en moyenne
>
> **Niveau de douleur exprimée :** 4/5 · *"Deuxième paire d'yeux."* — Valérie (J4) et plusieurs autres
>
> **Type de tâche IA :** Vérification (présence documents + cohérence Article 108 + cross-référence chiffres en Phase 3)
>
> **Complexité technique estimée :** Moyenne (Phase 1) → Moyenne–Élevée (Phase 3, requiert O2)
>
> **Risque métier / juridique :** Moyen · Risque de fausse confiance si le juriste traite un checklist vert comme définitif · EU AI Act high-risk dès Phase 2
>
> **Signal de validation disponible :** Dossiers clôturés rétrospectifs (liste de vérification vs. réalité) · Logs de soumission BSJ
>
> **→ Phase B–C · Savings Phase 1 : ~€80K/an → Phase complète : ~€320K/an**

---

> ### O2 — Extraction PDF pour la Déclaration de Succession
>
> **Tâche concernée :** *"Je dois extraire les chiffres des PDFs manuellement. C'est du travail qu'une simple OCR + extraction d'entités pourrait faire."* — Denis (J12)
>
> **Fréquence :** Une fois par dossier à l'étape déclaration (mois 3–4)
>
> **Volume estimé :** 34 juristes × 2 750 dossiers/an · 100% des juristes
>
> **Temps perdu estimé :** ~2h/dossier d'extraction mécanique (sur ~4h totales de déclaration)
>
> **Niveau de douleur exprimée :** **5/5** · La tâche la plus redoutée · Responsabilité légale directe sur la signature
>
> **Type de tâche IA :** Extraction — OCR + NER + mapping de champs structurés avec citation source par chiffre
>
> **Complexité technique estimée :** Moyenne · Formats PDF hétérogènes · Scoring de confiance par champ obligatoire · Question critique : accès API BSJ ?
>
> **Risque métier / juridique :** Moyen · Erreurs d'extraction = conséquences fiscales directes pour les héritiers · EU AI Act classification high-risk à confirmer · Validation : Fednot × ML6 (architecture identique, en production, 40% de réduction temps)
>
> **Signal de validation disponible :** Échantillon de 20 PDFs réels Legacio pour test d'extraction · Relevés bancaires, évaluations immobilières comme cas de test
>
> **→ Phase C · Savings : ~€385K/an + réduction non-quantifiée du risque légal**

---

### Priorisation

| # | Opportunité | Impact | Faisabilité | Savings/an | Risque | Phase |
|---|---|---|---|---|---|---|
| O6 | Workspace AI sécurisé | Prérequis | Élevée | — | Faible | **A — En premier** |
| O1 | Détection lacunes + complétude | **4.7/5** | 3.5/5 | €1.9M | Faible–Moyen | **B — En premier** |
| O4 Ph.1 | Vérification pré-soumission (présence) | 3.8/5 | 4.0/5 | ~€80K | Faible | B–C |
| O3 | Rédaction communications | 4.0/5 | **4.5/5** | €471K | Faible | B (après O1) |
| O2 | Extraction PDF déclaration | 4.3/5 | 3.0/5 | €385K | Moyen | C |
| O4 Ph.2–3 | Vérif. + Article 108 + chiffres | 4.0–4.3/5 | 2.5–3.0/5 | ~€320K | Moyen | C–D |

```
IMPACT ÉLEVÉ (≥4.0)
    │
    │   [O2 4.3]  [O4 Ph.2-3]          [O1 4.7]  [O3 4.0]
    │
    │   [O6 Plateforme*]
    │
    │                              [O4 Ph.1 3.8]
    │
IMPACT FAIBLE
    └─────────────────────────────────────────────────────
         FAISABILITÉ FAIBLE                FAISABILITÉ ÉLEVÉE
              2.0    2.5    3.0    3.5    4.0    4.5    5.0

  * O6 est un prérequis — position = effort de build, pas impact relatif.
```

**Séquence de build :**

```
Phase A (Semaines 0–10)
└── O6 — Infrastructure sécurisée + classification EU AI Act pour O2/O4

Phase B (Semaines 6–16, chevauchant A)
├── O1 — Détection lacunes + complétude  [highest impact, alimente O3]
└── O4 Ph.1 — Vérification présence documents  [faible complexité, valeur immédiate]

Phase B+ (après O1 en production)
└── O3 — Rédaction communications  [vue lacunes O1 + injection CRM]

Phase C (Semaines 16–28, conformité EU AI Act en parallèle)
├── O2 — Extraction PDF déclaration
└── O4 Ph.2 — Logique temporelle Article 108

Phase D (Semaines 28+, après assessment de conformité)
└── O4 Ph.3 — Cross-référence chiffres (requiert O2 en prod)
```

---

### Coût d'inférence AI — Back-of-envelope

> Le coût opérationnel AI à ce volume est négligeable. Le driver de coût est l'ingénierie (build), pas l'inférence.

**Hypothèses de calcul :**
- O1 (extraction + vérification) : 2 750 dossiers × 20 vérifications de documents × 2 000 tokens input + 300 tokens output = **~110M tokens input / 16.5M tokens output par an**
- O3 (rédaction) : 20 000 lettres × 1 500 tokens input (CRM + gap view O1 + prompt) × 700 tokens output = **~30M tokens input / 14M tokens output par an**

**Option 1 — API cloud fournisseur (path le plus rapide)**

| Fournisseur | Modèle O1 (extraction) | Modèle O3 (rédaction) | Coût O1/an | Coût O3/an | Total/an |
|---|---|---|---|---|---|
| **Anthropic** | Claude Haiku 4.5 ($1/1M in · $5/1M out) | Claude Sonnet 4.6 ($3/1M in · $15/1M out) | ~$193 | ~$300 | **~€460** |
| **OpenAI** | GPT-4o-mini ($0.15/1M in · $0.60/1M out) | GPT-4o ($2.50/1M in · $10/1M out) | ~$26 | ~$215 | **~€230** |
| **Google** | Gemini 2.5 Flash ($0.30/1M in · $2.50/1M out) | Gemini 3.1 Pro ($2/1M in · $12/1M out) | ~$74 | ~$228 | **~€290** |
| **Azure EU OpenAI** *(RGPD, résidence EU)* | GPT-4o EU (~$3.25/1M in · $13/1M out) | GPT-4o EU | ~$572 | ~$280 | **~€800** |

*Pricing mai 2026. Azure EU est la voie conforme la plus directe si le DPA commercial est validé — coût le plus élevé mais résidence EU garantie.*

**Option 2 — Self-hosted cloud (VM GPU privée)**

Déployer un LLM open-source (Llama 3.1 70B, Mistral Large) sur VM cloud dédiée — données hors API tier, traitement dans un périmètre contrôlé.

| Configuration | VM type (Azure) | Coût estimé/an | Modèle adapté |
|---|---|---|---|
| Standard (1× T4) | Standard_NC4as_T4_v3 | **~€3 000–4 500** (réservé 1 an) | Llama 3.1 8B — extraction O1 |
| Performance (1× A10) | Standard_NV36ads_A10_v5 | **~€5 500–8 000** (réservé 1 an) | Llama 3.1 70B — rédaction O3 |

*Justifié si : le chemin DPA cloud commercial est bloqué ou si l'équipe juridique impose que les données ne quittent pas une infra nominalement contrôlée. Coût 6–15× plus élevé qu'API — arbitrage à confirmer avec Tech Lead en Step 0.*

**Option 3 — Self-hosted on-premises**

Serveur GPU hébergé dans les locaux Legacio — zéro transit réseau externe, contrôle total des données.

| Configuration | Capex matériel | Ops/électricité/an | Coût total amorti (3 ans)/an |
|---|---|---|---|
| 2× RTX 4090 (24 GB VRAM each) | ~€6 000–9 000 | ~€5 000–8 000 | **~€7 000–11 000/an** |
| 1× NVIDIA A100 80GB | ~€25 000–40 000 | ~€8 000–12 000 | **~€17 000–25 000/an** |

*Justifié uniquement si les obligations légales (secret professionnel notarial, décision DPO) interdisent tout traitement hors locaux. À ce volume de fichiers, le ROI opérationnel ne justifie pas ce choix seul — c'est une décision de conformité, pas d'économie.*

> **Conclusion ROI :** Même avec Azure EU (option la plus chère, ~€800/an), le coût d'inférence représente **<0.03% des savings annuels (~€3.1M)**. Le vrai coût est la construction du pipeline (ingénierie), pas le run. L'argument pour repousser O1 ou O3 pour raison de coût opérationnel AI ne tient pas.

---

**Savings totaux addressables : ~€3.1M/an sur ~€4.25M de masse salariale juristes.**

> **Upside revenus (non capturé ci-dessus) :** O1 seul libère ~10h/dossier × 2 750 dossiers = 27 500h/an — soit la capacité de ~344 dossiers supplémentaires sans embauche. Le modèle de revenus Legacio étant au dossier, l'argument COO n'est pas seulement "réduire les coûts" mais "croître au même effectif".

---

## 5 — Protocole de validation pré-build

### Étape 0 — Gate technique & réglementaire *(avant tout build)*

> Cette étape est obligatoire. Découvrir la classification EU AI Act à l'Étape 6 signifie reconstruire depuis le début.

**Track A — Technique :**

| Vérification | Condition de passage |
|---|---|
| Chemin infrastructure confirmé (Azure EU OpenAI DPA ou self-hosted) | Confirmation écrite Tech Lead |
| Métadonnées DMS queryables | **BLOCKER : O1 ne peut pas être livré sans accès DMS confirmé. Si indisponible, la timeline décale de 6–8 semaines pour un travail de pipeline de données.** |
| Données CRM accessibles pour O3 | API ou export confirmé |
| % docs manuscrits/scannés entrants évalué | Calibre le choix pipeline OCR O1 |
| Build vs. buy évalué pour O2 | Si vendor couvre ≥80% formats Legacio avec résidence EU → buy accélère de 4–6 semaines |

**Track B — EU AI Act (O2 et O4) :**

Classification high-risk / limited-risk confirmée · Assessment de conformité formellement ouvert · Mécanisme de supervision humaine conçu · Architecture d'audit logging définie.

---

### Format carte hypothèse

```
Opportunité : [Nom]

Nous croyons que [action AI]
pour [persona]
pendant [étape workflow]
économisera [X heures par semaine / par dossier]
parce que [preuve issue des interviews + données temps].

Nous saurons que nous avons raison si [signal mesurable :
réduction de temps, taux d'erreur, taux d'adoption].

Risque d'adoption : [préoccupation clé du sondage sentiment AI]
Condition de confiance : [ce que les juristes ont dit les rendrait à l'aise]
Contrainte privacy : [flag si données client impliquées + mitigations]
```

---

### Étapes 1–6 résumées

| Étape | Propriétaire | Durée | Condition de passage |
|---|---|---|---|
| **0 — Gate tech & réglementaire** | Tech Lead + Legal + PM | Sem. 0–2 | Track A + B tous deux passés |
| **1 — Early adopters** | PM + Team Lead | Sem. 2–3 | 3–5 juristes identifiés (douleur top-2 + sentiment ≥3/5 + ≥25 dossiers simultanés) |
| **2 — Confirmation signal discovery** | PM | Sem. 2–3 | Signal ≥50% juristes · temps validé · douleur ≥3/5 |
| **3 — Prototype** | PM + Tech Lead | Sem. 3–6 | Plus basse fidélité possible démontrant l'action AI core |
| **4 — Qualité early-stage** | PM + Tech Lead | Sem. 6–8 | O1 ≥85% recall · O2 ≥90% précision champs · O3 ≥70% lettres "utilisables avec edits mineurs" |
| **5 — Sessions early adopters** | PM | Sem. 8–10 | Sentiment moyen ≥3.5/5 · aucun rejet catégorique |
| **6 — Pilote** | PM + Tech Lead + Team Lead | Sem. 10–14 | O6 live · RGPD actif · métriques baseline vs. pilote comparées |

**Go/No-Go à la Semaine 14 — Décideurs : COO + Head of Tech**

| Décision | Conditions |
|---|---|
| **Go** | Métrique primaire à la cible ET sentiment ≥3.5/5 ET zéro erreur non-catchée sérieuse |
| **Go conditionnel** | Métrique partiellement atteinte, erreurs catchées par review humaine, juristes veulent continuer |
| **No-go** | Métrique non-atteinte OU erreur sérieuse non-catchée OU sentiment <2.5/5 |

---

## 6 — Synthèse des décisions

### Ce que nous avons appris

- **La boucle de collecte documents est le coût caché dominant.** 40h/dossier de chasing × 2 750 dossiers = €7.7M/an de coût de statu quo. Ce chiffre n'existait pas avant la discovery — il a été *créé* par la méthode.
- **Le Shadow AI = demande latente + risque compliance actif.** Chaque personne interviewée (12/12) avait utilisé un outil AI public avec des données client, puis avait paniqué. La barrière à l'adoption n'est pas comportementale — c'est l'infrastructure.
- **"C'est moi qui signe" est la contrainte de design centrale.** Toute solution qui contourne la validation humaine avant envoi ou dépôt ne sera pas adoptée — et ne devrait pas l'être.

### Ce que nous avons choisi

O6 en prérequis · O1 en premier (impact le plus élevé, alimente O3) · O4 Phase 1 en parallèle (faible complexité, valeur immédiate) · O3 après O1 en production · O2 + O4 Ph.2–3 en Phase C–D après assessment EU AI Act.

### Ce que nous avons exclu

| Décision | Rationale |
|---|---|
| **S2 — Fragmentation outils hors roadmap** | Contrainte technique structurelle confirmée par COO et Tech Lead — pas adressable par une feature team dans la fenêtre actuelle |
| **Rédaction de testaments hors scope** | 15% du CA, workflows distincts, paysage d'opportunités séparé — mélanger les scopes diluerait la roadmap succession |
| **Pas d'AI côté client** | 10/10 juristes confirment que les familles en deuil nécessitent un accompagnement humain · Remplacer ce contact par de l'AI rejeté unanimement |

---

## 7 — Workflow AI

Ce case study a été produit de bout en bout avec assistance AI, de la familiarisation domaine jusqu'à la synthèse discovery et la carte d'opportunités.

> **Principe démontré :** L'AI prépare. Le PM décide. Pas une platitude — illustré ci-dessous.

### Tableau de synthèse

| Point de décision | Contribution AI | Jugement humain |
|---|---|---|
| Identifier Article 108 comme priorité | Graph : statut god node, 6 edges, central à 2 communautés | Décider qu'il était opérationnellement pertinent, pas seulement légalement central |
| Score sentiment AI de Sophie | Framework : profil de responsabilité → signal de résistance | Corriger 3/5 → 2/5 en captant la dimension responsabilité légale que l'AI n'avait pas pondérée |
| Exclure S2 (fragmentation outils) de la roadmap | Flaggué comme signal de douleur confirmé (10/10 occurrence) | Reclassifier en contrainte technique en attente de validation Thomas — pas une opportunité |
| Modèle économique | Modèle complet en un passage : 11 signaux, 5 clusters, ~€3.1M savings | Corriger les heures de travail, recompter les juristes, retirer Marc et Thomas du pool juristes |
| Merger O4 + pre-submit en une carte phasée | Deux cartes distinctes avec scopes séparés | Reconnaître le pipeline de données partagé → un produit phasé, pas deux |
| Placement EU AI Act en Étape 0 | Draft initial plaçait l'assessment en Étape 7 | Déplacé en Étape 0 — découvrir le statut high-risk en Étape 6 signifie reconstruire depuis le début |

### Ce que l'AI a bien fait

1. **Ancrage domaine avant les interviews.** Le knowledge graph a compressé une semaine de recherche domaine en une session et produit un finding (Article 108 god node) qui a survécu jusqu'à la carte d'opportunités finale.
2. **Scaffolding du modèle économique en un passage.** 11 signaux × 5 clusters × formule ROI produits structurellement en une itération ; les erreurs ont été catchées immédiatement en review.
3. **Cohérence des artefacts sur plusieurs sessions.** Framework de discovery → cartes personas → synthèse → opportunités → protocole de validation : la structure est restée cohérente sans reformulation à chaque étape.

### Ce que l'AI ne peut pas faire

1. **Générer de la surprise.** Les juristes simulées ont confirmé les hypothèses — elles ne pouvaient pas produire des signaux inattendus. Les vraies interviews révèlent le juriste qui utilise WhatsApp pour chaser, celui qui a imprimé un formulaire parce qu'il ne fait pas confiance au scan, l'équipe qui a construit un FAQ interne après une pénalité de €40k sur un délai manqué.
2. **Mesurer la distribution réelle.** Les taux d'occurrence (ex. S1 : 10/10 juristes) reflètent la force des hypothèses, pas la confiance statistique. Une vraie équipe de 30 juristes aurait des outliers.
3. **Interpréter le droit.** L'Article 108 a été identifié comme nœud central. Interpréter ses cas limites, variations régionales et jurisprudence récente requiert un avocat belge en droit successoral, pas un knowledge graph.

> **Ce workflow est une méthodologie PM valide :** utiliser l'AI pour être plus préparé, plus rapide, plus structuré — puis utiliser de vraies interviews pour stress-tester et se laisser surprendre.

---

*Full prompt/response log : `prompts.md` · Tous les artefacts sources : `phase-01` à `phase-03`, `discovery-synthesis.md`, `ai-workflow-retro.md`*
