# 👤 User stories

These stories describe the current static experience and clearly label proposed capabilities.

## Current visitor stories

### US-01: Browse the gallery
As a visitor, I want to open the home page and browse the image carousel so that I can view the artwork collection.

**Acceptance criteria**
- The home page loads directly.
- Local gallery images resolve.
- The carousel initializes when its dependencies load.
- The visitor can still understand the page if external resources fail.

### US-02: Read about the project
As a visitor, I want to open the About page so that I can read its descriptive content.

**Acceptance criteria**
- The About page opens directly.
- The profile image path resolves.
- Text remains readable on mobile and desktop.

### US-03: Open the media page
As a visitor, I want to navigate to the media page so that I can view the intended external media area.

**Acceptance criteria**
- The page opens directly.
- A failed third-party widget does not break the rest of the page.
- The widget is not described as operational until verified.

## Maintainer stories

### US-04: Add licensed artwork
As a maintainer, I want to add artwork with source and rights metadata so that the gallery does not redistribute content without permission.

### US-05: Validate a change
As a maintainer, I want automated checks for local links and assets so that broken references are caught before publishing.

### US-06: Maintain project documentation
As a contributor, I want a clear documentation index and architecture diagrams so that I can understand the project without reverse-engineering every file.

## Proposed future stories

Search, uploads, saved collections, and user accounts are not current features. Each needs separate product approval, security/privacy design, acceptance criteria, and implementation.
