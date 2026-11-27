# Alice — System Definition

**Document ID:** ALICE-SD-001  
**Version:** 1.0  
**Date:** 27 November 2026  
**Milestone:** M02  
**Status:** Proposed system definition, pending review and approval. Documentation only.  
**Dependency:** Alice Founding Constitution v1.0 (PR #1, pending merge).  

## 1. Purpose and authority

**Alice — An Adaptive, Objective-Oriented Research, Analysis and Discovery Agent.**

This document translates the agreed founding constitution into a proposed system scope, operational objectives, external boundaries, capabilities and evaluation approach. It does not authorise implementation, expenditure, changes to governance or expansion of existing engine contracts.

Controlling references:

- [Alice Founding Constitution v1.0](ALICE_FOUNDING_CONSTITUTION_V1_0.md), sections 1–12.
- [ALIS Core Boundary Register v1.0](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md), revision V1.0-R1.
- [GoDataBank Constitution](CONSTITUTION_V0_1.md) and [Agent Laws](AGENT_LAWS.md).

The existing GoDataBank policies and canonical artifact ownership remain authoritative for their current scope. Any extension requires a separately reviewed design. The term "adaptive" describes observable changes in questions, plans, tool selection and research pathways, not consciousness or autonomous model retraining.

## 2. System definition

Alice is an adaptive research coordinating agent. It transforms a question, intention, observation or hypothesis into a defined research objective, commissions appropriate research and analytical work through ALIS Core, evaluates the resulting evidence and returns findings, limitations and new possibilities.

ALIS Core is the modular, governed research execution infrastructure. GoDataBank remains an evidence repository and publication application with its own admission and publication rules. Abacus remains the analytical engine within ALIS Core. Alice does not replace any of the eight existing engines.

The proposed Research Formulation Engine (RFE) belongs to Alice's formulation layer. It is not yet an approved ninth ALIS Core engine.

## 3. Operational objectives

| ID | Objective | Expected observable outcome | Constitution reference |
| --- | --- | --- | --- |
| SD-01 | Formulate research precisely | Confirmed research specification capturing the user's intended scope, questions and exclusions | 2, 4, 7 |
| SD-02 | Select suitable methods and resources | Justified candidate sources, methods and eligible tools appropriate to the objective | 3, 4, 7 |
| SD-03 | Coordinate evidence acquisition | Relevant evidence retrieved and preserved through authorised engine contracts | 3, 5, 6 |
| SD-04 | Enable rigorous analysis | Reproducible analytical findings with methods, units, assumptions and limitations | 3, 6, 7 |
| SD-05 | Evaluate evidence and results | Explicit validity, uncertainty and objective-coverage assessment; unresolved items identified | 5, 6, 8, 9 |
| SD-06 | Discover possibilities | Clearly labelled hypotheses, ideas and opportunities with evidence links and proposed validation | 2, 3, 5 |
| SD-07 | Preserve continuity | Versioned mission state, decisions, artifact references and resumable work where authorised | 1, 7, 11 |
| SD-08 | Adapt within constraints | Revised questions or plans in response to new context or failures, without bypassing authority | 4, 9, 10, 11 |
| SD-09 | Deliver inspectable outcomes | Findings, methods, citations, limitations and status of the original objective | 6, 12 |
| SD-10 | Demonstrate utility | Measured relevance, accuracy, time, cost, usability and discovery value against baselines | 12 |

## 4. Intended users and research domains

Intended users include independent researchers, analysts, engineers, business investigators and people who have an incomplete research intention. Initial operation is for a single authorised operator; multi-user deployment is deferred.

Candidate domain profiles: scientific research, market and commercial research, political and policy analytics, economics and demographics, engineering and technology, financial research, and surveys/social research.

Domain profiles specify permitted sources, available methods, applicable constraints and output conventions. These are candidate domains, not commitments to implement every profile. Political research is analytical rather than manipulative; surveys require separately authorised recruitment and privacy protections. Primary research is a future extension.

## 5. System boundary and responsibilities

| Component | Responsibility |
| --- | --- |
| Human operator | Defines intentions, confirms objective and constraints, authorises consequential actions and reviews outputs |
| Front end | Presents domain selections, adaptive questions, selectable options, free-text input, mission review, progress and results |
| Alice | Maintains mission context, coordinates formulation and execution, evaluates progress and proposes changes within authorised scope |
| Research Formulation Engine (proposed) | Produces and revises candidate research specifications, identifies material ambiguity and proposes eligible capabilities |
| ALIS Core | Executes governed research capabilities through documented contracts |
| Domain profiles | Supply domain-specific methods and policy constraints, subject to review |
| GoDataBank | Presents approved evidence and publication packages under its existing policies |

Alice's mission-level planning is distinct from Abacus's canonical Execution Plan. Alice may request analytical work; it does not create, rewrite or approve Abacus-owned artifacts.

Existing engine responsibilities are preserved:

| Engine | Responsibility retained |
| --- | --- |
| Arya | Source proposals, Source Admission Requests and Retrieval Manifests |
| Hermes | External transport, Raw Transport Artifacts and Retrieved Evidence Packages |
| Thoth | Canonical Source Registry Entries, provenance, checksums, schema and lineage references |
| Aegis | Governance, Validation Reports, Gate Decisions and Validated Evidence Packages |
| Abacus | Canonical Execution Plans, analytical transformation, Analysis Packages and Chart-ready Datasets |
| Vyasa | Narrative Packages and Claim-to-Evidence Maps from approved inputs |
| Apollo | Rendering, Publication Packages and Publication Manifests |
| Argus | Observability, Audit Records, health and Incident Timelines |

Interface-first and single-builder principles apply. Alice consumes public contracts, never engine internals or another engine's canonical artifacts through unauthorised mutation. Source admission, evidence validation, analysis approval, synthesis approval and publication approval gates apply as prescribed by existing contracts and policy.

## 6. Operational concept

```text
Initial intention + optional domain selection
    -> Adaptive formulation loop
    -> Confirmed research specification
    -> Mission plan and capability eligibility
    -> Authorised research execution through ALIS Core
    -> Evidence / analysis / synthesis / evaluation
    -> Research outcome and proposed next inquiries

Feedback: new evidence may trigger bounded replanning.
Material changes to confirmed scope, cost or permissions return to user review.
```

### 6.1 Progressive formulation

First submission is a formulation request, not a request to conduct the full investigation. The interface may present buttons, dropdowns, radio choices, multiple selections and free-text responses. Subsequent questions depend on accumulated context; previously resolved questions are not repeated unless an inconsistency requires review.

Alice identifies material ambiguity, proposes targeted alternatives, accepts "other", "unsure", or "delegate this decision" responses, and permits users to revise prior selections. It should not force a user with an already precise objective through unnecessary stages.

Refinement stops when the objective is sufficiently actionable, constraints and material assumptions are recorded, suitable methods and candidate sources are identifiable, and the operator confirms the specification. If ambiguity persists, Alice asks for clarification, records an explicit assumption for approval, or returns a blocked formulation. It must not claim exact knowledge of the operator's intention.

Low-cost catalogue checks may support formulation if authorised. Bulk retrieval, paid requests and substantive analytical execution require the appropriate mission approval. The desired experience is seconds per interaction and seconds to a few minutes overall for ordinary formulation; latency, question count and relevance are to be measured, not assumed.

### 6.2 Tool eligibility and execution

UI selections constrain the eligible tool set; they do not grant access or execute tools directly. The backend resolves capability dependencies and intersects mission preferences with domain policy, user permissions, tool availability and execution budgets. Aegis gates and audit obligations remain mandatory as applicable. Eligible does not mean invoked. Tool input/output validation, timeout, cancellation and failure reporting are required design considerations.

Proposed modes: targeted (strict scope), exploratory (bounded adjacent discoveries), discovery (explicit cross-domain exploration). These affect relevance criteria, not permissions. Manual, assisted and delegated methodology selection are candidate interaction modes.

### 6.3 Mission state and termination

Proposed lifecycle: DRAFT -> REFINING -> READY_FOR_REVIEW -> AUTHORISED -> RUNNING -> EVALUATING -> COMPLETED / PARTIAL / BLOCKED / CANCELLED / FAILED. A material scope revision creates a new version requiring approval. Every mission has a termination condition, execution limits and an explicit outcome status. No unrestricted background activity or self-assigned goals.

## 7. Conceptual research specification

The RFE should produce a versioned structured artifact containing:

| Field group | Contents |
| --- | --- |
| Identity | Mission identifier, version, operator identity reference |
| Intent | Original query, selected domain(s), refined objective and research questions |
| Scope | Subject, population/geography where relevant, period, inclusion/exclusion criteria |
| Method | Candidate evidence sources, research methods, required capabilities, assumptions |
| Output | Deliverable format, audience, success criteria |
| Governance | Policy reference, permitted actions, time/cost limits, approval status |
| Trace | Refinement history, unresolved uncertainties, parent version reference |

The exact schema, canonical ownership, state transitions, engine interfaces and persistence strategy are reserved for the SRS and RFE specification. This artifact is not the existing Abacus Execution Plan or Arya Retrieval Manifest.

## 8. Evidence and discovery policy

Outputs distinguish established evidence, analytical findings, reasoned inference, hypotheses, predictions, generated ideas and unknowns. A plausible hypothesis is not a verified conclusion. Correlation is not sufficient to establish causation; forecasts state their assumptions and uncertainty. In exploratory research, generated ideas are explicitly labelled, with counterevidence and tests where relevant.

No candidate domain profile relaxes GoDataBank's source-admission and publication policies. Wider research source policies must be separately defined and approved; exploratory material cannot silently enter a GoDataBank publication. An admitted source is not automatically correct, and a citation alone is not proof of claim support.

## 9. Constraints and exclusions

- No unrestricted autonomous spending, public publication, communications, physical control, arbitrary code execution or self-modification.
- No assumption of consciousness, subjective experience or general intelligence.
- No foundation-model training or new hardware purchase required for the initial prototype.
- No provider, framework, API vendor or library is selected by this system definition.
- No new policy, engine interface or implementation is approved by this document.
- Personal or sensitive data, survey collection and external transfers require explicit governance and authorisation.
- Failure or insufficient evidence is a legitimate research outcome; partial results must not be presented as complete.

## 10. Initial reference mission and evaluation

Proposed first demonstrator: an exploratory question such as "What opportunities exist in AI-assisted manufacturing?" Refine it through user-driven selections (sector, region, enterprise type, constraints, desired evidence and output), produce a confirmed specification and determine candidate capabilities. The first demonstrator may use simulated tools and catalogue metadata; it must not claim live research execution until that capability is implemented and verified.

Proposed verification dimensions:

| Dimension | Test approach |
| --- | --- |
| Intent fidelity | Operator compares final specification with intended objective; record omissions and corrections |
| Adaptivity | Different initial intents and responses produce appropriate different refinements; precise queries avoid redundant prompts |
| Relevance | Compare retrieval precision and coverage with a single-pass baseline using labelled evidence |
| Efficiency | Measure formulation latency, turns, abandonment, execution cost and time |
| Governance | Test disabled tools, unauthorised actions, missing approvals and gate failures; all tested prohibited actions blocked |
| Reliability | Test invalid outputs, unavailable model/tool, cancellation and checkpoint recovery |
| Traceability | Inspect mission versions, source/method references, execution and evaluation records |
| Discovery | Independently assess whether proposed ideas are relevant, distinct, plausible and testable; no invented evidence |
| Analytical validity | Compare numerical outputs with known reference cases and preserve assumptions and units |

Thresholds, datasets, acceptance tests and benchmark protocols are to be specified in M03 and subsequent verification plans. No current performance claim is made.

## 11. Development sequence and decisions pending

M03: System Requirements Specification — testable requirements and traceability.  
M04: Research Formulation Engine specification — state, schemas, dialogue policy, UI behaviour, capability selection and tests.  
M05: ALIS Core architectural evolution — gap analysis against the existing engine contracts and repository implementation.  
M06: Tool/API/library selection — driven by approved requirements and feasibility.  
M07: Bounded prototype implementation.  
M08: Verification and validation.

Open decisions: exact MVP domain, evidence policy for non-GoDataBank research, ownership of mission and formulation artifacts, eligible tool registry authority, operator approval workflow, model/provider selection, performance thresholds, privacy and deployment architecture. The local source tree and tests have not been audited in preparing this document.

## 12. Change control

This is a proposed baseline for review, dependent on adoption of the founding constitution. Approval of the document is not approval to implement or to modify existing ALIS Core governance. Future changes must identify their rationale, affected requirements, contract impact and required authorisation.
