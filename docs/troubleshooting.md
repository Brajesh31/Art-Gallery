# 🧰 Troubleshooting guide

## Images do not appear

Check filename casing, relative paths, and whether the requested file exists under `images/`. Use a local static server and inspect the browser Network panel.

## Carousel does not work

Confirm that jQuery and the local Flipster JavaScript file load in the expected order. Inspect the browser console for plugin errors. The carousel should remain understandable when JavaScript is unavailable.

## Bootstrap styles do not load

Check network access to jsDelivr and review the exact CDN URL. Some layout and responsive navbar behaviour depends on Bootstrap resources.

## Font or icon resources are missing

Check the external resource requests and browser privacy settings. A browser may block mixed HTTP content on an HTTPS page. The original pages include an HTTP Font Awesome URL, which should be changed to a verified HTTPS resource in a deliberate cleanup change.

## Media widget is blank

The Elfsight container may be empty because the widget is unconfigured, unavailable, blocked by privacy settings, or restricted by provider-side conditions. The existence of a widget container is not proof that a feed is operational.

## Layout overflows on mobile

Check viewport metadata, fixed dimensions, image sizing, flex wrapping, and media queries in the relevant stylesheet. Review `about.css` and `footer.css` for page-specific responsive behaviour.

## Navigation opens the wrong location

Check relative links and exact page filenames. Linux static hosts are case-sensitive. Avoid relying on placeholder `href="#"` links as real navigation.

## Local server does not start

Check whether port 8000 is already in use. Choose another port:

```bash
python -m http.server 8001
```

Then open `http://localhost:8001`.

## Site works locally but fails after deployment

Check:
- published directory and configured entry page;
- relative image, CSS, and JavaScript paths;
- filename case;
- HTTPS and mixed-content requests;
- CDN and widget availability;
- static-host cache behaviour.
