# Thoth Registry Documentation Preservation Authorisation v1.0

## 1. Purpose

This document defines the planning-only preservation authorisation for already reviewed and frozen uncommitted ALIS Core Thoth registry governance and execution review documents. It specifies the exact files authorised for later staging and commit, the required git staging and commit commands, and the strict conditions and exclusions that must be met before execution.

The authorisation defines a future documentation-only commit scope. A separate independent review must occur before any preservation commit is executed.

---

## 2. Current Milestone Chain

The completed Thoth Registry governance and execution review chain consists of the following milestones:
1. Thoth Registry Implementation Revision Plan
2. Revision Plan Independent Review
3. Narrow Implementation Authorisation Plan
4. Narrow Implementation Execution Authorisation
5. Execution Authorisation Independent Review
6. Narrow Implementation Execution Commit Review
7. Narrow Implementation Execution Freeze
8. Narrow Implementation Freeze Review

---

## 3. Candidate Documents for Preservation

The following newly created design and review documents have been reviewed, frozen at version 1.0, and are eligible for preservation in git history:
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_AUTHORISATION_PLAN_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_AUTHORISATION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_INDEPENDENT_REVIEW_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_INDEPENDENT_REVIEW_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_COMMIT_REVIEW_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_COMMIT_REVIEW_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_FREEZE_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_FREEZE_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_FREEZE_REVIEW_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_FREEZE_REVIEW_V1_0.md)

*Note: This current authorisation document ([ALIS_CORE_THOTH_REGISTRY_DOCUMENTATION_PRESERVATION_AUTHORISATION_V1_0.md](file:///c:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_DOCUMENTATION_PRESERVATION_AUTHORISATION_V1_0.md)) is excluded from this future preservation scope unless explicitly authorised by a later tail-preservation milestone and separately reviewed and frozen.*

---

## 4. Explicitly Excluded Files and Paths

The following files and path groups are explicitly excluded from this future documentation-only commit:
* `backend/alis/source_registry.py`
* all other source files (including everything under `backend/`)
* all test files (including everything under `tests/`)
* `sources/source_registry.json`
* `.gitignore`
* generated data
* logs
* reports
* caches
* `__pycache__`
* `.pyc` files
* skeleton folders
* migration folders
* cleanup operations
* unrelated untracked documents
* unrelated modified tracked files

---

## 5. Future Preservation Boundary

The future documentation preservation commit is authorised for review only. Only the 8 candidate files listed in Section 3 are authorized for future staging and commit. No other modifications are allowed. No directory-level staging command and no glob-based staging command is authorised.

---

## 6. Required Future Verification Commands

Before staging, the executing agent must run:
```powershell
git diff --cached --name-only
```
If any staged file exists, the execution must abort.

After staging the authorised files, the executing agent must run:
```powershell
git diff --cached --name-only
```
The staged list must contain exactly the authorised documentation files listed in Section 3, and no other files.

---

## 7. Required Future Staging Command

Future staging must be explicit file-by-file staging only. Do not use `git add .`, `git add docs/`, or `git add docs/reviews/`.

```powershell
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_AUTHORISATION_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_AUTHORISATION_INDEPENDENT_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_COMMIT_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_EXECUTION_FREEZE_V1_0.md
git add docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_FREEZE_REVIEW_V1_0.md
```

---

## 8. Required Future Commit Message

The required commit message for the future documentation-only commit is:
```text
docs: preserve Thoth registry implementation governance
```

---

## 9. Abort Conditions

Any future execution milestone must immediately abort if:
* Files are already staged before execution begins.
* Any file outside the authorised 8-file list is staged.
* This authorisation document itself is staged.
* Any excluded path from Section 4 is staged.
* A directory-level or glob-based staging command is used.
* `.gitignore` is modified or staged.
* Source code, tests, generated artifacts, runtime logs, or data/report outputs are staged.
* Skeleton folders are created, or refactoring, restructuring, package movement, or import rewriting is attempted.

---

## 10. Risks

* **Risk of Command failure on Windows:** Powershell tool errors could interfere with checking cached diffs. This must be verified prior to staging.
* **Risk of Staging Bytecode/Cache:** Any untracked `__pycache__` directories or `.pyc` files could accidentally be staged if glob-based staging is used (mitigated by explicit file-by-file staging).
* **Risk of Staging Unrelated Uncommitted/Untracked Files:** Working tree may contain other untracked or modified files that are outside the scope of Thoth governance (mitigated by checking the exact output of `git diff --cached --name-only`).

---

## 11. Decision

AUTHORISATION PASSED — FUTURE DOCUMENTATION PRESERVATION MAY PROCEED AFTER INDEPENDENT REVIEW

---

## 12. Recommended Next Milestone

Independent Review of Thoth Registry Documentation Preservation Authorisation v1.0

---

STATUS: THOTH REGISTRY DOCUMENTATION PRESERVATION AUTHORISATION CREATED
CODEX IMPLEMENTATION: PAUSED AFTER AUTHORISED EXECUTION
SOURCE IMPLEMENTATION: PAUSED AFTER AUTHORISED EXECUTION
TEST IMPLEMENTATION: PAUSED
REGISTRY IMPLEMENTATION: PAUSED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
TEST CHANGES: NOT PERFORMED
REGISTRY CHANGES: NOT PERFORMED
CLEANUP: NOT PERFORMED
GITIGNORE CHANGES: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
