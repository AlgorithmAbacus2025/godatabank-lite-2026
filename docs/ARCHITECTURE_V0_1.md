# GoDataBank Architecture v0.1

## Mission

Official data. Verified evidence. Searchable insights.

GoDataBank exists to collect, verify, organise, summarise, and publish evidence from official institutional sources only. Every published output must be traceable to admitted source material with complete citation metadata.

Truth is retrieved, not generated.

## Build Milestone 1 Scope

This milestone is a documentation and structure baseline only. It defines the intended system boundaries and governance rules before implementation begins.

Included in this milestone:

- Architecture baseline
- Agent laws
- Source admission rule
- Exclusion policy
- Citation policy
- Report manifest scaffold
- Report HTML template
- Backend component README files

Excluded from this milestone:

- API connectors
- AI summarisation code
- Databases
- Subscription features
- Payment, account, or access-control features
- Any expansion beyond official, public, approved machine-readable English-language sources

## Core Principles

1. Official institutions only: admitted sources must be issued by recognised public, governmental, regulatory, statistical, judicial, standards, central-bank, or intergovernmental institutions.
2. Public API or approved machine-readable feed required: source material must be available through a public API, open data endpoint, approved bulk download, approved structured file, or approved machine-readable feed.
3. English content required: admitted source material must provide English-language content or English-language metadata sufficient for accurate publication.
4. Citation metadata required: no fact, figure, table, chart, or summary may be published without citation metadata.
5. No excluded publishers: news organisations, commercial data vendors, think tanks, blogs, social media, user-generated content, advocacy sites, personal sites, and unofficial aggregators are outside scope.
6. No unsourced output: publication requires evidence, citation, and a clear link between claim and source.
7. No speculation or opinion: if no admitted source matches a claim, the correct output is no output.

## Conceptual System Boundaries

The v0.1 architecture recognises three future backend areas. In Build Milestone 1 these are documentation placeholders only.

### ALIS

ALIS is the future source admission boundary. It should record source candidates, test them against the source admission rule, and prevent unadmitted sources from entering published outputs.

ALIS must not be treated as an API connector in this milestone.

### Validators

Validators are the future policy enforcement boundary. They should check whether source records, citation records, and report records meet the required rules before publication.

Validators must not fetch, scrape, transform, or summarise source content in this milestone.

### Abacus

Abacus is the future evidence organisation and report assembly boundary. It should organise admitted source material and ensure that all published claims remain linked to citation metadata.

Abacus must not contain AI summarisation logic in this milestone.

## Conceptual Data Flow

1. Candidate source is identified.
2. Source is screened against official-institution and exclusion rules.
3. Source is checked for public API or approved machine-readable feed availability.
4. English-language availability is confirmed.
5. Citation metadata is captured.
6. Source is either admitted, rejected, or held for review.
7. Only admitted sources may support report content.
8. Reports publish summaries, tables, or findings only when all claims are sourced.

## Publication Gate

A report is ready to publish only when:

- Every source is admitted under the source admission rule.
- Every source has complete citation metadata.
- Every report claim has a source reference.
- Every numerical result includes units and method notes where applicable.
- Excluded source categories have not been used.
- Uncertainty, missing fields, and limitations are disclosed.
- No speculation, opinion, or unmatched source claims are present.

## Version Notes

Architecture version `0.1` is intentionally narrow. It establishes governance and traceability before any collection, validation, summarisation, database, or publishing code is created.
