# ⚡ Performance and asset delivery

## Current performance profile

The site is static and avoids a server-side application runtime. The repository currently contains eleven local image assets: ten JPEG gallery images and one PNG used by the About page. Their combined size is meaningful for a small static site, so image delivery is a practical optimization area.

The pages also load external CSS and JavaScript from CDNs. These resources add network connections and can affect rendering if providers are slow or unavailable.

## Performance priorities

### Images
- Measure each image's intrinsic dimensions and file size.
- Resize assets to the largest dimensions actually needed by the design.
- Consider WebP or AVIF with a fallback only after checking host/browser support.
- Use responsive image candidates when the same image is served at substantially different viewport sizes.
- Add explicit width and height attributes to reduce layout shifts.
- Use lazy loading for below-the-fold images, but not for the primary visible gallery image if it delays the main experience.
- Preserve source artwork and licensing records.

### External dependencies
- Remove unused libraries only after checking all page references.
- Keep dependencies version-pinned.
- Avoid loading a widget script on pages that do not use the widget.
- Consider self-hosting stable dependencies if CDN privacy, availability, or integrity is a concern.
- Do not add preconnect hints for origins that are not used by the page.

### CSS and JavaScript
- Avoid adding another framework to a small static site without a clear benefit.
- Keep custom CSS understandable and remove duplicate rules only after checking rendered pages.
- Do not modify minified vendor files manually.
- Defer non-critical scripts where the page behaviour allows it.

## Measurement plan

Capture a baseline using browser DevTools or Lighthouse:
- total transferred bytes;
- number of requests;
- image transfer size;
- Largest Contentful Paint;
- Cumulative Layout Shift;
- Interaction to Next Paint;
- console errors and failed network requests.

Record the tested URL, browser, viewport, date, and commit SHA. Do not publish invented scores.

## Optimization order

1. Measure current pages.
2. Identify the largest image and slowest external resource.
3. Make one focused change.
4. Re-run the same measurement.
5. Compare the result and check visual quality.
6. Document any trade-off.
