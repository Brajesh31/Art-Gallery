# ⚙️ Configuration reference

## Configuration model

The current Art Gallery project is configured through static HTML, CSS, and JavaScript files. It does not load environment variables, use a package manifest, or read a server-side configuration file. The root `.env.example` is intentionally explanatory and does not define active settings.

## Configuration locations

| Concern | Current location | Notes |
|---|---|---|
| Page structure and navigation | `index.html`, `about.html`, `youtube.html` | Static markup |
| Global appearance | `style.css` | Shared base styles |
| About page layout | `about.css` | Page-specific presentation |
| Footer layout | `footer.css` | Shared footer styling |
| Carousel configuration | Inline initialization in `index.html` | Depends on jQuery and Flipster |
| Artwork list | Image elements in `index.html` | Paths point to `images/` |
| External media widget | `youtube.html` | Provider-owned configuration may be embedded in widget markup |
| External libraries | HTML script and stylesheet tags | CDN versions and URLs are explicit in markup |

## Environment variables

No active environment variables are required. Never put secrets in a static HTML or JavaScript file. Anything delivered to a browser can be inspected by visitors.

If a future static host requires build-time values, document exactly where they are injected and ensure no secret is exposed in the generated files.

## Safe change procedure

1. Identify the responsible page or stylesheet.
2. Search for every reference to the setting or asset.
3. Make the smallest change that preserves existing page behaviour.
4. Preview all three pages.
5. Check local requests and console output.
6. Update this guide if the configuration model changes.
