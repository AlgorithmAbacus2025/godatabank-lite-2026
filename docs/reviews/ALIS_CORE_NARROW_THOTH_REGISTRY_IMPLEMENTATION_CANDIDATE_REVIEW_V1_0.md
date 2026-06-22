# ALIS Core Narrow Thoth Registry Implementation Candidate Review v1.0

## 1. Purpose

This document reviews `backend/alis/source_registry.py` as a narrow Thoth
registry implementation candidate only. The review assesses whether the file is
suitable for later Thoth implementation authorisation, revision, deferral, or
rejection under the ALIS Core Boundary Register and the Thoth Registry Design.

This review does not authorise staging, commit, source edits, fixture promotion,
runtime storage, repository restructuring, or implementation work.

## 2. Source Documents Reviewed

| Document | Review use |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing ALIS Core engine boundary contract. |
| `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md` | Frozen Thoth registry design used as the candidate review contract. |
| `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md` | Review-plan scope for registry source/test candidates. |
| `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md` | Registry authority and blocked-candidate decision. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md` | Candidate classification and source-registry-blocked status. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md` | Source/test baseline sequencing and exclusions. |

Context references inspected without modification:

- `sources/source_registry.json`
- `tests/alis/test_source_registry.py`
- `tests/alis/test_registry_integration.py`

## 3. Candidate Reviewed

| Field | Value |
| --- | --- |
| Candidate path | `backend/alis/source_registry.py` |
| Current source-control status | Untracked |
| Candidate type | Thoth implementation candidate only |
| Review type | Narrow review-only assessment |
| Candidate disposition selected | Keep blocked |

## 4. Current Repository State

At the time of review:

| State item | Observed state |
| --- | --- |
| Staged files | None observed. |
| Modified tracked files | 13 observed in the working tree. |
| Untracked paths | 80 observed in the working tree. |
| `sources/source_registry.json` | Modified tracked file. |
| `backend/alis/source_registry.py` | Untracked file. |
| `tests/alis/test_source_registry.py` | Untracked file. |
| `tests/alis/test_registry_integration.py` | Untracked file. |
| Target skeleton folders | Not present: `src/`, `artifacts/`, `legacy/`, `docs/migration/`, `tests/alis_core/`, `tests/godatabank/`. |

This review did not change the repository state.

## 5. Review Scope

The review scope is limited to `backend/alis/source_registry.py`.

The review may reference `sources/source_registry.json`,
`tests/alis/test_source_registry.py`, and
`tests/alis/test_registry_integration.py` only to understand dependencies and
test implications.

The review does not assess any other backend source, tests, generated artifacts,
runtime logs, data files, report outputs, bytecode caches, or skeleton folders.

## 6. Non-Authorised Actions

This review does not authorise:

- staging files;
- committing files;
- moving files;
- renaming files;
- deleting files;
- cleaning generated artifacts;
- creating skeleton folders;
- refactoring code;
- changing imports;
- implementing engines;
- restructuring the repository;
- modifying `.gitignore`;
- promoting fixtures;
- creating runtime storage;
- editing `backend/alis/source_registry.py`;
- editing `sources/source_registry.json`;
- editing `tests/alis/test_source_registry.py`;
- editing `tests/alis/test_registry_integration.py`.

## 7. Summary of Candidate Behaviour

`backend/alis/source_registry.py` defines a `SourceRegistry` class that:

- accepts a JSON path during initialisation;
- checks that the JSON file exists;
- loads the JSON file with `json.load`;
- stores `data.get("sources", [])` as `self.sources`;
- lists source short names with `list_sources`;
- returns a source dictionary by `short_name`;
- filters sources by indicator category, geography, group, and publication type;
- returns `True` from `validate_source_access` when a source exists and
  `access_type` is `public`;
- returns unique group tags from the loaded source list.

The module docstring and class docstring describe the loaded JSON as canonical.
That wording conflicts with the Thoth Registry Design because
`sources/source_registry.json` is explicitly not approved as production
canonical registry state.

## 8. Thoth Responsibility Alignment

The candidate is directionally related to Thoth because it handles registry-like
source metadata lookup. It does not yet implement the frozen Thoth registry
contract.

Alignment:

- It is concerned with source metadata.
- It exposes read-oriented lookup behavior.
- It could be a prototype seed for later Thoth registry implementation review.

Misalignment:

- It treats a JSON path as registry authority.
- It does not model Source Registry Entries.
- It does not record provenance, lineage, checksums, schema references, contract
  references, mutation records, or registry failures.
- It does not separate prototype data, fixture data, and canonical production
  registry state.
- It does not fail closed against missing policy, schema, lineage, checksum, or
  admission evidence.

## 9. Boundary Check Against Arya

Arya owns source proposal, source admission requests, and retrieval planning.

The candidate does not explicitly create Source Proposals, Source Admission
Requests, or Retrieval Manifests. However, `filter_sources` can be used for
source selection, which may overlap Arya retrieval planning if treated as more
than read-only registry lookup.

Boundary result: acceptable only as a read-only registry helper prototype. Any
future implementation must ensure source selection, proposal creation, and
retrieval planning remain outside Thoth unless explicitly defined as read-only
metadata lookup.

## 10. Boundary Check Against Hermes

Hermes owns transport, external I/O, retrieval execution, raw transport
artifacts, and Retrieved Evidence Packages.

The candidate does not retrieve external data or call remote endpoints. It does
store and expose source URLs through dictionaries loaded from JSON, and it may
support endpoint lookup later.

Boundary result: no direct Hermes implementation is present, but future revision
must keep endpoint metadata read-only and prevent URL presence or source lookup
from becoming retrieval authority.

## 11. Boundary Check Against Aegis

Aegis owns governance, validation, policy gates, source admission gate decisions,
and evidence validation.

The candidate includes `validate_source_access`, which returns `True` when
`access_type` is `public`. This is a policy-like access check and could overlap
Aegis if treated as approval or admission authority.

Boundary result: high-risk overlap. Future revision must either remove policy
decision semantics from Thoth or reframe the method as metadata inspection only.
Any true access approval must reference Aegis gate decisions and fail closed
when required policy evidence is absent.

## 12. Boundary Check Against Abacus

Abacus owns analytical transformation, execution planning, and statistical
output.

The candidate does not perform analysis. Its filtering by geography, indicator
category, and publication type could be consumed by analytical workflows, but it
does not calculate metrics or produce Analysis Packages.

Boundary result: no direct Abacus ownership breach observed. Future revision
must keep analytical planning and evidence selection outside Thoth unless
provided as read-only registry metadata.

## 13. Boundary Check Against Apollo

Apollo owns rendering, publication packaging, publication manifests, and
publication assembly.

The candidate does not render pages, create publication packages, or assemble
publication manifests. It exposes source metadata that Apollo may later consume
for citations or provenance-linked publication output.

Boundary result: no direct Apollo ownership breach observed. Future revision
must ensure publication formatting, citation rendering, and manifest assembly
remain outside the registry implementation.

## 14. Boundary Check Against Argus

Argus owns observability, audit trails, health, alerts, and incidents.

The candidate does not emit structured audit events, health records, alerts, or
incident timelines. It also does not preserve failed registry attempts as audit
records, which the Thoth boundary expects for registry failure behavior.

Boundary result: no direct Argus ownership breach observed, but the candidate
lacks required audit-facing failure records. Future revision should expose
registry failure information for Argus observation without making Argus the
registry decision owner.

## 15. Product-Layer Boundary Check

The candidate docstring refers to the "GoDataBank ALIS Source Registry" and
loads a GoDataBank source registry JSON file. This creates product-layer
coupling risk.

Boundary result: product-layer risk present. A future Thoth implementation
should define ALIS Core registry contracts independently from GoDataBank product
catalogue presentation, while allowing product-specific layers to consume
read-only registry metadata through public contracts.

## 16. Canonical Registry Authority Check

The candidate is not suitable as a production-ready canonical registry
implementation in its current form.

Reasons:

- It describes the JSON registry as canonical.
- It depends on caller-supplied JSON path authority.
- It does not distinguish production state, prototype data, fixture data, or
  runtime state.
- It does not enforce Aegis admission decisions.
- It does not create Thoth mutation, provenance, lineage, checksum, schema, or
  contract records.

Conclusion: the file must not be accepted as production canonical registry
implementation while it treats `sources/source_registry.json` or any JSON path
as canonical production state.

## 17. Dependency on sources/source_registry.json

The implementation is structurally dependent on a JSON file path supplied during
initialisation. The observed tests pass `sources/source_registry.json` as that
path.

Risk:

- The candidate can make prototype JSON appear authoritative.
- Tests can lock in current JSON shape and path.
- The implementation does not mark the JSON file as prototype, fixture-only, or
  non-production.

Conclusion: this dependency is acceptable only for prototype review. It blocks
baseline acceptance until storage and fixture policy are explicitly resolved.

## 18. Source Registry Entry Contract Gap Analysis

The Thoth Registry Design defines a future Source Registry Entry concept with
canonical identity, authority, endpoint references, lifecycle state,
provenance, lineage, schema references, checksum policy, and mutation records.

Observed gap:

- The candidate loads untyped dictionaries from JSON.
- It does not define a Source Registry Entry model.
- It does not validate required entry structure.
- It does not distinguish canonical entry records from source catalogue rows.

Conclusion: major contract gap. The candidate is a helper prototype, not a
Source Registry Entry implementation.

## 19. Required Fields Gap Analysis

Required design fields include canonical registry entry identifiers, registry
entry versions, source keys, owners, source types, statuses, admission decision
references, admission request references, endpoint references, provenance
records, lineage roots, schema references, contract references, checksum policy
references, timestamps, owning engine, and mutation references.

Observed gap:

- The candidate assumes source dictionaries with fields such as `short_name`,
  `indicator_categories`, `geography`, `groups`, `publication_types`, and
  `access_type`.
- It does not require the Thoth required field set.
- It does not reject incomplete registry entries except when the file path is
  missing.

Conclusion: major required-field gap.

## 20. Canonical Identifier Gap Analysis

The Thoth design requires stable Thoth-owned canonical identifiers that are not
raw URLs, display names, or short names alone.

Observed gap:

- The candidate uses `short_name` for lookup.
- The integration context maps `short_name` into a `canonical_id` value.
- No Thoth-owned canonical identifier policy is implemented.

Conclusion: major canonical identifier gap. `short_name` is insufficient as
canonical registry authority.

## 21. Provenance Gap Analysis

The Thoth design requires provenance records for admission, mutation, actor,
timestamp, prior state, mutation reason, and supporting evidence.

Observed gap:

- The candidate does not create or read provenance records.
- It does not reference Arya admission requests.
- It does not reference Aegis gate decisions.
- It does not preserve prior registry state.
- It does not record mutation reasons or failed registry attempts.

Conclusion: major provenance gap.

## 22. Lineage Gap Analysis

The Thoth design requires lineage from source admission through retrieval,
evidence validation, analysis, publication, and audit references.

Observed gap:

- The candidate does not define lineage records.
- It does not link source entries to retrieval manifests, raw artifacts,
  evidence packages, validation reports, analysis packages, publication
  packages, or audit records.
- It can infer source relation from `short_name` or URL, which is not sufficient
  for canonical lineage.

Conclusion: major lineage gap.

## 23. Checksum Gap Analysis

The Thoth design requires checksum record references for registry entries,
registry snapshots, source-derived artifacts, and mutation verification.

Observed gap:

- The candidate does not compute, read, store, or verify checksums.
- It does not distinguish registry snapshot checksums from source data
  checksums.
- It does not record checksum algorithm, scope, timestamp, or verification
  status.

Conclusion: major checksum gap.

## 24. Schema/Contract Reference Gap Analysis

The Thoth design requires explicit schema and contract references for Source
Registry Entries, provenance records, lineage records, checksum records, Aegis
decisions, and Arya admission requests where applicable.

Observed gap:

- The candidate has no schema reference handling.
- The candidate has no contract version handling.
- It relies on implicit JSON shape and Python dictionary access.

Conclusion: major schema/contract reference gap.

## 25. Source Status Model Gap Analysis

The Thoth design requires a source status model including states such as
`proposed`, `admission_requested`, `admitted`, `active`, `suspended`,
`deprecated`, `retired`, `rejected`, `fixture_only`, and `prototype`.

Observed gap:

- The candidate does not model source status.
- It does not distinguish prototype, fixture-only, admitted, active, suspended,
  deprecated, retired, or rejected sources.
- `validate_source_access` can return `True` without status-state review.

Conclusion: major source-status gap.

## 26. Mutation-Rule Gap Analysis

The Thoth design requires controlled, auditable, append-only registry mutation
rules.

Observed gap:

- The candidate is read-only after JSON load.
- It does not implement create, update, suspend, retire, reject, or deprecate
  flows.
- It does not create mutation records.
- It does not preserve previous state.
- It does not enforce Thoth-only canonical mutation authority.

Conclusion: mutation support is absent. Read-only helper behavior is not enough
for canonical registry implementation.

## 27. Validation-Rule Gap Analysis

The Thoth design requires registry validation for required fields, identifier
uniqueness, alias collision, status transitions, Aegis decision references,
Arya admission references, provenance, lineage, checksums, schema references,
fixture isolation, prototype isolation, and fail-closed behavior.

Observed gap:

- The candidate validates only file existence and simple public access metadata.
- It does not validate registry entry completeness or consistency.
- It does not fail closed when admission, provenance, lineage, checksum, schema,
  or contract evidence is missing.
- It may conflate metadata inspection with policy validation.

Conclusion: major validation-rule gap.

## 28. Storage-Policy Gap Analysis

The Thoth design does not approve production registry storage and explicitly
does not treat `sources/source_registry.json` as production canonical storage.

Observed gap:

- The candidate accepts a JSON file path as its storage mechanism.
- It does not distinguish source-controlled prototype data, fixtures, runtime
  storage, or canonical production storage.
- It has no migration, retention, or storage authority model.

Conclusion: major storage-policy gap. The candidate must remain blocked until
storage policy is approved.

## 29. Fixture-Policy Gap Analysis

The Thoth design does not approve fixture promotion for
`sources/source_registry.json`.

Observed gap:

- The candidate can load the current JSON without marking it as fixture-only.
- The observed tests depend directly on the JSON path.
- There is no fixture namespace, fixture status, or production isolation.

Conclusion: fixture-policy gap. The candidate cannot be accepted with tests
that make prototype data look production-authoritative.

## 30. Runtime-State Gap Analysis

The candidate does not create runtime storage, but it also does not define a
runtime-state boundary.

Observed gap:

- Runtime caches, registry state, source data, and fixture data are not
  explicitly separated.
- The implementation provides no policy for durable runtime registry state.
- No runtime storage design exists.

Conclusion: runtime storage is not created by the candidate, but runtime-state
policy remains unresolved.

## 31. Source-Control Suitability

The candidate is not suitable for immediate source-control baseline acceptance.

Reasons:

- It is untracked and source-registry-blocked.
- It conflicts with the design by describing prototype JSON as canonical.
- It lacks required Thoth contract features.
- It depends on a blocked modified tracked JSON file.
- It has test implications that also remain blocked.

Future source-control eligibility requires a separate revision plan and narrow
authorisation. This review does not authorise staging or commit.

## 32. Test Implications

The observed tests depend directly on this candidate and
`sources/source_registry.json`.

Implications:

- `tests/alis/test_source_registry.py` currently tests prototype helper
  behavior, not the full Thoth Registry Design.
- `tests/alis/test_registry_integration.py` crosses registry lookup, source
  selection, access validation, and evidence-package-like mapping.
- Both tests remain blocked until implementation, fixture policy, and
  integration-test policy are resolved.

No test is authorised for staging or commit by this review.

## 33. Acceptance Risks

| Risk | Severity | Reason |
| --- | --- | --- |
| Prototype JSON becomes canonical production registry state. | High | Candidate docstrings describe JSON as canonical. |
| Aegis policy authority is absorbed by `validate_source_access`. | High | Public access metadata is treated as access validity. |
| Arya source planning is absorbed by registry filtering. | Medium | Filtering can be used as source selection. |
| Test fixtures are promoted accidentally. | High | Tests depend directly on the blocked JSON path. |
| Thoth design gaps are hidden by helper simplicity. | High | Missing provenance, lineage, checksum, schema, contract, mutation, status, and fail-closed validation support. |
| Product-layer assumptions enter ALIS Core. | Medium | Candidate names GoDataBank registry behavior directly. |

## 34. Deferral Reasons

The candidate should be deferred because:

- it is a prototype/helper rather than a full Thoth registry implementation;
- it depends on blocked registry data;
- it treats or describes that data as canonical;
- it lacks the Source Registry Entry contract;
- it lacks provenance, lineage, checksum, schema/contract, source-status,
  mutation, and validation support;
- it may overlap Aegis policy checks through access validation;
- it may overlap Arya planning through filtering/source selection;
- it requires a revision plan before any baseline acceptance.

## 35. Candidate Disposition Recommendation

Recommendation: Keep blocked.

Justification:

`backend/alis/source_registry.py` is a Thoth implementation candidate only, but
the current file should not be accepted for later narrow authorisation without a
revision plan. It currently behaves as a prototype JSON helper, depends on
`sources/source_registry.json`, describes the JSON as canonical, and does not
implement the frozen Thoth Registry Design.

Later path:

1. Create a Thoth Registry Implementation Revision Plan.
2. Define how the implementation will remove production-authority assumptions
   from prototype JSON loading.
3. Define the future Source Registry Entry model and required validation
   behavior before implementation work.
4. Review revised source and tests under separate narrow authorisation.

This review does not authorise staging, commit, edits, fixture promotion, or
runtime storage.

## 36. Files Remaining Blocked

The following files remain blocked:

| File | Reason |
| --- | --- |
| `backend/alis/source_registry.py` | Prototype/helper candidate requiring revision plan before baseline acceptance. |
| `sources/source_registry.json` | Transitional prototype data or possible future fixture candidate; not canonical production state. |
| `tests/alis/test_source_registry.py` | Depends on blocked source and blocked JSON data. |
| `tests/alis/test_registry_integration.py` | Depends on blocked source/data and unresolved integration policy. |

Blocked means no staging, no commit, no edit, no move, no delete, no fixture
promotion, no runtime storage, and no implementation work.

## 37. Explicit Exclusions

This review explicitly excludes:

- `sources/source_registry.json` edits or promotion;
- `tests/alis/test_source_registry.py` edits or acceptance;
- `tests/alis/test_registry_integration.py` edits or acceptance;
- all other `backend/` paths;
- all other `tests/` paths;
- generated artifacts;
- runtime logs;
- data files;
- reports;
- `.pyc` files;
- `__pycache__/` folders;
- `.gitignore`;
- skeleton folders;
- migration folders;
- fixture promotion;
- runtime storage creation;
- source-control staging or commits.

## 38. Risks

| Risk | Severity | Control |
| --- | --- | --- |
| Candidate is staged as harmless helper despite canonical wording. | High | Keep blocked until revision plan removes authority ambiguity. |
| JSON path dependency pulls blocked data into baseline. | High | Keep `sources/source_registry.json` blocked and review fixture/storage policy separately. |
| Tests are accepted before source contract is accepted. | Medium-high | Keep registry tests blocked until source and fixture path are clear. |
| Aegis policy responsibility is blurred. | High | Treat `validate_source_access` as a redesign item. |
| Future revision overcorrects into implementation without authorisation. | Medium | Require a separate revision plan before code changes. |

## 39. Abort Conditions

Any future milestone touching this candidate must abort if:

- staged files exist outside the authorised scope;
- `backend/alis/source_registry.py` is edited without explicit source-edit
  authorisation;
- `sources/source_registry.json` is treated as production canonical state;
- fixture promotion is attempted without fixture authorisation;
- runtime storage is created without storage authorisation;
- tests are staged before source and fixture policy are approved;
- Aegis policy checks are implemented under Thoth without a boundary decision;
- Arya source planning or Hermes retrieval behavior is absorbed into Thoth;
- generated artifacts, logs, data, reports, `.pyc`, `__pycache__/`, `.gitignore`,
  or skeleton folders enter the scope.

## 40. Recommended Next Milestone

The next milestone should be:

Independent Review of Narrow Thoth Registry Implementation Candidate Review
v1.0.

After independent approval, a later planning milestone may create:

Thoth Registry Implementation Revision Plan v1.0.

That later plan should remain planning-only unless a separate authorisation
explicitly permits source edits.

STATUS: NARROW THOTH REGISTRY IMPLEMENTATION CANDIDATE REVIEW CREATED
CANDIDATE: backend/alis/source_registry.py
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
