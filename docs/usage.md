# 🧭 Visitor and maintainer usage guide

## Visitor journey

The current site has three static pages:

1. **Home:** open `index.html` to view the image gallery and carousel.
2. **About:** use the page navigation to open `about.html`.
3. **Media:** use the navigation to open `youtube.html`, where a third-party widget container is present.

The visitor experience depends on the browser loading local styles, local image assets, the Flipster script, and selected CDN resources.

## Carousel interaction

The home page initializes a Flipster carousel on its configured carousel element. The plugin depends on jQuery. If the carousel does not initialize, the browser console and Network panel should be checked for missing scripts or JavaScript errors.

The current repository does not document autoplay as a guaranteed feature. Do not promise controls or behaviour that have not been verified in a live browser.

## Maintainer usage

- Add artwork only after confirming permission to use it.
- Add the image under `images/` with a stable, descriptive filename.
- Update the relevant HTML image reference.
- Provide alt text based on the actual image.
- Update the asset inventory and source/rights record.
- Test all pages after changing shared CSS or navigation.

## Features that are not currently available

The visible search form has no working search index or endpoint. The project has no user uploads, login, saved collections, comments, moderation, or admin dashboard. The media widget may be dependent on external provider configuration.

## Feedback

Report defects with the affected page, browser, viewport, steps to reproduce, and sanitized console errors. Never attach secrets or artwork that you do not have permission to share.
