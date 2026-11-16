# 🚀 Static deployment guide

## Current deployment model

Art Gallery is a static website. The hosting provider only needs to serve the repository files. There is no server runtime, build output directory, API service, database, or environment-specific backend configuration.

## GitHub Pages deployment

A typical GitHub Pages configuration can publish the repository root from the default branch:

1. Open repository Settings.
2. Open Pages.
3. Choose deployment from a branch.
4. Select the `main` branch and `/(root)` folder.
5. Save and wait for GitHub Pages to publish.
6. Open the Pages URL and test all three pages.

The exact Pages settings and availability are controlled by GitHub account/repository configuration. Do not assume deployment is active until the published URL is verified.

## Other static hosting

The root directory can be deployed to a static host that supports plain HTML, CSS, JavaScript, and images. Preserve directory structure and filename case.

## Pre-deployment checklist

- [ ] `index.html` is configured as the entry page.
- [ ] `about.html` and `youtube.html` load directly.
- [ ] All image, CSS, and local JavaScript references work.
- [ ] Relative paths remain valid from nested URLs.
- [ ] External resources use HTTPS.
- [ ] CDN version and integrity metadata have been reviewed.
- [ ] Image permissions and attribution are understood.
- [ ] Placeholder search and social links are not represented as working features.
- [ ] Media widget ownership, configuration, and privacy implications are reviewed.
- [ ] Mobile, desktop, keyboard, and zoom checks are completed.

## Base paths and custom domains

When deploying to a project subpath, check that every relative asset path is relative to the HTML page and not an assumed domain root. If a custom domain or redirect is used, verify HTTPS and canonical navigation.

## Caching and updates

Static hosts may cache HTML, CSS, JavaScript, and images differently. After deployment, verify the new version with a hard refresh and check response headers when an old image or stylesheet appears. Use content-hashed filenames only if introducing a build process deliberately; the current project uses direct file references.

## Content Security Policy

A restrictive CSP may block external Bootstrap, jQuery, Font Awesome, Google Fonts, or Elfsight resources. Build a policy from observed origins, test in report-only mode, and avoid broad wildcards.
