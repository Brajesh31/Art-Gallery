# ♿ Accessibility testing protocol

## Purpose

This guide defines repeatable checks for the gallery pages. It does not assert formal WCAG conformance or replace testing with people who use assistive technology.

## Keyboard-only review

1. Reload the page.
2. Use Tab and Shift+Tab to move through interactive elements.
3. Confirm focus is visible at every step.
4. Activate links using Enter.
5. Confirm no keyboard trap occurs.
6. Test carousel interaction without a pointer.
7. Confirm focus order follows the visual and semantic order.

## Screen-reader review

Where available, test at least one desktop screen reader and one mobile screen reader. Check page title, landmarks, heading hierarchy, link names, image alternative text, and carousel announcements. Record the screen reader and browser versions.

## Visual review

- Text contrast is sufficient against the dark background.
- Focus indicators are not removed.
- Content remains readable at 200% zoom.
- Layout does not require horizontal scrolling at common mobile widths.
- Motion does not prevent reading or interaction.
- Colour is not the only indicator of state.

## Image review

For each informative image, ask whether the image conveys content that is missing from surrounding text. If yes, write a concise description based on the actual image. If it is decorative and adds no information, empty alt text may be appropriate.

## Test record

Record date, commit, page, browser, assistive technology, input method, viewport, test result, and issue reference. A checklist without execution evidence is not a completed audit.
