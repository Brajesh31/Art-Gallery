# 🌐 API status

## Current status

Art Gallery does not expose or consume a project-owned backend API. The repository is a static HTML/CSS/JavaScript website. Page assets are loaded from the same static host or external CDN/widget providers.

## External resource requests

The pages make browser requests for:
- Bootstrap CSS and JavaScript from jsDelivr;
- jQuery from code.jquery.com;
- Font Awesome and Google Fonts resources;
- the Elfsight platform script on the media page.

The local Flipster plugin is loaded from repository files.

These are asset/widget requests, not a custom application API. Their availability, privacy behaviour, terms, and response content are controlled by their respective providers.

## Future integration requirements

Before introducing a project API, document:
1. the user problem and why static files are insufficient;
2. endpoint paths, methods, request and response schemas;
3. authentication and authorization;
4. rate limits, caching, retries, and failure behaviour;
5. data collection, user consent, retention, and deletion;
6. monitoring, availability, security, and operational ownership.

Do not add an API merely to increase repository complexity.
