# Abacus

## Status

Abacus v0.1 implements the first deterministic classification layer between Validator and future reporting systems.

This folder does not contain report-generation code, AI summarisation code, API connectors, databases, subscription features, search, publishing logic, or additional institution connectors.

## Purpose

Abacus organises approved metadata into a fixed taxonomy. In v0.1 it consumes only approved Validator records, classifies them with deterministic keyword rules, and writes classification output under `data/classified/`.

## v0.1 Responsibilities

Abacus v0.1 supports:

- Institution classification
- Country or region classification
- Sector classification
- Topic derivation from metadata title and fields
- Keyword extraction from metadata title
- Tag generation from deterministic classification values

## Evidence Rules

Abacus must not allow unsourced output. Every claim must be traceable to admitted official institutional source material with complete citation metadata.

No speculation, no opinion, and no source match means no output.

Abacus v0.1 does not make factual claims beyond classification labels derived from validated metadata.

## Input Boundary

Abacus v0.1 accepts approved Validator records only. Rejected or raw ALIS records are outside scope.

## Non-Goals

Abacus must not introduce:

- AI summarisation code in this milestone
- API connectors
- Databases
- Subscription features
- Publishing
- Search
- Subscriber systems
- Additional institutions
- Uncited claims
- Use of news organisations, commercial data vendors, think tanks, blogs, social media, user-generated content, or unofficial aggregators
