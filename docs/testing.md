# 🧪 Testing and validation

## Testing model
Art Gallery is a static site, so validation focuses on HTML structure, local links, CSS/JavaScript/image paths, external resource references, responsive behaviour, accessibility, and browser console errors. There is no backend API or database to integration-test.

## Static checks
The repository quality workflow validates local relative references in HTML files. It should run on pull requests and pushes that affect pages, styles, scripts, images, or workflows. It must not fetch arbitrary third-party scripts or execute page code.

## Manual browser checks
For each page:
1. Open it using a local HTTP server.
2. Check the browser console for errors.
3. Check the Network panel for failed local assets.
4. Test navigation between all three pages.
5. Test at mobile and desktop widths.
6. Zoom to 200%.
7. Navigate using keyboard only.
8. Review image alternative text and heading hierarchy.
9. Confirm external widgets and CDNs behave as documented.
10. Check the page with browser privacy protections enabled.

## Link and asset validation
Relative links should resolve from the HTML file's directory. Preserve case-sensitive paths because GitHub Pages and most Linux static hosts use case-sensitive filesystems. External links can change or become unavailable and should be reviewed before releases.

## Visual regression evidence
Capture screenshots from actual browser-rendered pages. Include browser, viewport size, and commit being checked. Do not fabricate screenshots or replace actual artwork with placeholders just to satisfy documentation.

## Release checklist
- [ ] All three HTML pages load.
- [ ] All local image, CSS, and JavaScript paths resolve.
- [ ] Navigation destinations are correct.
- [ ] Carousel works with required dependencies.
- [ ] No accidental mixed-content HTTP resources remain.
- [ ] No console errors remain unexplained.
- [ ] Keyboard and responsive checks are completed.
- [ ] Image rights and attribution have been reviewed.
- [ ] Third-party widgets are described accurately.
