# 🔭 Monitoring and observability

## Current observability

The project has no server process or application telemetry pipeline. The most useful current diagnostics are browser developer tools, GitHub Actions results, static-host deployment status, and provider dashboards for external widgets.

## Signals to collect

| Signal | Source | Why it matters |
|---|---|---|
| Failed local asset request | Browser Network panel | Broken page dependencies |
| JavaScript exception | Browser console | Carousel or widget initialization errors |
| HTTP response status | Browser/host tools | Missing pages and deployment failures |
| CI result | GitHub Actions | Detect broken repository references |
| External widget status | Provider dashboard and browser | Third-party integration health |
| Performance metrics | Lighthouse/DevTools | Image and rendering bottlenecks |

## Privacy boundaries

Do not introduce visitor analytics or tracking solely for the sake of a dashboard. Any telemetry must have a defined purpose, data-minimization plan, retention policy, and appropriate consent/legal review.

## Incident record

Record timestamp, affected page, browser, deployed commit, observed symptom, impact, cause, mitigation, and follow-up. Remove personal data and session tokens from logs before sharing them.
