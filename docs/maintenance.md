# 🧹 Maintenance schedule

## Every contribution
- Check all affected HTML pages.
- Validate local assets and links.
- Inspect console errors.
- Test mobile and desktop layouts.
- Review accessibility and licensing implications.
- Update the docs index and changelog where relevant.

## Monthly review
- Review GitHub Actions and Dependabot updates.
- Check third-party CDN versions and provider notices.
- Verify external widget behaviour.
- Review open issues and stale roadmap items.
- Check image attribution and rights records.
- Inspect deployed pages for mixed content and broken resources.

## Before each release
- Follow [RELEASE.md](../RELEASE.md).
- Run the repository quality workflow.
- Preview the exact commit that will be deployed.
- Verify all three pages and their direct URLs.
- Record browser and viewport test evidence.
- Review the rollback path.

## Dependency ownership
The project uses public CDNs and a local vendored Flipster plugin. Updates must be deliberate. Do not replace a library with a new major version without checking compatibility and updating documentation.

## Maintenance record
A maintenance record should include date, commit, files/dependencies reviewed, tests performed, issues found, and follow-up owner. Do not claim a review occurred unless it was actually performed.
