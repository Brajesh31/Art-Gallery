# 🚀 Installation and local development

## Prerequisites
- A modern browser.
- Git, if cloning the repository.
- Python 3 or another static file server for local preview.

No Node.js, npm, framework compiler, package manager, or build process is required by the current project.

## Clone
```bash
git clone https://github.com/Brajesh31/Art-Gallery.git
cd Art-Gallery
```

## Preview locally
From the repository root:
```bash
python -m http.server 8000
```

Open:
- Home: `http://localhost:8000/`
- About: `http://localhost:8000/about.html`
- Media: `http://localhost:8000/youtube.html`

Stop the server with `Ctrl+C`.

Opening an HTML file directly may work, but an HTTP server more closely resembles static hosting and avoids some browser restrictions around local resources.

## Editing workflow
1. Edit the relevant HTML or CSS file.
2. Refresh the browser page.
3. Check the browser developer console for JavaScript errors.
4. Check the Network panel for failed local assets or external CDN requests.
5. Test at desktop and mobile widths.
6. Verify every new relative path with exact filename case.

## Common local issues
- An unstyled page may indicate a CSS path or external-resource failure.
- Carousel failure may indicate jQuery or the local Flipster script did not load.
- Broken artwork generally indicates an incorrect relative path or filename case.
- The media widget may be unavailable due to provider scripts, privacy protections, or network restrictions.
