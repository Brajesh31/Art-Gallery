# 🚀 Release process

## Readiness checklist
1. Review the README, changelog, roadmap, and relevant docs.
2. Confirm all three pages load from a clean static deployment.
3. Verify local image, CSS, and JavaScript paths.
4. Check external CDN resources and version/integrity metadata.
5. Review keyboard, responsive, zoom, and image-alt behaviour.
6. Confirm artwork source and redistribution permissions are understood.
7. Verify that no placeholder form, social link, or external widget is described as a finished feature without evidence.
8. Review the browser console and Network panel.
9. Record browsers and viewport sizes tested.
10. Update release notes and known limitations.

## Versioning
Use semantic versioning if formal releases are adopted. Patch releases fix defects, minor releases add compatible user-facing functionality, and major releases indicate breaking changes or substantial redesign. Do not create a release tag until the checks have evidence.

## Rollback
If a release breaks navigation, asset delivery, accessibility, or third-party loading, restore the previous known-good revision or publish a corrected commit. Document user impact and the fix.
