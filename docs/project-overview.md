# 🎨 Project overview

## Purpose

Art Gallery is a small static website for presenting a collection of local images in a dark visual layout. It includes a home gallery with a 3D-style carousel, an about page, and a media-oriented page that contains an Elfsight widget mount point.

The goal is a lightweight browser experience that can be hosted as static files without a server-side runtime or build toolchain.

## Current implementation

| Area | Current implementation |
|---|---|
| Home gallery | `index.html` |
| About content | `about.html` |
| Media page | `youtube.html` |
| Main styling | `style.css` |
| About page styling | `about.css` |
| Shared footer styling | `footer.css` |
| Carousel | Local jQuery Flipster CSS and JavaScript |
| Image collection | Local assets under `images/` |
| UI framework | Bootstrap 5.1.3 via jsDelivr |
| DOM and carousel runtime | jQuery 3.6.0 and local Flipster |
| Media widget | Elfsight widget placeholder and externally hosted platform script |

## User journey

1. A visitor opens the home page.
2. The visitor browses the carousel of local gallery images.
3. Navigation links lead to the About page or Media page.
4. The About page presents descriptive text and a profile image.
5. The Media page provides a location where an external widget may render content, subject to that provider's availability.

## What the project does not currently provide

- No backend API or server-side application.
- No database or image upload management.
- No user login, account, comment, or moderation system.
- No confirmed functional search implementation.
- No confirmed content-management interface.
- No build command or package manager.
- No verified ownership metadata or licensing record for every image asset.
- No guarantee that the external media widget renders in every browser or network environment.

## Quality goals

- Preserve the lightweight static deployment model.
- Keep navigation and image paths valid on case-sensitive hosting.
- Make pages usable on mobile and desktop.
- Give informative images meaningful alternative text.
- Keep external dependencies documented, secure, and maintained.
- Avoid presenting placeholder links or forms as finished functionality.
- Preserve the existing image collection unless a change is specifically requested.
