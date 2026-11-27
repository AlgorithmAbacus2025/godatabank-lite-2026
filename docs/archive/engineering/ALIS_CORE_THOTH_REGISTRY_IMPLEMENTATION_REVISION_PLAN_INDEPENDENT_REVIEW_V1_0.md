# ALIS Core Thoth Registry Implementation Revision Plan Independent Review v1.0-R1

## 1. Purpose

This document presents the independent technical review of the Thoth Registry Implementation Revision Plan v1.0. It determines whether the plan is suitable as a planning-only design instrument for a future narrow implementation milestone of the Thoth registry helper `backend/alis/source_registry.py`.

---

## 2. Reviewed Document

* **Title:** ALIS Core Thoth Registry Implementation Revision Plan v1.0
* **Target Path:** `docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md`
* **Version/Status:** v1.0 (Untracked, planning-only)

---

## 3. Controlling Governance Documents

This review is conducted against the following frozen baseline and planning authorities:
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md)
* [ALIS_CORE_READINESS_GOVERNANCE_CHECKPOINT_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_CHECKPOINT_V1_0.md)

---

## 4. Scope Check

* **Planning-Only Verification:** The reviewed plan remains strictly planning-only. It does not authorise staging, committing, file edits, deletions, skeleton creation, or runtime storage setup.
* **Non-Authorisation Verification:** The plan explicitly lists all non-authorised activities, keeping the source codebase frozen.
* **Acceptance Criteria Verification:** The plan keeps the candidate code and related test/data files blocked and clarifies that tests remain blocked until source ownership and acceptance criteria are formally approved.

---

## 5. Alignment with Thoth Registry Design

The reviewed plan proposes an implementation revision direction for `backend/alis/source_registry.py` that aligns with the requirements of the Thoth Registry Design:
* **Canonical Identifier:** Stops treating display names or raw URLs as primary keys; plans for Thoth-owned unique canonical IDs.
* **Source Registry Entry Model:** References a structured entry schema covering status, version, provenance, and contract information.
* **Registry Status Transitions:** Enforces the defined lifecycle model (`proposed`, `admitted`, `active`, etc.).
* **Provenance and Lineage:** Specifies mutable audit traces, lineage trees, and checksum verifications to maintain metadata chain of custody.
* **Fail-Closed Validation:** Enforces robust checks on missing registry evidence before any query completion.

---

## 6. Boundary Check

The plan respects the strict engine separation defined in the ALIS Core Boundary Register:
* **Thoth:** Exclusively manages read-only metadata registry operations, schema contracts, and entry tracking.
* **Aegis:** Policy decisions and gate admission validations are kept separate from registry inspection.
* **Arya:** Proposal admissions and retrieval planning workflows are kept separate from registry filtering.
* **Hermes:** Transport execution, socket connections, and network calls are strictly excluded from endpoint metadata mapping.
* **Abacus:** Analytical logic, ranking, or statistical calculations are kept external to Thoth lookup.
* **Apollo:** Publication rendering and rendering manifest generation remain separated.
* **Argus:** Observable audit event logs remain external, and Thoth does not duplicate Argus tracking.
* **GoDataBank:** Product-layer UX and language are decoupled from Core registry modules.

---

## 7. Overengineering Check

The plan is highly scoped and avoids overengineering:
* No broad abstractions, interface hierarchies, or factories are planned.
* No service containers, dependency injection setups, or complex plugin registration architectures are introduced.
* It defines only the minimum revision path needed to correct the existing `source_registry.py` candidate, making it reviewable for a future narrow milestone.

---

## 8. Exclusion Check

The plan respects all registry exclusions:
* It does not treat `sources/source_registry.json` as a canonical production dependency. It classifies it as a prototype or possible fixture candidate only.
* All tests (`test_source_registry.py`, `test_registry_integration.py`) are kept blocked.
* Source code remains frozen.

---

## 9. Risks

* **Implicit JSON Loading:** Prototype file dependency could lead to hard-coded path dependencies. (Mitigated by requirements for a separate storage policy).
* **Policy Gates Leaking into Metadata Checks:** (Mitigated by fail-closed validation scoping).
* **Workspace Traversal Block:** The Git/PowerShell traversal issue remains unresolved. LibGit2Sharp was used previously as a milestone-specific workaround only. This review does not authorise permanent alternative Git tooling, environment repair, dependency changes, cleanup, or implementation work.

---

## 10. Decision

**REVIEW PASSED — PLAN SUITABLE FOR FUTURE NARROW IMPLEMENTATION AUTHORISATION**

The Thoth Registry Implementation Revision Plan v1.0 is suitable as a planning instrument. It aligns with the frozen Thoth Registry Design, respects core boundaries, excludes prototype files from production canonical state, and avoids overengineering. It does not authorise any code edits, staging, or commits.

---

## 11. Recommended Next Milestone

The recommended next milestone is:
```text
Thoth Registry Narrow Implementation Authorisation Plan v1.0
```

This next milestone is authorisation-planning only and must not itself implement registry code.

---

STATUS: THOTH REGISTRY IMPLEMENTATION REVISION PLAN INDEPENDENT REVIEW REVISED
REVISION: V1.0-R1
REVIEW TARGET: ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md
CODEX IMPLEMENTATION: PAUSED
SOURCE IMPLEMENTATION: PAUSED
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
