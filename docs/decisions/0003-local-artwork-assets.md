# ADR 0003: Keep artwork as local static assets

- **Status:** Accepted, reviewable
- **Date:** 2026-11-16
- **Decision owners:** Repository maintainer

## Context

The current gallery references local image files in the repository. There is no image CDN, upload service, database, or asset management backend.

## Decision

Keep existing artwork files in the repository and preserve their filenames during maintenance work. New artwork must have verified source and redistribution permission, accurate alternative text, and a documented asset record.

## Alternatives considered

- Load artwork from a third-party image host.
- Add an object-storage bucket and image delivery service.
- Introduce a content management system.

Those options add external dependencies or infrastructure and are not justified by the current static gallery scope.

## Consequences

- Static deployment remains simple.
- The repository carries the image transfer size.
- Asset rights and provenance must be managed carefully.
- Large collections may eventually justify responsive image delivery or a content catalogue.

## Revisit when

The gallery size, publishing frequency, image delivery requirements, or content governance needs materially change.
