# 🗂️ Project structure

## Current repository map

```text
Art-Gallery/
├── .github/
│   ├── ISSUE_TEMPLATE/              # Bug, feature and documentation issue forms
│   ├── workflows/                   # Quality checks and README maintenance
│   ├── dependabot.yml               # GitHub Actions update schedule
│   └── PULL_REQUEST_TEMPLATE.md
├── assets/
│   ├── art-gallery-banner.svg       # README/project banner
│   ├── architecture-overview.svg    # Static architecture visual
│   ├── visitor-journey.svg          # Visitor navigation visual
│   └── artwork-publishing-flow.svg  # Artwork governance visual
├── docs/
│   ├── decisions/                   # Architecture Decision Records
│   ├── templates/                   # Reusable document templates
│   └── *.md                         # Project-specific technical guides
├── images/
│   ├── img1.jpg ... img10.jpg       # Existing gallery artwork
│   └── sample.png                  # Existing About page image
├── scripts/
│   └── validate_repository.py       # Local reference and SVG validation
├── tests/
│   └── test_repository_validation.py
├── index.html                       # Home gallery and carousel
├── about.html                       # About page
├── youtube.html                     # Media page/widget mount point
├── style.css                        # Shared base styles
├── about.css                        # About page styles
├── footer.css                       # Shared footer styles
├── jquery.flipster.min.css          # Vendored carousel styles
├── jquery.flipster.min.js           # Vendored carousel behaviour
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── SUPPORT.md
├── GOVERNANCE.md
├── MAINTAINERS.md
├── ACCESSIBILITY.md
├── RELEASE.md
├── CHANGELOG.md
├── ROADMAP.md
└── LICENSE
```

## File responsibilities

| Path | Responsibility |
|---|---|
| `index.html` | Home navigation, carousel markup, image references, footer, carousel initialization |
| `about.html` | About content, profile image, navigation, footer |
| `youtube.html` | Third-party widget mount point, navigation, footer |
| `style.css` | Shared reset, backgrounds, and page-level layout |
| `about.css` | About content layout, typography, responsive breakpoints |
| `footer.css` | Footer layout and responsive behaviour |
| `jquery.flipster.min.css` | Vendored Flipster carousel styles |
| `jquery.flipster.min.js` | Vendored Flipster carousel script |
| `images/` | Original local artwork and page image |
| `assets/` | Project banner and documentation diagrams |
| `docs/` | Architecture, operations, testing, security, and contributor guides |
| `scripts/` | Standard-library repository validation |
| `tests/` | Unit tests for validation helpers |
| `.github/workflows/` | CI validation and README automation |

## Runtime boundaries

HTML pages load local CSS, scripts, and images. External libraries and widget code are loaded from public providers. There is no first-party API, data store, user session, or server-side execution.

## Change rules

- Update this inventory when a page, stylesheet, script, or asset directory changes.
- Preserve existing image filenames unless all references are updated.
- Verify path case using a Linux-compatible check before deployment.
- Keep vendored minified libraries separate from project-authored code.
- Do not add build tooling or a framework solely to make the tree look more complex.
