# 🐞 Known issues and verification gaps

This page separates repository-observed gaps from issues that require live browser verification.

## Confirmed from source inspection

1. The search form has no implemented search index or endpoint in the repository.
2. Some social links are placeholders rather than verified profile destinations.
3. The original HTML references Font Awesome over HTTP, which can be blocked on HTTPS pages.
4. Existing image elements use empty alt attributes and need image-by-image review.
5. The media page includes an Elfsight widget mount point, but the repository does not prove the widget is configured or active.
6. The project has no backend, API, database, user accounts, or image upload flow.

## Requires manual verification

- Carousel keyboard interaction and screen-reader announcements.
- Reduced-motion behaviour.
- Current CDN availability and security metadata.
- Elfsight account ownership, widget content, cookies, and privacy behaviour.
- Visual layout across actual browsers and devices.
- Actual deployed URL and static-host configuration.
- Image creator, source, redistribution permissions, and attribution.

## Reporting a new issue

Include page, browser/version, viewport, reproduction steps, expected and observed behaviour, and sanitized console/network diagnostics. Do not post credentials, private data, or artwork without sharing rights.

## Resolution policy

Update this page when an issue is genuinely fixed or when a new verified issue is discovered. A roadmap checkbox or documentation edit alone does not resolve a user-facing defect.
