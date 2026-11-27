# Alice — ALIS Core Architectural Audit and Evolution Plan

**Document ID:** ALICE-AUD-001  
**Version:** 1.0 (proposed)  
**Date:** 27 November 2026  
**Milestone:** M05  
**Status:** Read-only engineering assessment and proposed evolution plan. Documentation only.  
**Audited repository:** AlgorithmAbacus2025/godatabank-lite-2026  
**Audited baseline:** main commit `054114b3d0d711eecca005bfcce708b86b0e616b`; tree `56d70dc32d237913606d011a1dae5eae53c423c5` (complete recursive tree, not truncated).  
**Design dependencies:** M01–M04, review branches/PRs #1–4; pending adoption.

## 1. Executive assessment

Retain the ALIS Core eight-engine architecture and existing GoDataBank product governance. Establish Alice as a separate mission/formulation and coordination layer, not an engine that replaces or bypasses ALIS Core.

The repository provides a useful legacy deterministic World Bank metadata pipeline, a narrowly scoped Thoth registry helper, manual research workbench examples and static report artifacts. These are valuable reusable assets but do not collectively establish a functioning adaptive research agent or full implementation of the eight-engine contracts.

Two concrete compatibility defects are identified by static source inspection: five undefined validator schema constants and an incompatible transitional source registry JSON shape. Neither was corrected during this audit. A further structural gap is that legacy source admission validation occurs after retrieval in the pipeline, whereas the intended ALIS Core contract requires the relevant Aegis admission decision before retrieval.

The previous local repository audit reports substantially more code than is present in this committed snapshot. Reconcile the local working tree, committed history and current governance before rebuilding or migrating anything. No conclusion that those local assets have been deleted is supported.

Recommended sequence: preserve frozen assets; build a segregated P0 formulation demonstrator using simulated capability adapters only after authorisation; establish verified P1 evidence contracts and remediate the existing pipeline in an independently approved scope; integrate one bounded real research mission. Do not introduce new vendors, APIs, databases or large architectural refactors until their necessity is demonstrated.

## 2. Method, sources and limitations

Read-only inspection: GitHub branch metadata, recursive tree, source files, historical review documents, governing policies, workbench examples and current Alice design artifacts.

Controlling documents:

- [Alice Founding Constitution](ALICE_FOUNDING_CONSTITUTION_V1_0.md)
- [Alice System Definition](ALICE_SYSTEM_DEFINITION_V1_0.md)
- [Alice SRS](ALICE_SYSTEM_REQUIREMENTS_SPECIFICATION_V1_0.md), M03, blob `29d0176849d44185088a5f942e8319db24d4ab25`.
- [Alice RFE specification](ALICE_RESEARCH_FORMULATION_SPEC_V1_0.md), M04, blob `143d933d0ed12b8f9490d2000734a784c0626c12`.
- [ALIS Core Boundary Register](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md), V1.0-R1.
- [Thoth Registry Design](architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md).
- [GoDataBank Agent Laws](AGENT_LAWS.md), [Source Admission Rule](SOURCE_ADMISSION_RULE.md), [Pipeline Contract](PIPELINE_CONTRACT_V0_1.md).
- [Historical repository audit](reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md).
- [Thoth narrow implementation freeze](reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_FREEZE_V1_0.md) and [freeze review](reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_FREEZE_REVIEW_V1_0.md).
- [Documentation preservation freeze](reviews/ALIS_CORE_THOTH_REGISTRY_DOCUMENTATION_PRESERVATION_FREEZE_V1_0.md).

The audited implementation snapshot is main, not the stacked Alice documentation branches. The review is not a complete security audit, runtime certification or exhaustive history review. Local uncommitted code, other branches, runtime configuration, live APIs, dependency installations and deployment state have not been audited. No Python tests, imports, pipeline runs or external retrieval calls were performed. Findings of absent implementation mean not found in the inspected committed tree, not proven absent everywhere. Historical documentation describes its own review context, not today's runtime state.

## 3. Inventory and maturity

| Area | Tracked files |
| --- | ---: |
| docs | 60 |
| workbench | 51 |
| backend | 12 |
| data | 9 |
| site | 5 |
| reports | 2 |
| sources | 2 |
| root | 2 |
| scripts | 1 |
| templates | 1 |
| tests | 1 |
| **Total** | **146** |

The tree has 199 entries including directories. There are 16 Python files: eight backend modules, one pipeline runner, one test module and six workbench scripts. No tracked dependency manifest, package/build specification or GitHub Actions workflow was found by tree inspection. This does not rule out external CI or local environments.

Maturity labels: D = design or documented policy only; L = legacy or narrow implementation evidence, not demonstrated compliant with new contracts; F = historical/fixture/output artifact only; N = not found. No component is designated production-ready on this static audit.

The historical repository audit recorded 274 files, 63 Python files, a much larger backend and tests, including Pydantic models, connectors, visualisation and publishing modules. Its local inventory and the present Git tree are different populations. The historical audit mentions directories not present in the audited tree. Neither count establishes that all earlier work was committed, lost, or currently executable. Review other branches/history and the operator's local working tree before making implementation disposition final.

## 4. Component disposition register

| ID | Component and evidence | Maturity | Recommended disposition | Dependency/constraint |
| --- | --- | --- | --- | --- |
| C01 | Arya: source-admission rule, source records and workbench source plans | D/L | Retain policy; develop explicit proposal/admission-request/manifest interfaces | Aegis decision must precede authorised retrieval |
| C02 | Hermes: backend/alis/world_bank_connector.py, config.py; topic-specific fetch scripts | L | Retain transport primitives and normalisation candidates; adapt under reviewed manifest contract | Separate raw transport from evidence validation; no direct bypass |
| C03 | Thoth: backend/alis/source_registry.py; registry design; one registry test module | L | Preserve frozen helper; separately review and complete canonical registry, provenance, checksums, lineage, mutation history | Existing freeze, no production promotion of prototype JSON |
| C04 | Aegis: backend/validators/schema.py and validator.py, source admission JSON | L | Retain validation rules; separately repair baseline incompatibility and extend gate interfaces | F01–F03; no Alice self-approval |
| C05 | Abacus: classifier.py, taxonomy.py; workbench analysis scripts | L | Retain deterministic classification and reusable pure calculations; extend method registry and approved analytical artifact contracts | Abacus alone builds canonical Execution Plan and Analysis Package |
| C06 | Vyasa: backend/summary/summary_generator.py | L | Retain controlled template synthesis; later add claim map and approved synthesis interface | No invented claims or direct calculations |
| C07 | Apollo: templates/report_template.html; site/ and reports/ static artifacts | F/D | Retain outputs/templates; develop reviewed rendering and publication manifest interface when needed | Public promotion deferred; existing gates mandatory |
| C08 | Argus: timestamped connector and validator logs; boundary register | L/D | Retain log evidence patterns; develop structured audit/incident interface | Never replace engine-specific obligations; redact sensitive fields |
| C09 | scripts/run_world_bank_pipeline.py | L | Preserve as legacy regression target; adapt through a new facade only after compatibility and authorisation | Direct fetch/validate/classify, no summary or publication in runner |
| C10 | Workbench topic template, GDP/remittance scripts, ONS and welfare report artifacts | L/F | Preserve manual research workflow and candidate fixtures; review before reuse as evidence | Manual verification is not an Aegis gate; no automatic promotion |
| C11 | sources/source_registry.json | F | Preserve transitional prototype; do not load as canonical or silently change format | F02, frozen registry-data status |
| C12 | data/, site/, reports/ and other produced artifacts | F | Preserve as historical artifacts; classify, provenance-check and approve any fixture use | No deletion, regeneration or publication |
| C13 | tests/alis/test_source_registry.py | L | Preserve, review scope and authorise verification before running/editing | Test status not certified by this audit |
| C14 | Static site index and report pages | F | Retain existing product presentation; create independent P0 UI candidate | No existing adaptive interface located |
| C15 | Alice mission state, RFE, adaptive question selection and approval controller | D/N | Develop new isolated P0 subsystem | M03/M04 requirements; exact schema before implementation |
| C16 | Capability catalogue, model abstraction, policy resolver, persistence | D/N | Develop minimum necessary P0 contracts with simulation | No live connector registry or authority inferred from source registry |
| C17 | Build/dependency management and automated verification | N | Establish separately approved reproducible development/test baseline | First reconcile local assets and permissions |

### 4.1 Concrete evidence

- World Bank connector uses urllib.request, a fixed Documents & Reports API query, timeout and JSON storage. Its README explicitly limits it to one publication metadata retrieval path; it is not a general research API.
- Registry helper defines SourceRegistryEntry and SourceRegistry, enforces Thoth-owned identifiers and requires production reference fields. Its docstring explicitly excludes network retrieval, gate decisions and analytics. It declares provenance, lineage, mutation-history and checksum handling incomplete.
- Validator inspects metadata and admission records and writes a legacy approved JSON artifact; classifier accepts records carrying APPROVED status, applies fixed keyword taxonomies and writes classified JSON. This is not equivalent to validating a canonical Aegis evidence package with verified gate and provenance references.
- Summary generator accepts CLASSIFIED records, creates fixed-template JSON and citation blocks. It is not an AI synthesis or canonical claim-to-evidence map implementation.
- Manual GDP workbench analysis reads fetched raw JSON, filters null values and calculates latest/minimum/maximum values. Its verification note explicitly limits nominal GDP claims and states draft-only publication status. This is a useful candidate regression example, not proof of full engine integration.
- Historical publication-gate re-verification and static reports record previous publication work. They do not establish that the current runner regenerates those outputs or that current gates pass.

## 5. Findings and risk register

Severity here refers to proposed Alice integration risk, not a security certification.

| ID | Severity | Finding and evidence | Required action / exit criterion |
| --- | --- | --- | --- |
| F01 | High | Validator references five constants absent from current schema.py (see below). | Review intended contract, separately authorise minimal correction and negative/positive tests; verify fixture pipeline before any live integration. |
| F02 | High | Registry JSON's sources is an object, but SourceRegistry._load_prototype_json requires a list. | Preserve both frozen assets; establish explicit fixture/conversion policy if authorised; never silently normalise into production authority. |
| F03 | High | Legacy runner calls world_bank_connector.run before validator.validate_file; admission validation is downstream of retrieval. | Preserve old flow as legacy; P1 must check authorised admission/manifest before network I/O and evidence validation before analysis. |
| F04 | High | Historical local audit inventory differs materially from GitHub snapshot. | Reconcile read-only local tree, branches/history, generated/untracked assets and governance; classify actual missing capabilities before reconstruction. |
| F05 | High | Eight engine contracts are not end-to-end implemented in inspected snapshot. | Establish interface and ownership acceptance per engine; use isolated simulators until verified. |
| F06 | High | No adaptive formulation, version-bound approval or server-side capability control implementation found. | Deliver P0 according to M04 and SRS, including negative tests. |
| F07 | High | Registry helper explicitly defers production provenance/lineage/mutation/checksum behaviour; prototype reference presence is not proof of valid references. | Separate Thoth milestone; prove referential integrity and provenance through Aegis/Thoth contracts. |
| F08 | Medium | Legacy approved/classified status fields and path references are not sufficient canonical integrity proof. | Define adapters and immutable artifact/version/digest verification; reject arbitrary user-written approval flags. |
| F09 | Medium | Only one tracked test module; no tracked dependency manifest or CI workflow found. | Review existing local tests; separately authorise controlled baseline, reproducible environment and CI/test scope. |
| F10 | High | GoDataBank prohibits speculative output and excludes categories required for some wider research domains. | Keep GoDataBank policy unchanged; separately approve research-only policies and isolate artifacts. |
| F11 | Medium | Current RFE specification uses conceptual contract tables, not machine-validated schemas. Some open semantics require resolution. | Define typed field registry, digest serialisation, state/approval guards, blocked-preview handling, budgets and dependency ownership before coding. |
| F12 | Medium | No general evidence discovery, model interface, advanced quantitative engine or survey collection implementation established by this audit. | Defer live expansion; select one P1 domain and verify actual needed capabilities. |

### F01 — exact static compatibility finding

The inspected `backend/validators/schema.py` defines APPROVED_INSTITUTIONS, REQUIRED_FIELDS, FIELD_TYPES, ALIS_DOCUMENT_ID_FIELDS, APPROVED_STATUS and REJECTED_STATUS. `backend/validators/validator.py` additionally refers to:

- SOURCE_ADMISSION_REQUIRED_FIELDS
- SOURCE_ADMISSION_REQUIRED_STRING_FIELDS
- WORLD_BANK_SOURCE_ID
- ADMITTED_SOURCE_STATUS
- VERIFIED_SOURCE_STATUS

All five names are absent from the schema module's inspected source. On the code path where a source-admission file is present and check_source_admission executes against these modules, the first missing attribute is expected to raise AttributeError. The command-line exception handlers may report rejection/failure. This is a static prediction, not an observed runtime test. A prior historical re-verification is not evidence that this precise commit passes.

### F02 — exact static compatibility finding

`sources/source_registry.json` has version 0.1 and a sources mapping keyed by world_bank and ons, both planned. The helper's prototype JSON loader checks isinstance(raw_sources, list) and raises ValueError otherwise. Loading that tracked file through the helper is therefore expected to fail. The existing test uses a temporary list-shaped JSON fixture, not proof of compatibility with the tracked mapping. This is consistent with the helper's explicit non-production boundary; do not fix by granting admission or rewriting the registry data without review.

### F03 — order of admission

The runner calls fetch first and validator second. The new Boundary Register's intended sequence is Arya request -> Aegis admission -> Thoth registration -> Arya manifest -> Hermes transport -> Aegis evidence validation. An existing static admission record is not a per-mission gate/manifest contract. The legacy runner must not be exposed as Alice's unrestricted live tool.

## 6. Target logical architecture

```text
Human operator
  -> Alice interaction layer
  -> Alice formulation / RFE / mission controller
      -> validated review snapshot and approval
      -> capability resolver (policy, permissions, dependencies, limits)
      -> authorised mission orchestration facade
           -> ALIS Core public contracts
                Arya proposal / admission request
                Aegis admission decision
                Thoth registry / provenance
                Arya retrieval manifest
                Hermes transport / retrieved evidence
                Thoth checksum / lineage references
                Aegis validated evidence package
                Abacus canonical execution plan / analysis
                Aegis approval where applicable
                Vyasa synthesis / claim-to-evidence map
                Aegis synthesis approval where applicable
                Apollo publication package if separately authorised
                Aegis publication approval before promotion
                Argus audit throughout; Thoth lineage throughout
      <- outcome references / limitations / evaluation
  <- research findings and proposed next inquiry

GoDataBank remains a separate application consuming approved publication artifacts.
P0: replace live execution facade with simulation; no actual engine invocation.
```

The detailed sequence must follow the Boundary Register, not this simplified diagram where contract-specific order differs. Alice owns proposed mission-level objectives, questions, review snapshots and coordination state; this is distinct from Abacus analytical Execution Plans. Aegis owns approval decisions under its contract; user confirmation of a research scope is not evidence approval, source admission or publication approval. No new engine, authority or canonical ownership change is introduced.

Proposed logical namespaces only, not approved folder moves:
- Alice: interaction, formulation, mission, orchestration, model adapters, evaluation.
- ALIS Core: public engine contracts, shared services, approved engine implementations/adapters.
- GoDataBank: product UI, product policy, publishing consumption.
- Legacy: preserved current files under existing paths until an explicit migration plan is approved.
- Tests/fixtures: separated by unit, contract, integration and product boundaries after authorisation.

Do not create or rename packages in M05. Existing documentation includes prior skeleton and migration proposals; reconcile those before selecting physical layout.

## 7. SRS/RFE gap traceability

| Requirements | Current evidence | Gap / proposed delivery |
| --- | --- | --- |
| RFE-001–015 | Manual topic-to-question workflow; no adaptive implementation located | P0 formulation controller, typed schema, question planner, review UI, versioned state |
| ORC-001–003,009 | Static pipeline and manual controls | P0 simulated capability resolver, bounded lifecycle and cancellation |
| ORC-004–008,010–011 | Legacy runner; boundary register | P1 contracts, gates, safe replanning, checkpoint/approval semantics and replaceable model adapter |
| EVD-001–003 | Source rules, validator, Thoth helper | P1 remediate F01–F03; authorised evidence chain and canonical packages |
| ANA-001–003 | Classifier/taxonomy; isolated workbench calculations | P1 approved analytical methods, missing-data checks and interpretation limits |
| SYN-001–002 | Fixed template summaries and citation block | P1 claim map, category labels, evidence support checks |
| DSC-001–002 | Manual research questions and workbench | P1 labelled hypothesis and discovery proposals, separate from approved factual outputs |
| EVAL-001, OUT-001 | Historical verification notes and static reports | P1 objective-by-criterion evaluation and inspectable outcome |
| OUT-002, EXT-001–003 | GoDataBank governance and manual reports | P2 separately authorised profiles, publication, surveys and monitoring |
| NFR-001–010 | Existing policies, timestamps and one registry test module | P0/P1 enforce and test server-side authority, privacy, contracts, audit, performance, reproducibility and comparison baselines |

This is a grouped requirements gap assessment, not a completed 52-requirement implementation verification. P0 F01–F20 RFE verification scenarios remain unexecuted; P1 evidence metrics require a labelled approved corpus.

## 8. Phased evolution and decision gates

| Stage | Proposed work | Exit evidence |
| --- | --- | --- |
| G0 — baseline reconciliation | Inspect local working tree and repository history/branches read-only; confirm frozen scopes and reconcile available code/test candidates | Signed inventory and source/test/registry disposition; no unresolved assumption that historical files are missing |
| G1 — P0 contract readiness | Review M01–M05; resolve typed field registry, canonical serialisation, approval transitions, simulated catalogue, limits, test authorisation | Versioned executable schemas and test plan approved; no live effects |
| G2 — P0 formulation demonstrator | Isolated implementation of adaptive questioning, validation, review, revision and simulation | RFE F01–F20 executed; SRS targets reported; negative tests pass; no existing runtime mutation |
| G3 — legacy repair and P1 contract readiness | Separate authorisation to resolve F01–F03, verify Thoth references/registry policy, preserve existing evidence | Reproducible offline fixture pipeline, contract tests, reviewed scope and gate compliance |
| G4 — bounded real research prototype | One approved evidence domain, one controlled read-only connector path, one analytical method, evidence-linked outcome | Traceable end-to-end run, objective evaluation, documented errors and limitations |
| G5 — extension | Additional domains, discovery methods, monitoring or publication only after separate approval | Per-domain policy, risk and verification; no dilution of GoDataBank |

G0 and G1 can be assessed in parallel; G2 must remain isolated from frozen source. G3 can be separately planned without delaying P0 simulation, but cannot be bypassed before G4. Implementation and test execution require explicit scoped authorisation. Existing freeze documents remain in force for the reviewed legacy implementation and documentation scopes. M05 is not a replacement freeze or permission to edit legacy source, tests, registry or outputs.

Candidate P1 reference mission: a single official statistical dataset with a clearly defined indicator, geography, time period and deterministic descriptive analysis, potentially reusing the Mauritius GDP workbench as a reviewed fixture. This would exercise scope, admission, retrieval, validation, units, missing values, citations and limitations. It is a candidate, not a selected source or live research authorisation.

## 9. M06 selection criteria

Evaluate tools and libraries against actual gaps, not engine names or novelty. Candidate categories: schema validation, deterministic state transitions, persistence, model adapter, UI, HTTP transport, quantitative methods, testing, logging and provenance. Start with existing Python standard library and available environment; demonstrate need before adding dependencies. Compare local model and optional hosted provider only after security, cost, latency and interface criteria are agreed. No vendor, API key, package, database, hosting service or hardware purchase is selected by this audit.

M06 should record capability/requirement mapping, reuse vs addition, alternatives, licence, compatibility, maintenance, privacy, cost, resource footprint, testing and replacement strategy. P0 must operate with simulation and no live research credentials. P1 requires separately approved connector/evidence policy and contract compliance.

## 10. Verification and unresolved decisions

Before implementation, review scope and status of all stacked PRs in order; independently review this audit. Confirm local code inventory, baseline reproduction, existing test authorisation, canonical mission artifact ownership, exact schema and digest representation, data retention, approved policy domains, capability catalogue authority and whether the P0 subsystem should live in the existing repository or a separate package/repository.

Reviewers should independently inspect F01/F02 using the pinned commit and verify file inventory. If approved, construct isolated offline regression fixtures and execute separately; never infer current run success from historical report artifacts. Review tests for mocked network, stale approval, missing schema fields, blocked tools, policy rejection, provenance and claim support.

This audit deliberately does not perform migration, cleanup, source edits, test edits, registry changes, dependency installation, live research, deployment or merge. The only proposed new artifact is this review document on a dedicated documentation branch, dependent on M04. Existing governance remains unchanged. Numerical targets inherited from M03/M04 remain provisional. Adoption does not authorise implementation.

**M05 conclusion:** Preserve design and existing assets; reconcile committed and local evidence; isolate Alice formulation; verify contracts and remediate legacy gaps before live integration.
