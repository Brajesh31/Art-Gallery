# Art Gallery

Art Gallery is a small static website that presents local images in a dark carousel layout. It contains a home gallery, an about page, and a YouTube/media page, with shared CSS and footer styling.

## Technology

- HTML5 and CSS3.
- Bootstrap 5.1.3 loaded from jsDelivr.
- jQuery Flipster (`jquery.flipster.min.js`) for the carousel.
- Local images under `images/`.

## Run locally

There is no build step or package manager. Clone the repository and open [index.html](./index.html) in a browser, or serve the folder with any static file server:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`. A static host can publish the repository root directly. See [docs/installation.md](./docs/installation.md) and [docs/deployment.md](./docs/deployment.md).

## Pages

- `index.html` — image gallery and navigation.
- `about.html` — gallery/about content.
- `youtube.html` — media-oriented page.
- `style.css`, `about.css`, and `footer.css` — layout and presentation.
- `images/` — local image assets.

The project has no server-side API, database, authentication, or user-submitted content. CDN dependencies should be reviewed and pinned with integrity attributes before production use.

## Maintainer and license

Brajesh Kumar — [@brajesh31](https://github.com/brajesh31). This project is available under the MIT License; see [LICENSE](./LICENSE).

Last updated: 2026-10-21 21:07 UTC
