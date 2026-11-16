# 🏛️ Project governance

## Stewardship
Art Gallery is a small static website maintained by its repository owner. The maintainer reviews contributions, controls releases, and coordinates changes to site structure and dependencies.

## Decision principles
1. Preserve the static-site model unless a concrete requirement justifies a backend or build system.
2. Keep existing artwork and page content intact unless a change is explicitly scoped.
3. Prioritize accessibility, responsive behaviour, security, and correct attribution.
4. Treat third-party scripts and widgets as external dependencies that require review.
5. Do not claim placeholder controls or unverified widgets are functional.
6. Avoid adding infrastructure purely to increase repository complexity.

## Changes that deserve prior discussion
Discuss major changes such as adding image uploads, visitor accounts, analytics, a backend, user comments, a new external widget, or a different build system before implementation. These affect privacy, security, maintenance, and hosting.

## Contribution review
Pull requests should explain the problem, affected pages, implementation, validation, accessibility impact, and image/dependency licensing. Changes should not remove existing assets without a clear reason and updated references.

## Releases
A release should identify the source revision, pages affected, tested browsers, important dependency changes, known limitations, and any migration required for static hosting.
