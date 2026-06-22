# ALIS Core Codex Readiness Remediation Plan v1.0

## 1. Purpose

This document defines the planning-only remediation plan for the ALIS Core and GoDataBank repository. It outlines the specific technical, structural, and environmental blockers that must be resolved before the repository can be declared ready to receive any future Codex implementation packages.

**This plan is documentation only.** It does not authorise staging, committing, file movement, renaming, deletion, cleanup, skeleton folder creation, code refactoring, import changes, engine implementation, repository restructuring, `.gitignore` modification, fixture promotion, runtime storage creation, or edits to source, test, or registry files.

**Current Operational Status:**
* Codex implementation is paused.
* Codex may continue only with narrow planning/review documents.
* No source implementation is authorised.
* No test implementation is authorised.
* No registry implementation is authorised.
* No cleanup is authorised.
* No `.gitignore` change is authorised.
* No skeleton creation is authorised.
* No migration is authorised.
* No staging or commit is authorised.

---

## 2. Source Documents Reviewed

The following architectural and review documents were audited in the preparation of this plan:
* [ALIS_CORE_BOUNDARY_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md) (Governing engine boundaries and artifact ownership)
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md) (Thoth registry specifications)
* [ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md) (Source/test baseline review plan)
* [ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md) (Source/test candidate classifications)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md) (Registry authority decisions)
* [ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md) (Registry review plan)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md) (Narrow registry implementation candidate review)

---

## 3. Gemini Readiness Verdict Summary

**Verdict: CODEX NOT READY**

The repository is not in a suitable state to receive implementation code. The key reasons for this verdict are:
1. **High Boundary Debt**: GoDataBank product-specific logic (layouts, visualizations, static page generation, Cloudflare checks) is tightly coupled within the platform backend package (`backend/alis`).
2. **Registry Non-Compliance**: The prototype registry module treats an unapproved, source-controlled JSON file as canonical authority, missing mandatory Thoth design features (canonical identifiers, lineage records, checksums, provenance records, and mutation history).
3. **Repository Hygiene Debt**: The workspace is cluttered with Python bytecode caches (`.pyc` and `__pycache__`), local runtime logs, and generated raw/classified data files.
4. **Shell/Environment Degradation**: Environment-level PowerShell configuration issues prevent the execution of standard git commands, blocking automated staging and release validation.

---

## 4. Current Repository Readiness State

* **Staged Files**: None.
* **Modified Tracked Files**: 13 files (representing a mixture of prototype logic, tracked data, and logs).
* **Untracked Paths**: 249+ paths (including 81 backend source files, 83 test files, and numerous bytecode caches).
* **Target Skeleton Folders**: Absent (missing `src/`, `artifacts/`, `legacy/`, `docs/migration/`, `tests/alis_core/`, and `tests/godatabank/`).
* **Tool/Command Capability**: Degraded. Powershell execution is currently unable to load the `FileSystem` provider, throwing a `DriveNotFoundException` on `git` or `cmd.exe` invocations.

---

## 5. Codex Readiness Blockers

Codex cannot begin implementation due to three primary classes of blockers:
1. **Tool and Infrastructure Blockers**: The inability of the agent to execute git or file commands under PowerShell prevents automated staging, workspace resets, and baseline validation.
2. **Architectural Blockers**: The absence of target skeleton directories and the lack of separation between ALIS Core (platform) and GoDataBank (product) mean any new code would be placed in coupled directories.
3. **Data Registry Blockers**: The lack of an approved, non-production storage policy for Thoth metadata registry entries prevents the baseline integration of registry components.

---

## 6. Repository Hygiene Blockers

The active development directory contains untracked bytecode, log files, and generated output datasets in the source tree. This hygiene debt:
* Distorts `git status` output.
* Obscures tracking of functional source code changes.
* Risks committing OS-specific bytecode or sensitive execution logs to the canonical repository history.
* Prevents automated clean-build verification.

---

## 7. Shell/Environment Reliability Blocker

The terminal environment fails to resolve the standard `Microsoft.PowerShell.Core\FileSystem` drive provider. As a result, directory-level context is lost, and the agent is blocked from running `git status`, `git diff`, `git add`, or invoking system commands. Standard PowerShell/CMD terminal interaction is completely degraded and must be stabilized before any staging, cleanup, or automated test runners can run.

---

## 8. Modified Tracked File Blockers

Thirteen modified tracked files remain in the working directory. Staging them in their current mixed condition is blocked because they contain:
* Unresolved line-ending warnings.
* Outdated prototype code.
* Runtime log output and generated data records.

These files must be individually preserved, reverted, or separated under narrow documentation review before any baseline commit.

---

## 9. Untracked Source Candidate Blockers

Eighty-one untracked files are present in the `backend/` directory. They cannot be staged because:
* They are grouped under a broad `backend/alis` package that violates the engine boundaries defined in the Boundary Register.
* Product-layer code (e.g., HTML page layout and Cloudflare upload scripts) is mixed with engine-layer code (e.g., connectors, validators).
* Deferrals and rejections of duplicate modules (such as duplicate World Bank and ONS connectors) remain unresolved.

---

## 10. Untracked Test Candidate Blockers

Eighty-three untracked test files in `tests/alis/` are blocked because:
* They mirror the coupled structure of the backend source candidates.
* They are placed under a flat namespace (`tests/alis/`) rather than being separated into engine unit tests (`tests/alis_core/`) and product integration tests (`tests/godatabank/`).
* Unit tests for Thoth, Aegis, and Hermes depend on blocked data fixtures and unapproved storage layouts.

---

## 11. Source-Registry Blockers

The source registry remains blocked because:
* The registry data candidate (`sources/source_registry.json`) does not define Thoth canonical identifiers, provenance links, lineage roots, or Aegis gate approval references.
* It is treated as production authority by prototype code, violating the Thoth design constraints.
* The boundary between Arya (admission request), Aegis (gate decision), and Thoth (canonical record) is not enforced in the registry schema or code.

---

## 12. Line-Ending Blockers

Tracked files (including [classifier.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/abacus/classifier.py), [taxonomy.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/abacus/taxonomy.py), [validator.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/validators/validator.py), and `README.md` files) are blocked by line-ending format warnings. Line endings must not be remediated while retention and repository restructuring choices are pending, to avoid mixing format changes with structural reviews.

---

## 13. Generated Artifact Blockers

Generated data files (e.g., [evidence_package_output.json](file:///C:/Users/kmudh/Documents/GoDataBank/evidence_package_output.json), files in `data/classified/`, `data/validated/`, and `data/publishing/`, and reports in `reports/`) are mixed with source code. These files must remain blocked from source control. They require a separate artifact retention policy and automated git-exclude rules to prevent them from entering repository history.

---

## 14. Runtime Log Blockers

Runtime log files (such as `data/validated/validator.log`, `data/raw/world_bank/logs/world_bank_connector.log`, and `data/raw/ons/logs/ons_connector.log`) are actively written to the source tree. These must be blocked from staging. Implementing runtime log redirection to non-tracked directories is a prerequisite for repository hygiene.

---

## 15. .pyc and __pycache__ Blockers

Over 100 untracked `.pyc` and `__pycache__/` paths are present in backend and test directories. They must remain blocked from source control. Staging or deleting them is prohibited until a global ignore policy is defined and the shell environment is stabilized to permit a clean checkout.

---

## 16. Skeleton-Folder Absence Blocker

Target folders representing the canonical ALIS Core structure (`src/`, `artifacts/`, `legacy/`, `docs/migration/`, `tests/alis_core/`, and `tests/godatabank/`) do not exist. Staging or creating these folders is blocked until candidate source files are mapped to their respective engine owners and the staging/migration sequence is explicitly authorized.

---

## 17. Core/Product Boundary Blockers

The code violates the Boundary Register:
* Visualisation, static site assembly, and report formatting exist within the platform package `backend/alis`.
* GoDataBank product-facing pages and indices are packaged as core code.
* Apollo generic publication packaging is coupled with product layouts.

These modules must be split into platform engine-owned utilities and product-layer presentation code before any implementation milestone.

---

## 18. Registry Implementation Blockers

The candidate [source_registry.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/alis/source_registry.py) is a read-only prototype helper. It cannot be baselined as Thoth registry code because it lacks:
* A Source Registry Entry schema model.
* Append-only mutation logic.
* Checksum verification.
* Provenance and lineage capture capabilities.
* Aegis policy-gate enforcement checks.

---

## 19. Test-Placement Blockers

All test candidates are located under a unified `tests/alis/` directory. Baselining them is blocked because they do not separate:
* Reusable platform engine unit tests.
* GoDataBank product-layer verification.
* Cross-engine integration tests.

A defined test placement policy and target test folder skeleton are required.

---

## 20. Recommended Remediation Sequence

Remediation must be planned in the following logical sequence:
1. **Stabilize Shell and Git Command Reliability**: Resolve the PowerShell environment and `FileSystem` provider issues to allow local execution of git status and command staging.
2. **Preserve or Dispose of Governance Documents**: Complete the narrow documentation baseline commits to track all planning, review, and design files in git history.
3. **Decide Repository Hygiene Policy**: Define which directories must be excluded from tracking without performing immediate deletions.
4. **Decide `.gitignore` Policy**: Document the rules for ignoring caches, bytecode, data, and logs without editing `.gitignore`.
5. **Decide Generated Artifact/Log/Cache Disposition**: Standardize on local paths for log outputs and generated data outside the repository tree without modifying files.
6. **Continue Source/Test Review via Narrow Groups**: Conduct narrow, file-level reviews for candidates eligible for future staging (e.g., Hermes adapters, shared schemas).
7. **Keep Registry Candidates Blocked**: Prevent staging of registry files until a schema, mutation policy, and non-production storage design are approved.
8. **Prepare Codex Implementation Package**: Assemble the implementation packages only after all structural, boundary, and environmental blockers listed in this plan are resolved.

---

## 21. Planning Milestones Required Before Implementation

Before Codex receives any implementation packages, the following documentation and planning milestones must be completed and approved:
1. **ALIS Core Boundary Register v1.0 Approval**: A formal review and sign-off on engine boundaries.
2. **Thoth Registry Design v1.0 Approval**: Approval of schema, checksum, mutation, and lineage contracts.
3. **Repository Hygiene and Exclude Policy**: Approved guidelines for ignoring caches, logs, and outputs.
4. **Target Skeleton Folder and Migration Plan**: An authorized blueprint defining the destination folders and the file-by-file movement sequence.
5. **Thoth Registry Implementation Revision Plan**: A revision specification addressing the gaps in the prototype registry code.

---

## 22. Conditions Required Before Codex Implementation

Codex implementation may resume only when:
* The terminal environment is fully stabilized, and git commands execute successfully.
* The repository contains a clean, unstaged git working tree.
* All generated artifacts, runtime logs, and bytecode caches are removed or excluded.
* Target skeleton directories are created under separate, authorized milestones.
* The file-by-file boundary register is frozen, separating platform and product logic.

---

## 23. Conditions Required Before Source/Test Baseline Staging

No source or test file may be staged for a baseline commit until:
* The file has passed a narrow, independent review matching its designated engine owner.
* All duplicate implementations (e.g., duplicate connectors or validators) are resolved.
* Line-ending warnings on the target file are corrected in an independent step.
* Registry data and registry tests are decoupled from production-authority claims.

---

## 24. Conditions Required Before Skeleton Creation

Target skeleton folders must not be created until:
* The source migration plan is approved.
* The test-placement policy is defined.
* Import translation rules are drafted to map existing package names (e.g., `backend.alis`) to target structures (e.g., `src.alis_core`).

---

## 25. Conditions Required Before Cleanup or .gitignore Changes

No deletion, cleanup, or `.gitignore` edit may be performed until:
* The repository exclude policy is approved.
* Terminal tools are functional and capable of executing cleanups.
* A narrow cleanup authorization plan is written and approved.

---

## 26. Files/Groups That Must Remain Blocked

The following files and groups are blocked and must not be staged, committed, edited, or moved:
* **Registry Candidates**:
  * [source_registry.json](file:///C:/Users/kmudh/Documents/GoDataBank/sources/source_registry.json)
  * [source_registry.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/alis/source_registry.py)
  * [test_source_registry.py](file:///C:/Users/kmudh/Documents/GoDataBank/tests/alis/test_source_registry.py)
  * [test_registry_integration.py](file:///C:/Users/kmudh/Documents/GoDataBank/tests/alis/test_registry_integration.py)
* **Line-Ending Blocked tracked files**:
  * [classifier.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/abacus/classifier.py)
  * [taxonomy.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/abacus/taxonomy.py)
  * [validator.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/validators/validator.py)
  * [schema.py](file:///C:/Users/kmudh/Documents/GoDataBank/backend/validators/schema.py)
  * `backend/abacus/README.md` and `backend/validators/README.md`
* **Boundary-Blocked Candidates**:
  * `backend/alis/pipelines/**`
  * `backend/alis/publishing/**` (except static manifest validation if reviewed separately)
  * `backend/alis/visualisation/html_chart_embedding.py`
  * `backend/publisher/**` and `backend/publishing/**`
  * Related pipeline, publishing, report, and embedding tests under `tests/alis/`.
* **Exclusions**:
  * All `.pyc` and `__pycache__/` folders.
  * All runtime logs (`data/**/logs/` and `data/validated/validator.log`).
  * All generated datasets and reports in the root, `data/`, and `reports/`.

---

## 27. Files/Groups Eligible Only for Later Narrow Review

The following isolated groups are eligible for narrow, file-level planning review in subsequent milestones:
* **Hermes Connector candidates**: `backend/alis/connectors/ons.py`, `backend/alis/connectors/world_bank.py`, and related unit tests.
* **Shared Schema candidates**: `backend/alis/schemas/evidence_package.py`, `backend/alis/schemas/visualisation_dataset.py`, and related unit tests.
* **Abacus Mapper candidate**: `backend/alis/mappers/evidence_to_visualisation.py` and its matching test file.
* **Apollo Render candidates**: `backend/alis/visualisation/static_chart_renderer.py`, `backend/alis/visualisation/svg_export_integration.py`, and matching tests.

---

## 28. Risks if Codex Implementation Resumes Too Early

Resuming implementation too early will introduce:
1. **Contract and Design Gaps**: Implementation of registry logic will lock in the unapproved, JSON-based storage model instead of a compliant Thoth registry.
2. **Boundary Violations**: Feature development will continue inside the coupled `backend/alis` package, further mixing platform and product concerns.
3. **Staged/Commit Noise**: Committing files in a dirty repository will permanently record bytecode, logs, and generated files in the git history.
4. **Code Churn**: Lack of skeleton directories will force code to be written in temporary folders, leading to massive refactoring and import rewrites when the target structure is introduced.

---

## 29. Abort Conditions

Any future milestone or operation must abort immediately if:
* Files are staged before a narrow staging step is authorized.
* Registry candidates are proposed for staging before a Thoth Registry Design is approved.
* Directory-level or glob-based staging (e.g., `git add .`) is attempted.
* Skeleton folders are created, or files are moved, renamed, deleted, or refactored.
* Imports are changed.
* `.gitignore` is modified without a separate exclude authorization.
* Generated artifacts, logs, bytecode, or cache directories are staged or modified.
* An implementation task is started.

---

## 30. Recommended Next Milestone

The recommended next milestone is:
```text
Independent Review of ALIS Core Codex Readiness Remediation Plan v1.0
```
This review will verify that the technical, architectural, and environmental blockers identified in this plan are fully understood and agreed upon before any further documentation baseline or planning reviews are scheduled.

---

STATUS: CODEX READINESS REMEDIATION PLAN CREATED
CODEX IMPLEMENTATION: PAUSED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
TEST CHANGES: NOT PERFORMED
REGISTRY CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
CLEANUP: NOT PERFORMED
GITIGNORE CHANGES: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
