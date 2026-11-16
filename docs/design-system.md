# 🎨 Visual design and UI conventions

## Current visual direction

The existing site uses a dark visual presentation, a prominent image carousel on the home page, page-specific About styling, and a shared footer. This guide documents review conventions rather than claiming a fully implemented design-token system.

## Styling ownership

| File | Responsibility |
|---|---|
| `style.css` | Shared base rules and page background |
| `about.css` | About page content and responsive layout |
| `footer.css` | Footer columns, spacing, and responsive stacking |
| `jquery.flipster.min.css` | Third-party carousel styles |

## UI principles for future changes

1. Let artwork remain the primary visual focus.
2. Keep typography readable against the dark background.
3. Use consistent spacing and alignment across pages.
4. Preserve clear hover, focus, and active states.
5. Avoid unnecessary animation and respect reduced-motion preferences.
6. Keep controls understandable on touch and keyboard.
7. Avoid adding decorative icons where they reduce clarity.
8. Use responsive layouts instead of fixed-width assumptions.

## Design tokens

A future token layer may define background, surface, text, muted text, accent, border, spacing, and typography values. Do not document token names as implemented until they exist in CSS.

## Review checklist

- [ ] Text contrast is sufficient.
- [ ] Interactive states are visible.
- [ ] Layout works on small screens.
- [ ] Images retain appropriate crop and aspect ratio.
- [ ] Footer does not overlap page content.
- [ ] Carousel remains usable without pointer-only interaction.
- [ ] Reduced motion is considered.
