# 🗄️ Database and data persistence

## Current status

The project has no database and no persistent application data layer. It displays local image files and static HTML content. The home gallery is built from image references written directly into the HTML.

## Why no database is currently needed

For a small static gallery, a database would add operational and security overhead without solving a demonstrated requirement. Static HTML and local assets can be hosted cheaply and loaded directly by a browser.

## What would justify persistence?

A future database or content service might be appropriate only if the project adds capabilities such as:
- a maintainer-facing artwork management system;
- metadata editing for titles, artists, descriptions, and licenses;
- user-submitted artwork with moderation;
- authenticated private collections;
- search over a large structured artwork catalogue.

Those are not current capabilities.

## Future data model considerations

If an artwork catalogue is introduced, consider fields such as:

| Field | Purpose |
|---|---|
| `artwork_id` | Stable internal record identifier |
| `title` | Artwork title |
| `creator_name` | Artist or photographer |
| `image_path` | Stored or CDN image path |
| `source_url` | Original source reference |
| `license_name` | Permission or license |
| `attribution_text` | Required credit |
| `alt_text` | Accessible image description |
| `created_at` | Record creation timestamp |
| `updated_at` | Record update timestamp |

This is a design suggestion only, not an implemented schema. A future system would require authentication, validation, upload scanning, authorization, retention, backups, and moderation decisions.
