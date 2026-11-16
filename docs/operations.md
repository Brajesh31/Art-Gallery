# 🧰 Operations and maintenance

## Operational model

The site is served as static files. There is no application server, database process, queue, scheduled backend job, or runtime service to monitor. Operational work is primarily repository maintenance, deployment verification, external dependency review, and content/asset governance.

## Routine maintenance

### On every change
- Validate local paths.
- Open all affected pages.
- Inspect browser console and network failures.
- Check responsive layout and keyboard access.
- Update docs and changelog when behaviour or dependencies change.

### Monthly or before a release
- Review external library versions and known security advisories.
- Verify CDN URLs and integrity metadata.
- Check third-party widget availability and privacy behaviour.
- Review image attribution and takedown requests.
- Review open issues and outdated roadmap items.
- Check deployed HTTPS and response headers.

## Operational signals

| Signal | Where to inspect | Expected action |
|---|---|---|
| Failed image/CSS/JS request | Browser Network panel | Correct path, host, or dependency |
| JavaScript exception | Browser console | Reproduce and fix or document |
| Widget not rendered | Media page and provider dashboard | Verify provider configuration and privacy blockers |
| Old content after deploy | Hosting cache and response headers | Purge or wait for cache expiry |
| CI validation failure | GitHub Actions | Inspect exact broken local reference |

## Ownership

The repository maintainer is responsible for release readiness, dependency review, content ownership, and incident coordination. The project does not currently define a formal on-call service or response-time commitment.

## Incident notes

Record date, affected page, deployed revision, impact, cause, mitigation, and follow-up. Never publish credentials, session data, or private visitor information in incident notes.
