# 🔐 Security Policy

## Scope

Art Gallery is a static client-side website with no application authentication, backend API, or database. The primary security considerations are third-party scripts, CDN dependencies, external widgets, browser-visible source, and image/document metadata.

## Reporting

Report suspected vulnerabilities privately through the maintainer contact route on [GitHub](https://github.com/Brajesh31). Include the affected page, browser, sanitized reproduction steps, impact, and any suggested mitigation. Do not open a public issue containing a working exploit or private data.

## Dependency and embed guidance

- Use HTTPS for all external resources.
- Keep third-party library versions explicit.
- Preserve or add Subresource Integrity only when the hash matches the exact resource bytes.
- Avoid untrusted or dynamically injected scripts.
- Review third-party widget permissions, cookies, tracking, and data collection.
- Apply a restrictive Content Security Policy only after inventorying required origins and testing it.
- Keep browser-delivered source free of credentials and private configuration.

## Data and asset guidance

Do not publish private contact details, personal information, location metadata, or credentials in HTML, CSS, JavaScript, image EXIF, or documentation. Confirm image redistribution rights before adding or republishing artwork.

## Incident response

For a suspected compromise:
1. Identify affected pages and external resources.
2. Remove or disable the unsafe dependency or content.
3. Preserve relevant logs without redistributing private data.
4. Rotate credentials if any were exposed.
5. Validate the fix across all pages.
6. Document user impact and follow-up actions without publishing secrets.
