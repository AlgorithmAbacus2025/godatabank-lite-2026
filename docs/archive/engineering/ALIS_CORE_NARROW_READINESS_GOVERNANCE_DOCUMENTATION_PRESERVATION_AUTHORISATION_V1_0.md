# ALIS Core Narrow Readiness Governance Documentation Preservation Authorisation v1.0-R1

## 1. Purpose

This document defines the planning-only preservation authorisation for already reviewed and frozen uncommitted ALIS Core readiness, registry, and source/test governance documents. It specifies the exact files authorised for later staging and commit, the required git staging and commit commands, and the strict conditions and exclusions that must be met before execution.

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

The following files and baseline planning records were audited:
* [ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md)
* [ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md)
* [ALIS_CORE_BOUNDARY_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md)

---

## 3. Current Codex Readiness State

**Readiness Verdict: CODEX NOT READY**

The overall repository is not ready for implementation due to critical gaps in platform/product separation, non-compliant prototype registry models, untracked bytecode cache pollution, and degraded terminal command tools. Therefore, all implementation tasks are suspended, and only narrow planning, design, and documentation activities are authorised.

---

## 4. Current Git-Status Basis for Authorisation

Based on current scoped git status and historical repository commits:
* No files are currently staged.
* The authorised readiness and registry governance documents exist on disk as untracked files in the `docs/architecture/` and `docs/reviews/` directories.
* `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` is already preserved in commit `b16410d` and is excluded unless a future git status check shows it has been modified.
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md` is currently untracked but excluded from this authorisation because it requires separate independent review and preservation authorisation.
* Modified tracked source, test-adjacent, registry data, generated data, and runtime log paths remain excluded.

---

## 5. Documents Eligible for Preservation

The following newly created design and review documents have been reviewed, frozen at version 1.0, and are eligible for preservation in git history:
* `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
* `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
* `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`
* `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md`

---

## 6. Documents Explicitly Excluded

The following file is explicitly **excluded** from this preservation authorisation:
* `docs/reviews/ALIS_CORE_NARROW_READINESS_GOVERNANCE_DOCUMENTATION_PRESERVATION_AUTHORISATION_V1_0.md` (this document), which must remain untracked for now.

`docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md` is not excluded by this section. It is included in the authorised eight-file list because it has been corrected to V1.0-R1 and is eligible for preservation subject to independent review and execution verification.

---

## 7. Already Committed Documents Excluded from Preservation

The following document is already preserved in git history and is excluded:
* `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` (Already preserved in commit `b16410d` and has no modifications).

---

## 8. Documents Pending Review Excluded from Preservation

The following document is excluded because it has not been independently reviewed and frozen:
* `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`

---

## 9. Source/Test Exclusions

All candidate source files and test candidates are strictly excluded. This includes all files under `backend/abacus/`, `backend/validators/`, `backend/publisher/`, `backend/publishing/`, and `tests/`.

---

## 10. Registry Data/Source/Test Exclusions

All registry candidates are strictly excluded:
* `sources/source_registry.json`
* `backend/alis/source_registry.py`
* `tests/alis/test_source_registry.py`
* `tests/alis/test_registry_integration.py`

---

## 11. Generated Artifact/Log/Cache Exclusions

All generated outputs, bytecode caches, and operational logs are strictly excluded:
* `evidence_package_output.json`
* `data/classified/**`
* `data/validated/**`
* `data/publishing/**`
* `data/**/logs/`
* `reports/`
* `**/*.pyc` and `**/__pycache__/`

---

## 12. `.gitignore` Exclusion

Modifications to `.gitignore` are strictly excluded. Ignore rules must be handled in a separate milestone.

---

## 13. Skeleton-Folder Exclusion

The creation of folder skeletons (e.g., `src/`, `legacy/`, `tests/alis_core/`, `tests/godatabank/`) is strictly excluded.

---

## 14. Cleanup Exclusion

No automated or manual file deletions or caching cleanups are permitted.

---

## 15. Migration Exclusion

No refactoring, restructuring, package movement, or import rewriting is authorised.

---

## 16. Implementation Exclusion

No implementation of core engine logic or API endpoints is authorised.

---

## 17. Authorised File List

The following exact list of files is authorised for preservation:
1. `docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md`
2. `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
3. `docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md`
4. `docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md`
5. `docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md`
6. `docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md`
7. `docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md`
8. `docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md`

---

## 18. Exact Future Staging Commands

The execution milestone must stage files using explicit file paths only. Directory-level `git add` or globbing is prohibited.

```powershell
git add docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md
```

---

## 19. Exact Future Commit Message

The execution commit message must be exactly:
```text
docs: preserve ALIS Core readiness governance
```

---

## 20. Verification Commands Required Before Execution

Before running any staging command, the executing agent must run:
```powershell
git diff --cached --name-only
```

If this command returns any staged file, execution must abort before staging with:

```text
ABORTED: PRE-EXISTING STAGED FILES DETECTED
```

After staging the authorised eight files, the executing agent must run:

```powershell
git diff --cached --name-only
```

The staged list must exactly match:

```text
docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md
docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md
docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md
docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md
docs/reviews/ALIS_CORE_THOTH_REGISTRY_SOURCE_TEST_CANDIDATE_REVIEW_PLAN_V1_0.md
docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md
docs/reviews/ALIS_CORE_CODEX_READINESS_REMEDIATION_PLAN_V1_0.md
docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_DISPOSITION_PLAN_V1_0.md
```

If the staged list differs in any way, execution must abort before commit with:

```text
ABORTED: STAGED FILE LIST DOES NOT MATCH AUTHORISED SCOPE
```

---

## 21. Abort Conditions

The execution milestone must immediately abort if:
* Files are already staged before execution begins.
* Any source (`.py`), test (`test_*.py`), registry, data, or log file is staged.
* Glob-based staging (e.g., `git add .`) is attempted.
* Skeleton folders are created, or `.gitignore` is modified.
* PowerShell tools remain unstable, preventing short-status evaluation.

---

## 22. Decision

The narrow documentation preservation is **authorised** to proceed in a subsequent execution milestone, subject to the file lists, commands, exclusions, and abort conditions defined in this document.

---

## 23. Recommended Next Milestone

The recommended next milestone is:
```text
Execution of Narrow Readiness Governance Documentation Preservation v1.0
```
This milestone will run the staging, verification, and commit commands authorised by this document, ensuring that only the frozen design and auditing reviews are committed to the repository history.

---

STATUS: NARROW READINESS GOVERNANCE DOCUMENTATION PRESERVATION AUTHORISATION REVISED
REVISION: V1.0-R1
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
