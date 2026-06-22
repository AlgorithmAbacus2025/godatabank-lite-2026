# ALIS Core Thoth Registry Source/Test Candidate Review Plan v1.0

## 1. Purpose

This document defines a planning-only review plan for the current Thoth registry
source/test candidates. It explains how the registry implementation candidate,
registry data candidate, and registry test candidates should be reviewed against
the ALIS Core Boundary Register and the Thoth Registry Design before any source,
test, data, fixture, storage, staging, or commit action is authorised.

This plan does not accept, stage, commit, edit, move, promote, or implement any
candidate.

## 2. Source Documents Reviewed

The following documents were reviewed:

| Document | Review use |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing ALIS Core engine ownership and boundary rules. |
| `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md` | Controlling Thoth registry design contract for this review plan. |
| `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md` | Registry authority decision and blocked-candidate conclusions. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md` | Candidate classification and source-registry blocked status. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md` | Source/test baseline sequencing and exclusions. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Repository-level classification and future-location planning. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Source-control disposition constraints. |
| `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` | Dirty/untracked working-tree resolution constraints. |

The following candidates were assessed without modification:

| Candidate | Assessment basis |
| --- | --- |
| `sources/source_registry.json` | Modified tracked registry data candidate. |
| `backend/alis/source_registry.py` | Untracked implementation candidate. |
| `tests/alis/test_source_registry.py` | Untracked unit-test candidate. |
| `tests/alis/test_registry_integration.py` | Untracked integration-test candidate. |

## 3. Current Repository State

At the time of this review-plan creation:

| State item | Observed state |
| --- | --- |
| Staged files | None observed. |
| Modified tracked files | 13 observed in the working tree. |
| Untracked paths | 79 observed in the working tree. |
| `sources/source_registry.json` | Modified tracked file. |
| `backend/alis/source_registry.py` | Untracked file. |
| `tests/alis/test_source_registry.py` | Untracked file. |
| `tests/alis/test_registry_integration.py` | Untracked file. |
| `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md` | Present and untracked at this point. |
| Target skeleton folders | Not present: `src/`, `artifacts/`, `legacy/`, `docs/migration/`, `tests/alis_core/`, `tests/godatabank/`. |

This plan does not alter that state.

## 4. Review Scope

The review scope is limited to planning how to review these four candidates:

| Candidate | Scope |
| --- | --- |
| `sources/source_registry.json` | Registry data candidate review only. |
| `backend/alis/source_registry.py` | Thoth implementation candidate review only. |
| `tests/alis/test_source_registry.py` | Thoth unit-test candidate review only after implementation review path is clear. |
| `tests/alis/test_registry_integration.py` | Integration-test candidate review only after integration policy is clear. |

The scope excludes all other source files, tests, generated artifacts, runtime
logs, data, reports, bytecode caches, skeleton folders, fixture promotion, and
runtime storage.

## 5. Non-Authorised Actions

This plan does not authorise:

- staging;
- committing;
- moving files;
- renaming files;
- deleting files;
- cleaning generated artifacts;
- creating skeleton folders;
- modifying `.gitignore`;
- refactoring code;
- changing imports;
- implementing engines;
- restructuring the repository;
- promoting fixtures;
- creating runtime registry storage;
- editing registry source, registry data, or registry tests.

## 6. Controlling Design Contract

The controlling design contract is
`docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`.

Required design conclusions that govern this plan:

- Thoth owns the canonical Source Registry Entry contract.
- `sources/source_registry.json` is not production canonical registry state.
- `sources/source_registry.json` is transitional prototype data or a possible
  future fixture candidate only.
- `backend/alis/source_registry.py` is a Thoth implementation candidate only.
- `tests/alis/test_source_registry.py` is a Thoth test candidate pending source
  acceptance.
- `tests/alis/test_registry_integration.py` is an integration test candidate
  pending source ownership and integration-test policy.
- All four candidates remain blocked from staging and commit until separate
  review and authorisation.

## 7. Registry Candidate Inventory

| Candidate | Current status | Current behavior or content | Required conclusion |
| --- | --- | --- | --- |
| `sources/source_registry.json` | Modified tracked | Prototype source catalogue with policy metadata and source records. | Remains blocked; not canonical production state. |
| `backend/alis/source_registry.py` | Untracked | Loads the JSON file and exposes list, lookup, filter, access-validation, and group helpers. | May be reviewed only as a Thoth implementation candidate. |
| `tests/alis/test_source_registry.py` | Untracked | Tests helper loading, listing, lookup, filtering, access validation, and groups against the JSON file. | May be reviewed only as a Thoth unit-test candidate after source review path is clear. |
| `tests/alis/test_registry_integration.py` | Untracked | Simulates registry query selection and evidence-package-like source mapping. | May be reviewed only as an integration-test candidate pending integration policy. |

## 8. Review Plan for sources/source_registry.json

`sources/source_registry.json` must be reviewed as registry data, not as
production registry authority.

Review steps:

1. Confirm it is not treated as canonical production Thoth state.
2. Compare its fields against the Source Registry Entry concept and required
   field direction in the Thoth Registry Design.
3. Identify missing canonical identifiers, provenance references, lineage
   references, checksum references, schema/contract references, mutation
   records, and Aegis decision references.
4. Decide whether it is best classified later as transitional prototype data,
   possible test fixture data, archive-later data, or do-not-touch data.
5. Keep it blocked from staging until storage and fixture policy are separately
   approved.

Required conclusion: it remains blocked and must not be treated as production
canonical registry state.

## 9. Review Plan for backend/alis/source_registry.py

`backend/alis/source_registry.py` may be reviewed only as a Thoth implementation
candidate.

Review steps:

1. Check whether the module is limited to Thoth registry responsibilities.
2. Identify any language or behavior that treats `sources/source_registry.json`
   as canonical production state.
3. Check whether the helper model can support the future Source Registry Entry
   contract, or whether it is only a prototype loader/query helper.
4. Check whether access validation overlaps Aegis policy authority.
5. Check whether filtering or source selection overlaps Arya retrieval planning.
6. Check whether endpoint usage overlaps Hermes transport authority.
7. Check whether implementation would require schema/contract, provenance,
   lineage, checksum, mutation, and validation support before acceptance.
8. Keep the file blocked from staging until a separate narrow implementation
   candidate review or authorisation exists.

Required conclusion: it may be reviewed as a Thoth implementation candidate
only; this plan does not edit, stage, or commit it.

## 10. Review Plan for tests/alis/test_source_registry.py

`tests/alis/test_source_registry.py` may be reviewed only as a Thoth unit-test
candidate after the source implementation review path is clear.

Review steps:

1. Confirm the test depends on blocked implementation and blocked JSON data.
2. Determine which assertions verify prototype helper behavior only.
3. Identify missing unit-test coverage for the future Thoth contract, including
   canonical identifiers, status transitions, provenance, lineage, checksums,
   schema/contract references, mutation rules, and validation rules.
4. Confirm whether any fixture dependency is explicit and non-production.
5. Keep the test blocked until source implementation and fixture policy are
   reviewed separately.

Required conclusion: it may be reviewed as a Thoth unit-test candidate only
after the implementation review path is clear; this plan does not stage or edit
it.

## 11. Review Plan for tests/alis/test_registry_integration.py

`tests/alis/test_registry_integration.py` may be reviewed only as an
integration-test candidate.

Review steps:

1. Confirm the test crosses registry, source selection, access validation, and
   evidence-package-like mapping concerns.
2. Identify which assertions belong to Thoth and which belong to Arya, Hermes,
   Aegis, Abacus, shared evidence contracts, or integration orchestration.
3. Confirm that integration-test placement policy exists before acceptance.
4. Confirm that fixture data is approved before any JSON-backed integration test
   is accepted.
5. Keep the test blocked until integration ownership and fixture policy are
   separately approved.

Required conclusion: it may be reviewed only as an integration-test candidate
pending integration policy; this plan does not stage or edit it.

## 12. Required Thoth Contract Checks

Any future candidate review must check whether the candidate supports or
conflicts with:

- Thoth ownership of canonical Source Registry Entries;
- required registry entry fields;
- optional registry entry field boundaries;
- canonical identifier policy;
- provenance policy;
- lineage policy;
- checksum policy;
- schema/contract reference policy;
- source status model;
- registry mutation rules;
- registry validation rules;
- storage policy;
- fixture policy;
- runtime-state policy;
- source-control policy;
- test placement policy.

Failure to satisfy these checks does not imply immediate rejection, but it blocks
baseline acceptance until the candidate is revised under separate authorisation
or deferred.

## 13. Required Boundary Checks

Candidate review must verify that Thoth does not absorb another engine's
responsibility.

| Boundary | Required check |
| --- | --- |
| Arya | Candidate must not own source proposals, admission requests, or retrieval planning. |
| Hermes | Candidate must not perform or decide transport/retrieval behavior. |
| Aegis | Candidate must not own policy gates, access approval, validation decisions, or source admission decisions. |
| Abacus | Candidate must not perform analytical planning or analysis. |
| Apollo | Candidate must not assemble publication packages or publication manifests. |
| Argus | Candidate must not own audit monitoring, alerting, or incident decisions. |
| GoDataBank product layer | Candidate must not become product presentation or catalogue UX logic. |

Any overlap requires defer or separate boundary review.

## 14. Required Storage-Policy Checks

Future review must verify:

- no production canonical storage is inferred from `sources/source_registry.json`;
- no runtime storage is created;
- no source-controlled file is treated as runtime state without policy approval;
- no fixture data is mixed with production registry state;
- no generated source snapshot is accepted as registry authority;
- any proposed storage mechanism has a separate design and migration plan.

If storage authority remains unresolved, all data and tests depending on that
storage remain blocked.

## 15. Required Fixture-Policy Checks

Future review must verify:

- no fixture is promoted by default;
- fixture data, if later approved, is explicitly marked non-production;
- fixture identifiers cannot collide with production identifiers;
- tests cannot treat fixture entries as admitted production sources;
- fixture placement waits for authorised skeleton or test path decisions;
- fixture content is minimal, deterministic, and reviewed.

`sources/source_registry.json` may only become a fixture through a separate
fixture authorisation milestone.

## 16. Required Runtime-State Checks

Future review must verify:

- registry source code does not write runtime registry state into source files;
- runtime caches, transport receipts, logs, and registry records are separated;
- test execution does not create persistent runtime storage;
- runtime state does not bypass provenance, lineage, checksum, mutation, or
  validation rules;
- no storage directory is created as part of review.

If runtime state is needed, a separate runtime storage design is required first.

## 17. Required Source-Control Checks

Future review must verify:

- no candidate is staged without exact file-level authorisation;
- no directory-level `git add` is used;
- generated artifacts, runtime logs, data, reports, `.pyc`, and `__pycache__/`
  remain excluded;
- line-ending warnings remain separate from source acceptance;
- source-control state is checked before any future staging;
- blocked registry data is not included in a source implementation commit by
  dependency convenience.

This plan authorises no source-control action.

## 18. Required Test-Placement Checks

Future review must verify:

- Thoth unit tests are separated from integration tests;
- integration tests are not accepted until integration policy exists;
- fixture-dependent tests use approved fixture locations only;
- current `tests/alis/` placement is not treated as final architecture;
- no `tests/alis_core/` or `tests/godatabank/` folder is created without a
  skeleton authorisation milestone.

Test placement remains planning-only.

## 19. Required Provenance Checks

Future review must verify whether each candidate supports:

- admission request references;
- Aegis decision references;
- mutation actor and timestamp records;
- prior-state references for updates;
- source metadata evidence references;
- failure records for rejected or incomplete registry operations.

Current candidates do not demonstrate full provenance support and therefore
remain blocked from baseline acceptance.

## 20. Required Lineage Checks

Future review must verify whether each candidate supports lineage from:

- source proposal to admission decision;
- admission decision to Source Registry Entry;
- Source Registry Entry to Hermes retrieval manifest;
- retrieved artifact to evidence package;
- validated evidence to analysis;
- analysis and narrative packages to publication packages;
- registry operations to audit records.

Any candidate that infers lineage from a URL, short name, or test fixture alone
must be deferred or revised under separate authorisation.

## 21. Required Checksum Checks

Future review must verify whether the candidate distinguishes:

- registry entry checksums;
- registry snapshot checksums;
- raw source artifact checksums;
- retrieved evidence package checksums;
- validation report checksums;
- publication package checksums.

The review must also check algorithm metadata, checksum scope, timestamps,
artifact identifiers, verification status, and mutation references. Absence of
checksum support blocks registry baseline acceptance.

## 22. Required Schema/Contract Reference Checks

Future review must verify whether each candidate references:

- Source Registry Entry contract version;
- provenance record contract version;
- lineage record contract version;
- checksum record contract version;
- Aegis gate decision contract version;
- Arya admission request contract version where required;
- shared schema or contract registry references.

Implicit Python object shape or JSON field shape is not sufficient as the only
contract.

## 23. Required Mutation-Rule Checks

Future review must verify whether the candidate can enforce or support:

- Thoth-only canonical mutation authority;
- append-only mutation records;
- previous-state preservation;
- Aegis decision references for policy-driven status transitions;
- rejection of silent in-place edits;
- alias or supersession handling for identity changes;
- failed mutation recording.

Prototype read-only query behavior may be useful, but it does not satisfy the
future mutation contract by itself.

## 24. Required Validation-Rule Checks

Future review must verify whether the candidate can enforce or support:

- required field validation;
- canonical identifier uniqueness;
- alias collision checks;
- source status transition checks;
- provenance consistency;
- lineage consistency;
- checksum reference requirements;
- schema and contract reference requirements;
- fixture-only isolation;
- prototype-status isolation;
- fail-closed behavior.

Any validation behavior that substitutes for Aegis policy authority must be
rejected or redesigned.

## 25. Candidate Acceptance Criteria

A future candidate may become eligible for authorisation only if:

- the review is limited to an exact file or file group;
- ownership is clearly Thoth or explicitly integration-test scope;
- no production canonical registry state is accepted accidentally;
- fixture status, if relevant, is explicitly authorised;
- runtime storage is not created implicitly;
- provenance, lineage, checksum, schema, contract, mutation, and validation
  gaps are documented;
- cross-engine overlaps are either absent or explicitly deferred;
- source-control scope excludes generated artifacts, logs, data, reports,
  bytecode, cache folders, `.gitignore`, and skeleton folders;
- independent review approves the next authorisation step.

Acceptance criteria identify eligibility for later authorisation only. They do
not authorise staging or commits.

## 26. Candidate Rejection/Defer Criteria

A candidate must be rejected or deferred if:

- it treats `sources/source_registry.json` as production canonical state;
- it depends on unapproved fixture data;
- it creates or requires runtime storage without design approval;
- it mutates registry authority outside Thoth;
- it owns Arya, Hermes, Aegis, Abacus, Apollo, Argus, or product-layer
  responsibilities;
- it lacks required provenance, lineage, checksum, schema, contract, mutation,
  or validation support and claims production readiness;
- it requires import changes, refactoring, movement, or skeleton creation to be
  reviewed;
- it brings generated artifacts, runtime logs, data, reports, `.pyc`, or
  `__pycache__/` into source control.

## 27. Files Remaining Blocked

The following files remain blocked:

| File | Blocked reason |
| --- | --- |
| `sources/source_registry.json` | Not canonical production state; storage and fixture policy unresolved. |
| `backend/alis/source_registry.py` | Implementation candidate not yet reviewed against the Thoth design contract. |
| `tests/alis/test_source_registry.py` | Unit-test candidate depends on blocked source and blocked registry data. |
| `tests/alis/test_registry_integration.py` | Integration-test candidate depends on blocked source/data and unresolved integration policy. |

Blocked means no staging, no commit, no edit, no move, no delete, no fixture
promotion, no runtime storage, and no source-control action.

## 28. Files Potentially Eligible for Later Authorisation

Potential later authorisations, after independent approval, may include:

| Candidate | Possible later authorisation |
| --- | --- |
| `backend/alis/source_registry.py` | Narrow Thoth Registry Implementation Candidate Review v1.0. |
| `tests/alis/test_source_registry.py` | Narrow Thoth Registry Unit-Test Candidate Review after source path is clear. |
| `tests/alis/test_registry_integration.py` | Registry integration-test review after integration policy is approved. |
| `sources/source_registry.json` | Transitional-data or fixture review after storage and fixture policy are approved. |

No candidate is eligible for immediate staging or commit under this plan.

## 29. Generated Artifact Exclusion

Generated artifacts remain excluded from registry source/test review.

Excluded groups include:

- `evidence_package_output.json`;
- generated evidence outputs;
- generated classified data;
- generated summary data;
- generated publication artifacts;
- generated reports;
- generated manifests unless separately reviewed.

This plan does not authorise artifact cleanup, movement, deletion, retention, or
commit.

## 30. Runtime Log Exclusion

Runtime logs remain excluded.

Excluded groups include:

- `data/**/logs/*.log`;
- validation logs;
- connector logs;
- any future registry runtime logs.

This plan does not authorise runtime log cleanup, deletion, movement, retention,
or commit.

## 31. Data/Report Exclusion

Data and report outputs remain excluded.

Excluded groups include:

- `data/raw/`;
- `data/validated/`;
- `data/classified/`;
- `data/summaries/`;
- `data/publishing/`;
- `data/published/`;
- `reports/`.

No data or report path may be treated as registry source/test material without
separate artifact, fixture, or retention review.

## 32. .pyc and __pycache__ Exclusion

Bytecode and cache artifacts remain excluded.

Excluded groups include:

- `**/*.pyc`;
- `**/__pycache__/`.

This plan does not authorise cleanup, deletion, `.gitignore` changes, movement,
or commit for bytecode/cache artifacts.

## 33. Skeleton-Folder Exclusion

This plan does not authorise skeleton folder creation.

The following folders must not be created by this milestone:

- `src/`;
- `artifacts/`;
- `legacy/`;
- `docs/migration/`;
- `tests/alis_core/`;
- `tests/godatabank/`.

Any future file placement decision must wait for a separate skeleton or
repository-architecture authorisation milestone.

## 34. Risks

| Risk | Severity | Control |
| --- | --- | --- |
| Prototype registry JSON is treated as canonical production state. | High | Keep `sources/source_registry.json` blocked and require storage/fixture review. |
| Implementation candidate bakes in blocked JSON authority. | High | Review source separately before any test or data acceptance. |
| Unit tests lock the prototype data shape into the contract. | Medium-high | Review tests only after source and fixture path is clear. |
| Integration test crosses engine boundaries without policy. | High | Require integration-test policy before acceptance. |
| Aegis policy authority is absorbed into Thoth helper validation. | High | Boundary-check access and admission behavior explicitly. |
| Fixture promotion occurs accidentally. | High | Require a future fixture authorisation milestone. |
| Runtime storage is created by test or implementation review. | High | Keep runtime storage excluded until design approval. |
| Source-control cleanup or staging occurs before review. | Medium | Require narrow future authorisations with exact file lists. |

## 35. Abort Conditions

Any future Thoth registry source/test review or authorisation must abort if:

- staged files exist outside the authorised scope;
- a candidate is edited as part of review;
- `sources/source_registry.json` is treated as production canonical state;
- fixture promotion is attempted without separate approval;
- runtime storage is created or required without separate approval;
- source-control commands use directory-level add or globs;
- generated artifacts, logs, data, reports, `.pyc`, or `__pycache__/` are
  included;
- `.gitignore` modification is introduced;
- skeleton folders are created;
- imports are changed;
- source code is refactored;
- engine implementation work begins;
- cross-engine ownership is unresolved but the candidate is proposed for
  staging.

## 36. Recommended Next Milestone

The next milestone should be:

Independent Review of Thoth Registry Source/Test Candidate Review Plan v1.0.

After independent approval, the next reviewable operational step may be:

Narrow Thoth Registry Implementation Candidate Review v1.0.

That later milestone should remain review-only unless a separate authorisation
explicitly permits staging or commits.

STATUS: THOTH REGISTRY SOURCE/TEST CANDIDATE REVIEW PLAN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
FIXTURE PROMOTION: NOT PERFORMED
RUNTIME STORAGE: NOT CREATED
NEXT RECOMMENDED STEP: Independent Review
