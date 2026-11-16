# ADR 0001: Keep the website static

- **Status:** Accepted
- **Date:** 2026-11-16
- **Decision owners:** Repository maintainer

## Context

The repository currently consists of three HTML pages, CSS stylesheets, a local Flipster carousel library, and image assets. It has no backend API, database, authentication, server-side rendering, or build process.

## Decision

Keep the website as a static multi-page site for the current scope. Do not introduce a backend or frontend framework without a concrete feature requirement that cannot be served effectively by static files.

## Alternatives considered

1. **Introduce a full-stack framework:** rejected for current scope because it adds build, dependency, deployment, and maintenance complexity without an established need.
2. **Add a small backend immediately:** rejected because no current feature requires persistent or private server-side data.
3. **Continue with static HTML/CSS/JavaScript:** accepted because it matches the existing implementation and can be deployed on simple static hosting.

## Consequences

### Positive
- Simple deployment and low operational overhead.
- No database administration or server process.
- Source and content are easy to inspect.
- Existing page design can be maintained incrementally.

### Trade-offs
- Content is edited in source files.
- Search, uploads, accounts, comments, and moderation are not provided.
- Browser-visible source cannot contain secrets.
- Third-party CDN and widget dependencies remain relevant risks.

## Revisit when

A genuine requirement for authenticated content management, visitor submissions, private data, or dynamic catalogue search is approved.
