# 🚦 Error and failure behaviour

## Current application boundary

The project does not contain a backend, request handler, database, or custom application API. Most failures are static resource failures or browser-side JavaScript failures.

## Failure scenarios

| Failure | Visitor-visible effect | Maintainer response |
|---|---|---|
| Local image path missing | Broken image or empty carousel item | Restore file or correct path and case |
| Local stylesheet missing | Page appears unstyled | Fix link path and validate all pages |
| jQuery unavailable | Flipster initialization fails | Restore dependency availability or plan a tested fallback |
| Flipster script unavailable | Carousel interaction fails | Check local script reference and console |
| CDN unavailable | Bootstrap/icons/fonts may be missing | Check provider and consider an approved fallback |
| Elfsight unavailable | Media widget area may remain empty | Verify provider configuration and display a clear fallback |
| Static host cache stale | Old content or assets appear | Inspect cache headers and redeploy/purge if supported |

## User-facing failure design

A missing external widget should not make the entire page unusable. Keep surrounding navigation and page content meaningful. Avoid an endless spinner or a blank full-page area for a non-critical third-party component.

## Diagnostics

Use the browser developer console and Network panel. Record the URL, HTTP status, browser, viewport, page, and commit. Remove cookies, tokens, and private query values before sharing diagnostics.

## Future interactive features

If forms, uploads, or APIs are introduced, define validation errors, retry behaviour, rate limits, user feedback, and logging separately. Do not describe backend error codes before an API exists.
