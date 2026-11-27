# Alice — Research Formulation Engine Specification

**Document ID:** ALICE-RFE-001  
**Version:** 1.0 (proposed design baseline)  
**Date:** 27 November 2026  
**Milestone:** M04  
**Status:** Pending review; documentation only.  
**Dependencies:** M01, M02 and M03 (PRs #1–3, pending adoption).

## 1. Purpose and boundaries

Alice is an Adaptive, Objective-Oriented Research, Analysis and Discovery Agent. The RFE transforms incomplete human intentions into a sufficiently precise, user-confirmed, executable research specification, minimising irrelevant retrieval and unnecessary interaction.

Controlling documents:
- [Founding Constitution](ALICE_FOUNDING_CONSTITUTION_V1_0.md)
- [System Definition](ALICE_SYSTEM_DEFINITION_V1_0.md)
- [System Requirements Specification](ALICE_SYSTEM_REQUIREMENTS_SPECIFICATION_V1_0.md)
- [ALIS Core Boundary Register](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md)

The RFE belongs to Alice's formulation layer, not a ninth ALIS Core engine. It proposes research specifications, not canonical Abacus Execution Plans or Arya Retrieval Manifests. Existing Aegis gates, GoDataBank source policies and artifact ownership remain unchanged. P0 is a single-operator demonstrator with simulated capability catalogue and simulated execution. No live bulk retrieval, external effects, publication, paid calls or implementation is authorised by this document.

## 2. Design principles

- Progressive refinement: every question should resolve a material uncertainty or conflict.
- Context preservation: explicit user constraints survive subsequent turns unless explicitly revised.
- Hybrid design: model proposes interpretations, questions and methods; deterministic controller validates schemas, transitions, constraints, permissions and limits.
- User authority: a proposal is not a decision; capability selection is not permission; confirmation is tied to an exact specification revision.
- Proportionate interaction: precise queries bypass redundant stages; complex queries may require several rounds.
- Discovery without dilution: adjacent opportunities are separate from the confirmed objective.
- Fail closed: missing policy, authority, dependencies or mandatory fields block execution.
- Provider independence: model-facing interfaces do not own persistent mission state.

## 3. Functional decomposition

| Component | Responsibility | Boundary |
| --- | --- | --- |
| Interaction adapter | Render questions, controls, selections and review | Never directly invoke research tools |
| Intent interpreter | Extract candidate objectives, domains, constraints and ambiguities | Model output is untrusted proposal |
| Context reducer | Apply validated events, maintain revisions and attribution | Sole proposed builder of formulation state |
| Question planner | Generate and rank relevant clarification candidates | Cannot override explicit choices |
| Domain profile catalogue | Define fields, question templates, methods and candidate capability IDs | No source admission or tool permissions granted |
| Readiness evaluator | Check material fields, contradictions and feasibility | Cannot infer approval |
| Capability resolver | Resolve dependencies and intersect policy, permissions, scope and availability | Preview only at P0 |
| Specification builder | Produce immutable review snapshots | No ownership of existing engine artifacts |
| Approval controller | Bind explicit confirmation to snapshot and operator | No model-issued approval |
| Persistence/audit adapter | Preserve events, versions and trace references | Argus/Thoth production interfaces require M05 review |

Ownership assignments are proposed within Alice, not changes to existing ALIS Core contracts.

## 4. Interaction flow

1. Operator enters free text, optionally chooses a domain and submits.
2. Controller creates DRAFT, validates input and transitions to REFINING.
3. Intent interpreter proposes populated fields and unresolved dimensions. Controller preserves user statements and records provenance.
4. Question planner generates a small batch of useful questions, each with options or free text. Controller removes duplicates, conflicts, invalid questions and questions outside scope.
5. Operator selects or edits answers, chooses other/unsure/delegate where permitted, or cancels.
6. Controller applies events atomically, invalidates dependent proposals and reassesses readiness.
7. Repeat steps 3–6 only while useful and within limits.
8. Present an editable review snapshot including objective, scope, exclusions, assumptions, methods, sources, eligible capabilities, restrictions, deliverable and success criteria.
9. Explicit confirmation creates a version-bound approval. P0 may invoke only a simulated execution adapter; P1 requires rechecking real policies and engine interfaces.
10. Any material revision invalidates approval and returns to review.

The first submit is not research execution. Candidate source catalogue lookup at P0 uses local fixture metadata, not live retrieval. No model-generated content may auto-trigger a tool or approval.

## 5. Progressive questioning and convergence

### 5.1 Material dimensions

Domain, objective, subject/entity/population, geography, time, inclusions/exclusions, method, evidence policy, deliverable, success criteria and resource limits are candidate dimensions. Not all apply to every mission. Domain profiles classify dimensions as mandatory, conditional or optional, with dependency predicates. Examples: scientific literature may have global scope; market analysis may require geography; trend analysis requires an appropriate time range.

### 5.2 Question representation

Each question has a stable question ID, target field paths, semantic key, prompt, control type, options, optional free-text support, materiality reason, dependencies, originating revision and candidate source (template/model). Each option has a stable ID, display label and validated proposed field changes. A question targeting a resolved field is suppressed unless a conflict or explicit revision makes it relevant.

Control types: single_choice, multi_choice, dropdown, text, number, date_range, confirmation. Option IDs are data, not executable instructions. Other, unsure and delegate are explicit response dispositions, never silent defaults.

### 5.3 Candidate ranking

For P0 use an interpretable heuristic, not an unsupported claim of exact information gain:

S(q) = w_m M(q) + w_d D(q) + w_r R(q) - w_b B(q) - w_x X(q)

All component scores are normalised to [0,1]:
- M: materiality (effect on objective, method or constraints).
- D: dependency impact (fraction of currently unresolved relevant dependent fields).
- R: expected ambiguity reduction, a rubric-based estimate.
- B: response burden (complexity or number of choices).
- X: redundancy penalty (similarity to previous resolved or asked questions).

Provisional weights: w_m=0.35, w_d=0.20, w_r=0.30, w_b=0.10, w_x=0.05. These are heuristic parameters for evaluation, not calibrated probabilities. Hard conflicts and missing mandatory policy fields take precedence regardless of score. Filter resolved questions before ranking; ties break by stable ID. Display up to three compatible questions per round; prefer one when a response determines subsequent options. Do not ask irrelevant optional fields merely to fill a form.

If reliable distributions over candidate intents later become available, evaluate expected information gain H(I|s) - sum_a P(a|s,q) H(I|s,q,a), where H is Shannon entropy in bits. This is not computable reliably from arbitrary LLM confidence scores alone and is deferred. Compare heuristic ranking with fixed templates and unranked model proposals.

### 5.4 Readiness and stopping

READY_FOR_REVIEW requires:
- objective and scope sufficient for the intended domain;
- all applicable mandatory dimensions resolved, explicitly delegated with a proposed choice awaiting review, or supported by an explicit permissible assumption awaiting review;
- no unresolved hard conflict or missing authority/policy prerequisite for the proposed scope;
- candidate method and capability path identified, or a clearly disclosed unavailable capability that blocks execution;
- deliverable and measurable success criteria present;
- resource limits and policy references recorded.

A blocked capability may be shown in a non-executable review preview, but cannot transition to AUTHORISED until resolved. User confirmation resolves reviewable assumptions only if shown explicitly; non-delegable permissions cannot be inferred.

Provisional interaction settings: target median <=4 follow-up rounds, median response <=3 seconds and p95 <=10 seconds; ordinary interaction target <=120 seconds including user time (SRS section 8). Proposed hard cap: six automatic follow-up rounds per refinement session, configurable by operator before work; after cap offer review if valid, explicit permissible assumptions, a deliberate extension within budget, or BLOCKED/CANCELLED. No infinite repeated questions. A timeout is not consent. User pace is not a forced deadline. Model errors permit a bounded retry or deterministic fallback; failure is visible.

## 6. Structured contracts (proposed v1)

The following data definitions are normative for the proposed P0 interface, subject to review. Implementation-language and JSON Schema library selection are deferred. All contracts reject unknown properties except explicitly versioned extension maps; strings are bounded, IDs opaque, enumerations validated, and UTC timestamps ISO 8601. Numeric amounts include currency or units. Absent, unknown and not_applicable are distinct. Model-generated values are never authoritative by default.

### 6.1 Core field contracts

| Contract | Required fields and types |
| --- | --- |
| FieldValue | path:string; status: enum(unresolved,user_stated,proposed,delegated,confirmed,not_applicable); value: typed value or null; origin: enum(user,model,template,policy); event_id:string; revision:integer; rationale:string or null |
| MissionState | schema_version:string; mission_id:string; operator_ref:string; revision:integer >=0; state:MissionStatus; original_intent:string; fields: map of FieldValue by schema path; active_question_ids:string[]; history_ref:string; policy_ref:string; profile_ref:string; limits:Limits; unresolved:string[]; conflicts:string[]; updated_at:timestamp |
| Question | question_id:string; revision:integer; semantic_key:string; targets:string[]; prompt:string; control:enum; options:Option[]; dispositions:enum[]; dependencies:string[]; reason:string; origin:enum(template,model) |
| Option | option_id:string; label:string; proposed_changes:FieldChange[] |
| FieldChange | path:string; typed_value: schema-defined type or null; disposition:enum(answer,other,unsure,delegate,clear) |
| InteractionEvent | event_id:string; mission_id:string; expected_revision:integer; operator_ref:string (server authenticated); kind:enum(submit,answer,revise,review,confirm,cancel,extend); question_id:string or null; changes:FieldChange[]; timestamp:timestamp |
| Limits | max_rounds:integer; max_model_calls:integer; max_execution_seconds:integer or null; max_cost:decimal string and currency or null; external_access:enum(none,approved_read_only); scope_revision:integer |
| CapabilityDecision | capability_id:string; status:enum(eligible,ineligible,unavailable,dependency_blocked); reason_codes:string[]; dependency_ids:string[]; mode:enum(simulated,live); policy_ref:string |
| ReviewSnapshot | schema_version:string; mission_id:string; revision:integer; objective:string; questions:string[]; domain_profiles:string[]; scope:typed object; exclusions:string[]; assumptions:FieldValue[]; methods:string[]; candidate_sources:string[]; capability_decisions:CapabilityDecision[]; deliverable:string; success_criteria:string[]; policy_ref:string; limits:Limits; trace_ref:string; unresolved:string[]; executable:boolean; digest:string |
| ApprovalRecord | mission_id:string; revision:integer; snapshot_digest:string; operator_ref:string; approved_at:timestamp; permissions_ref:string; policy_ref:string; mode:enum(simulated,live); status:enum(active,revoked,expired) |

Scope fields: subject:string[]; population:string or null; geography:string[] or null; time_range: start/end ISO dates or explicit relative interval with reference date, or null; inclusion:string[]; exclusions:string[]. Each field retains status and origin through FieldValue references. Review snapshots reference frozen fields, not mutable pointers. Approval metadata is separate from immutable snapshot content. Digest calculated over canonical serialisation excluding digest itself, with specified stable encoding and key ordering to be fixed before implementation.

### 6.2 Validation invariants

- Expected revision must equal current revision; stale actions return conflict without mutation.
- Authenticated operator identity and ownership checked server-side, not from model/user-supplied identity.
- Selected option must exist for active question and revision; free text validated against target field constraints.
- Dates ordered; costs non-negative and currency explicit; required scope fields present.
- User-stated hard constraints cannot be overwritten by model proposals.
- Changing a field invalidates dependent proposals, question sets, review snapshot and applicable approval, not independent decisions.
- Confirmation requires current digest, matching revision, explicit review and executable=true.
- Duplicate event ID is idempotent with identical payload; different payload is rejected.
- Invalid model output cannot become state or tool arguments; reject and retry/fallback within budget.

### 6.3 Illustrative review payload (not a live mission)

```json
{
  "schema_version": "1.0",
  "mission_id": "example-001",
  "revision": 4,
  "objective": "Identify AI-assisted inspection opportunities for small manufacturers in Wales",
  "questions": ["Which documented inspection problems could AI address?"],
  "domain_profiles": ["market_research", "engineering"],
  "scope": {
    "subject": ["AI-assisted inspection"],
    "population": "small manufacturers",
    "geography": ["Wales"],
    "time_range": null,
    "inclusion": ["low-capital applications"],
    "exclusions": ["large-scale production equipment"]
  },
  "exclusions": ["large-scale production equipment"],
  "assumptions": [],
  "methods": ["evidence_review", "opportunity_assessment"],
  "candidate_sources": ["official_business_statistics", "approved_technical_literature"],
  "capability_decisions": [
    {
      "capability_id": "demo.evidence_review",
      "status": "eligible",
      "reason_codes": ["SIMULATED_CATALOGUE"],
      "dependency_ids": [],
      "mode": "simulated",
      "policy_ref": "demo-policy-v1"
    }
  ],
  "deliverable": "Evidence-linked shortlist of testable hypotheses",
  "success_criteria": ["Each hypothesis includes evidence, uncertainty and a validation proposal"],
  "policy_ref": "demo-policy-v1",
  "limits": {
    "max_rounds": 6,
    "max_model_calls": 12,
    "max_execution_seconds": null,
    "max_cost": {"amount": "0.00", "currency": "GBP"},
    "external_access": "none",
    "scope_revision": 4
  },
  "trace_ref": "fixture-trace-001",
  "unresolved": ["time_range"],
  "executable": false,
  "digest": "illustrative-not-computed"
}
```

This is intentionally a non-executable example: time range has not been resolved, digest is illustrative, and candidate sources are categories, not admitted sources.

## 7. State machine and transition rules

| Current | Event / guard | Next | Action |
| --- | --- | --- | --- |
| DRAFT | Valid initial submission | REFINING | Initialise state and propose missing fields |
| REFINING | Valid answer or revision; not ready | REFINING | Atomic update, rank questions |
| REFINING | Readiness checks pass | READY_FOR_REVIEW | Freeze snapshot |
| REFINING | Budget/cap reached and unresolved | BLOCKED | Preserve reason and permitted alternatives |
| READY_FOR_REVIEW | Valid revision | REFINING | Invalidate snapshot and approval |
| READY_FOR_REVIEW | Explicit confirmation, all guards pass | AUTHORISED | Create approval record |
| AUTHORISED | Start, policy/permission/budget rechecked | RUNNING | P0 simulation only |
| AUTHORISED | Material change or expired approval | REFINING | Revoke approval |
| RUNNING | Work complete or bounded interruption | EVALUATING | Assess results and limitations |
| RUNNING | Material scope change requested | REFINING | Stop new execution, checkpoint, revoke approval |
| EVALUATING | All criteria satisfied | COMPLETED | Store outcome |
| EVALUATING | Some criteria unmet | PARTIAL | Store limitations |
| EVALUATING | Cannot proceed safely | BLOCKED | Store reason |
| Nonterminal | Cancel | CANCELLED | Prevent new operations; stop safely |
| Nonterminal | Unrecoverable error | FAILED | Preserve diagnostic state |
| BLOCKED | Explicit authorised revision or extension | REFINING | New revision; recheck limits |
| COMPLETED/PARTIAL/CANCELLED/FAILED | Explicit new inquiry | New DRAFT | New mission ID or linked revision, no automatic work |

Undefined transitions reject without mutation. Repeated submit/start events cannot duplicate execution. BLOCKED may be reopened deliberately; other terminal outcomes remain historical. P1 checkpoint and side-effect semantics require separate design; P0 simulates them.

## 8. Dependency invalidation and tool selection

Proposed field dependency graph:
- domain -> profile-specific questions, source categories, methods, capabilities;
- subject/population/geography/time -> relevant source candidates and analytical suitability;
- method -> capabilities and deliverable feasibility;
- evidence policy/permissions/limits -> eligibility and executable status;
- deliverable -> success criteria and output capability.

Explicit user constraints remain unless revised. Where a dependent field was user-specified, flag for re-review instead of deleting it. Recompute descendants using a cycle-free declared graph; reject cyclic configuration. Each material change increments revision and invalidates approval.

Capability eligibility:
1. Derive requested capability IDs from confirmed objectives and methodology.
2. Resolve transitive declared dependencies, reject cycles and missing IDs.
3. Evaluate each candidate against profile, operator permissions, policy, scope, availability and remaining budget.
4. Reject dependent capability if any mandatory dependency is ineligible.
5. Return decision and reason codes; no automatic fallback to prohibited tools.
6. On actual invocation, recheck runtime authorisation and validation gates (P1).

Conceptually E = dependency_closure(requested) intersect available intersect authorised intersect policy_allowed intersect budget_feasible, with dependency consistency enforced after intersection. Mandatory governance cannot be disabled by UI selection. Candidate sources are not source approvals. Aegis retains gate decisions; Arya owns retrieval manifests; Hermes retrieves; Abacus owns analytical plans; no direct bypass.

P0 catalogue fields: capability_id, owner_ref, purpose, input_contract_ref, output_contract_ref, dependencies, supported_profiles, side_effect_class, policy_tags, estimated_cost, enabled, mode. All capabilities are simulated; no actual network connectors required.

## 9. Proposed public interface

| Operation | Input | Output / errors |
| --- | --- | --- |
| create_mission | Initial intent, optional domain, operator context | MissionState; INVALID_INPUT |
| propose_refinement | Mission ID/revision | Question[] or readiness result; MODEL_INVALID, LIMIT_REACHED |
| apply_response | InteractionEvent | Updated MissionState; STALE_REVISION, INVALID_OPTION, CONFLICT |
| revise_field | InteractionEvent | Updated state and invalidated references |
| preview_specification | Mission ID/revision | ReviewSnapshot or NOT_READY |
| confirm_specification | Mission ID, revision, digest, authenticated approval | ApprovalRecord or NOT_AUTHORISED |
| preview_capabilities | Mission ID/revision | CapabilityDecision[] |
| start_simulation | ApprovalRecord reference | Simulated execution status; POLICY_DENIED |
| cancel_mission | Mission ID/revision | Status and cancellation receipt |
| resume_formulation | Mission ID, operator context | Persisted state; NOT_AUTHORISED |

These are logical contracts, not implemented APIs or binding endpoint names. Responses include trace ID and recoverability where applicable. Use deterministic errors rather than silently substituting values.

## 10. UI interaction specification

Screen A: broad domain (optional), free-text intention, submit-and-refine button.  
Screen B: adaptive question group with selectable controls, other/unsure/delegate, back/edit, contextual summary and cancel.  
Screen C: objective review, explicit constraints, assumptions, exclusions, methodology, candidate source categories, eligible/disabled capabilities with reasons, limits and success criteria. Confirm disabled if not executable.  
Screen D: authorised P0 simulation, status and clearly labelled simulated results.  

Only material unanswered dimensions shown; stages can collapse for precise queries. Keyboard accessibility, clear labels, non-colour status indicators, visible loading/error/retry states and retained input on failure are required. Do not present a fake progress percentage. No research claims from simulated results.

Illustrative branching:
- Initial: "Explore opportunities in AI."
- Commercial selection -> sector, market/geography, capital ceiling, intended customer.
- Scientific selection -> research field, literature period, evidence type, research gap or hypothesis.
- If commercial + manufacturing + Wales + low capital, ask what low capital means only if material and not already given; propose evidence review and opportunity assessment.
- Changing Wales to UK invalidates location-dependent source candidates while retaining capital ceiling.
- Present candidate specification; user confirms before simulation.

## 11. P0 verification plan

Use synthetic fixtures with scripted operator answers and independent expected intent, no live personal data. Test deterministic controller separately from model proposals and run integration with recorded valid/invalid model responses. No performance claim until executed.

| Test | Scenario / expected result | Trace |
| --- | --- | --- |
| F01 | Empty input rejected; broad and precise intentions accepted | RFE-001 |
| F02 | First submission never invokes research tools | RFE-002 |
| F03 | Ambiguous intent yields materially relevant questions, no invented constraints | RFE-003,004 |
| F04 | Commercial vs scientific branching differs appropriately | RFE-004,015 |
| F05 | Single/multi/dropdown/text/other/unsure/delegate validated | RFE-005 |
| F06 | Previously resolved capital constraint not asked again; conflicts surfaced | RFE-006,008 |
| F07 | Geography revision invalidates dependent sources, preserves budget | RFE-007,012 |
| F08 | Precise input bypasses redundant rounds; unresolved hard conflict blocks readiness | RFE-009 |
| F09 | Review shows scope, assumptions, limits and eligible tools | RFE-010, ORC-002 |
| F10 | Stale snapshot, forged operator or missing approval cannot start | RFE-011, NFR-001 |
| F11 | Save/reopen preserves state, history and revisions | RFE-012 |
| F12 | Repetitive answers and max-round exhaustion terminate safely | RFE-013 |
| F13 | Targeted vs discovery mode separates adjacent proposals | RFE-014 |
| F14 | Disabled tools, missing/cyclic dependencies and forged choices rejected | ORC-001, NFR-001 |
| F15 | Simulated execution differentiates eligible, invoked, failed, skipped | ORC-003 |
| F16 | Duplicate event idempotent; stale response rejected; cancel prevents new work | ORC-009, NFR-004 |
| F17 | Invalid model JSON or timeout retains state and offers bounded recovery | NFR-004,008 |
| F18 | Audit contains required trace references, no secrets | NFR-003,005 |
| F19 | Measure latency, turns, intent fidelity and user burden vs fixed-form and single-pass baselines | NFR-006,009 |
| F20 | UI keyboard navigation, error recovery, back/revise and confirmation | NFR-008 |

Proposed initial benchmark: 30 synthetic intents across at least three domain profiles, including 10 precise cases, 10 ambiguous and 10 conflicting/edge cases; independently label mandatory fields and expected constraints before running. Repeat model-dependent cases three times with recorded settings; report per-case results and variation. Use paired comparisons and publish failures; sample is exploratory, not population-representative. P1 retrieval precision/recall and evidence tests remain deferred until approved real evidence fixtures exist. P0 passes require the SRS thresholds and all applicable deterministic negative tests, subject to review of thresholds and test corpus.

## 12. Implementation boundaries and decisions

M04 specifies the formulation controller, logical interfaces, state machine, question structure, convergence heuristic, eligibility and tests. M05 must audit existing code and contract compatibility before actual integration. M06 selects minimum tools/libraries and model provider after feasibility checks. No runtime changes are authorised here.

Proposed decisions needing review: six-round cap, three-question batch cap, heuristic weights, initial benchmark size, state ownership within Alice, persistence and canonical serialisation details, exact typed domain field registry, real evidence policies and catalogue authority. The conceptual contract tables are not yet executable JSON Schema files; these must be generated and validated before implementation. Approval and security policies must be reviewed for the deployment environment. No tests run, no latency measured, no claims of implemented functionality.

Change control: any amendment must reference affected SRS requirements, update verification cases and preserve existing GoDataBank governance. Adoption is dependent on M01–M03 review.
