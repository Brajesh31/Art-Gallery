# 🌍 Browser and hosting compatibility

## Support policy

The project uses standard HTML, CSS, and browser-side JavaScript, plus Bootstrap, jQuery, Flipster, and external font/icon/widget resources. Compatibility is therefore influenced by the browser's HTML/CSS support and the availability of external scripts.

No formal browser test matrix or automated cross-browser run is currently recorded. Do not claim support for a specific browser version without testing it.

## Browser test matrix

| Browser family | Desktop | Mobile | Test status |
|---|---|---|---|
| Chromium-based | Required | Required | Not yet formally recorded |
| Firefox | Required | Android where relevant | Not yet formally recorded |
| Safari | macOS | iOS | Not yet formally recorded |
| Edge | Required | Optional | Not yet formally recorded |

## Hosting compatibility

Static hosting is sufficient. The host must serve HTML, CSS, JavaScript, images, and the local Flipster files while preserving directory names and filename case.

Test direct navigation to `about.html` and `youtube.html`, not only the home page. This catches host configurations that rewrite or restrict nested static paths.

## Common compatibility risks

- Mixed-content HTTP resources may be blocked on HTTPS pages.
- Privacy protections may block third-party fonts, widgets, or tracking scripts.
- Content Security Policy headers may block CDN resources.
- Case-sensitive hosts may expose incorrect asset paths.
- Browser extensions may interfere with externally hosted widgets.
- Older browsers may not support every CSS feature used by the current layout.

## Verification record

For release evidence, record browser name/version, operating system, viewport, test date, tested pages, result, and any known limitation. Update this matrix only from actual test results.
