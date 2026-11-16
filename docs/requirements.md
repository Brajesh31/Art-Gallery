# 📋 Project requirements

## Purpose

This document records requirements supported by the current repository and separates them from proposed future requirements. It is not a claim that every proposed feature is implemented.

## Current functional requirements

| ID | Requirement | Current status |
|---|---|---|
| FR-01 | Serve a home page containing the gallery | Implemented in `index.html` |
| FR-02 | Present the local image collection | Implemented through local image references |
| FR-03 | Provide carousel presentation | Implemented through jQuery Flipster |
| FR-04 | Provide an About page | Implemented in `about.html` |
| FR-05 | Provide a media-oriented page | Implemented as `youtube.html` with external widget integration point |
| FR-06 | Provide shared footer styling | Implemented through `footer.css` |
| FR-07 | Provide responsive layout rules | Present in CSS, requires full viewport validation |

## Known missing functional requirements

| ID | Capability | Status |
|---|---|---|
| FR-08 | Search artwork by title/artist | Not implemented |
| FR-09 | Upload or manage artwork | Not implemented |
| FR-10 | Visitor accounts or saved collections | Not implemented |
| FR-11 | Comments, ratings, or moderation | Not implemented |
| FR-12 | First-party API or persistent catalogue | Not implemented |

## Non-functional requirements

- Pages should load over HTTPS on the chosen static host.
- Local paths must work on case-sensitive filesystems.
- The layout should remain usable on mobile and desktop.
- Informative images need meaningful alternative text.
- Interactive controls should be keyboard operable.
- External dependencies should be versioned and reviewed.
- Artwork must have a documented permission basis before redistribution.
- Documentation and diagrams must describe real behaviour.

## Requirement change control

A proposed capability should state the user problem, scope, user journey, data processed, privacy/security implications, accessibility impact, acceptance criteria, and maintenance cost before implementation.
