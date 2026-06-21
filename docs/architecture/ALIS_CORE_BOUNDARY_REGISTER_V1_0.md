# ALIS Core Boundary Register v1.0

## Document Control

This register defines the ALIS Core engine boundaries for Milestone 1.

It is documentation only. It does not start implementation, change production
architecture, refactor code, rename modules, or grant permission for engines to
cross their documented boundaries.

The words "must", "must not", "may", and "should" are normative in this
document. API names are contract identifiers, not implemented functions.

Version: 1.0

Revision: V1.0-R1

Scope:

- Abacus
- Arya
- Vyasa
- Hermes
- Thoth
- Aegis
- Apollo
- Argus

## ALIS Core Overview

ALIS Core is the contract boundary layer for GoDataBank evidence, analysis,
synthesis, publishing, governance, and observability workflows.

The core principle is separation of responsibility. Each engine owns one class
of work, emits explicit artifacts, and consumes upstream artifacts through a
versioned public contract. No engine may silently mutate another engine's
outputs. No engine may infer authority from access to a file, table, endpoint,
or folder.

ALIS Core is designed around traceable data movement:

```text
source proposal
  -> source admission
  -> retrieval
  -> validation
  -> provenance registration
  -> analysis
  -> synthesis
  -> publishing
  -> audit and monitoring
```

Every step must leave enough evidence for a reviewer to answer:

- What artifact was received?
- Which engine produced it?
- Which contract version governed it?
- Which inputs and checksums were used?
- Which validation gates passed or failed?
- Which downstream engine consumed it?

## Interface First Principle

No ALIS Core engine should be implemented or extended before its public
interface is documented.

An engine interface must define:

- accepted inputs
- emitted outputs
- artifact schemas or schema references
- allowed side effects
- failure states
- logging obligations
- version ownership

Downstream engines must depend on public interfaces and artifact contracts, not
on internal implementation details. Internal APIs may change without downstream
coordination only if the public contract remains stable.

## Single Builder Principle

Each canonical artifact must have one builder.

An engine may read another engine's artifact only through the declared public
contract. It may transform that artifact only by producing a new artifact under
its own ownership. It must not edit, complete, repair, or reinterpret another
engine's canonical output in place.

This prevents ambiguous ownership. For example:

- Arya may admit a source, but must not validate retrieved evidence.
- Hermes may retrieve bytes, but must not decide whether the source is valid.
- Aegis may reject an artifact, but must not rewrite it into compliance.
- Abacus may analyse validated evidence, but must not publish final reports.
- Apollo may render approved outputs, but must not alter analytical findings.

## Canonical Artifact Ownership

Each canonical artifact must have exactly one owning builder. No engine may edit
another engine's canonical artifact in place.

| Artifact | Canonical builder |
| --- | --- |
| Execution Plan | Abacus |
| Source Proposal | Arya |
| Source Admission Request | Arya |
| Retrieval Manifest | Arya |
| Raw Transport Artifact | Hermes |
| Raw Artifact Checksum Record | Thoth |
| Source Registry Entry | Thoth |
| Provenance Record | Thoth |
| Lineage Record | Thoth |
| Retrieved Evidence Package | Hermes |
| Validation Report | Aegis |
| Gate Decision | Aegis |
| Validated Evidence Package | Aegis |
| Analysis Package | Abacus |
| Chart-ready Dataset | Abacus |
| Narrative Package | Vyasa |
| Claim-to-Evidence Map | Vyasa |
| Publication Package | Apollo |
| Publication Manifest | Apollo |
| Audit Record | Argus |
| Incident Timeline | Argus |

## Shared Services

Shared services are common capabilities used by engines. They do not override
engine boundaries.

| Shared service | Purpose | Boundary rule |
| --- | --- | --- |
| Contract registry | Stores public contract versions and compatibility notes. | Engines must read contracts before consuming artifacts. |
| Source registry | Records admitted source metadata and identifiers. | Arya owns admission; Thoth owns registry provenance. |
| Artifact store | Preserves raw, validated, analytical, synthesized, and rendered artifacts. | Only the owning engine may create the canonical artifact for its stage. |
| Schema registry | Stores artifact schemas and validation versions. | Aegis validates against schemas; Thoth records schema lineage. |
| Checksum service | Computes stable hashes for lineage and tamper detection. | Hashes describe artifacts; they do not approve artifacts. |
| Clock service | Provides consistent retrieval, validation, and publication timestamps. | Timestamps must be recorded with timezone or UTC convention. |
| Configuration service | Provides runtime configuration, feature gates, and environment labels. | Configuration must not be used to bypass governance gates. |
| Identity and permission service | Records actor, engine, and execution identity. | Access does not imply permission to cross an engine boundary. |
| Logging and audit service | Captures structured run events and operational traces. | Argus owns observability; engines still emit their own required events. |
| Error taxonomy | Defines shared failure categories and severity levels. | Engines must report failures in shared terms without hiding local detail. |

## Engine Interaction Flow

```text
1. Abacus or a user-facing product creates an analysis request.
2. Arya receives or creates a source proposal.
3. Arya evaluates source admission requirements and requests Aegis policy review where required.
4. Aegis issues a Source Admission Gate decision.
5. Thoth records the canonical source registry entry, source metadata and initial provenance record.
6. Arya creates a retrieval manifest for the admitted source.
7. Hermes executes the retrieval manifest and produces the raw transport artifact.
8. Thoth records raw artifact checksum, lineage, schema reference and registry linkage.
9. Hermes produces a Retrieved Evidence Package.
10. Aegis validates the Retrieved Evidence Package using Hermes output and Thoth provenance records.
11. Aegis issues an Evidence Validation Gate decision.
12. Aegis produces the Validated Evidence Package.
13. Abacus consumes only Validated Evidence Packages and produces Analysis Packages.
14. Aegis applies an Analysis Approval Gate where required.
15. Vyasa consumes approved Analysis Packages and produces Narrative Packages and Claim-to-Evidence Maps.
16. Aegis applies a Synthesis Approval Gate where required.
17. Apollo consumes approved analysis and narrative artifacts and creates Publication Packages.
18. Aegis applies the Publication Approval Gate before promotion or deployment.
19. Argus records events, health signals, failures, alerts, audit trails and observability gaps throughout.
20. Thoth records artifact lineage, validation references and publication lineage throughout.
```

No step implies production implementation. This flow defines the intended
contract order for future work.

Thoth records provenance and lineage. Aegis makes approval decisions.

Hermes produces raw transport artifacts and Retrieved Evidence Packages. Thoth
records provenance, lineage, checksum, registry, schema, and contract references.
Aegis consumes Hermes evidence plus Thoth provenance and registry records. Aegis
is the sole producer of the Validated Evidence Package. Abacus consumes
Validated Evidence Packages but does not build, repair, or approve them.

## Aegis Gate Model

| Gate | Purpose | Input artifact | Output decision | Pass/fail/escalate behaviour | Downstream consequence |
| --- | --- | --- | --- | --- | --- |
| Source Admission Gate | Decide whether a proposed source may enter ALIS Core retrieval planning. | Source Admission Request from Arya, source policy, source metadata, and registry context. | Gate Decision owned by Aegis. | Pass admits the source for registry entry and retrieval planning; fail rejects or quarantines the source; escalate requires human review. | Arya may create a Retrieval Manifest only after pass or explicit reviewed approval. |
| Evidence Validation Gate | Decide whether retrieved evidence is valid for analytical consumption. | Retrieved Evidence Package from Hermes plus Thoth provenance, checksum, schema, lineage, and registry records. | Gate Decision and Validation Report owned by Aegis. | Pass allows Aegis to produce the Validated Evidence Package; fail blocks analytical use and may quarantine; escalate requires review. | Abacus may consume only the Validated Evidence Package produced after this gate passes. |
| Analysis Approval Gate | Decide whether an Analysis Package may be used for synthesis or publication. | Analysis Package and Chart-ready Dataset from Abacus plus Thoth lineage records. | Gate Decision owned by Aegis. | Pass allows synthesis and publication preparation where required; fail blocks downstream use; escalate requires methodological or governance review. | Vyasa may consume the Analysis Package only when approval is passed or explicitly not required by policy. |
| Synthesis Approval Gate | Decide whether narrative artifacts are evidence-traceable and suitable for publication assembly. | Narrative Package and Claim-to-Evidence Map from Vyasa plus approved analysis references. | Gate Decision owned by Aegis. | Pass allows publication assembly; fail blocks narrative use; escalate requires claim, citation, or caveat review. | Apollo may consume narrative artifacts only after pass or explicit reviewed approval. |
| Publication Approval Gate | Decide whether a Publication Package may be promoted or deployed. | Publication Package and Publication Manifest from Apollo plus validation, analysis, synthesis, lineage, and audit references. | Gate Decision owned by Aegis. | Pass allows promotion or deployment; fail blocks release; escalate requires release review. | No publication bundle may be promoted unless the Publication Approval Gate has passed. |

## Boundary Matrix

| Engine | Owns | Consumes | Produces | Must not produce |
| --- | --- | --- | --- | --- |
| Abacus | Analytical transformation, execution planning, and statistical output. | Validated Evidence Packages, analysis requests, taxonomies. | Execution Plans, Analysis Packages, Chart-ready Datasets, caveats. | Validated Evidence Packages, Narrative Packages, source admission decisions, final publications. |
| Arya | Source proposal, source admission request, and retrieval planning. | Analysis requests, source policies, registry context, gate decisions. | Source Proposals, Source Admission Requests, Retrieval Manifests, readiness and acquisition logs. | Canonical Source Registry Entries, Validated Evidence Packages, analytical findings, rendered reports. |
| Vyasa | Narrative synthesis from approved evidence and analysis. | Approved Analysis Packages, citation maps, audience or style constraints. | Narrative Packages, Claim-to-Evidence Maps, methodology text, caveat text. | New data, calculations, source retrievals, publication bundles. |
| Hermes | Transport, external I/O, raw retrieval, and retrieved evidence packaging. | Retrieval Manifests, endpoint metadata, delivery requests. | Raw Transport Artifacts, Retrieved Evidence Packages, receipts, retry records. | Source admission decisions, validation approvals, analysis. |
| Thoth | Metadata, provenance, schemas, registry state, checksums, and lineage. | Artifact metadata, validation reports, engine versions, registry update requests. | Source Registry Entries, Provenance Records, Lineage Records, Checksum Records, schema and contract references. | Gate Decisions, payload edits, narrative claims, rendered reports. |
| Aegis | Governance, validation, policy gates, boundary enforcement, and Validated Evidence Packages. | Artifacts, policies, schemas, transition requests, provenance records. | Validation Reports, Gate Decisions, Validated Evidence Packages, quarantine records. | Rewritten artifacts, analytical outputs, transport artifacts. |
| Apollo | Rendering, packaging, and publication assembly. | Approved analysis and narrative packages, assets, release approvals. | Publication Packages, rendered pages, bundles, Publication Manifests. | Analytical findings, validation decisions, raw evidence. |
| Argus | Observability, audit trails, health, alerts, and incidents. | Structured events, logs, heartbeats, run metadata. | Audit Records, health reports, alerts, Incident Timelines. | Artifact payloads, policy decisions, analysis, publication content. |

## Engine Registers

### Abacus

Purpose:

Abacus is the analytical engine. It converts Validated Evidence Packages into
Execution Plans and structured analytical artifacts that can be reviewed,
visualised, synthesized, and published by downstream engines.

Responsibilities:

- consume only validated evidence packages
- create canonical Execution Plans for approved analytical work
- apply documented classification, calculation, and statistical methods
- produce analysis packages with method references and limitations
- generate chart-ready datasets and chart specification references
- preserve input identifiers, checksums, and contract versions
- expose caveats where source evidence or methods limit interpretation
- consume Validated Evidence Packages without building, repairing, or approving them

Inputs:

- validated evidence package
- analysis request or analytical question
- classification taxonomy
- metric definitions
- accepted transformation rules
- chart or visualisation requirements
- engine configuration and contract version

Outputs:

- execution plan
- analysis package
- transformed analytical dataset
- classification result
- statistical check report
- chart-ready data
- chart specification reference
- limitations and caveats
- analysis run log reference

Dependencies:

- Thoth for evidence package metadata, lineage, schemas, and contract versions
- Aegis for evidence validation status, analysis approval gates, and boundary gate decisions
- Argus for run logging, monitoring, and audit trail capture
- shared checksum, clock, configuration, and error taxonomy services

Public API:

- `submit_analysis_request`
- `get_execution_plan`
- `get_analysis_status`
- `get_analysis_package`
- `list_supported_analysis_methods`
- `list_required_input_contracts`

Internal API:

- method registry
- transformation pipeline
- classifier registry
- statistical checker
- chart-ready dataset builder
- caveat generator

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- analysis request identifier
- input artifact identifiers and checksums
- Abacus engine version and public contract version
- method names and method versions
- taxonomy and configuration versions
- validation status inherited from Aegis
- warnings, caveats, and incomplete-result markers
- output artifact identifiers and checksums
- failure category, severity, and recovery recommendation

Failure behaviour:

- fail closed when required evidence, schema, or validation status is missing
- produce no canonical analysis package unless the package is complete and marked valid
- partial outputs may be retained only as non-canonical diagnostic artifacts
- never fill missing data with invented values
- never suppress caveats caused by input quality or method limitations
- never build or repair a Validated Evidence Package to satisfy an analysis request

Permitted actions:

- read validated evidence packages
- produce Execution Plans under Abacus ownership
- transform copies of validated data for analysis
- classify data under approved taxonomies
- calculate documented metrics and statistical checks
- emit analysis artifacts under Abacus ownership

Forbidden actions:

- fetch source documents directly
- modify raw or validated evidence artifacts in place
- validate evidence
- build Validated Evidence Packages
- approve source admission
- override Aegis validation or release gates
- generate unsupported conclusions
- produce narrative packages
- write reports
- publish final reports or dashboards

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Abacus analytical maintainer, to be assigned before implementation

### Arya

Purpose:

Arya is the source proposal, source admission request, and retrieval planning
engine. It prepares source proposals and retrieval manifests, but it does not
produce the canonical Source Registry Entry.

Responsibilities:

- receive source proposals and dataset identifiers
- apply source admission rules before retrieval is attempted
- create Source Admission Requests for Aegis review
- prepare retrieval manifests for Hermes
- preserve source rationale, admission request, Aegis gate decision reference, and policy references
- reject or defer sources that do not meet admission requirements
- maintain acquisition logs for source planning activity
- request Thoth registry linkage without creating canonical registry entries

Inputs:

- source proposal
- dataset identifier
- source URL, endpoint, or catalogue reference
- geography and timeframe requirements
- retrieval mode
- source admission policy
- source registry context
- Aegis policy decision or policy requirement

Outputs:

- source proposal
- source admission request
- source readiness status
- retrieval manifest
- acquisition log
- source rejection or deferral report

Dependencies:

- Aegis for policy checks and admission gate decisions
- Thoth for source registry references and provenance records
- Hermes for execution of retrieval manifests
- Argus for admission and planning audit logs
- shared configuration, identity, clock, and error taxonomy services

Public API:

- `propose_source`
- `evaluate_source_admission`
- `create_source_admission_request`
- `request_source_registry_linkage`
- `create_retrieval_manifest`
- `get_source_status`

Internal API:

- source normaliser
- admission rule evaluator
- retrieval manifest builder
- source readiness checker
- policy reference mapper

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- source proposal identifier
- source name, endpoint, and dataset identifier where available
- admission policy version
- decision outcome and reason
- retrieval manifest identifier
- actor or engine identity
- timestamps for proposal, decision, and manifest creation
- rejection, deferral, or escalation reason

Failure behaviour:

- fail closed when source identity or admission policy cannot be resolved
- do not create a retrieval manifest for a rejected or unreviewed source
- record deferral when evidence is insufficient for admission
- escalate to human review when policy cannot be applied deterministically
- never silently substitute an alternative source

Permitted actions:

- propose, reject, or defer source proposals according to policy
- create Source Admission Requests
- prepare retrieval manifests for admitted sources
- request Aegis review for ambiguous cases
- request canonical registry linkage from Thoth after Aegis gate approval

Forbidden actions:

- execute external retrieval directly
- classify evidence
- validate source claims
- validate retrieved evidence packages
- analyse data values or produce findings
- build canonical provenance records
- build canonical source registry entries
- rewrite retrieved artifacts
- publish reports or dashboards
- bypass source admission policy

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Arya source-admission maintainer, to be assigned before implementation

### Vyasa

Purpose:

Vyasa is the narrative synthesis engine. It turns approved analytical artifacts
into structured explanatory text while preserving citations, caveats, and
method boundaries.

Responsibilities:

- consume approved analysis packages and evidence references
- produce cited narrative artifacts for reports and summaries
- express methods, limitations, and caveats in clear language
- maintain a claim-to-evidence map
- distinguish observed evidence from interpretation
- preserve numerical values exactly as supplied by approved analytical artifacts

Inputs:

- approved analysis package
- evidence and provenance references
- citation map
- intended audience or style profile
- report section request
- caveats and limitations from Abacus
- synthesis template or narrative contract

Outputs:

- narrative package
- executive summary text
- methodology text
- caveat and limitation text
- claim-to-evidence map
- citation list
- synthesis run log reference

Dependencies:

- Abacus for analytical findings, statistics, and caveats
- Thoth for provenance, citation, and artifact references
- Aegis for synthesis gate checks and unsupported-claim rejection
- Argus for synthesis event logging and audit capture
- shared contract registry, identity, and error taxonomy services

Public API:

- `request_synthesis`
- `get_synthesis_status`
- `get_narrative_package`
- `list_synthesis_templates`
- `get_claim_evidence_map`

Internal API:

- narrative template renderer
- claim extractor
- citation resolver
- caveat composer
- unsupported-claim detector

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- synthesis request identifier
- input analysis package identifiers and checksums
- cited evidence identifiers
- template and style profile versions
- generated claim identifiers
- unsupported-claim warnings or rejections
- output narrative package identifier and checksum
- failure category, severity, and review recommendation

Failure behaviour:

- fail closed when required evidence references are missing
- reject narratives containing claims not traceable to approved inputs
- preserve original numbers and units from Abacus outputs
- mark incomplete narrative packages as non-canonical
- escalate ambiguous interpretation to review rather than inventing certainty

Permitted actions:

- explain approved analytical outputs
- reorganise approved findings into report sections
- generate summaries with explicit citations
- surface caveats and uncertainty
- produce narrative artifacts under Vyasa ownership

Forbidden actions:

- calculate new metrics
- alter analytical results or units
- fetch source data
- approve evidence
- approve validation gates
- make gate decisions
- publish final outputs
- omit required caveats to improve readability

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Vyasa synthesis maintainer, to be assigned before implementation

### Hermes

Purpose:

Hermes is the transport and external I/O engine. It moves data and messages
between ALIS Core and external systems, produces Raw Transport Artifacts and
Retrieved Evidence Packages, and does not make domain, validation, or
analytical decisions.

Responsibilities:

- execute retrieval manifests created by Arya
- perform HTTP, API, file, or other approved transport operations
- capture raw response bodies and transport metadata
- apply bounded retry, timeout, and rate-limit behaviour
- emit delivery receipts and transport artifacts
- produce Retrieved Evidence Packages from raw transport artifacts and transport metadata
- preserve external response evidence without semantic modification

Inputs:

- retrieval manifest
- endpoint metadata
- approved credential handle
- transport configuration
- rate-limit policy
- delivery request
- correlation identifier

Outputs:

- raw transport artifact
- retrieved evidence package
- response metadata
- delivery receipt
- retry record
- transport failure report
- transport log reference

Dependencies:

- Arya for retrieval manifests and source intent
- Aegis for credential, access, and transport policy checks
- Thoth for endpoint metadata and artifact registration references
- Argus for transport logs, retries, and health monitoring
- shared clock, checksum, configuration, and error taxonomy services

Public API:

- `execute_retrieval_manifest`
- `get_transport_status`
- `get_transport_artifact`
- `send_artifact`
- `list_supported_transport_adapters`

Internal API:

- adapter registry
- request signer
- retry controller
- response envelope builder
- credential resolver
- timeout manager

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- retrieval manifest identifier
- endpoint and adapter identifier
- credential handle identifier, never credential secret material
- request timestamp and response timestamp
- HTTP status or equivalent transport status
- retry count, timeout, and rate-limit events
- raw artifact identifier and checksum
- retrieved evidence package identifier and checksum
- transport failure category and severity

Failure behaviour:

- apply only documented retry behaviour
- never silently switch endpoints or credentials
- preserve failed response evidence where policy allows
- return explicit timeout, authentication, rate-limit, network, or parsing failure
- mark artifacts as retrieved evidence only until Aegis validates them

Permitted actions:

- contact approved external endpoints
- retrieve raw bytes or records according to a manifest
- store raw transport artifacts
- build Retrieved Evidence Packages without changing source meaning
- emit receipts and transport metadata
- deliver artifacts between approved engine boundaries

Forbidden actions:

- decide source admission
- approve source admission
- validate evidence
- validate evidence quality
- analyse data content
- rewrite retrieved payloads into semantic form
- modify source meaning
- generate citations independently of Aegis and Thoth
- publish reports
- expose secrets in logs or artifacts

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Hermes transport maintainer, to be assigned before implementation

### Thoth

Purpose:

Thoth is the metadata, provenance, schema, and registry engine. It records what
artifacts exist, where they came from, which contracts govern them, and how they
relate to each other. Thoth records provenance and lineage; Aegis makes
approval decisions.

Responsibilities:

- maintain source, artifact, schema, and contract registries
- record lineage between inputs and outputs
- store artifact identifiers, checksums, timestamps, and owners
- expose provenance lookup for downstream engines and reviewers
- preserve validation and gate decision references
- prevent inconsistent or duplicate registry records
- alone produce and maintain canonical Source Registry Entries
- alone produce and maintain canonical Provenance Records, Checksum Records, and Lineage Records
- alone produce and maintain schema references and contract version references

Inputs:

- source metadata
- artifact metadata
- schema references
- validation reports
- engine version declarations
- checksum records
- contract version declarations
- lineage update requests

Outputs:

- canonical source registry entry
- provenance record
- checksum record
- lineage record
- artifact lookup result
- schema reference
- contract version reference
- lineage graph query result
- registry failure report

Dependencies:

- all engines for metadata emission through public contracts
- Aegis for validation reports and gate decisions
- Argus for operational audit and registry health monitoring
- shared checksum, clock, identity, and contract registry services

Public API:

- `register_artifact`
- `register_source`
- `register_contract_version`
- `lookup_artifact`
- `get_lineage`
- `get_schema_reference`

Internal API:

- provenance graph updater
- registry consistency checker
- schema index
- checksum verifier
- duplicate detector
- contract compatibility resolver

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- registry request identifier
- artifact, source, schema, or contract identifier
- owning engine
- input and output lineage references
- checksum and timestamp values
- duplicate or conflict detection result
- registry version
- failure category, severity, and remediation path

Failure behaviour:

- reject inconsistent lineage updates
- reject duplicate identifiers with conflicting metadata
- block downstream lookup when provenance is incomplete
- preserve failed registry attempts as audit records
- never infer missing lineage without explicit upstream evidence

Permitted actions:

- record metadata and provenance
- expose read-only registry and lineage lookups
- check identifier consistency
- associate artifacts with schemas and contract versions
- record validation and release gate references
- produce canonical Source Registry Entries, Provenance Records, Checksum Records, and Lineage Records

Forbidden actions:

- edit artifact payloads
- make gate decisions
- approve or reject evidence
- validate artifact content in place of Aegis
- validate claims
- retrieve external source data
- perform analysis
- generate narrative claims
- render or publish reports
- produce reports
- alter provenance to satisfy validation

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Thoth provenance maintainer, to be assigned before implementation

### Aegis

Purpose:

Aegis is the governance, validation, policy, and boundary enforcement engine. It
decides whether artifacts may move between stages, but it does not repair or
replace the artifacts it reviews. Aegis is the sole producer of the Validated
Evidence Package.

Responsibilities:

- validate artifacts against schemas, source rules, and transition policies
- enforce engine boundary rules
- approve, reject, quarantine, or escalate artifacts and transitions
- preserve validation reports and gate decisions
- check that required logs, lineage, and checksums exist
- block downstream activity when required evidence is missing or invalid
- consume Hermes evidence plus Thoth provenance and registry records
- produce Validated Evidence Packages after the Evidence Validation Gate passes

Inputs:

- artifact reference
- retrieved evidence package
- schema reference
- provenance record
- source registry entry
- source admission policy
- transition request
- engine contract version
- lineage record
- checksum record
- release policy

Outputs:

- validation report
- gate decision
- validated evidence package
- policy violation report
- quarantine record
- escalation request
- boundary compliance report
- validation log reference

Dependencies:

- Thoth for schemas, lineage, contract versions, and artifact metadata
- Argus for validation event logging, alerts, and audit monitoring
- all engines for transition requests and declared public contracts
- shared identity, configuration, clock, and error taxonomy services

Public API:

- `validate_artifact`
- `evaluate_transition`
- `get_gate_decision`
- `get_validated_evidence_package`
- `assert_boundary_compliance`
- `list_active_policies`
- `request_human_review`

Internal API:

- schema validator
- policy rule evaluator
- boundary checker
- quarantine manager
- severity classifier
- release gate evaluator

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- validation request identifier
- artifact identifier and checksum
- policy and schema versions
- source and destination engine identifiers
- gate decision and reason
- violations, warnings, and severity
- quarantine or escalation status
- reviewer identity where human review is required

Failure behaviour:

- fail closed when policy, schema, lineage, or checksum data is missing
- quarantine artifacts that fail critical validation
- block transitions with unresolved boundary violations
- emit explicit decision states rather than returning ambiguous success
- never modify an artifact to make it pass validation

Permitted actions:

- validate artifacts and transitions
- approve, reject, quarantine, or escalate according to policy
- produce Validated Evidence Packages after evidence validation passes
- enforce source admission, evidence, analysis, synthesis, and release gates
- require human review
- publish boundary compliance reports

Forbidden actions:

- fetch data
- retrieve external data
- alter source records
- rewrite provenance
- rewrite artifacts
- calculate analytical results
- generate narrative text
- generate public narrative beyond validation notices
- render publication bundles
- repair artifacts to make them pass validation
- suppress required failures or warnings

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Aegis governance maintainer, to be assigned before implementation

### Apollo

Purpose:

Apollo is the rendering, packaging, and publication assembly engine. It converts
approved analytical and narrative artifacts into report, chart, dashboard, or
static-site Publication Packages.

Responsibilities:

- consume only approved analysis and narrative artifacts
- render report pages, chart embeds, dashboards, PDFs, or static bundles
- create Publication Packages, Publication Manifests, and preview artifacts
- preserve references to source analysis, narrative, validation, and release gates
- package assets without changing analytical meaning
- request release validation before promotion

Inputs:

- approved analysis package
- approved narrative package
- chart-ready data
- chart specification
- publication template
- asset references
- release gate decision
- publishing configuration

Outputs:

- publication package
- rendered report page
- static publication bundle
- chart embed artifact
- dashboard artifact
- PDF or export artifact where approved
- publication manifest
- preview artifact
- rendering log reference

Dependencies:

- Abacus for chart-ready analytical data and chart specifications
- Vyasa for narrative packages
- Aegis for release gates and publication policy decisions
- Thoth for lineage, artifact references, and manifest registration
- Hermes for approved external delivery where required
- Argus for rendering logs, build health, and publication audit trails

Public API:

- `render_report`
- `build_publication_bundle`
- `get_preview_artifact`
- `get_publication_manifest`
- `request_release_candidate`
- `list_supported_render_targets`

Internal API:

- template renderer
- chart embed builder
- asset bundler
- manifest builder
- export renderer
- preview builder

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- render request identifier
- input analysis and narrative artifact identifiers
- template and asset versions
- render target
- release gate reference
- output bundle identifier and checksum
- warnings about missing assets, unsupported chart targets, or layout failures
- publication manifest identifier

Failure behaviour:

- fail closed when required approval or input artifact is missing
- produce preview-only artifacts when release approval is absent
- mark incomplete bundles as non-canonical
- never promote a bundle that failed validation
- preserve rendering errors with enough context for reproduction

Permitted actions:

- render approved artifacts into publication formats
- package static assets and manifests
- create previews and release candidates
- request Aegis release validation
- hand approved bundles to a deployment or delivery boundary

Forbidden actions:

- alter analytical findings, numbers, units, or caveats
- fetch raw source evidence
- perform statistical analysis
- invent claims
- bypass Aegis
- publish unvalidated material
- alter evidence meaning
- approve its own release gate
- bypass failed validation
- generate unsupported narrative claims

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Apollo publishing maintainer, to be assigned before implementation

### Argus

Purpose:

Argus is the observability, audit, monitoring, and incident evidence engine. It
records what the system did, when it happened, which engine did it, and whether
the behaviour remained inside contract boundaries.

Responsibilities:

- collect structured events from every engine
- maintain run, health, failure, and incident timelines
- correlate events across engines using shared identifiers
- raise alerts for policy, transport, validation, analysis, rendering, or audit failures
- preserve audit trails for review and governance
- report missing logs or degraded observability as first-class failures

Inputs:

- structured engine events
- run identifiers
- health checks
- failure reports
- gate decisions
- transport receipts
- artifact identifiers
- correlation identifiers

Outputs:

- audit record
- run timeline
- engine health report
- alert
- incident record
- observability gap report
- monitoring dashboard data

Dependencies:

- all engines for structured events and health signals
- Thoth for artifact and lineage references
- Aegis for policy severity and gate decision context
- shared clock, identity, error taxonomy, and configuration services

Public API:

- `record_event`
- `get_run_timeline`
- `get_engine_health`
- `raise_alert`
- `get_audit_record`
- `report_observability_gap`

Internal API:

- event collector
- log normaliser
- correlation engine
- alert rule evaluator
- retention manager
- incident timeline builder

Internal APIs must not be consumed directly by other engines.

Logging requirements:

- Argus must log its own ingestion, processing, retention, and alert failures
- every event must include timestamp, engine identifier, severity, and correlation identifier
- audit-critical events must include artifact or gate references where applicable
- dropped, delayed, malformed, or duplicate events must be recorded
- retention decisions must be traceable to policy

Failure behaviour:

- observability failure must not modify source, evidence, analysis, or publication artifacts
- engines may continue local non-release work only if they can write fallback logs
- release gates should block when audit-critical Argus records cannot be reconciled
- missing telemetry must be reported as an observability gap, not ignored
- alert storms must be rate-limited without deleting underlying audit events

Permitted actions:

- observe engine activity
- append audit records
- correlate run events
- raise alerts
- report health and incident state
- preserve monitoring evidence

Forbidden actions:

- alter artifact payloads
- alter engine outputs
- modify business logic
- approve or reject policy gates
- approve deployment
- execute retries on behalf of Hermes
- analyse evidence values
- generate narrative content
- render or publish outputs
- repair missing audit trails by inventing events

Version:

- Boundary version: 1.0-R1
- Implementation status: not started by this milestone

Ownership:

- Contract owner: ALIS Core documentation owner
- Engine owner: Argus observability maintainer, to be assigned before implementation

## Governance Rules

1. Interface before implementation: public contracts must exist before production code.
2. One canonical builder per artifact: each artifact has exactly one owning engine.
3. Read through contracts: engines consume public artifacts, not internal APIs.
4. No in-place mutation across boundaries: downstream work creates new artifacts.
5. Fail closed on missing governance data: absent validation is not approval.
6. Preserve lineage: every canonical output must identify its inputs and versions.
7. Preserve evidence: raw and validated evidence must not be rewritten for convenience.
8. Log every transition: engine handoffs must produce structured audit events.
9. Make uncertainty visible: caveats, warnings, and incomplete states must survive downstream.
10. Separate transport from judgment: moving data is not admission, validation, or analysis.
11. Separate rendering from analysis: publication formatting must not change findings.
12. Version every boundary: contract changes require explicit version notes and review.
13. Escalate ambiguity: unclear policy, missing provenance, or unsupported claims require review.
14. Keep shared services subordinate: shared utilities do not own engine responsibilities.
15. Do not implement from this register alone: this milestone creates boundaries, not code.

## Contract Change Rules

Boundary changes must be reviewed when they:

- add a new public API identifier
- remove or rename a public API identifier
- change an engine's canonical outputs
- allow a new side effect
- alter failure behaviour
- change ownership of an artifact type
- weaken logging, validation, or provenance requirements

Minor wording changes that do not alter behaviour may remain in the same
version. Behavioural changes require a new boundary register version or an
explicit amendment.

## Milestone Constraint

This document authorises documentation of ALIS Core boundaries only.

It does not authorise:

- production code
- refactoring
- architecture changes
- file moves outside the requested register naming alignment
- new engine implementations
- new runtime dependencies
- hidden cross-engine coupling

STATUS: BOUNDARY REGISTER REVISED
REVISION: V1.0-R1
IMPLEMENTATION: NOT STARTED
FREEZE: PENDING REVIEW
NEXT RECOMMENDED STEP: Independent Re-Review
