# 🏛️ Static-site architecture

## Architectural style
Art Gallery is a browser-rendered static multi-page website. The browser opens an HTML document, downloads linked stylesheets and scripts, loads local images, and runs client-side carousel initialization where configured. There is no application server, database, API, account system, or build process in the tracked tree.

## Component diagram
```mermaid
flowchart TB
  B[Visitor browser]
  subgraph Pages
    H[index.html]
    A[about.html]
    Y[youtube.html]
  end
  subgraph Local_assets
    CSS[style.css]
    AC[about.css]
    FC[footer.css]
    FL[Flipster local CSS and JS]
    IMG[images folder]
  end
  subgraph External_dependencies
    BS[Bootstrap CDN]
    JQ[jQuery CDN]
    F[Font Awesome and Google Fonts]
    EW[Elfsight platform script]
  end
  B --> H
  B --> A
  B --> Y
  H --> CSS
  H --> FC
  H --> FL
  H --> IMG
  A --> CSS
  A --> AC
  A --> FC
  A --> IMG
  Y --> CSS
  Y --> FC
  H --> BS
  A --> BS
  Y --> BS
  H --> JQ
  H --> F
  A --> F
  Y --> F
  Y --> EW
```

## Home-page carousel flow
```mermaid
sequenceDiagram
  participant Visitor
  participant Browser
  participant Home as index.html
  participant Assets as Local image assets
  participant Flipster as jQuery Flipster
  Visitor->>Browser: Open home page
  Browser->>Home: Parse HTML
  Home->>Assets: Request gallery images
  Assets-->>Browser: Image files
  Home->>Flipster: Initialize .carousel
  Flipster-->>Browser: Carousel behaviour
  Browser-->>Visitor: Render gallery
```

## Page responsibilities
- **Home:** presents the image collection and initializes Flipster on the carousel element.
- **About:** presents descriptive text and a local profile image.
- **Media:** contains an Elfsight mount point and platform script.

## Dependency boundaries
HTML pages use relative paths for local CSS, JavaScript, and images. Bootstrap, jQuery, Font Awesome, Google Fonts, and Elfsight are external runtime dependencies. If a CDN or provider is unavailable, some presentation or widget behaviour may degrade.

## Operational implications
- Static hosting is sufficient.
- CDN availability and provider-side changes can affect runtime behaviour.
- A restrictive Content Security Policy must allow required sources or external resources will fail.
- Local image paths must preserve filename case.
- Browser-delivered source is public. Do not add secrets to HTML or JavaScript.
