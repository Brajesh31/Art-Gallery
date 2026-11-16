# 🧩 System diagrams

This page is the diagram index. All diagrams must describe the current repository accurately. A future capability must be labeled as proposed, not implemented.

## 1. System context

```mermaid
flowchart LR
  Visitor[Visitor] -->|HTTP request| StaticHost[Static host]
  StaticHost -->|HTML CSS JS images| Browser[Browser]
  Browser -->|Library requests| CDN[Public CDNs]
  Browser -->|Widget request| Elfsight[Elfsight platform]
  Maintainer[Maintainer] -->|Reviewed commits| GitHub[GitHub repository]
  GitHub -->|Static deployment| StaticHost
```

## 2. Use-case view

```mermaid
flowchart TB
  Visitor((Visitor))
  Maintainer((Maintainer))
  Visitor --> U1[Open home gallery]
  Visitor --> U2[Browse carousel]
  Visitor --> U3[Read About page]
  Visitor --> U4[Open media page]
  Maintainer --> M1[Update page content]
  Maintainer --> M2[Add licensed artwork]
  Maintainer --> M3[Review dependencies]
  Maintainer --> M4[Publish static files]
```

## 3. Data-flow view

```mermaid
flowchart TD
  HTML[Static HTML documents] --> Browser[Visitor browser]
  CSS[Local CSS files] --> Browser
  JS[Local Flipster script] --> Browser
  Images[Local image assets] --> Browser
  CDN[External CDN resources] --> Browser
  Widget[Third-party media widget] --> Browser
  Browser --> Visitor[Rendered page]
```

No first-party visitor data store or backend process is represented because none exists in the current repository.

## 4. Page-navigation view

```mermaid
stateDiagram-v2
  [*] --> Home
  Home --> About: About Me
  Home --> Media: Youtube
  About --> Home: Home
  About --> Media: Youtube
  Media --> Home: Home
  Media --> About: About Me
```

## 5. Release workflow

```mermaid
flowchart TD
  Change[Change files] --> Review[Review diff and rights]
  Review --> Local[Preview all pages]
  Local --> CI[Run static reference checks]
  CI --> Pass{Checks pass?}
  Pass -->|No| Fix[Correct defects]
  Fix --> Local
  Pass -->|Yes| Merge[Commit to main]
  Merge --> Deploy[Static hosting deployment]
  Deploy --> Smoke[Verify deployed pages]
  Smoke --> Complete[Record release evidence]
```

## Diagram maintenance

- Keep Mermaid syntax in fenced code blocks.
- Label external providers and trust boundaries.
- Do not show an API/database that is not implemented.
- Update diagrams when pages, scripts, or assets change.
- Verify diagrams render in GitHub before release.
