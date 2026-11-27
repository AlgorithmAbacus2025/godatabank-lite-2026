# ALIS Core Readiness Governance Disposition Plan v1.0-R1

## 1. Purpose

This document defines the planning-only disposition plan for the readiness, registry, and review documents created during recent auditing activities. It determines which governance and readiness documents should be preserved in git history, which should remain uncommitted, and details the sequencing of a future narrow documentation-only commit authorisation.

**Current Operational Status:**
* Codex implementation remains paused.
* Source/test implementation remains paused.
* Registry implementation remains paused.
* No cleanup is authorised.
* No `.gitignore` change is authorised.
* No skeleton creation is authorised.
* No migration is authorised.
* No staging is authorised.
* No commit is authorised.
* This plan itself is not authorised for staging or commit until separately reviewed and authorised.

---

## 2. Source Documents Reviewed

The following files and planning records were audited:
* [ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md)
* [ALIS_CORE_BOUNDARY_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md)
* [ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md)
* [ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md)
* [ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md)

---

## 3. Current Governance State

The repository is currently in a transitional auditing state. Multiple detailed architectural plans, candidate classification registers, and readiness documents exist in different preservation states.

The ALIS Core Boundary Register is already preserved in git history. Current git history shows `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` was included in commit `b16410d` (`docs: freeze ALIS Core planning baseline`), and current scoped git status does not show it as modified. It must therefore be treated as an already-preserved controlling document unless a future git status check shows it has changed.

Other later ALIS Core registry/readiness documents are currently observed as untracked or otherwise unpreserved. Those documents require independent review and a separate narrow documentation authorisation before any staging or commit.

---

## 4. Current Codex Readiness State

**Readiness Verdict: CODEX NOT READY**

The overall repository is not ready for Codex implementation due to:
* High coupling of product publishing/visualization code within the platform package `backend/alis`.
* Incomplete and prototype-coupled Thoth registry modules that rely on unapproved, source-controlled registry JSON.
* Pervasive repository hygiene debt (bytecode caches, generated indicator packages, and active runtime log files located inside the source tree).
* Degraded PowerShell workspace tools throwing `DriveNotFoundException` on standard filesystem and git commands.

Consequently, implementation is fully paused, and work is restricted to documentation and review steps only.

---

## 5. Observed Uncommitted Governance and Readiness Documents

Current git status shows more than two uncommitted documentation files. The following ALIS Core governance/readiness documents are observed as untracked and therefore not yet preserved in git history:

* `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`
* `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md` (this corrected plan)

Additional non-ALIS Core review documents are also observed as untracked under `docs/reviews/`. They are not automatically included in this ALIS Core readiness governance preservation scope and require separate product/deployment disposition if preservation is later desired.

---

## 6. Document Preservation Classes

The current governance set must be separated into distinct preservation classes:

### Already committed/frozen documents

These documents are already preserved in git history and should not be included in a future preservation grouping unless current git status shows they have been modified:

* `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`

The boundary register remains the controlling ALIS Core boundary document and is already preserved through the earlier planning baseline commit.

### Frozen but uncommitted documents

These documents represent governing design outputs but are currently observed as untracked or unpreserved:

* `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`

`ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md` should remain a preservation candidate only while git status shows it is untracked or modified.

### Created but pending independent review

The following observed untracked documents were created during the continuing governance/readiness chain and require independent review before any preservation authorisation:

* `docs/reviews/ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md`

### Documents not recommended for preservation yet

These document groups should not be included in the next ALIS Core readiness preservation grouping:

* this corrected readiness governance disposition plan until it is independently reviewed and separately authorised;
* non-ALIS Core product, deployment, Cloudflare, visualisation, production-candidate, and generated-output review files under `docs/reviews/`;
* any document not verified as untracked or modified by current git status.

---

## 7. Documents Pending Preservation Decision

The following observed untracked ALIS Core auditing reviews, candidate registers, and planning documents are pending a formal preservation decision:
* `docs/reviews/ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md` (this plan)

---

## 8. Documents That Should Remain Uncommitted for Now

The following document must remain uncommitted and untracked in the working tree for now:
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md` (this corrected document), as it requires independent review and a separate narrow commit authorisation before staging.

---

## 9. Documents Recommended for Later Narrow Documentation Preservation

To preserve audit trails and align git history with current design rules, it is recommended to preserve only files verified as untracked or modified by current git status in a subsequent **narrow, documentation-only commit**.

The following files are preservation candidates because current git status shows them as untracked:
* **Architectural Boundaries**:
  * `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`
* **Auditing and Classification Registers**:
  * `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
  * `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
  * `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* **Thoth Registry Reviews**:
  * `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
  * `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
  * `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
* **Remediation Plans**:
  * `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`

`docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` is intentionally excluded from this future preservation grouping because it is already committed and current scoped git status does not show it as modified.

---

## 10. Documents Not Recommended for Preservation Yet

The following documents are not recommended for preservation in the next milestone:
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md` (this corrected plan), until it is independently reviewed and separately authorised.
* `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`, unless a future git status check shows it has been modified.
* All non-ALIS Core product, deployment, Cloudflare, visualisation, generated-report, and production-candidate review files observed under `docs/reviews/`.
* All files outside the defined ALIS Core architectural, review, and remediation set.
* Draft templates or notes that have not achieved version 1.0 review status.

---

## 11. Explicit Source/Test Exclusions

All source files and test candidates are strictly excluded from documentation preservation steps. Specifically, `backend/abacus/classifier.py`, `backend/abacus/taxonomy.py`, `backend/validators/validator.py`, `backend/validators/schema.py`, and all files under `backend/alis/` and `tests/` must not be staged or committed.

---

## 12. Explicit Registry Exclusions

All registry candidates (including `sources/source_registry.json`, `backend/alis/source_registry.py`, `tests/alis/test_source_registry.py`, and `tests/alis/test_registry_integration.py`) are excluded from staging and commits. They must remain blocked until a Thoth registry database storage design is completed.

---

## 13. Explicit Artifact/Log/Cache Exclusions

All generated reports, indicator packages, manifests, `.pyc` files, `__pycache__` directories, and runtime logs (`data/validated/validator.log` and raw World Bank/ONS connector logs) are strictly excluded from staging, commits, and cleanup.

---

## 14. Explicit `.gitignore` Exclusion

Modifications to the `.gitignore` file are excluded. The ignore policy must be evaluated in a separate, dedicated milestone.

---

## 15. Explicit Skeleton-Folder Exclusion

The creation of new directories (e.g., `src/`, `legacy/`, `tests/alis_core/`, `tests/godatabank/`) is strictly excluded.

---

## 16. Explicit Cleanup Exclusion

No automated or manual cleanup of caches, data directories, or files is authorised under this disposition plan.

---

## 17. Explicit Migration Exclusion

No code migration, package renaming, or directory restructuring is authorised.

---

## 18. Explicit Implementation Exclusion

No implementation of core engine boundaries, API endpoints, or analytical structures is permitted.

---

## 19. Recommended Documentation Preservation Grouping

A future preservation commit should group documentation logically to keep the commit logs clear and narrow:

* **Group 1: Registry Designs Verified Uncommitted**
  * `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`
* **Group 2: Baseline Auditing and Classification Registers**
  * `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
  * `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
  * `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* **Group 3: Thoth Candidate Reviews and Remediation Plans**
  * `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
  * `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
  * `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
  * `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`

Already committed unchanged documents, including `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`, must not be included in this future grouping.

---

## 20. Risks

* **Staging Noise**: Committing files outside the designated groups might accidentally pull untracked bytecode or runtime logs into git history.
* **Loss of Audit Trail**: If these review documents remain uncommitted indefinitely, the rationale for keeping source registry files blocked will not be recorded in git provenance.
* **Accidental Implementation Resumption**: Preparing a commit could lead to accidental staging of modified tracked Python files (`classifier.py`, `validator.py`).

---

## 21. Abort Conditions

The staging and commit of any documentation group must immediately abort if:
* Any staged files exist before the designated documentation preservation process starts.
* Any source code file (`.py`), test file (`test_*.py`), registry file, or data file (`.json`, `.html`) is proposed for staging.
* A `.gitignore` edit or cleanup action is included in the commit.
* Skeleton folders are created, or directory structure is modified.
* PowerShell tools remain unstable, preventing the precise file-level execution of `git add <file>`.

---

## 22. Recommended Next Milestone

The recommended next milestone is:
```text
Independent Review of Readiness Governance Disposition Plan v1.0-R1
```
After independent review, a later milestone may draft the explicit staging and commit commands required to preserve approved uncommitted documentation groups in git, while keeping all functional implementation, tests, registry files, caches, and logs completely blocked and excluded.

---

STATUS: READINESS GOVERNANCE DISPOSITION PLAN REVISED
REVISION: V1.0-R1
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
