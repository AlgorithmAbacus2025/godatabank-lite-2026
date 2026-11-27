# Alice — System Requirements Specification

**ID:** ALICE-SRS-001  
**Version:** 1.0 (proposed baseline)  
**Date:** 27 November 2026  
**Milestone:** M03  
**Status:** Pending review. Documentation only; no implementation or policy change authorised.

## 1. Authority and scope

Alice is an Adaptive, Objective-Oriented Research, Analysis and Discovery Agent. This specification derives from [System Definition v1.0](ALICE_SYSTEM_DEFINITION_V1_0.md) (M02, PR #2) and [Founding Constitution v1.0](ALICE_FOUNDING_CONSTITUTION_V1_0.md) (M01, PR #1). Both are pending repository adoption.

The [ALIS Core Boundary Register v1.0-R1](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md), [GoDataBank Constitution](CONSTITUTION_V0_1.md) and [Agent Laws](AGENT_LAWS.md) remain unchanged. Alice is a coordinating agent; RFE is a proposed formulation subsystem, not an approved ninth engine. Abacus retains ownership of the canonical Execution Plan. Other engine artifact ownership and gates remain unchanged.

"Shall" specifies a proposed mandatory requirement for the indicated release scope, not a currently implemented capability. Numerical thresholds in section 8 are provisional engineering targets requiring approval and benchmarking.

## 2. Release boundaries

- **P0 — formulation demonstrator:** single operator, local or controlled environment; progressive refinement, user confirmation, capability eligibility preview and simulated execution. No live research, publication or external side effects required.
- **P1 — bounded research prototype:** one approved domain and evidence policy, read-only approved connectors, analysis, evidence validation, synthesis, persistence and evaluation. No public release required.
- **P2 — extensions:** additional approved domain profiles, forecasting, primary survey research, scheduled monitoring and publication integration where separately authorised.

A higher phase inherits applicable lower-phase requirements. Phase labels are proposed priorities, not delivery commitments.

## 3. Functional requirements — Research Formulation Engine

Each requirement has a unique identifier, upstream System Definition objective(s), release priority and verification condition. Verification cases use controlled fixtures and explicitly approved operator intent, not the model's confidence alone.

| ID | Shall requirement | Trace | Phase | Acceptance condition |
| --- | --- | --- | --- | --- |
| RFE-001 | Accept free-text questions, intentions, observations or hypotheses, with optional domain selections. | SD-01 | P0 | Accept vague and precise inputs; reject empty input with a recoverable message. |
| RFE-002 | Treat first submission as formulation, not authorisation for full research. | SD-01,08 | P0 | No substantive retrieval or analysis tool calls on first submission. |
| RFE-003 | Identify material uncertainties in intent, scope, method and intended output. | SD-01 | P0 | On labelled ambiguous fixtures, identify unresolved material dimensions without inventing answers. |
| RFE-004 | Generate targeted questions and candidate choices based on accumulated context. | SD-01,08 | P0 | Different answers to the same initial query yield appropriately different follow-up questions. |
| RFE-005 | Support single choice, multiple choice, dropdowns and free-text responses; allow other, unsure and delegated decisions where appropriate. | SD-01 | P0 | Each supported input type updates the candidate specification correctly. |
| RFE-006 | Preserve resolved constraints and avoid asking equivalent questions again unless a conflict requires resolution. | SD-01,07 | P0 | Repeated and conflicting-input fixtures show preserved facts or an explicit conflict prompt. |
| RFE-007 | Allow editing previous choices and invalidate only dependent decisions affected by the change. | SD-01,08 | P0 | Changing geography updates dependent source candidates while retaining unaffected constraints. |
| RFE-008 | Distinguish user-supplied facts, system proposals, delegated decisions and unresolved assumptions. | SD-01,05 | P0 | All candidate fields in a fixture have attributable status; proposals are not represented as confirmed facts. |
| RFE-009 | Stop refinement when material ambiguity is resolved or accepted explicitly, a suitable methodology is identifiable and a specification is ready for review. | SD-01,02 | P0 | Precise prompts skip redundant questions; unresolved material ambiguities do not silently transition to ready. |
| RFE-010 | Provide an editable, structured mission preview before authorisation. | SD-01,09 | P0 | Preview exposes objective, questions, scope, exclusions, assumptions, methods, candidates, output and limits. |
| RFE-011 | Require explicit operator confirmation of a mission version before substantive execution. | SD-01,08 | P0 | Unconfirmed and stale-version approvals cannot start execution. |
| RFE-012 | Preserve the original query, refinement history and confirmed version. | SD-07 | P0 | A saved session can be reopened and its decisions inspected. |
| RFE-013 | Enforce bounded refinement with a review, explicit assumption, cancellation or blocked outcome if convergence fails. | SD-01,08 | P0 | Ambiguous or repetitive fixtures terminate safely under configured limits. |
| RFE-014 | Support targeted, exploratory and discovery intent without conflating scope or authority. | SD-06,08 | P0 | Exploratory adjacent topics appear separately and do not override exclusions or permissions. |
| RFE-015 | Identify candidate source categories and methodology appropriate to the confirmed objective. | SD-02 | P0 | Domain fixtures distinguish relevant from irrelevant candidates; missing capability is reported. |

## 4. Functional requirements — orchestration and execution

| ID | Shall requirement | Trace | Phase | Acceptance condition |
| --- | --- | --- | --- | --- |
| ORC-001 | Derive eligible tools from mission preferences, dependencies, available capabilities, policy, permissions and limits. | SD-02,08 | P0 | Denied or unavailable capabilities remain ineligible even if selected by the UI. |
| ORC-002 | Present candidate capabilities, exclusions and reasons before authorisation. | SD-02,09 | P0 | Preview explains why selected and rejected capabilities are classified as such. |
| ORC-003 | Separate tool eligibility, invocation and successful execution states. | SD-02,07 | P0 | Simulated runs distinguish enabled, invoked, succeeded, failed and skipped. |
| ORC-004 | Coordinate research through versioned public engine contracts without mutating other engines' canonical artifacts. | SD-03,04 | P1 | Contract and ownership tests reject invalid inputs and unauthorised artifact writes. |
| ORC-005 | Preserve Aegis authority over applicable gates and Abacus authority over canonical analytical Execution Plans. | SD-03,04,08 | P1 | Missing or failed gates block downstream operations; Alice cannot overwrite an Execution Plan. |
| ORC-006 | Validate tool inputs and outputs, enforce deadlines and bounded retries, and report failures. | SD-05,08 | P1 | Invalid schema, timeout and network error fixtures produce explicit failures or bounded recovery. |
| ORC-007 | Replan within approved scope when evidence or tool availability changes. | SD-08 | P1 | Simulated failure produces an eligible alternative or an explicit blocked result. |
| ORC-008 | Require renewed authorisation for material changes to scope, costs or permissions. | SD-08 | P1 | A modified scope or budget cannot execute using stale approval. |
| ORC-009 | Support cancellation, resource limits and explicit terminal status. | SD-07,08 | P0 | Cancellation and exhausted-budget fixtures stop further work and preserve permitted state. |
| ORC-010 | Record mission status, plan versions and checkpoints sufficient for authorised resume. | SD-07 | P1 | Restart from checkpoint does not duplicate completed side effects or bypass revalidation. |
| ORC-011 | Use a documented replaceable model interface rather than binding mission state to a provider. | SD-08,10 | P1 | Same bounded task and state schema work with two compatible test providers; differences recorded. |

## 5. Functional requirements — evidence, analysis and discovery

| ID | Shall requirement | Trace | Phase | Acceptance condition |
| --- | --- | --- | --- | --- |
| EVD-001 | Apply the approved domain evidence policy before source retrieval as required by existing contracts. | SD-03,05 | P1 | Rejected or unreviewed source fixtures cannot yield authorised retrieval manifests. |
| EVD-002 | Preserve provenance, retrieval date, source identity, versions and applicable artifact checksums through Thoth contracts. | SD-03,07 | P1 | Trace a sample output back to recorded source and input artifact identifiers. |
| EVD-003 | Require Aegis-produced Validated Evidence Packages for canonical Abacus analysis. | SD-03,04 | P1 | Raw, missing or failed-validation evidence cannot enter canonical analysis. |
| ANA-001 | Select and document suitable analytical methods, inputs, assumptions, units, definitions and caveats. | SD-04 | P1 | Reference calculation fixtures reproduce expected results with stated tolerances. |
| ANA-002 | Identify missing, incomparable or conflicting data and methodological limitations. | SD-04,05 | P1 | Incomplete or inconsistent datasets are flagged; invented values do not fill gaps. |
| ANA-003 | Distinguish descriptive, inferential, causal and predictive claims and disclose applicable assumptions. | SD-04,05 | P1 | Correlation-only fixtures do not produce unsupported causal findings. |
| SYN-001 | Produce narratives through approved synthesis interfaces with claim-to-evidence mapping. | SD-05,09 | P1 | Each factual claim is linked to supporting evidence; unsupported claims are rejected or labelled appropriately. |
| SYN-002 | Distinguish evidence, analytical findings, inference, hypothesis, prediction, generated idea and unknown. | SD-05,06 | P1 | Mixed-output fixtures preserve labels and avoid presenting hypotheses as facts. |
| DSC-001 | Generate research-relevant ideas or hypotheses when requested, identify their rationale and propose validation steps. | SD-06 | P1 | Human reviewers can inspect each idea's rationale, evidence references, uncertainties and proposed test. |
| DSC-002 | Separate adjacent discoveries from direct answers; permit user acceptance of further research as a new or revised mission. | SD-06,08 | P1 | Adjacent discovery cannot silently expand confirmed scope. |
| EVAL-001 | Compare outcome against each confirmed success criterion and report fulfilled, partial or unmet conditions. | SD-05,09 | P1 | Incomplete evidence fixtures cannot be reported as fully achieved. |
| OUT-001 | Provide an inspectable research outcome including objective, findings, methods, sources, limitations and status. | SD-09 | P1 | Report inspection confirms all mandatory fields and traceable evidence. |
| OUT-002 | Preserve existing GoDataBank publication policy, claim traceability and release gates. | SD-09 | P2 | Non-admitted evidence and unapproved publication packages cannot be promoted. |
| EXT-001 | Permit additional approved domain profiles through versioned capability and policy contracts. | SD-02,08 | P2 | A new profile can be added without weakening existing policies or mutating unrelated profile definitions. |
| EXT-002 | Require separate authorisation and privacy safeguards for primary surveys, external communications and personal data collection. | SD-03,08 | P2 | Unauthorised participant contact and personal-data export are blocked. |
| EXT-003 | Permit explicitly configured, bounded monitoring programmes with cancellation and resource controls. | SD-07,08 | P2 | No work starts without an authorised schedule and scope; cancellation prevents future runs. |

## 6. Proposed mission specification and state

Conceptual fields (exact schemas and artifact ownership deferred to M04/M05):

- Identity: mission ID, revision, operator reference, parent revision.
- Intent: original query, domain profile, refined objective, research questions.
- Scope: subjects, populations, geography, time period, inclusions and exclusions where applicable.
- Method: candidate sources, methods, capabilities, assumptions and unresolved items.
- Deliverable: type, audience, observable success criteria.
- Governance: policy version, permissions, resource limits, approval record.
- Trace: selection history, field attribution, dependency and artifact references.

Proposed states: DRAFT, REFINING, READY_FOR_REVIEW, AUTHORISED, RUNNING, EVALUATING, COMPLETED, PARTIAL, BLOCKED, CANCELLED, FAILED. A material revision invalidates prior approval and returns to review. Terminal states do not initiate new missions automatically. Exact transition table is a required M04 deliverable.

## 7. Non-functional and assurance requirements

| ID | Shall requirement | Trace | Phase | Verification |
| --- | --- | --- | --- | --- |
| NFR-001 | Enforce permissions and mandatory gates server-side independently of model output and front-end controls. | SD-08 | P0/P1 | Negative tests include forged requests, disabled tools and prompt-based override attempts. |
| NFR-002 | Treat external content and model-generated tool arguments as untrusted; prevent instruction injection from granting authority. | SD-05,08 | P1 | Adversarial document and malformed-argument tests cannot cause disallowed actions. |
| NFR-003 | Protect secrets and personal data, restrict external transfers, redact sensitive audit fields and use least privilege. | SD-07,08 | P0/P1 | Inspect logs, storage and connector configuration against approved data-handling policy. |
| NFR-004 | Use documented versioned contracts and explicit error categories. | SD-07,08 | P0/P1 | Schema compatibility and failure-path tests pass. |
| NFR-005 | Record sufficient mission events, model/tool versions and execution status for traceability while respecting privacy. | SD-07,09 | P0/P1 | Inspect audit records and reconstruct sample mission decisions. |
| NFR-006 | Provide responsive adaptive questioning and bounded execution costs. | SD-10 | P0/P1 | Benchmark against section 8 targets; report environment and distributions. |
| NFR-007 | Support reproducibility of deterministic analysis and preserve provenance of non-deterministic model outputs. | SD-04,09 | P1 | Repeat reference calculations; retain model configuration and output records without claiming identical LLM responses. |
| NFR-008 | Expose intelligible progress, error, cancellation and completion states to the operator. | SD-01,09 | P0/P1 | Usability test verifies the operator can revise, confirm, cancel and understand incomplete outcomes. |
| NFR-009 | Compare adaptive formulation against a single-pass baseline, including relevance, coverage and interaction burden. | SD-10 | P0/P1 | Publish benchmark protocol and measured results; do not claim superiority without comparison. |
| NFR-010 | Restrict scope to the smallest necessary dependencies and allow replacement of implementations behind stable interfaces. | SD-02,10 | P1 | Review dependency inventory and replacement tests; no unnecessary vendor commitments. |

## 8. Provisional measurable acceptance targets

All numerical thresholds below are proposals, not empirically established capabilities. P0 testing may use a simulated capability catalogue. P1 relevance and factual-claim tests require approved evidence fixtures. Record failures, dataset size, model/runtime, hardware, warm/cold conditions and measurement scope. No production readiness claim follows solely from these tests.

| Metric | Definition and proposed target | Phase |
| --- | --- | --- |
| Interaction latency | Submit selection to rendered next question: median <= 3 s, 95th percentile <= 10 s on an agreed test environment; exclude human response time. | P0 |
| Refinement duration | Typical ordinary interactive sessions aim for <= 120 s including human responses; report observed variation, not a hard deadline on users. | P0 |
| Refinement count | Median <= 4 follow-up rounds on an agreed ordinary-intent set; precise fixture skips redundant clarification. | P0 |
| Intent fidelity | At least 90% of labelled cases preserve all material operator constraints and exclusions at review; zero silently contradicted explicit hard constraints in the release suite. | P0 |
| Context retention | 100% of deterministic revision and preservation tests pass. | P0 |
| Authorisation safety | 100% of tested prohibited operations and stale approvals blocked; this is finite-suite evidence, not a guarantee of absolute security. | P0/P1 |
| Traceability completeness | 100% of sampled mandatory mission/tool/artifact audit fields present, subject to data minimisation. | P0/P1 |
| Relevance | Precision = relevant retrieved items / all retrieved items; recall = relevant retrieved items / relevant items in the labelled reference corpus. Proposed target: precision >= 0.80 and recall >= 0.80 in the pilot corpus; compare against single-pass baseline and report trade-offs. | P1 |
| Numerical reliability | All selected deterministic reference calculations match exact results or method-specific tolerances set before testing. | P1 |
| Claim support | 100% of factual claims in the release evaluation set have a source link and are assessed as supported by human or deterministic checks where suitable; unresolved claims excluded or marked as such. | P1 |
| Recovery | All defined timeout, failure, cancellation and checkpoint cases reach valid bounded states. | P0/P1 |
| Cost control | No execution exceeds configured permitted budget in release tests; reserve capacity or stop before a call when cost cannot be bounded. | P1 |
| Discovery quality | Review ideas on relevance, distinctness, plausibility and testability using a rubric; establish quantitative threshold after pilot rather than assume commercial value. | P1 |

## 9. Reference verification scenarios

| Case | Input or disturbance | Expected behaviour | Principal requirements |
| --- | --- | --- | --- |
| V01 | "I want to explore AI opportunities." | Adaptive questions narrow intent and present editable mission; no full retrieval. | RFE-001–005,009–011 |
| V02 | Same prompt, choose scientific rather than commercial research. | Different relevant follow-ups, sources and methods. | RFE-004,015 |
| V03 | Precise objective with geography, period, constraints and output supplied. | Skip redundant questions; offer review. | RFE-006,009 |
| V04 | Revise Wales to UK after selection; keep cost ceiling. | Dependent selections change; cost ceiling persists. | RFE-007,008,012 |
| V05 | Select a disabled survey-distribution capability. | Capability remains ineligible; reason displayed. | ORC-001–003,NFR-001 |
| V06 | Attempt execution with an unconfirmed or obsolete version. | No execution; review required. | RFE-011,ORC-008 |
| V07 | Inject instructions through retrieved source or model output. | Ignore authority escalation and reject prohibited operations. | NFR-001,002 |
| V08 | Reject source or fail evidence-validation gate. | No canonical downstream analysis. | EVD-001,003,ORC-005 |
| V09 | Missing data, inconsistent units or correlation-only evidence. | Explicit limitation; no invented or causal conclusion. | ANA-001–003 |
| V10 | Timeout, tool failure, cancellation or depleted budget. | Bounded retry, alternative or valid terminal state. | ORC-006–010 |
| V11 | Validated dataset with known analytical result. | Reproduce result and trace methods and evidence. | ANA-001,EVD-002,SYN-001,NFR-007 |
| V12 | Model generates an appealing but untested business idea. | Hypothesis label, rationale, counterevidence and test proposal. | SYN-002,DSC-001,002 |
| V13 | Material success criterion unfulfilled. | Partial or blocked outcome, not false completion. | EVAL-001,OUT-001 |
| V14 | Attempt non-admitted public publication or unauthorised survey action. | Reject; preserve existing policies. | OUT-002,EXT-002 |
| V15 | Resume saved session and switch compatible model implementation. | Preserve authorised state and contract compatibility. | ORC-010,011 |
| V16 | Compare adaptive and single-pass runs on matched corpus and intents. | Measure precision, recall, latency, turns and corrections; disclose uncertainty. | NFR-006,009 |

## 10. Traceability and development gates

| System objective | Principal requirements |
| --- | --- |
| SD-01 | RFE-001–014, NFR-008 |
| SD-02 | RFE-015, ORC-001–003, EXT-001 |
| SD-03 | ORC-004,005, EVD-001–003 |
| SD-04 | ANA-001–003, NFR-007 |
| SD-05 | EVD-001,003, SYN-001,002, EVAL-001 |
| SD-06 | DSC-001,002, RFE-014 |
| SD-07 | RFE-012, ORC-009,010, NFR-005 |
| SD-08 | RFE-007,013, ORC-005–011, NFR-001,002 |
| SD-09 | SYN-001, EVAL-001, OUT-001,002 |
| SD-10 | NFR-006,009,010 and section 8 |

M04 shall resolve refinement state, question contracts, stopping criteria, UI behaviour, exact schema, dependency invalidation and P0 test fixtures. M05 shall audit the current implementation against this SRS before any expansion of existing engines. M06 shall choose tools and libraries based on approved contracts and actual gaps. M07 and M08 require separate implementation and verification authorisation.

Open decisions: MVP domain and research corpus; non-GoDataBank evidence policy; canonical mission/specification ownership; capability registry authority; approval UI; data retention/security policy; benchmark sample size and rubric; exact provider and deployment choices. The numerical targets, phase boundaries and first single-operator prototype are proposed design decisions requiring review. No tests were executed and no implementation was inspected as part of this specification drafting exercise.

## 11. Change control

Changes require rationale, affected requirement IDs, impact on governing documents and tests, and human review. This SRS does not supersede existing governance, authorise spending or modify code. Repository adoption is dependent on M01 and M02 approval.
