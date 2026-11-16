# ⚠️ Limitations and future roadmap

## Current limitations
- The project is a static front-end website with no server-side features.
- There is no database, content management, user account, or image upload flow.
- The search form shown in the pages has no implemented search behaviour.
- Social icons include placeholder links.
- The media page's Elfsight mount point does not prove that the widget is configured or active.
- The original home page includes an HTTP Font Awesome stylesheet reference, which may be blocked on HTTPS hosting.
- Artwork rights and creator metadata are not established for every image.
- Current HTML image elements use empty alternative text, which should be reviewed against actual content.
- External scripts and fonts depend on provider uptime and privacy behaviour.

## Roadmap

### Phase 1: Correctness and maintenance
- [ ] Remove or implement placeholder search forms.
- [ ] Replace placeholder navigation and social links.
- [ ] Correct mixed-content resource URLs.
- [ ] Validate all local and external links.
- [ ] Ensure page metadata and titles are consistent.

### Phase 2: Accessibility and responsive polish
- [ ] Add descriptive alternative text to informative artwork.
- [ ] Improve semantic landmarks and heading order.
- [ ] Verify keyboard access to carousel and navigation.
- [ ] Support reduced-motion preferences where practical.
- [ ] Check all pages across mobile, tablet, and desktop sizes.

### Phase 3: Asset and dependency governance
- [ ] Document image creator, source, license, and attribution.
- [ ] Review image dimensions and optimize transfer sizes.
- [ ] Pin external dependencies and verify integrity hashes.
- [ ] Review third-party widget privacy and availability.
- [ ] Test a restrictive Content Security Policy before enforcing it.

### Phase 4: Optional product features
- [ ] Add an image detail view only if the collection requires it.
- [ ] Add search/filtering only with a defined content index and tested behaviour.
- [ ] Add content management or upload only if there is a real publishing requirement and appropriate security design.

## Definition of done
A task is complete only when behaviour exists, local assets resolve, relevant browser and accessibility checks are performed, documentation is updated, and new third-party resources or images have been reviewed. A roadmap item is not complete merely because it appears in a document.
