# ❓ Frequently asked questions

## Does the project need Node.js or npm?

No. The current website is plain HTML, CSS, and browser-side JavaScript. A browser or static file server is sufficient.

## Does it have a backend?

No. There are no server APIs, user accounts, authentication flows, or database operations in the current repository.

## Can it be deployed to GitHub Pages?

Yes. Publish the repository root as a static site and ensure `index.html` is selected as the entry page. Preserve relative image and script paths.

## Where are the images stored?

The current artwork files are under `images/`. The repository does not yet document verified creator and usage rights for every file. Confirm permission before redistribution.

## Is the search bar functional?

The HTML contains a search form, but the inspected repository does not include a search implementation, index, or endpoint. Treat it as a placeholder until functional behaviour is implemented and tested.

## Does the media page embed a working feed?

The page includes an Elfsight widget container and platform script. Their presence does not prove the account/widget is configured or currently available.

## Why might the carousel fail?

The carousel depends on jQuery and the local Flipster plugin. Check load order, network requests, and browser console for errors.

## Does the website store visitor information?

No first-party backend or database is present in the repository. Third-party resources and embedded widgets may have their own network and privacy behaviour. Review their current policies before production use.

## Can I add a new image?

Yes, after confirming redistribution rights, using a sensible filename, adding appropriate alt text, and updating asset documentation.
