# ALIS Core Thoth Registry Design v1.0

## 1. Purpose

This document defines the future ALIS Core Thoth source registry contract before
any registry source code, registry data, registry tests, fixture promotion, or
runtime storage decision is accepted into the baseline.

The design exists to prevent prototype registry files from becoming canonical
production authority by accident. It establishes what Thoth owns, what it must
not own, how the registry interacts with other ALIS Core engines, and which
current files remain blocked until separate review and authorisation.

## 2. Source Documents Reviewed

The following governing and planning documents were reviewed:

| Document | Use in this design |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Controlling ALIS Core engine boundary contract. |
| `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md` | Registry authority decision and blocked-candidate disposition. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md` | Classification of registry source and test candidates. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md` | Source/test baseline planning constraints. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Repository-level classification and future-location guidance. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Source-control disposition for tracked and untracked path groups. |
| `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` | Remaining dirty/untracked working-tree resolution constraints. |

The following current candidates were assessed without modification:

| Candidate | Observed state | Planning conclusion |
| --- | --- | --- |
| `sources/source_registry.json` | Modified tracked JSON source list with policy metadata and source records. | Transitional prototype data or possible future fixture candidate only. |
| `backend/alis/source_registry.py` | Untracked helper that loads the JSON file and exposes query/access helpers. | Thoth implementation candidate only; not accepted for staging. |
| `tests/alis/test_source_registry.py` | Untracked tests for JSON loading, filtering, lookup, and access checks. | Thoth test candidate pending source acceptance. |
| `tests/alis/test_registry_integration.py` | Untracked integration-style test mapping registry sources into evidence-package-like structures. | Integration test candidate pending source ownership and integration policy. |

## 3. Design Scope

This design defines the conceptual Thoth registry contract, authority model,
metadata model, validation policy, storage policy direction, source-control
policy direction, and test-placement policy direction.

This design does not implement Thoth. It does not accept any current registry
file into the baseline. It does not create storage, fixtures, schemas, tests,
directories, imports, or source-code changes.

The design is limited to ALIS Core source registry authority. Broader Thoth
artifact, schema, provenance, lineage, and checksum services remain governed by
the Boundary Register and require separate implementation design before code is
accepted.

## 4. Non-Authorised Actions

This document does not authorise:

- staging or committing any file;
- moving, renaming, deleting, or cleaning any file;
- modifying `.gitignore`;
- creating `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
  `tests/alis_core/`, or `tests/godatabank/`;
- promoting `sources/source_registry.json` to canonical state;
- promoting registry JSON to fixture status;
- creating runtime registry storage;
- changing imports;
- refactoring source;
- implementing Thoth;
- restructuring the repository;
- modifying registry source code, registry data, registry tests, generated
  artifacts, runtime logs, data, reports, `.pyc` files, or `__pycache__/`
  folders.

## 5. Thoth Registry Responsibility Boundary

Thoth is the ALIS Core metadata, provenance, schema, checksum, contract-reference,
lineage, and registry engine. For source registry concerns, Thoth is the sole
owner of canonical Source Registry Entries and their authoritative lifecycle.

Thoth records source metadata and registry state. Thoth does not decide policy
approval, perform retrieval, validate evidence payloads, generate analysis,
write narrative claims, render publications, or operate as the audit-monitoring
engine.

The core boundary is:

| Concern | Owner |
| --- | --- |
| Source proposal and admission request | Arya |
| Source admission gate and policy decision | Aegis |
| Canonical source registry entry | Thoth |
| Source endpoint retrieval | Hermes |
| Evidence validation and gating | Aegis |
| Analysis consumption of source metadata | Abacus |
| Publication consumption of provenance | Apollo |
| Registry operation observability and audit events | Argus |

## 6. What Thoth Owns

Thoth owns:

- the Source Registry Entry contract;
- canonical source identifiers;
- registry entry lifecycle state;
- source metadata records after admission is approved;
- provenance links for source admission, artifact creation, and registry
  mutation;
- lineage records connecting source entries, retrieved artifacts, validated
  evidence, analytical outputs, and publication packages;
- checksum records for registry snapshots and associated artifacts;
- schema and contract version references used by registry entries;
- registry consistency checks;
- read-only registry lookup contracts for downstream engines;
- append-only registry mutation records;
- registry failure records when a registry operation is rejected or incomplete.

## 7. What Thoth Must Not Own

Thoth must not own:

- Arya source proposals;
- Arya retrieval planning;
- Aegis policy gate decisions;
- Aegis validation reports as decision authority;
- Hermes transport adapters or retrieval retries;
- retrieved evidence payload edits;
- Abacus analytical results;
- narrative claims or explanations;
- Apollo rendered publication output;
- Argus audit policy or incident handling;
- runtime log retention policy;
- product-layer source presentation rules;
- GoDataBank-specific catalogue UX;
- deletion or cleanup decisions for current repository artifacts.

Thoth may reference these artifacts by identifier, version, checksum, and
lineage relation, but it must not become their owner.

## 8. Relationship with Arya

Arya may propose sources, prepare Source Admission Requests, and request
canonical registry linkage after Aegis policy review.

Arya must not create or mutate canonical Source Registry Entries. Arya outputs
are inputs to Thoth only after they are accompanied by the required Aegis gate
decision and provenance context.

Required handoff:

| Arya output | Thoth handling |
| --- | --- |
| Source Proposal | May be referenced as proposal evidence. |
| Source Admission Request | May become registry mutation input after Aegis approval. |
| Retrieval Manifest | May be linked to an admitted source but is not registry authority. |
| Source rationale | Preserved as provenance context, not accepted as policy approval. |

## 9. Relationship with Hermes

Hermes retrieves from approved source endpoints and produces raw transport
artifacts and Retrieved Evidence Packages.

Hermes must not decide whether a source is admitted to the registry. Hermes must
not infer canonical source identity from URLs, endpoint responses, or transport
success.

Thoth may provide Hermes with read-only approved endpoint metadata and source
identifiers. Hermes may return retrieval receipts, artifact identifiers,
timestamps, and checksums for Thoth lineage and provenance registration.

## 10. Relationship with Aegis

Aegis owns governance, validation, policy gates, and boundary enforcement.

Aegis may approve, reject, suspend, or require review of source admission
requests. Thoth records the resulting decision reference and registry lifecycle
state, but Thoth must not replace Aegis gate authority.

Thoth registry mutation must fail closed when required Aegis gate evidence is
missing, contradictory, expired, or outside the current contract version.

## 11. Relationship with Abacus

Abacus may consume read-only registry metadata when planning or performing
analysis over Validated Evidence Packages.

Abacus must not mutate registry authority, alter source status, rewrite source
metadata, or decide source admission. If Abacus detects source metadata
inconsistency, it may emit a finding or escalation request, but Thoth and Aegis
must resolve registry and policy authority respectively.

## 12. Relationship with Apollo

Apollo may consume registry-linked provenance, citations, artifact identifiers,
contract references, and lineage when assembling publication packages.

Apollo must not alter registry state, rewrite source metadata, decide source
status, or treat publication needs as registry authority. Publication manifests
may reference Thoth registry entries, but they do not become registry records.

## 13. Relationship with Argus

Argus observes registry operations, records operational events, captures audit
evidence, and reports health or incident state.

Argus must not own registry decisions or source metadata. Argus records can
support review of registry operations, but they cannot substitute for Arya
source proposals, Aegis gate decisions, or Thoth registry mutation records.

## 14. Source Registry Entry Concept

A Source Registry Entry is the canonical Thoth record for an admitted or
review-tracked source. It describes the source identity, authority, endpoint
references, lifecycle state, provenance, lineage, schema references, checksum
policy, and contract version needed for ALIS Core engines to reference that
source consistently.

A Source Registry Entry is not:

- a raw source catalogue scraped from the web;
- a runtime cache;
- a transport receipt;
- a fixture unless explicitly marked as such;
- a product-facing display model;
- an Aegis policy decision;
- a Hermes retrieval manifest;
- an Apollo publication manifest.

## 15. Required Registry Entry Fields

The future Source Registry Entry contract must define required fields before
implementation. At design level, the required field set is:

| Field | Purpose |
| --- | --- |
| `registry_entry_id` | Stable Thoth-owned canonical identifier. |
| `registry_entry_version` | Version of this registry entry record. |
| `source_key` | Stable machine-safe source key or alias root. |
| `source_name` | Human-readable source name. |
| `source_owner` | Institution, publisher, or accountable data owner. |
| `source_type` | Type of source, such as official statistics provider, API, dataset, publication feed, or internal fixture. |
| `source_status` | Current lifecycle state under the Thoth status model. |
| `admission_decision_ref` | Reference to the Aegis admission or policy gate decision. |
| `admission_request_ref` | Reference to Arya source admission request or approved equivalent. |
| `canonical_endpoint_ref` | Reference to approved endpoint metadata, not necessarily a raw URL. |
| `provenance_record_id` | Thoth provenance record for admission or latest mutation. |
| `lineage_root_id` | Root lineage reference for source-derived artifacts. |
| `schema_ref` | Schema or metadata contract reference governing the entry. |
| `contract_ref` | ALIS Core contract version reference. |
| `checksum_policy_ref` | Checksum policy or checksum record reference. |
| `created_at` | Creation timestamp from the shared clock service. |
| `updated_at` | Last mutation timestamp from the shared clock service. |
| `created_by_engine` | Engine that requested or caused creation; canonical owner remains Thoth. |
| `owning_engine` | Must identify Thoth for canonical registry entries. |
| `mutation_record_ref` | Latest append-only mutation record reference. |

This field list is a design contract direction, not an implemented schema.
Final field names and serialization format require a separate contract file or
schema milestone.

## 16. Optional Registry Entry Fields

Optional fields may be defined later when they are needed by contracts and do
not blur engine ownership:

| Field | Purpose |
| --- | --- |
| `aliases` | Non-canonical names or legacy identifiers. |
| `homepage_url` | Human-facing source homepage. |
| `endpoint_url` | Raw endpoint URL, if policy allows direct storage. |
| `licence_ref` | Licence, terms-of-use, or legal access reference. |
| `citation_template_ref` | Citation template reference for downstream publication. |
| `geographic_coverage` | Coverage description. |
| `temporal_coverage` | Coverage time span. |
| `update_cadence` | Expected source update frequency. |
| `access_requirements` | Authentication, rate limit, or transport constraints. |
| `quality_tier` | Non-decision metadata used by review workflows. |
| `deprecation_ref` | Replacement, retirement, or supersession reference. |
| `fixture_ref` | Explicit fixture reference when a registry fixture is approved. |
| `tags` | Controlled labels for lookup and grouping. |
| `notes` | Non-authoritative human notes. |

Optional fields must not become hidden policy gates. Any field that affects
admission, validation, suspension, or release must reference Aegis decision
authority.

## 17. Canonical Identifier Policy

Thoth owns canonical registry identifiers.

Canonical identifiers must be:

- stable across display-name changes;
- independent of raw URLs where practical;
- opaque enough to avoid embedding policy assumptions in the identifier;
- version-aware when the source identity or contract boundary changes;
- unique within the Thoth registry namespace;
- mapped to aliases separately from the canonical identifier.

Raw URLs, short display names, and organisation names must not be the sole
canonical identifier. They may change, collide, or represent multiple datasets
under a single publisher.

The exact identifier syntax is deferred to a later schema/contract milestone,
but any future syntax must make Thoth ownership explicit and must not imply Arya,
Hermes, Aegis, Abacus, Apollo, Argus, or product-layer ownership.

## 18. Provenance Policy

Every canonical Source Registry Entry must be linked to a Thoth provenance
record.

The provenance record must identify:

- the source admission request or equivalent upstream evidence;
- the Aegis decision reference that allowed or changed registry state;
- the actor, engine, and contract version involved in the mutation request;
- the timestamp from the shared clock service;
- the prior registry state, if the mutation updates an existing entry;
- the mutation reason;
- any source metadata artifacts used to justify the entry;
- checksum references for registry snapshots or relevant artifacts.

Thoth records provenance. It must not fabricate missing upstream evidence or
alter provenance to satisfy validation.

## 19. Lineage Policy

Thoth must preserve lineage from Source Registry Entries to source-derived
artifacts and downstream ALIS Core outputs.

Minimum lineage links include:

- source entry to Arya admission request;
- source entry to Aegis gate decision;
- source entry to Hermes retrieval manifest, when retrieval is performed;
- source entry to retrieved raw artifacts;
- raw artifacts to Retrieved Evidence Packages;
- Retrieved Evidence Packages to Aegis validation reports;
- Validated Evidence Packages to Abacus analysis packages;
- analysis and narrative packages to Apollo publication packages;
- publication packages to Argus audit records where applicable.

Lineage must be explicit. Thoth must reject inferred lineage that lacks an
upstream identifier, checksum, timestamp, or contract reference required by the
current registry contract.

## 20. Checksum Policy

Thoth owns checksum record references for registry entries and source-derived
artifacts, while shared checksum services may provide hashing primitives.

Checksum policy must record:

- algorithm name;
- algorithm version or implementation reference;
- content scope hashed;
- artifact identifier;
- timestamp;
- producing engine or service;
- verification result;
- registry or artifact version;
- mutation record that introduced or verified the checksum.

Registry snapshot checksums must not be confused with source data checksums.
Changing metadata, source payload, or runtime storage state must use the correct
checksum scope.

## 21. Schema/Contract Reference Policy

Every Source Registry Entry must reference the schema and contract version that
governed its creation or mutation.

Registry entries must not depend on implicit code structure as their only
contract. The future implementation must be traceable to explicit schema or
contract references, including:

- Source Registry Entry contract version;
- provenance record contract version;
- lineage record contract version;
- checksum record contract version;
- Aegis decision contract version;
- Arya admission request contract version, where applicable.

Schema and contract references are Thoth-owned metadata records or shared
contract service references. They are not product UI fields.

## 22. Source Status Model

The Thoth source status model must support at least the following states:

| Status | Meaning |
| --- | --- |
| `proposed` | Source has been proposed but is not admitted. |
| `admission_requested` | Arya or an approved requester has submitted an admission request. |
| `admitted` | Aegis gate allows a canonical Thoth entry to exist. |
| `active` | Source may be used by approved workflows. |
| `suspended` | Source is temporarily blocked from use by policy or quality decision. |
| `deprecated` | Source remains historically valid but should not be selected for new work. |
| `retired` | Source is no longer available for new retrieval or use. |
| `rejected` | Source admission was denied. |
| `fixture_only` | Source metadata exists only as an approved test fixture. |
| `prototype` | Transitional non-canonical state for prototype data under review. |

Only Thoth may record the registry status. Aegis owns the policy decision that
permits or blocks status transitions. Hermes transport success must not change
status by itself.

## 23. Registry Mutation Rules

Registry mutation must be controlled and auditable.

Required rules:

- only Thoth may create, update, deprecate, suspend, retire, or reject canonical
  Source Registry Entries;
- every mutation must reference an upstream request, decision, or correction
  authority;
- every mutation must create or update a provenance record;
- every mutation must create a mutation record;
- every mutation must preserve the previous state;
- silent in-place edits are forbidden;
- status changes require Aegis decision references where policy is involved;
- endpoint changes require endpoint metadata review and lineage impact review;
- identity changes require alias/supersession handling rather than overwriting
  the old identity;
- failed mutations must be recorded as failure events for audit and review.

The current repository files do not satisfy these mutation rules as canonical
production state and therefore remain blocked.

## 24. Registry Validation Rules

Thoth registry validation must verify registry consistency. Aegis validation
continues to verify policy and evidence gates.

Thoth registry validation must check:

- required fields are present;
- canonical identifiers are unique;
- aliases do not collide with canonical identifiers;
- source status transitions are allowed;
- Aegis decision references exist where required;
- Arya admission references exist where required;
- provenance records exist and match the mutation;
- lineage references are present and consistent;
- checksum references are present for the required scope;
- schema and contract references are declared;
- endpoint references are valid metadata references, not uncontrolled authority;
- fixture-only entries cannot leak into production workflows;
- prototype entries cannot be treated as admitted or active.

Registry validation failure must fail closed. A failed registry validation must
not be bypassed by Hermes retrieval success, Abacus analysis need, Apollo
publication need, or product-layer convenience.

## 25. Storage Policy

This design does not select or create production registry storage.

Future Thoth registry storage may be source-controlled contract fixtures,
runtime durable storage, an artifact store, a database, or another approved
storage layer. That decision requires a separate Thoth implementation/storage
design milestone.

Policy direction:

- do not treat `sources/source_registry.json` as production canonical storage;
- do not create runtime registry storage in this milestone;
- do not move registry data;
- do not infer storage authority from existing file paths;
- do not mix fixture data, runtime state, and canonical production registry
  state in the same uncontrolled file;
- require a migration plan before any future storage transition.

## 26. Fixture Policy

Registry fixtures may be useful later, but fixture promotion is not authorised
by this design.

Future fixture policy must require:

- explicit fixture status;
- minimal deterministic data;
- no production authority;
- no hidden dependency on live endpoints;
- fixture-specific identifiers or clear fixture namespace;
- placement under an approved test fixture path after skeleton creation is
  authorised;
- tests that cannot accidentally treat fixture entries as production registry
  state.

`sources/source_registry.json` may be reviewed later as a possible fixture
candidate, but it is not approved as a fixture now.

## 27. Runtime-State Policy

Runtime registry state must not be stored implicitly in source files.

Future runtime-state policy must separate:

- canonical registry state;
- runtime caches;
- transport receipts;
- retrieval logs;
- validation reports;
- generated data;
- publication artifacts;
- audit records.

No runtime registry storage is created or authorised by this document. Runtime
state must remain blocked until a storage design, retention policy, security
policy, and migration plan are approved.

## 28. Source-Control Policy

Source control may later contain Thoth registry implementation code, registry
contracts, test fixtures, and tests if each item is separately reviewed and
authorised.

Source control must not accidentally contain:

- production runtime registry state;
- unreviewed prototype registry JSON;
- generated source snapshots;
- runtime logs;
- generated reports;
- bytecode caches;
- source registry files whose authority is unresolved.

The four assessed registry candidates remain excluded from staging and commit
until separate review and authorisation.

## 29. Test Placement Policy

Future Thoth registry tests must be placed according to approved repository
architecture after skeleton creation is separately authorised.

Policy direction:

- Thoth unit tests should verify the Source Registry Entry contract, identifier
  handling, mutation rules, validation rules, provenance references, lineage
  references, and checksum references.
- Registry fixture tests should use explicit fixture data, not production
  registry state.
- Integration tests should live separately from Thoth unit tests when they cross
  Arya, Hermes, Aegis, Abacus, Apollo, Argus, or product-layer boundaries.
- Current tests under `tests/alis/` remain candidates only and must not be moved
  or staged by this design.

No test path is created or changed by this document.

## 30. Treatment of sources/source_registry.json

`sources/source_registry.json` is not production canonical Thoth registry state.

Current assessment:

- it is a modified tracked JSON file;
- it contains prototype source catalogue data and policy-like metadata;
- it lacks explicit Thoth canonical identifiers;
- it lacks Aegis decision references;
- it lacks Arya admission request references;
- it lacks Thoth provenance records;
- it lacks lineage records;
- it lacks checksum records;
- it lacks schema and contract references;
- it lacks mutation records and lifecycle status history.

Required treatment:

- keep blocked from registry baseline acceptance;
- treat as transitional prototype data or possible future fixture candidate;
- do not stage or commit as part of a registry design milestone;
- do not move, delete, clean, or promote;
- require separate fixture, storage, or Thoth registry data authorisation before
  any future action.

## 31. Treatment of backend/alis/source_registry.py

`backend/alis/source_registry.py` is a Thoth implementation candidate only.

Current assessment:

- it is untracked;
- it loads `sources/source_registry.json`;
- its module docstring describes the JSON file as canonical;
- it exposes helper functions for list, lookup, filter, access validation, and
  group extraction;
- it does not implement the full Thoth registry contract defined here;
- it does not enforce provenance, lineage, checksum, mutation, schema,
  contract-reference, or Aegis gate requirements.

Required treatment:

- keep blocked from staging and commit;
- review later against this design and the Boundary Register;
- correct any accidental canonical-language mismatch only in a separate
  authorised source milestone;
- do not refactor, edit, move, or import-adjust in this milestone.

## 32. Treatment of tests/alis/test_source_registry.py

`tests/alis/test_source_registry.py` is a Thoth test candidate pending source
acceptance.

Current assessment:

- it is untracked;
- it imports `backend.alis.source_registry.SourceRegistry`;
- it depends directly on `sources/source_registry.json`;
- it tests prototype helper behavior, not the full future Thoth contract;
- it does not test mutation records, provenance, lineage, checksum, schema
  references, contract references, or Aegis decision requirements.

Required treatment:

- keep blocked from staging and commit;
- review later only after the source implementation candidate is reviewed;
- prevent fixture and production registry authority from being conflated;
- do not move, edit, or promote in this milestone.

## 33. Treatment of tests/alis/test_registry_integration.py

`tests/alis/test_registry_integration.py` is an integration test candidate
pending source ownership and integration test policy.

Current assessment:

- it is untracked;
- it imports `backend.alis.source_registry.SourceRegistry`;
- it depends directly on `sources/source_registry.json`;
- it simulates query selection and evidence-package-like source metadata;
- it crosses registry, retrieval planning, access validation, and evidence
  packaging concerns.

Required treatment:

- keep blocked from staging and commit;
- review later after integration-test policy is approved;
- separate Thoth registry behavior from Arya planning, Hermes retrieval, Aegis
  validation, Abacus analysis, and evidence-package ownership before acceptance;
- do not move, edit, or promote in this milestone.

## 34. Files Remaining Blocked

The following files remain blocked:

| File | Blocker |
| --- | --- |
| `sources/source_registry.json` | Not canonical production state; possible transitional prototype or fixture candidate only. |
| `backend/alis/source_registry.py` | Thoth implementation candidate not reviewed against this design. |
| `tests/alis/test_source_registry.py` | Test candidate depends on blocked implementation and blocked JSON authority. |
| `tests/alis/test_registry_integration.py` | Integration test candidate crosses unresolved ownership and policy boundaries. |

Blocked means no staging, no commit, no movement, no deletion, no cleanup, no
fixture promotion, no import changes, and no implementation changes without
separate authorisation.

## 35. Files Eligible for Later Review, If Any

The following later reviews may be appropriate after independent review of this
design:

| File | Later review type | Condition before review |
| --- | --- | --- |
| `backend/alis/source_registry.py` | Narrow Thoth implementation candidate review. | Confirm intended contract alignment and remove accidental production-authority assumptions under separate authorisation. |
| `tests/alis/test_source_registry.py` | Narrow Thoth test candidate review. | Accept or reject source implementation candidate first. |
| `tests/alis/test_registry_integration.py` | Integration test policy review. | Define integration-test boundaries and fixtures. |
| `sources/source_registry.json` | Fixture or transitional-data review. | Decide fixture policy, storage policy, and non-production status explicitly. |

No file is eligible for immediate staging or commit under this design.

## 36. Generated Artifact Exclusion

Generated artifacts remain excluded from this design and from any registry
baseline action.

Excluded generated artifact groups include:

- `evidence_package_output.json`;
- generated evidence files;
- generated classified data;
- generated summaries;
- generated publication artifacts;
- generated report HTML;
- publication manifests unless separately reviewed;
- any generated registry snapshot or exported registry state.

This design does not authorise artifact cleanup, artifact movement, artifact
retention decisions, or artifact deletion.

## 37. Runtime Log Exclusion

Runtime logs are excluded from registry design acceptance.

Runtime logs under `data/**/logs/`, validation logs, connector logs, and any
future registry logs must not be committed, deleted, moved, cleaned, or treated
as registry source without separate retention and audit review.

Argus may later observe registry operations and record audit events, but this
design does not create an Argus logging implementation or runtime log policy.

## 38. Data/Report Exclusion

Data and report outputs are excluded.

Excluded groups include:

- `data/raw/`;
- `data/validated/`;
- `data/classified/`;
- `data/summaries/`;
- `data/publishing/`;
- `data/published/`;
- `reports/`;
- product publication outputs;
- source-derived snapshots not explicitly approved as fixtures.

Some of these artifacts may later be retained as evidence, fixtures, or release
records, but that requires separate artifact-retention and ownership review.

## 39. .pyc and __pycache__ Exclusion

Bytecode and cache artifacts are excluded.

Excluded groups include:

- `**/*.pyc`;
- `**/__pycache__/`.

This design does not authorise cleaning, deletion, `.gitignore` modification, or
cache movement. Bytecode and cache files must remain outside source/test
baseline decisions unless a separate cleanup authorisation is approved.

## 40. Skeleton-Folder Exclusion

This design does not authorise skeleton folder creation.

The following paths remain excluded from creation:

- `src/`;
- `artifacts/`;
- `legacy/`;
- `docs/migration/`;
- `tests/alis_core/`;
- `tests/godatabank/`.

Future Thoth source, contract, fixture, or test placement must wait until the
target skeleton is independently authorised.

## 41. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Prototype JSON becomes canonical registry state by accident. | High | Keep `sources/source_registry.json` blocked until fixture or storage policy is approved. |
| Existing helper module implies canonical authority before design approval. | High | Treat `backend/alis/source_registry.py` as implementation candidate only. |
| Tests lock in prototype file paths and data shape. | Medium-high | Keep registry tests blocked until source and fixture policies are approved. |
| Thoth boundary overlaps Aegis policy authority. | High | Require Aegis decision references for admission and policy status transitions. |
| Thoth boundary overlaps Arya source proposal work. | Medium | Preserve Arya proposals as inputs, not canonical registry records. |
| Hermes retrieval success is mistaken for source admission. | High | Require Aegis and Thoth registry references before approved use. |
| Fixture data leaks into production workflows. | High | Require explicit fixture-only status and test placement policy. |
| Line-ending or dirty working-tree churn obscures review. | Medium | Keep line-ending review separate from registry design and source acceptance. |
| Skeleton creation is attempted before blockers are resolved. | Medium | Maintain skeleton exclusion until a separate milestone authorises creation. |

## 42. Abort Conditions

Any future registry source/test/data milestone must abort if:

- any staged file is outside its authorised scope;
- `sources/source_registry.json` is proposed as production canonical state
  without approved storage and mutation policy;
- registry tests depend on production registry state rather than approved
  fixtures;
- Aegis decision references are omitted for policy-driven source status;
- Arya admission references are omitted for source admission;
- Hermes transport behavior is used as admission authority;
- provenance, lineage, checksum, schema, or contract references are missing from
  canonical entry design;
- `.gitignore` modification, cleanup, deletion, movement, skeleton creation,
  refactoring, import changes, or implementation work is introduced without
  separate authorisation;
- generated artifacts, runtime logs, data, reports, `.pyc` files, or
  `__pycache__/` folders are included in a registry source/test decision.

## 43. Recommended Next Milestone

The next milestone should be an independent review of this Thoth Registry Design
document.

After independent approval, a later milestone may create a narrow Thoth Registry
source/test candidate review plan. That later plan should continue to keep
`sources/source_registry.json`, `backend/alis/source_registry.py`,
`tests/alis/test_source_registry.py`, and
`tests/alis/test_registry_integration.py` blocked until exact source, fixture,
storage, and test-scope authorisations are written.

STATUS: THOTH REGISTRY DESIGN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
