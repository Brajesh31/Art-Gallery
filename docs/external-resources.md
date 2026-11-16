# 🌐 External resources and third-party dependencies

## Current external resources
| Resource | Current role | If unavailable |
|---|---|---|
| Bootstrap 5.1.3 via jsDelivr | Navigation and responsive utility classes | Some layout and navbar behaviour may degrade |
| jQuery 3.6.0 via code.jquery.com | Required by Flipster initialization | Carousel initialization will fail |
| Font Awesome 4.2.0 | Footer icon glyphs | Icons may be missing |
| Google Fonts | Typography | Browser fallback fonts are used |
| Elfsight platform script | Loads the media widget on the media page | Widget area may remain empty |

The carousel library itself is stored locally as `jquery.flipster.min.js` and `jquery.flipster.min.css`.

## Security and reliability review
- Prefer HTTPS URLs for all external resources. The original pages include an HTTP Font Awesome stylesheet reference, which browsers may block on an HTTPS-hosted site.
- Preserve Subresource Integrity attributes for CDN files when the provider supplies stable versioned assets and matching hashes.
- Avoid floating or unversioned external script URLs where possible.
- Review third-party privacy and cookie behaviour before embedding widgets.
- Treat external scripts as trusted code with access to the page context.
- Do not place API keys or private information in browser-visible source.

## Integrity and version pinning
A production hardening change should use exact, supported library versions and integrity hashes generated from the exact downloaded file. Never copy an integrity value from a different version or resource. Test that the CDN returns the expected bytes before publishing.

## Elfsight widget
The media page includes an Elfsight mount point and platform script. The repository alone does not establish which account owns the widget, what content it will display, what data the provider processes, or whether the widget is currently active. Confirm ownership, privacy disclosures, terms, and live behaviour before promising a working feed.

## Content Security Policy
A future CSP must account for the site's own scripts, Bootstrap, jQuery, Font Awesome, Google Fonts, and Elfsight resources. Build the policy from observed, necessary origins and test in report-only mode before enforcing it. Do not add a permissive wildcard policy simply to make embeds work.
