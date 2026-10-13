# Deployment

Publish the repository root to any static hosting provider. No build command is required. Configure the host to serve `index.html` as the entry page and preserve the `images/` and local JavaScript/CSS paths.

Before publishing, verify external CDN URLs, HTTPS, responsive pages, image licenses, and cache behavior. A strict Content Security Policy should be tested if the host adds one, because the pages currently load Bootstrap and other resources from CDNs.
