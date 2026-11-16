# 🔏 Privacy and third-party data

## Current first-party architecture

The tracked project contains static HTML, CSS, JavaScript, and image assets. It has no first-party backend, database, account system, or application API. The repository itself does not implement visitor registration or user-submitted content storage.

## Third-party requests

The pages load resources from public CDNs and the media page includes an Elfsight widget script. A browser request to a third-party host can disclose technical request metadata such as IP address, user agent, referrer, and requested resource. The exact collection, cookies, retention, and processing depend on the provider and current configuration.

Do not claim that the site is tracker-free or collects no visitor data without reviewing the live deployed pages and every third-party resource.

## Privacy review checklist

- [ ] Inventory every external script, stylesheet, font, iframe, and widget.
- [ ] Identify the provider and the reason each resource is loaded.
- [ ] Review current provider privacy notices and terms.
- [ ] Check whether cookies, local storage, or tracking pixels are used.
- [ ] Determine whether consent is required for the deployment jurisdiction.
- [ ] Avoid sending personal or sensitive information to external widgets.
- [ ] Minimize referrer information where appropriate.
- [ ] Re-test after third-party scripts or embed settings change.

## Static-site data boundary

Because the site is static, anything written into HTML, JavaScript, CSS, or public image metadata is available to visitors. Never include secrets, private contact information, private configuration, or personal data in repository files.

## Future features

Visitor accounts, uploads, comments, analytics, and contact forms would introduce new data processing. Each feature needs a documented purpose, minimum data set, consent and retention model, access controls, security review, and deletion procedure before implementation.
