# 🗂️ Project structure

## Current repository map

```text
Art-Gallery/
├── .github/
│   ├── ISSUE_TEMPLATE/          # Structured bug, feature, and documentation reports
│   ├── workflows/               # GitHub Actions workflows
│   └── PULL_REQUEST_TEMPLATE.md
├── images/
│   ├── img1.jpg ... img10.jpg   # Gallery images
│   └── sample.png               # About/profile image
├── docs/
│   ├── README.md
│   ├── project-overview.md
│   ├── project-structure.md
│   ├── architecture.md
│   ├── installation.md
│   ├── deployment.md
│   ├── external-resources.md
│   ├── image-assets.md
│   ├── accessibility.md
│   ├── testing.md
│   ├── limitations-and-roadmap.md
│   └── ...
├── index.html                   # Home gallery and carousel
├── about.html                   # About page
├── youtube.html                 # Media page with external widget mount point
├── style.css                    # Shared base and page backgrounds
├── about.css                    # About page layout and typography
├── footer.css                   # Shared footer styles
├── jquery.flipster.min.css      # Local carousel styles
├── jquery.flipster.min.js       # Local carousel behaviour
├── README.md
├── LICENSE
└── ...
```

## File responsibilities

| Path | Responsibility |
|---|---|
| `index.html` | Home navigation, carousel markup, image references, footer, and carousel initialization |
| `about.html` | About content, profile image, navigation, and footer |
| `youtube.html` | External media-widget mount point, navigation, and footer |
| `style.css` | Shared reset, backgrounds, and page-level layout |
| `about.css` | About content layout, text styles, and responsive breakpoints |
| `footer.css` | Distributed footer layout and responsive footer styles |
| `jquery.flipster.min.css` | Vendored Flipster carousel styles |
| `jquery.flipster.min.js` | Vendored Flipster carousel script |
| `images/` | Local artwork and page image assets |
| `.github/workflows/` | Repository validation and README automation |

## Runtime dependency direction

The HTML pages load CSS and JavaScript into a browser. Local assets are addressed using relative paths. External libraries are loaded from public CDNs. There is no application server or data persistence layer.

## Change rules

- Update this inventory when a page, stylesheet, script, or asset directory changes.
- Preserve image filenames unless every reference is updated.
- Verify path case using a Linux-compatible check before deployment.
- Do not add build tooling or a framework solely to make the tree look more complex.
- Keep minified vendor libraries intact unless intentionally upgrading them from a traceable upstream release.
