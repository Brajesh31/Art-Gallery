# Troubleshooting

## Images do not appear

Check filename casing, relative paths, and whether the requested file exists under `images/`. Use a local static server instead of opening files through an unusual browser extension.

## Carousel does not work

Confirm the local Flipster JavaScript file and jQuery are loaded in the expected order, then inspect the browser console. The gallery should remain understandable if JavaScript is unavailable.

## Bootstrap styles do not load

Check network access to jsDelivr and review the CDN URL. Consider vendoring or pinning dependencies for offline or production use.

## Layout overflows on mobile

Check viewport metadata, fixed dimensions, image sizing, and media queries in the relevant stylesheet.
