# 📦 Dependency register

## Runtime dependencies

| Dependency | Current use | Location | Ownership |
|---|---|---|---|
| Bootstrap 5.1.3 | Responsive navigation/layout classes | CDN references in HTML | External provider |
| jQuery 3.6.0 | Flipster runtime dependency | CDN reference in home page | External provider |
| jQuery Flipster | Home carousel | Local minified JS/CSS | Vendored project file |
| Font Awesome 4.2.0 | Footer icons | CDN reference in HTML | External provider |
| Google Fonts | Typography | CSS/HTML external font references | External provider |
| Elfsight platform | Media widget | Media page script | External provider |

## Development dependencies

The current static site has no package.json, npm dependency tree, bundler, or compile step. Repository validation uses Python's standard library and GitHub Actions.

## Maintenance rules

- Verify the exact version and source of every new library.
- Prefer HTTPS.
- Do not add an external library for a feature that can be handled safely with existing browser capabilities.
- Review licenses and maintenance activity before adopting a new dependency.
- Keep vendor files distinguishable from project-authored files.
- Remove a dependency only after checking every page and script reference.
- Do not fabricate version upgrades or security status.

## Review record

Record dependency, version, source URL, date reviewed, license, purpose, affected pages, integrity value where applicable, and migration notes. Review external resources before a release and when a provider announces a breaking change.
