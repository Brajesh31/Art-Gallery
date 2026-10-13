# Architecture

Art Gallery is a static multi-page site. Each HTML page references shared or page-specific CSS and external Bootstrap/jQuery resources. The carousel behavior is provided by the local Flipster library and page scripts. Local artwork is stored under `images/`.

There is no runtime server, API, database, authentication, or build pipeline. Any static host can serve the repository root.
