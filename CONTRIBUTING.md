# 🤝 Contributing

Thank you for considering a contribution. The most useful changes improve content accuracy, accessibility, responsive behaviour, security of third-party dependencies, or maintainability.

## Before starting

1. Read the README and relevant guides under `docs/`.
2. Search existing issues before opening a new one.
3. For substantial changes, describe the intended behaviour in an issue first.
4. Check whether image use, attribution, or external data is affected.
5. Keep the current static-site architecture unless there is a documented reason to change it.

## Local workflow

```bash
git clone https://github.com/Brajesh31/Art-Gallery.git
cd Art-Gallery
python -m http.server 8000
```

Open all three pages and inspect the browser console and Network panel.

## Change standards

- Use semantic HTML and logical heading levels.
- Preserve working navigation and exact local asset paths.
- Use meaningful alternative text for informative images.
- Do not use placeholder links for controls presented as working features.
- Keep external dependencies on HTTPS and pin exact versions where possible.
- Use valid Subresource Integrity hashes for the exact CDN resource.
- Record source and usage rights for new images.
- Do not add secrets, personal information, or unlicensed artwork.
- Do not add build tooling or a framework without a real project requirement.

## Validation expectations

- [ ] Home page checked.
- [ ] About page checked.
- [ ] Media page checked.
- [ ] Local image, CSS, and JavaScript paths resolve.
- [ ] Browser console has no unexplained errors.
- [ ] External resource behaviour has been reviewed.
- [ ] Desktop and mobile layouts checked.
- [ ] Keyboard access and visible focus checked.
- [ ] Image alt text and attribution reviewed.
- [ ] Documentation and changelog updated where relevant.

## Pull requests

Keep each pull request focused. Explain the reason for the change, pages affected, expected result, validation evidence, accessibility implications, and any external-resource or image-licensing changes.

## Security and privacy

The current repository is static and has no application backend. Never include secrets in browser-visible HTML, CSS, or JavaScript. Report vulnerabilities privately using the instructions in [SECURITY.md](SECURITY.md).
