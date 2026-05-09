# Graph Report - ./raw  (2026-05-06)

## Corpus Check
- 71 files · ~81,826 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 168 nodes · 225 edges · 10 communities detected
- Extraction: 57% EXTRACTED · 42% INFERRED · 1% AMBIGUOUS · INFERRED: 94 edges (avg confidence: 0.81)
- Token cost: 49,500 input · 12,600 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Succession Tax & Costs|Succession Tax & Costs]]
- [[_COMMUNITY_Wills & Intestate Distribution|Wills & Intestate Distribution]]
- [[_COMMUNITY_Asset Liability & Property in Succession|Asset Liability & Property in Succession]]
- [[_COMMUNITY_Child Heirs & Reserved Shares|Child Heirs & Reserved Shares]]
- [[_COMMUNITY_Advance Directives & Organ Donation|Advance Directives & Organ Donation]]
- [[_COMMUNITY_Will Registration & Succession Definition|Will Registration & Succession Definition]]
- [[_COMMUNITY_Acceptance, Refusal & Debt Liability|Acceptance, Refusal & Debt Liability]]
- [[_COMMUNITY_Post-Death Procedures & Certificate|Post-Death Procedures & Certificate]]
- [[_COMMUNITY_Declaration Filing & Notary Services|Declaration Filing & Notary Services]]
- [[_COMMUNITY_End-of-Life Declarations & Body Donation|End-of-Life Declarations & Body Donation]]

## God Nodes (most connected - your core abstractions)
1. `Testament Olographe (Holographic Will)` - 9 edges
2. `Réserve héréditaire des enfants` - 8 edges
3. `Déclaration de Succession` - 8 edges
4. `Testament Notarié (Authentique)` - 7 edges
5. `Certificat d'Hérédité` - 7 edges
6. `Déclaration de succession (Wallonie/Bruxelles)` - 6 edges
7. `Article 108 – Présomption fiscale d'actifs dessaisis` - 6 edges
8. `Testament authentique (notarié)` - 6 edges
9. `Utilité du testament en Belgique` - 6 edges
10. `Succession (Définition et Types)` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Auto-déclaration de succession` --semantically_similar_to--> `Testament olographe (fait maison)`  [INFERRED] [semantically similar]
  raw/Remplir_declaration_succession_Wallonie_Bruxelles.html → raw/Rédiger soi-même un testament _ notaire.be.html
- `Bureau de succession (alternative notaire)` --semantically_similar_to--> `Bureau de sécurité juridique (BSJ)`  [AMBIGUOUS] [semantically similar]
  raw/Remplir_declaration_succession_Wallonie_Bruxelles.html → raw/Chapitre_28_Bureau_securite_juridique.html
- `Transfert de propriété immobilière par testament` --conceptually_related_to--> `Liquidation du régime matrimonial`  [INFERRED]
  raw/Chapitre_12_Testament_immobilier.html → raw/Regime_matrimonial_succession.html
- `Conditions pour Certificat d'Hérédité Gratuit` --conceptually_related_to--> `Testament Notarié (Authentique)`  [INFERRED]
  raw/Chapitre_21_Certificat_heredite.html → raw/Le testament notarié _ notaire.be.html
- `Droits de Succession (Fiscalité)` --semantically_similar_to--> `Paiement des Droits de Succession`  [INFERRED] [semantically similar]
  raw/Definition_succession.html → raw/Chapitre_17_Succession_demarches.html

## Hyperedges (group relationships)
- **Flux procédural de la déclaration de succession belge** — regime_matrimonial_succession_liquidation_regime_matrimonial, succession_deces_parents_grands_parents_certificat_heredite, remplir_declaration_succession_wallonie_bruxelles_declaration_succession, chapitre_28_bureau_securite_juridique_bsj, chapitre_39_frais_passif_actif_net_succession [INFERRED 0.85]
- **Types de testaments et formes alternatives** — chapitre_09_testament_prix_testament_authentique, rediger_soi_meme_testament_notaire_be_testament_olographe, chapitre_13_testament_contenu_testament_en_ligne [INFERRED 0.90]
- **Système de protection des réserves héréditaires** — chapitre_22_enfants_heritiers_reserve, reserve_patrimoniale_quotite_disponible, reserve_patrimoniale_reserve_conjoint, chapitre_22_enfants_heritiers_action_en_reduction [INFERRED 0.88]
- **Processus Successoral Belge Complet** — chapitre_21_certificat_heredite_certificat_heredite, chapitre_32_etapes_succession_deblocage_comptes_bancaires, chapitre_26_declaration_succession_declaration_de_succession, chapitre_17_succession_demarches_droits_de_succession, chapitre_17_succession_demarches_division_patrimoine [EXTRACTED 0.95]
- **Options de l'Héritier face à la Succession** — acceptation_tacite_succession_acceptation_tacite, belges_refusent_heritage_renonciation_succession, chapitre_30_mineurs_heritiers_mineur_heritier [INFERRED 0.85]
- **Instruments de Planification Anticipée** — mandat_extrajudiciaire_mandat_extrajudiciaire, chapitre_02_declaration_anticipee_negative_declaration_anticipee_negative, le_testament_notarie_testament_notarie, guide_preparer_son_testament_testament_olographe [INFERRED 0.85]
- **Processus de Déclaration de Succession (Death → Certificate → Declaration → Tax Payment)** — guide_succession_apres_deces_certificat_heredite, declaration_succession_notairebe_official_declaration, chapitre_24_couts_succession_droits_succession, temps_notaire_succession_legal_deadlines [EXTRACTED 0.90]
- **Cadre de Répartition de l'Héritage (Reserve, Quotité, Ordre, Héritiers Réservataires)** — chapitre_27_repartition_heritage_reserve_legale, chapitre_27_repartition_heritage_quotite_disponible, chapitre_27_repartition_heritage_ordre_succession, chapitre_27_repartition_heritage_heritiers_reservataires [EXTRACTED 0.95]
- **Déclarations de Fin de Vie (Advance Directives, Organ Donation, Body Donation, Euthanasia)** — guide_anticiper_declarations_volonte_advance_directives, guide_anticiper_declarations_volonte_organ_donation, chapitre_05_don_corps_science_body_donation, guide_anticiper_declarations_volonte_euthanasia_declaration [EXTRACTED 0.90]

## Communities

### Community 0 - "Succession Tax & Costs"
Cohesion: 0.1
Nodes (28): Réduction pour Double Héritage (50% Reduction for Assets Inherited Twice in a Year), Allègement pour Entreprises Familiales (Family Business Relief), Abattements Successoraux (Succession Tax Allowances), Droits de Succession (Succession Tax - Primary Cost), Frais Funéraires (Funeral Costs in Succession), Coûts Totaux d'une Succession (avg. €10,000), Calcul des Frais de Notaire (% of Gross Assets, Case-by-Case), Alternative Legacio aux Frais de Notaire (Fixed Transparent Pricing) (+20 more)

### Community 1 - "Wills & Intestate Distribution"
Cohesion: 0.13
Nodes (22): Personnes Exclues sans Testament (Unmarried Partners, Stepchildren, Friends), Cinq Principes de Dévolution Légale (Ligne, Ordre, Degré, Substitution, Fente), Succession Sans Testament (Intestate Succession - Dévolution Légale), Codicille (Testament Amendment), Testament Olographe (Holographic Will), Types de Legs (Universel, Titre Universel, Particulier), Registre Central des Testaments, Holographic Will Validity Requirements (+14 more)

### Community 2 - "Asset Liability & Property in Succession"
Cohesion: 0.14
Nodes (18): Délai de présomption 3 ans (5 ans Wallonie), Documentation pour contrer l'article 108, Article 108 – Présomption fiscale d'actifs dessaisis, Acceptation sous bénéfice d'inventaire, Assurance-vie (protection paiement hypothèque), Hypothèque héritée par les héritiers, Transfert de propriété immobilière par testament, Bureau de sécurité juridique (BSJ) (+10 more)

### Community 3 - "Child Heirs & Reserved Shares"
Cohesion: 0.14
Nodes (18): Action en réduction (récupération réserve), Indignité successorale, Nue-propriété des enfants (conjoint survivant), Réserve héréditaire des enfants, Succession légale (sans testament), Donation (planification successorale), Donation-partage, Donation avec réserve d'usufruit (+10 more)

### Community 4 - "Advance Directives & Organ Donation"
Cohesion: 0.14
Nodes (18): Déclarations de volonté anticipées, Don du corps à la science, Préférences funéraires (déclaration anticipée), Coma irréversible (déclencheur euthanasie), Déclaration anticipée d'euthanasie, Témoins requis (déclaration euthanasie), Consentement présumé au don d'organes (Belgique), Déclaration de don d'organes (+10 more)

### Community 5 - "Will Registration & Succession Definition"
Cohesion: 0.15
Nodes (16): Enregistrement au Registre Central des Testaments, Stockage Physique Sécurisé du Testament, Événements de Vie Nécessitant Révision Testament, Mise à Jour du Testament, Droits de Succession (Fiscalité), Succession (Définition et Types), Succession Internationale, Succession Légale (ab intestat) (+8 more)

### Community 6 - "Acceptance, Refusal & Debt Liability"
Cohesion: 0.14
Nodes (16): Acceptation Tacite de Succession, Actes Constitutifs d'Acceptation Tacite, Responsabilité des Dettes du Défunt, Refus d'Héritage pour Limiter les Dettes, Renonciation à la Succession, Déclaration Anticipée Négative (Refus de Soins), Représentant Désigné (Déclaration Anticipée), Désignation d'un Tuteur dans le Testament (+8 more)

### Community 7 - "Post-Death Procedures & Certificate"
Cohesion: 0.17
Nodes (15): Gel des Comptes Bancaires au Décès, Ouverture de la Succession, Conditions pour Certificat d'Hérédité Gratuit, Certificat d'Hérédité, Portail MyMinfin (Demande Certificat en Ligne), Formalités Administratives Post-Décès, Gestion des Contrats et Abonnements, Gestion des Véhicules après Décès (+7 more)

### Community 8 - "Declaration Filing & Notary Services"
Cohesion: 0.22
Nodes (10): Division du Patrimoine Successoral, Paiement des Droits de Succession, Risques d'Erreurs dans la Déclaration de Succession, Succession Sans Notaire (DIY), Tarification des Services Notariaux, Bureau de Sécurité Juridique, Déclaration de Succession, Délais de Dépôt de la Déclaration de Succession (+2 more)

### Community 9 - "End-of-Life Declarations & Body Donation"
Cohesion: 0.38
Nodes (7): Don du Corps à la Science (Body Donation to Science), Conditions for University Refusal of Body Donation, University Body Donation Procedure (Belgium), Déclarations Anticipées de Volonté (Advance Directives), Déclaration d'Euthanasie (Euthanasia Declaration), Déclaration Anticipée Négative (Refusal of Life-Prolonging Treatment), Déclaration de Don d'Organes (Organ Donation Declaration)

## Ambiguous Edges - Review These
- `Bureau de succession (alternative notaire)` → `Bureau de sécurité juridique (BSJ)`  [AMBIGUOUS]
  raw/Remplir_declaration_succession_Wallonie_Bruxelles.html · relation: semantically_similar_to
- `Saut de Génération (Generation Skipping Inheritance)` → `Réduction pour Double Héritage (50% Reduction for Assets Inherited Twice in a Year)`  [AMBIGUOUS]
  raw/Abattements_succession.html · relation: conceptually_related_to

## Knowledge Gaps
- **41 isolated node(s):** `Pénalités pour fraude fiscale successorale`, `Indignité successorale`, `Donation-partage`, `Réforme successorale 2017 (réserve 50%)`, `Documentation pour contrer l'article 108` (+36 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Bureau de succession (alternative notaire)` and `Bureau de sécurité juridique (BSJ)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Saut de Génération (Generation Skipping Inheritance)` and `Réduction pour Double Héritage (50% Reduction for Assets Inherited Twice in a Year)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Testament Olographe (Holographic Will)` connect `Wills & Intestate Distribution` to `End-of-Life Declarations & Body Donation`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `Héritier vs Légataire (Heir vs Legatee Distinction)` connect `Wills & Intestate Distribution` to `Succession Tax & Costs`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `Déclaration de succession (Wallonie/Bruxelles)` connect `Asset Liability & Property in Succession` to `Child Heirs & Reserved Shares`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Testament Olographe (Holographic Will)` (e.g. with `Succession Sans Testament (Intestate Succession - Dévolution Légale)` and `Quotité Disponible (Discretionary Share)`) actually correct?**
  _`Testament Olographe (Holographic Will)` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Réserve héréditaire des enfants` (e.g. with `Donation (planification successorale)` and `Petits-enfants héritiers (décès parents)`) actually correct?**
  _`Réserve héréditaire des enfants` has 2 INFERRED edges - model-reasoned connections that need verification._