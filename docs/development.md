# 🛠️ Development guide

## Project conventions

Art Gallery is plain HTML, CSS, and browser-side JavaScript. Keep the implementation approachable and avoid introducing build tooling, frameworks, or a backend unless the project has a concrete requirement that the current static architecture cannot meet.

## Local development

```bash
python -m http.server 8000
```

Open `http://localhost:8000` and inspect each page. There is no dependency installation step for the current static files.

## Where to make changes

- Home page structure and carousel initialization: `index.html`.
- About page content and layout: `about.html` and `about.css`.
- Media page mount point: `youtube.html`.
- Shared backgrounds and layout defaults: `style.css`.
- Footer layout: `footer.css`.
- Carousel vendor files: `jquery.flipster.min.js` and `jquery.flipster.min.css`.
- Artwork: `images/`.

## Implementation standards

- Use semantic HTML and meaningful headings.
- Keep responsive layout behaviour intact.
- Add useful alt text to informative images.
- Avoid `href="#"` placeholders for controls presented as working navigation.
- Use HTTPS for external dependencies.
- Keep CDN versions fixed and integrity hashes matched to exact downloaded files.
- Do not add API keys, private tokens, personal contact details, or other secrets to browser-visible source.
- Document image source and usage rights before adding or redistributing assets.
- Do not claim the search form or third-party widget is functional without verification.

## Validation workflow

1. Open all three pages using the local static server.
2. Check local image, CSS, and JavaScript requests in the browser Network panel.
3. Check the developer console.
4. Test mobile and desktop layouts.
5. Navigate using keyboard only.
6. Review focus, heading hierarchy, and image alt text.
7. Test external CDN and widget failure behaviour.
8. Run the repository quality workflow before merging.

## Pull request expectations

Keep changes focused. Explain which page or asset changes, expected visual behaviour, validation performed, responsive/accessibility implications, and whether any third-party resource or image rights are affected. Update relevant documentation and the changelog.
