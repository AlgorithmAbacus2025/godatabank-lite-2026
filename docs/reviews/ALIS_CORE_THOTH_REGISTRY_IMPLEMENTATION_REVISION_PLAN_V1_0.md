# ALIS Core Thoth Registry Implementation Revision Plan v1.0

## 1. Purpose

This document defines a planning-only revision plan for
`backend/alis/source_registry.py`. It describes how the candidate would need to
be revised later to align with the ALIS Core Boundary Register and the Thoth
Registry Design.

This plan does not authorise source edits, staging, commits, fixture promotion,
runtime storage creation, tests, migration, cleanup, or implementation.

## 2. Source Documents Reviewed

| Document | Use in this plan |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing engine boundaries and ownership rules. |
| `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md` | Frozen Thoth registry design contract. |
| `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md` | Candidate review and keep-blocked disposition. |
| `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md` | Source/test candidate review constraints. |
| `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md` | Registry authority and storage/fixture deferral decision. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md` | Source/test classification and blocked registry status. |
| `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md` | Source/test baseline sequencing and exclusion rules. |

The following paths were assessed without modification:

- `backend/alis/source_registry.py`
- `sources/source_registry.json`
- `tests/alis/test_source_registry.py`
- `tests/alis/test_registry_integration.py`

## 3. Candidate Under Revision Planning

| Field | Value |
| --- | --- |
| Candidate path | `backend/alis/source_registry.py` |
| Current status | Untracked |
| Candidate class | Thoth registry implementation candidate only |
| Current disposition | Keep blocked |
| Revision plan status | Planning only |

The candidate remains blocked until a later narrow source-edit authorisation
exists.

## 4. Current Candidate Problems

The current candidate has these planning-level problems:

- it describes `sources/source_registry.json` as canonical;
- it loads caller-provided JSON and treats the `sources` array as registry
  content;
- it stores untyped dictionaries rather than Source Registry Entry records;
- it uses `short_name` for lookup, which is not a Thoth-owned canonical
  identifier;
- it has no provenance records;
- it has no lineage records;
- it has no checksum records;
- it has no schema or contract version references;
- it has no source status model;
- it has no mutation records;
- it does not preserve previous registry state;
- it does not enforce fail-closed registry validation;
- `validate_source_access` risks overlapping Aegis policy authority;
- `filter_sources` risks becoming Arya source-planning authority;
- URL metadata could be mistaken for Hermes retrieval authority;
- its naming and docstrings couple ALIS Core registry behavior to GoDataBank
  product-layer language.

## 5. Non-Authorised Actions

This plan does not authorise:

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

## 6. Revision Principles

Any future revision must follow these principles:

- revise against the Thoth Registry Design, not against the current JSON shape;
- keep `sources/source_registry.json` non-canonical unless separately approved;
- make Thoth responsible for registry metadata, provenance, lineage, checksum,
  schema, contract, status, and mutation references;
- keep Arya responsible for source proposals, admission requests, and retrieval
  planning;
- keep Hermes responsible for transport and retrieval execution;
- keep Aegis responsible for policy gates and validation decisions;
- keep Abacus, Apollo, Argus, and GoDataBank product-layer behavior outside the
  registry implementation;
- require explicit contracts before production implementation;
- fail closed when required registry evidence is absent.

## 7. Required Boundary Corrections

The future revision must correct boundary ambiguity before the candidate can be
considered for source baseline acceptance.

| Boundary | Required correction |
| --- | --- |
| Thoth | Implement or declare only registry metadata and registry contract behavior. |
| Arya | Ensure filtering/lookup does not create source plans or admission requests. |
| Hermes | Ensure endpoint metadata does not trigger retrieval or imply transport approval. |
| Aegis | Ensure access and status checks do not become policy gate decisions. |
| Abacus | Ensure registry lookup does not perform analytical selection or analysis. |
| Apollo | Ensure source metadata is not publication rendering or manifest generation. |
| Argus | Ensure audit observation remains external while registry failures are reportable. |
| GoDataBank product layer | Remove product-specific authority from ALIS Core registry implementation. |

## 8. Required Correction for Canonical JSON Wording

Any future source edit must remove or correct wording that describes
`sources/source_registry.json` as canonical production registry state.

Future wording should distinguish:

- Thoth canonical registry contract;
- prototype data;
- fixture data, if later approved;
- runtime storage, if later approved;
- product-layer catalogue data.

The revised source must not imply that the current JSON file is production
registry authority.

## 9. Required Correction for sources/source_registry.json Dependency

`sources/source_registry.json` must not be a production dependency of the
canonical Thoth registry implementation.

Any future revision must:

- treat JSON loading as prototype or fixture-only unless a separate storage
  policy approves otherwise;
- avoid hard-coding the current path as canonical authority;
- avoid accepting arbitrary JSON path contents as trusted registry state;
- require explicit storage policy metadata before loading registry state;
- reject or quarantine entries that lack required contract references;
- keep runtime storage creation out of the revision unless separately
  authorised.

## 10. Required Thoth Source Registry Entry Model Direction

A future revision should define or reference a Source Registry Entry model before
the implementation is accepted.

The model direction should include:

- a stable Thoth-owned entry identity;
- registry entry version;
- source key and source name;
- source owner and source type;
- source status;
- Aegis admission decision reference;
- Arya admission request reference;
- endpoint metadata reference;
- provenance record reference;
- lineage root reference;
- schema reference;
- contract reference;
- checksum policy or checksum record reference;
- created and updated timestamps;
- owning engine marker;
- mutation record reference.

This plan does not create the model.

## 11. Required Canonical Identifier Direction

Any future revision must stop treating `short_name`, raw URL, or display name as
canonical registry authority.

The revised direction should:

- introduce a Thoth-owned canonical identifier concept;
- preserve aliases separately from canonical identifiers;
- allow `short_name` only as display metadata or lookup alias;
- reject duplicate canonical identifiers;
- reject alias collisions;
- avoid using URL as the primary identity.

## 12. Required Provenance Direction

Any future revision must plan for provenance records before accepting registry
state.

The revised direction should require:

- source admission request reference;
- Aegis decision reference;
- mutation actor or requesting engine;
- mutation timestamp;
- previous-state reference for updates;
- mutation reason;
- supporting source metadata evidence reference;
- failed registry attempt records.

No provenance implementation is authorised by this plan.

## 13. Required Lineage Direction

Any future revision must support explicit lineage rather than inferred
relationships from `short_name`, URL, or source lists.

The revised direction should connect:

- Arya source proposal and admission request;
- Aegis admission gate decision;
- Thoth Source Registry Entry;
- Hermes retrieval manifest;
- raw transport artifact;
- Retrieved Evidence Package;
- Aegis validation report and Validated Evidence Package;
- Abacus analysis package;
- Apollo publication package;
- Argus audit record where applicable.

## 14. Required Checksum Direction

Any future revision must support checksum references and distinguish checksum
scope.

The revised direction should identify:

- registry entry checksum scope;
- registry snapshot checksum scope;
- raw source artifact checksum scope;
- retrieved evidence checksum scope;
- validation and publication artifact checksum scopes;
- checksum algorithm;
- checksum algorithm version;
- verification timestamp;
- artifact identifier;
- mutation reference.

This plan does not authorise checksum implementation.

## 15. Required Schema/Contract Reference Direction

Any future revision must require explicit schema and contract references.

The revised direction should reference:

- Source Registry Entry contract version;
- provenance record contract version;
- lineage record contract version;
- checksum record contract version;
- Aegis gate decision contract version;
- Arya admission request contract version;
- shared contract registry reference.

Implicit JSON shape or Python dictionary access must not be the only contract.

## 16. Required Source-Status Model Direction

Any future revision must implement or reference the Thoth source status model
defined by the design.

The revised direction should distinguish:

- `proposed`;
- `admission_requested`;
- `admitted`;
- `active`;
- `suspended`;
- `deprecated`;
- `retired`;
- `rejected`;
- `fixture_only`;
- `prototype`.

Status transitions must reference Aegis policy decisions where policy is
involved. Prototype and fixture-only records must not leak into production
workflows.

## 17. Required Mutation-Rule Direction

Any future revision must support controlled registry mutation before canonical
use.

The revised direction should require:

- Thoth-only canonical mutation authority;
- append-only mutation records;
- previous-state preservation;
- mutation reason;
- Aegis decision references for policy-driven transitions;
- alias and supersession handling for identity changes;
- failed mutation records;
- no silent in-place edits.

The current helper can remain read-only only if it is explicitly scoped as a
non-canonical prototype or fixture reader.

## 18. Required Validation-Rule Direction

Any future revision must fail closed when registry contract evidence is missing.

The revised direction should validate:

- required fields;
- canonical identifier uniqueness;
- alias collision absence;
- valid source status transitions;
- Aegis decision references;
- Arya admission request references;
- provenance consistency;
- lineage consistency;
- checksum references;
- schema and contract references;
- fixture-only isolation;
- prototype isolation.

Validation must not substitute for Aegis policy gate decisions.

## 19. Required Aegis Boundary Correction

The current `validate_source_access` behavior risks turning public access
metadata into a policy decision.

Any future revision must:

- avoid naming metadata inspection as policy validation;
- avoid returning approval based only on `access_type`;
- reference Aegis gate decisions for policy-relevant access or admission;
- fail closed when Aegis decision references are missing;
- keep evidence validation and policy enforcement outside Thoth.

## 20. Required Arya Boundary Correction

The current `filter_sources` behavior risks becoming source selection or
retrieval planning.

Any future revision must:

- present filtering as read-only registry lookup only;
- avoid creating Source Proposals;
- avoid creating Source Admission Requests;
- avoid creating Retrieval Manifests;
- avoid ranking or selecting sources for analysis without Arya ownership;
- require Arya-owned workflows for planning and admission requests.

## 21. Required Hermes Boundary Correction

The candidate exposes source URL metadata through loaded dictionaries.

Any future revision must:

- treat endpoint data as metadata only;
- avoid network calls;
- avoid retrieval execution;
- avoid retry, receipt, or transport-artifact behavior;
- avoid treating endpoint availability as source admission;
- provide endpoint references for Hermes only through approved public contracts.

## 22. Required Abacus Boundary Protection

Any future revision must protect Abacus ownership.

The revised implementation must not:

- select analytical methods;
- prepare analysis execution plans;
- rank sources for analytical suitability;
- consume Validated Evidence Packages;
- produce Analysis Packages;
- produce chart-ready datasets.

Abacus may consume read-only registry metadata later, but Thoth must not become
an analysis engine.

## 23. Required Apollo Boundary Protection

Any future revision must protect Apollo ownership.

The revised implementation must not:

- render publication output;
- assemble publication packages;
- create publication manifests;
- format product reports;
- alter analytical or narrative outputs for publication.

Thoth may provide registry-linked provenance and citation metadata to Apollo
through public contracts.

## 24. Required Argus Boundary Protection

Any future revision must protect Argus ownership while making registry failures
observable.

The revised implementation should:

- produce registry failure reports or structured failure records under Thoth
  ownership;
- allow Argus to observe registry operations through audit events;
- avoid owning alert, incident, health, or monitoring decisions;
- avoid replacing Argus audit trails.

## 25. Required Product-Layer Decoupling

The current candidate uses GoDataBank product wording in module and class
documentation.

Any future revision must:

- describe ALIS Core Thoth registry behavior independently from GoDataBank
  product catalogue behavior;
- avoid product-specific catalogue assumptions in core registry contracts;
- keep product display names, product navigation, and product UX outside Thoth;
- permit GoDataBank to consume read-only registry metadata later through public
  contracts.

## 26. Storage-Policy Handling

This plan does not approve storage.

Future revision planning must keep storage policy separate:

- do not treat `sources/source_registry.json` as production storage;
- do not create runtime storage;
- do not create artifact storage;
- do not move registry data;
- do not decide source-controlled registry state without storage authorisation;
- document whether the implementation is prototype reader, fixture reader,
  contract adapter, or production storage adapter before source acceptance.

## 27. Fixture-Policy Handling

This plan does not approve fixture promotion.

Future revision planning must:

- keep `sources/source_registry.json` blocked as prototype data or possible
  future fixture candidate;
- require explicit fixture namespace and fixture-only status before tests use
  registry data;
- prevent fixture entries from being admitted or active production sources;
- keep fixture placement blocked until skeleton/test path policy is approved;
- keep tests blocked until fixture policy exists.

## 28. Runtime-State Handling

This plan does not approve runtime state.

Future revision planning must:

- keep runtime caches separate from registry records;
- keep transport receipts separate from registry records;
- keep validation reports separate from registry records;
- keep audit records separate from registry records;
- avoid writing runtime state into source files;
- require separate runtime storage design before durable registry state exists.

## 29. Test Impact Analysis

The current tests depend directly on the blocked implementation and blocked JSON
data.

Test impacts:

- `tests/alis/test_source_registry.py` verifies prototype helper behavior rather
  than the frozen Thoth design.
- `tests/alis/test_registry_integration.py` crosses registry lookup, source
  filtering, access validation, and evidence-package-like mapping.
- Both tests would need revision after source design and fixture policy are
  approved.
- Tests must remain blocked until the revised implementation path and fixture
  policy are approved.
- No test edit is authorised by this plan.

## 30. Proposed Future Source-Edit Scope

A later source-edit authorisation, if approved, should be narrow and limited to
`backend/alis/source_registry.py`.

Possible future source-edit scope:

- correct canonical-production wording;
- decouple ALIS Core Thoth language from GoDataBank product language;
- introduce or reference a Source Registry Entry model;
- separate metadata lookup from Aegis policy decisions;
- separate registry lookup from Arya planning;
- separate endpoint metadata from Hermes retrieval;
- mark JSON loading as prototype or fixture-only unless storage policy is
  approved;
- add fail-closed validation direction for required registry contract evidence;
- document unimplemented mutation, provenance, lineage, checksum, schema, and
  contract behavior as blocked until authorised.

This section is not an execution authorisation.

## 31. Files That Must Remain Blocked

The following files must remain blocked:

| File | Reason |
| --- | --- |
| `backend/alis/source_registry.py` | Source edit requires later narrow authorisation. |
| `sources/source_registry.json` | Not production canonical state; storage and fixture policy unresolved. |
| `tests/alis/test_source_registry.py` | Depends on blocked source and blocked data. |
| `tests/alis/test_registry_integration.py` | Integration policy and fixture policy unresolved. |

## 32. Files Explicitly Not Authorised for Staging

This plan does not authorise staging for:

- `backend/alis/source_registry.py`;
- `sources/source_registry.json`;
- `tests/alis/test_source_registry.py`;
- `tests/alis/test_registry_integration.py`;
- any other `backend/` file;
- any other `tests/` file;
- any generated artifact;
- any runtime log;
- any data or report output;
- `.gitignore`;
- `.pyc` files;
- `__pycache__/` folders;
- skeleton folders.

## 33. Files Explicitly Not Authorised for Editing

This plan does not authorise editing for:

- `backend/alis/source_registry.py`;
- `sources/source_registry.json`;
- `tests/alis/test_source_registry.py`;
- `tests/alis/test_registry_integration.py`;
- `.gitignore`;
- any source file;
- any test file;
- any generated artifact;
- any runtime log;
- any data or report file.

Only this revision plan document is created by this milestone.

## 34. Risks

| Risk | Severity | Control |
| --- | --- | --- |
| Future edit treats prototype JSON as canonical state. | High | Require wording correction and storage policy before acceptance. |
| Metadata lookup becomes Aegis policy approval. | High | Separate metadata inspection from Aegis gate decisions. |
| Filtering becomes Arya retrieval planning. | Medium-high | Define lookup-only behavior and keep planning with Arya. |
| Endpoint metadata becomes Hermes retrieval authority. | Medium-high | Keep endpoint references read-only and transport-free. |
| Product-layer wording leaks into core registry contract. | Medium | Decouple GoDataBank product language from ALIS Core Thoth contract. |
| Tests encode old prototype behavior. | High | Keep tests blocked until revised implementation and fixture policy exist. |
| Source edits begin before authorisation. | High | Require a later narrow source-edit authorisation. |

## 35. Abort Conditions

Any later milestone involving the candidate must abort if:

- source edits are attempted without explicit source-edit authorisation;
- `sources/source_registry.json` is treated as production canonical state;
- fixture promotion is attempted without fixture authorisation;
- runtime storage is created without storage authorisation;
- tests are edited or staged before source and fixture policy are approved;
- `validate_source_access` or equivalent behavior makes Aegis decisions inside
  Thoth;
- filtering behavior creates Arya source plans or retrieval manifests;
- endpoint lookup performs Hermes retrieval;
- Abacus, Apollo, Argus, or product-layer behavior enters the registry source;
- staging includes files outside a future exact authorised scope;
- generated artifacts, logs, data, reports, `.pyc`, `__pycache__/`, `.gitignore`,
  or skeleton folders enter scope.

## 36. Recommended Next Milestone

The next milestone should be:

Independent Review of Thoth Registry Implementation Revision Plan v1.0.

After independent approval, a later milestone may create a narrow source-edit
authorisation plan for `backend/alis/source_registry.py` only. That future
authorisation must continue to exclude `sources/source_registry.json`, registry
tests, fixtures, runtime storage, staging, commits, skeleton creation, migration,
cleanup, and unrelated source changes unless separately authorised.

STATUS: THOTH REGISTRY IMPLEMENTATION REVISION PLAN CREATED
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
