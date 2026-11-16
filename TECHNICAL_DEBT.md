# 🧱 Technical debt register

This register records known maintenance work in the current static website. Items are observations from the repository, not claims that a browser audit has been completed.

## High priority

| ID | Debt | Risk | Recommended action |
|---|---|---|---|
| TD-01 | Search form is present without a search implementation | Visitors may expect a non-functional feature | Implement a real client-side index or remove/disable the form |
| TD-02 | Placeholder social links are present | Navigation can mislead visitors | Replace with verified profile URLs or remove the controls |
| TD-03 | Font Awesome resource uses HTTP | Mixed-content blocking on HTTPS hosting | Change to a verified HTTPS resource and validate |
| TD-04 | Existing images have empty alt attributes | Informative artwork may be inaccessible | Inspect each image and write accurate alt text |

## Medium priority

| ID | Debt | Risk | Recommended action |
|---|---|---|---|
| TD-05 | Artwork source and license metadata are incomplete | Redistribution and attribution risk | Verify provenance and complete the artwork rights records |
| TD-06 | Carousel keyboard and reduced-motion behaviour are not formally audited | Accessibility barrier | Perform keyboard and assistive-technology testing |
| TD-07 | External CDN dependencies are not centrally governed | Provider changes or compromise can affect the site | Maintain dependency register and verify versions/integrity |
| TD-08 | Third-party widget configuration and privacy behaviour are not verified | Broken embed or unexpected visitor data processing | Confirm account ownership, configuration, provider terms and privacy behaviour |

## Low priority / ongoing

| ID | Debt | Risk | Recommended action |
|---|---|---|---|
| TD-09 | No documented cross-browser test evidence | Regressions may be missed | Maintain the browser test matrix |
| TD-10 | Image dimensions and responsive delivery are not fully inventoried | Larger transfer sizes and layout shift | Measure, optimize, and document images |
| TD-11 | No verified public demo URL is configured | Visitors cannot open a confirmed hosted preview from README | Deploy to static hosting and verify before adding a live badge |

## Prioritization

Address misleading controls, mixed-content resources, accessibility, and image rights before optional features. Do not close an item until the change is implemented and evidence is recorded.

## Non-goals

Do not add a backend, database, account system, or build framework merely to clear a documentation checklist. Such architecture would add complexity without a current product requirement.
