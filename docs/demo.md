# 🎬 Demo and preview guide

## Live demo status

A verified public demo URL is not currently configured in repository metadata. The presence of a GitHub repository is not the same as a deployed live website. Do not publish a "Live Demo" badge until a stable deployed URL has been checked.

## Run a local demo

From the repository root:

```bash
python -m http.server 8000
```

Open the following pages:

| Page | Local URL | What to review |
|---|---|---|
| Home gallery | `http://localhost:8000/` | Carousel, artwork images, navigation, footer |
| About | `http://localhost:8000/about.html` | Profile image, content, layout, footer |
| Media | `http://localhost:8000/youtube.html` | Widget placeholder, external script, footer |

Stop the server with `Ctrl+C`.

## Screenshot capture plan

Capture screenshots from the actual running site. Do not create illustrative mockups and label them as product screenshots.

| Screenshot | Suggested viewport | Evidence |
|---|---|---|
| Home desktop | 1440 × 900 | Full hero/gallery and footer |
| Home mobile | 390 × 844 | Responsive navigation and carousel |
| About desktop | 1440 × 900 | Text and image layout |
| About mobile | 390 × 844 | Stacked layout and readable text |
| Media page | 1440 × 900 | Actual widget result or visible empty-state behaviour |

For every screenshot, record the browser, viewport, tested commit, and whether external resources were available.

## Live demo release checklist

- [ ] A static host has been selected.
- [ ] The correct repository root is published.
- [ ] HTTPS is enabled.
- [ ] All three pages work when opened directly.
- [ ] All image, CSS, and JavaScript paths resolve.
- [ ] External scripts and widget behaviour have been checked.
- [ ] A mobile viewport has been tested.
- [ ] The exact public URL has been verified.
- [ ] The repository homepage metadata and README badge point to that verified URL.

## Demo badge policy

Until a public deployment is verified, use repository and workflow badges only. A fake demo link is worse than no demo badge.
