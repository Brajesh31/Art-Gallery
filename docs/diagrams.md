# 🧩 System diagrams

This page is the editable diagram catalogue. Diagrams describe the current repository unless a section is explicitly marked as a future proposal.

## 1. System context diagram

```mermaid
flowchart LR
  Visitor[Visitor] -->|HTTP request| Host[Static host]
  Host -->|HTML CSS JS images| Browser[Visitor browser]
  Browser -->|Library requests| CDN[Public CDNs]
  Browser -->|Widget request| Widget[Elfsight platform]
  Maintainer[Maintainer] -->|Reviewed commits| GitHub[GitHub repository]
  GitHub -->|Static deployment| Host
```

## 2. Component diagram

```mermaid
flowchart TB
  subgraph BrowserRuntime[Browser runtime]
    Home[index.html]
    About[about.html]
    Media[youtube.html]
    Shared[style.css and footer.css]
    AboutStyle[about.css]
    Flipster[Flipster CSS and JS]
    Artwork[images folder]
  end
  Home --> Shared
  Home --> Flipster
  Home --> Artwork
  About --> Shared
  About --> AboutStyle
  About --> Artwork
  Media --> Shared
  Home -.->|external dependencies| CDN[Bootstrap and jQuery CDNs]
  About -.->|external fonts/icons| CDN
  Media -.->|external widget| Elfsight[Elfsight platform]
```

## 3. Use-case diagram

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

## 4. Data-flow diagram

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

## 5. Page-navigation state diagram

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

## 6. Home-page loading sequence

```mermaid
sequenceDiagram
  actor Visitor
  participant Browser
  participant Home as index.html
  participant Local as Local assets
  participant JQuery as jQuery CDN
  participant Carousel as Flipster
  Visitor->>Browser: Open home page
  Browser->>Home: Request HTML
  Home->>Local: Request CSS and images
  Local-->>Browser: Return local assets
  Home->>JQuery: Load jQuery
  JQuery-->>Browser: jQuery runtime
  Home->>Carousel: Initialize carousel
  Carousel-->>Browser: Carousel interaction
  Browser-->>Visitor: Render gallery
```

## 7. Static deployment flow

```mermaid
flowchart TD
  Commit[Reviewed commit] --> CI[Repository validation]
  CI --> Result{Checks pass?}
  Result -->|No| Fix[Fix links, assets or tests]
  Fix --> CI
  Result -->|Yes| Deploy[Static host publishes files]
  Deploy --> Smoke[Open all three public pages]
  Smoke --> Good{Pages and assets work?}
  Good -->|No| Rollback[Restore last known-good revision]
  Good -->|Yes| Release[Record deployed commit]
```

## 8. Data model and ER diagram status

An entity-relationship diagram is not applicable to the current implementation. There is no database, persistent application data, or structured artwork catalogue. The proposed artwork metadata fields are documented in [Content model](content-model.md), but they are not a live database schema.

## 9. API diagram status

There is no project-owned API. The pages request static files and external third-party resources. Do not draw endpoints or request/response schemas as implemented until an API is introduced and verified.

## 10. Visual SVG assets

- ![Architecture overview](../assets/architecture-overview.svg)
- ![Visitor journey](../assets/visitor-journey.svg)
- ![Artwork publishing workflow](../assets/artwork-publishing-flow.svg)

## Diagram maintenance

- Keep Mermaid source editable in Markdown.
- Label external providers and trust boundaries.
- Do not show an API/database that is not implemented.
- Update diagrams when pages, scripts, or assets change.
- Verify diagrams render in GitHub before release.
