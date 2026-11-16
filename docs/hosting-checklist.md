# ☁️ Static hosting checklist

## Before choosing a host
- Confirm static HTML/CSS/JS support.
- Confirm custom domain and HTTPS support if required.
- Check cache controls and custom response headers.
- Confirm direct access to nested HTML pages.
- Check whether the provider supports redirects and custom 404 pages.

## Deployment configuration
- Publish the repository root.
- Use `index.html` as the home entry point.
- Preserve the `images/` and `assets/` directories.
- Preserve exact file and directory casing.
- Do not configure a build command for the current plain static project.
- Do not configure a nonexistent output directory such as `dist/`.

## Post-deployment smoke test
- [ ] Home page loads from the public URL.
- [ ] About page opens directly.
- [ ] Media page opens directly.
- [ ] Carousel assets load.
- [ ] All gallery images render.
- [ ] Footer and responsive navigation work.
- [ ] HTTPS has no mixed-content errors.
- [ ] Third-party widget behaviour is known.
- [ ] Browser console has no unexplained errors.
- [ ] Canonical URL, sitemap, and robots policy are correct if configured.

## Rollback
Keep the last known-good commit available. If a deployment breaks, restore that revision, run static checks, and repeat the smoke test before considering the incident resolved.
