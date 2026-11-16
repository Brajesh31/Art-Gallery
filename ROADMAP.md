# 🗺️ Roadmap

This roadmap describes future work, not features already delivered. Close an item only after implementation and validation.

## Phase 1: Correctness and hygiene
- [ ] Remove or implement placeholder search forms.
- [ ] Replace placeholder social links with confirmed destinations or remove them.
- [ ] Replace mixed-content HTTP resource URLs with HTTPS.
- [ ] Validate all local paths and navigation links.
- [ ] Review page titles and metadata for consistency.

## Phase 2: Accessibility and responsive quality
- [ ] Add meaningful alt text to informative artwork.
- [ ] Improve semantic landmarks and heading order.
- [ ] Test keyboard access to the carousel.
- [ ] Review reduced-motion behaviour.
- [ ] Test mobile, tablet, desktop, 200% zoom, and screen-reader basics.

## Phase 3: Image and dependency governance
- [ ] Record creator, source, license, and attribution for each artwork.
- [ ] Optimize image delivery and consider responsive formats.
- [ ] Pin CDN dependencies and validate Subresource Integrity hashes.
- [ ] Review Elfsight widget ownership, provider behaviour, and privacy.
- [ ] Test a restrictive Content Security Policy in report-only mode.

## Phase 4: Optional product capabilities
- [ ] Add image detail views only if the user experience needs them.
- [ ] Add client-side search only with a defined metadata index and tests.
- [ ] Add a content-management or upload system only if there is a real publishing requirement and an appropriate security design.

## Current non-goals
- No backend or database is required for the current static gallery.
- No visitor accounts or upload flow are currently provided.
- Do not add complexity solely to increase file count.
