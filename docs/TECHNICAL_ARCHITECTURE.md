# Technical Architecture

## Current phase

Pre-production documentation. No engine or runtime is fixed yet.

## Data-first design

Narrative entities should be represented through stable IDs and validated data: missions, characters, factions, regions, locations, evidence, routes, documents, rescues, resources, and state transitions.

## Suggested layers

- Content data.
- Schema validation.
- Narrative state and deterministic rules.
- Simulation adapters.
- Runtime presentation.
- Tooling and tests.

## Validation requirements

Validate unique IDs, required mission fields, valid references, chronological dates, faction membership, region membership, deterministic input declarations, rescue requirements, and forbidden random dependencies.

## Repository language

All documentation, schemas, tools, tests, and code comments are written in English.