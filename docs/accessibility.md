# ♿ Accessibility and responsive design

## Scope
This guide sets review expectations for the three existing static pages. It is not a declaration of formal WCAG conformance. A real audit is required before claiming a conformance level.

## Page structure
- Use a clear primary page heading.
- Keep heading levels in logical order.
- Use semantic navigation landmarks and meaningful link text.
- Provide visible focus states for interactive links and controls.
- Ensure active navigation is represented accessibly.
- Keep the document language declared.

## Images
Informative artwork should have concise alt text describing relevant content. Decorative imagery should use empty alternative text. Avoid filenames or generic words such as "image" as the only description.

## Carousel
The image carousel should remain understandable without relying on motion or perspective effects. Check keyboard navigation, focus visibility, reduced-motion preferences, and whether all images remain reachable to screen-reader users. Avoid autoplay unless it has a user-controlled pause mechanism and a clear reason to animate.

## Navigation and forms
The current search form is visually present but has no implemented search behaviour or endpoint. Do not present it as a working search feature. A form that does not submit a meaningful query should be removed or explicitly disabled as part of a deliberate UI change.

Links with `href="#"` are placeholders. Replace them with real destinations or remove them. Empty social links should not be represented as working profiles.

## Responsive checks
Review all pages at narrow mobile, tablet, laptop, and wide desktop widths. Check that navigation works with keyboard and touch, text does not overflow, footer columns stack cleanly, and the About image/text layout remains usable.

## Manual checklist
- [ ] All navigation is keyboard accessible.
- [ ] Focus indicators remain visible.
- [ ] Images have appropriate alternative text.
- [ ] Page headings and landmarks are logical.
- [ ] Text and controls have adequate contrast.
- [ ] Zoom to 200% does not hide essential content.
- [ ] Layout works on mobile widths.
- [ ] Carousel controls and images can be reached without a mouse.
- [ ] Motion can be reduced where practical.
- [ ] Placeholder links and inert controls are addressed.
- [ ] External widgets do not trap keyboard focus.
