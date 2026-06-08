# Source Admission Rule

## Purpose

The source admission rule defines whether a source may enter GoDataBank. Admission is required before a source can support any report, summary, table, chart, or published claim.

## Admission Standard

A source is admissible only when all of the following conditions are met:

1. The issuing body is an official institution.
2. The source is publicly accessible.
3. The source provides a public API or approved machine-readable feed.
4. The relevant content or metadata is available in English.
5. Citation metadata can be captured.
6. The source is not excluded by the exclusion policy.

Failure on any required condition means the source must not be admitted.

## Official Institution Requirement

An admissible institution may include:

- National, regional, or local government bodies
- Government departments and agencies
- National statistical offices
- Regulators
- Courts and official legal publishers
- Central banks and public monetary authorities
- Public standards bodies
- Intergovernmental organisations
- Official public health, environment, education, transport, labour, finance, or science bodies

The source must be issued or maintained by the institution itself, not by an unofficial mirror, commentary site, media outlet, vendor, or third-party aggregator.

## Machine-Readable Requirement

At least one public machine-readable access path is required, such as:

- Public API endpoint
- Open data portal endpoint
- Bulk CSV, JSON, XML, RDF, Parquet, XLSX, or similar structured download
- Official structured feed
- Official metadata catalogue with machine-readable records

Human-only web pages, PDFs without structured data access, screenshots, press releases without structured data, and manually copied tables are insufficient for admission unless an official machine-readable companion source is also available.

## English Requirement

The source must provide English content or English metadata sufficient to identify, interpret, and cite the data accurately. If translation would be required to understand the source, the source is not admissible under this milestone.

## Required Admission Record

Each admitted source must have a record containing:

- Source ID
- Institution name
- Institution type
- Jurisdiction or governing body
- Official source URL
- Public API or approved machine-readable access URL
- Access method and approval basis
- Data format
- English-language evidence
- Source title or dataset name
- Publication date, release date, or version date where available
- Retrieval timestamp
- Citation metadata status
- Licence or terms URL where available
- Verification status
- Reviewer or admitting agent
- Admission decision date

## Admission Decisions

Use the following decision states:

- `admitted`: all admission conditions are met.
- `rejected`: one or more required conditions fail.
- `review_required`: evidence is incomplete and the source must not support reports yet.

Only `admitted` sources may support published output.

If no admitted source matches the required claim, geography, metric, time period, or definition, the output must not be produced.

## Re-Verification

An admitted source should be re-verified when:

- Its endpoint, feed, or structured file changes.
- Its issuing institution changes ownership or publication responsibility.
- Citation metadata becomes incomplete or outdated.
- The source becomes unavailable.
- A report depends on a time-sensitive release.
