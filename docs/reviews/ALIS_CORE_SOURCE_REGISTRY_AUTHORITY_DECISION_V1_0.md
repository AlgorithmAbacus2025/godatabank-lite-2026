# ALIS Core Source-Registry Authority Decision v1.0

## 1. Purpose

This document records a planning-only authority decision for the ALIS Core
source registry and the currently blocked source-registry candidates.

The decision does not authorise staging, commits, source changes, test changes,
registry data movement, registry data deletion, fixture promotion, `.gitignore`
modification, generated artifact cleanup, skeleton creation, migration, import
changes, or implementation.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`

Current repository state was also inspected using read-only source-control and
filesystem checks.

## 3. Current Registry Candidate State

Observed state before this decision document was created:

| Candidate | Current source-control state | Prior classification |
| --- | --- | --- |
| `sources/source_registry.json` | Modified tracked | Source-registry-blocked / review-before-decision |
| `backend/alis/source_registry.py` | Untracked | Source-registry-blocked Thoth implementation candidate |
| `tests/alis/test_source_registry.py` | Untracked | Source-registry-blocked Thoth test candidate |
| `tests/alis/test_registry_integration.py` | Untracked | Source-registry-blocked integration test candidate |

Repository state before creation:

| Item | Observed state |
| --- | --- |
| Staged files | None |
| Modified tracked files | 13 |
| Untracked paths | 251 |
| Skeleton folders checked | Not present |

## 4. Registry Authority Question

The authority question is whether the current registry candidates should be
treated as:

- canonical Thoth source-controlled registry state;
- fixture or test data;
- generated artifact;
- runtime storage;
- transitional prototype data;
- or deferred pending Thoth implementation design.

The answer must preserve the Boundary Register rule that Thoth owns canonical
Source Registry Entries, provenance records, lineage records, checksums, and
schema/contract references, while Arya owns source proposal and admission
requests and Aegis owns gate decisions.

## 5. Thoth Responsibility Boundary

Thoth is the metadata, provenance, schema, and registry engine. For source
registry work, Thoth may:

- produce canonical Source Registry Entries;
- maintain registry state once design and storage policy are approved;
- record provenance, lineage, checksum, schema, and contract references;
- link artifacts to source registry entries.

Thoth must not:

- make source admission decisions owned by Arya and Aegis workflows;
- validate evidence as an Aegis gate;
- retrieve external data as Hermes;
- perform analysis as Abacus;
- produce product presentation as Apollo or GoDataBank.

The current repository does not yet contain an approved Thoth registry design or
storage policy sufficient to treat existing registry data as production
canonical state.

## 6. Registry Data Options Considered

| Option | Assessment | Decision |
| --- | --- | --- |
| Canonical Thoth source-controlled registry state | Not approved yet because Thoth registry design, schema, mutation policy, and storage policy are not frozen. | Reject for now. |
| Fixture/test data | Plausible, but fixture scope and tests are not yet approved. | Possible later review. |
| Generated artifact | Plausible if produced by prototype runs, but generation source and retention policy are not confirmed. | Possible later review. |
| Runtime storage | Plausible future model, but no runtime storage design is approved. | Defer. |
| Transitional prototype data | Best current classification for `sources/source_registry.json`. | Adopt as planning decision. |
| Deferred pending Thoth implementation design | Required before any registry data acceptance. | Adopt as blocking rule. |

## 7. Registry Implementation Options Considered

| Option | Assessment | Decision |
| --- | --- | --- |
| Accept `backend/alis/source_registry.py` as Thoth source now | Premature without Thoth registry design and boundary review. | Reject for immediate baseline. |
| Treat as Thoth implementation candidate | Consistent with Boundary Register and prior classification. | Adopt as planning classification. |
| Treat as shared service | Not preferred because canonical Source Registry Entries are Thoth-owned. | Defer unless design proves shared support. |
| Treat as legacy/prototype source | Possible, but not proven. | Review later. |

## 8. Registry Test Options Considered

| Option | Assessment | Decision |
| --- | --- | --- |
| Accept `tests/alis/test_source_registry.py` now | Premature because matching source is blocked. | Reject for immediate baseline. |
| Treat as Thoth test candidate | Appropriate if source is later accepted as Thoth implementation. | Adopt as planning classification. |
| Accept `tests/alis/test_registry_integration.py` now | Premature because integration policy and source ownership are unresolved. | Reject for immediate baseline. |
| Treat as integration test candidate | Appropriate pending source ownership and integration policy. | Adopt as planning classification. |

## 9. Decision on sources/source_registry.json

Decision:

```text
Transitional prototype data or possible fixture candidate; not canonical
production Thoth registry state.
```

Rationale:

- The file is modified tracked data, not implementation source.
- Thoth owns canonical registry entries, but no approved Thoth registry design,
  schema, mutation policy, storage policy, or fixture policy exists yet.
- Treating the file as canonical now would resolve authority accidentally inside
  a source/test baseline.

Disposition:

- Remain blocked.
- Do not stage.
- Do not move.
- Do not delete.
- Do not promote to fixture.
- Review later after Thoth Registry Design approval.

## 10. Decision on backend/alis/source_registry.py

Decision:

```text
Thoth implementation candidate; not accepted for staging until reviewed against
the Boundary Register and a Thoth Registry Design.
```

Rationale:

- The source registry implementation aligns with Thoth responsibilities.
- The current implementation has not been reviewed for separation from Arya
  admission, Aegis validation, Hermes retrieval, or runtime storage concerns.
- Implementation acceptance requires a design contract first.

Disposition:

- Remain blocked.
- Do not stage.
- Review later as Thoth source candidate.

## 11. Decision on tests/alis/test_source_registry.py

Decision:

```text
Thoth test candidate pending source acceptance.
```

Rationale:

- The test likely belongs with Thoth registry behavior if
  `backend/alis/source_registry.py` is accepted later.
- Tests should not be baselined before source ownership and registry authority
  are decided.

Disposition:

- Remain blocked.
- Do not stage.
- Review after Thoth source candidate review.

## 12. Decision on tests/alis/test_registry_integration.py

Decision:

```text
Integration test candidate pending source ownership and integration policy.
```

Rationale:

- Registry integration may cross Thoth, Arya, Hermes, Aegis, and runtime
  boundaries.
- Integration tests require accepted source owners and a test placement policy.

Disposition:

- Remain blocked.
- Do not stage.
- Review after Thoth registry design and integration test policy.

## 13. Canonical Registry Ownership Recommendation

Recommendation:

```text
Canonical source registry ownership belongs to Thoth, but no current file is
approved as canonical production registry state.
```

Thoth should own the future canonical registry contract, implementation design,
registry entry schema, registry mutation rules, provenance linkage, and storage
policy. Existing candidates remain blocked until that design exists.

## 14. Storage Policy Recommendation

Recommended future storage policy direction:

- Define a Thoth Registry Design before accepting any registry file.
- Separate implementation source from registry state.
- Decide whether registry state is source-controlled, fixture-only,
  artifact-managed, or runtime-managed.
- Define mutation rules, versioning, schema, provenance links, and audit
  behavior before staging registry state.

No storage policy is authorised by this document.

## 15. Fixture Policy Recommendation

Recommended future fixture policy direction:

- Treat `sources/source_registry.json` as a possible fixture candidate only
  after fixture scope is approved.
- Fixture data must be minimal, deterministic, non-production, and clearly
  labelled.
- Fixture promotion must occur in a separate milestone.
- Fixture tests must not imply production registry authority.

No fixture promotion is authorised by this document.

## 16. Runtime-State Policy Recommendation

Recommended future runtime-state policy direction:

- Runtime registry state should not be silently stored in source-controlled
  prototype paths.
- If Thoth uses runtime storage, define where state lives, how it is migrated,
  how it is backed up, and how it is audited.
- Runtime state must remain separate from test fixtures and source code.

No runtime storage creation or migration is authorised by this document.

## 17. Source-Control Policy Recommendation

Recommended source-control policy:

- Source code may be versioned only after design and boundary review.
- Registry tests may be versioned only after source ownership and test placement
  are clear.
- Registry data must not be treated as canonical production state unless the
  Thoth Registry Design explicitly authorises source-controlled registry state.
- Generated registry artifacts and bytecode must remain excluded.

No registry file is authorised for source-control staging by this document.

## 18. Files Remaining Blocked

The following files remain blocked:

- `sources/source_registry.json`
- `backend/alis/source_registry.py`
- `tests/alis/test_source_registry.py`
- `tests/alis/test_registry_integration.py`

Blocking condition:

```text
Pending Thoth Registry Design and explicit registry storage/fixture/test policy.
```

## 19. Files Eligible for Later Review, If Any

The following files are eligible for later review, but not staging:

| File | Later review path |
| --- | --- |
| `backend/alis/source_registry.py` | Narrow Thoth source candidate review after Thoth Registry Design. |
| `tests/alis/test_source_registry.py` | Narrow Thoth test candidate review after source acceptance. |
| `tests/alis/test_registry_integration.py` | Integration test policy review after source ownership is clear. |
| `sources/source_registry.json` | Fixture/data authority review after storage and fixture policy are approved. |

## 20. Explicit Exclusions

This decision explicitly excludes:

- staging;
- commits;
- source changes;
- test changes;
- registry data movement;
- registry data deletion;
- fixture promotion;
- `.gitignore` modification;
- generated artifact cleanup;
- skeleton creation;
- migration;
- import changes;
- implementation.

It also excludes all files outside the four assessed registry candidates.

## 21. Generated Artifact Exclusion

Generated artifacts remain excluded from registry authority decisions.

Excluded examples include:

- generated evidence packages;
- generated classified, validated, and summary data;
- generated publishing outputs;
- generated manifests and reports.

Generated artifact retention, archival, cleanup, or deletion requires a separate
milestone.

## 22. Runtime Log Exclusion

Runtime logs remain excluded.

Known excluded logs include:

- `data/raw/world_bank/logs/world_bank_connector.log`
- `data/raw/ons/logs/ons_connector.log`
- `data/validated/validator.log`

Runtime logs must not be reclassified as registry authority evidence by this
decision.

## 23. Data/Report Exclusion

Data and report outputs remain excluded.

Excluded groups include:

- `data/raw/**`
- `data/classified/**`
- `data/validated/**`
- `data/summaries/**`
- `data/publishing/**`
- `reports/**`
- `evidence_package_output.json`

This exclusion does not decide whether `sources/source_registry.json` is a
fixture, artifact, or prototype. It remains specifically blocked as registry
prototype data.

## 24. .pyc and __pycache__ Exclusion

Python bytecode and cache folders remain excluded:

- `**/*.pyc`
- `**/__pycache__/`

No bytecode or cache cleanup is authorised. No `.gitignore` modification is
authorised.

## 25. Skeleton-Folder Exclusion

The following skeleton folders remain excluded and were not present during this
review:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

No skeleton creation is authorised by this decision.

## 26. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Treating prototype registry data as canonical production state | High | Keep `sources/source_registry.json` blocked until Thoth Registry Design approval. |
| Accepting registry implementation before boundary review | High | Require Thoth design review before source baseline authorisation. |
| Tests encode an unapproved registry model | Medium-high | Keep registry tests blocked until source ownership and storage policy are clear. |
| Fixture data becomes production state by accident | High | Require explicit fixture policy before any fixture promotion. |
| Runtime state is stored in source paths | Medium-high | Define runtime-state policy before registry migration or implementation. |
| Registry decisions leak into cleanup or `.gitignore` changes | Medium | Keep cleanup and ignore policy separate. |

## 27. Abort Conditions

Any future registry-related milestone should abort if:

- files are already staged before an authorised staging step begins;
- any registry candidate is proposed for staging before Thoth Registry Design is
  approved;
- `sources/source_registry.json` is proposed as canonical production state
  without an approved storage policy;
- fixture promotion is proposed without fixture policy approval;
- runtime storage is created or migrated without explicit approval;
- `.gitignore` is modified;
- generated artifacts, runtime logs, `.pyc` files, or `__pycache__/` folders are
  staged, deleted, or cleaned;
- skeleton folders are created;
- imports are changed;
- files are moved, renamed, deleted, cleaned, refactored, implemented, migrated,
  or restructured;
- independent review requires revision.

## 28. Recommended Next Milestone

Recommended next milestone:

```text
Thoth Registry Design v1.0
```

Purpose of the next milestone:

```text
Define the ALIS Core Thoth registry contract, storage policy, fixture policy,
runtime-state policy, registry mutation rules, schema/versioning requirements,
and test placement policy before any registry source, registry data, or registry
tests are staged.
```

Alternative if implementation design is deferred:

```text
Low-Risk Source/Test Baseline Authorisation Plan v1.0
```

That alternative must keep all registry candidates blocked and excluded.

STATUS: SOURCE-REGISTRY AUTHORITY DECISION CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
