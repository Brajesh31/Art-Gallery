# ADR 0002: Retain the existing Flipster carousel

- **Status:** Accepted, reviewable
- **Date:** 2026-11-16
- **Decision owners:** Repository maintainer

## Context

The home page currently uses a local copy of jQuery Flipster and depends on jQuery. The carousel is part of the site's existing visual presentation.

## Decision

Preserve the existing carousel implementation during documentation and repository-governance work. Do not replace or rewrite vendor code without a scoped user-facing requirement and a tested migration plan.

## Alternatives considered

- Replace with a native CSS/JavaScript carousel.
- Adopt a different maintained carousel package.
- Remove the carousel and render a static image grid.

No alternative is selected in this ADR because the existing interaction has not yet been audited against keyboard, screen-reader, and reduced-motion requirements.

## Consequences

- Existing appearance and interaction are preserved.
- The site retains a jQuery dependency.
- Vendor version and license provenance should be reviewed.
- Keyboard navigation and motion behaviour require manual accessibility testing.

## Revisit when

The carousel blocks accessibility, has unresolved security/maintenance concerns, or a new gallery interaction is explicitly requested.
