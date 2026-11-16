# 🖼️ Image assets and usage rights

## Current asset inventory
The repository includes ten JPEG files and one PNG file under `images/`:
- `img1.jpg` through `img10.jpg` are referenced by the home carousel.
- `sample.png` is referenced by the About page.

The repository does not establish the creator, source URL, model releases, or redistribution permission for every image. Do not invent missing metadata.

## Asset handling rules
1. Record the creator/source and applicable license for every new image.
2. Do not redistribute copyrighted artwork without permission.
3. Preserve existing filenames unless all HTML/CSS references are updated.
4. Use meaningful alt text for informative images and empty alt text for decorative images.
5. Optimize new image assets without damaging visible quality.
6. Consider responsive formats only after checking browser support and preserving fallbacks where required.
7. Avoid storing unnecessary EXIF metadata, especially precise GPS coordinates.
8. Keep image dimensions and file sizes documented for large new assets.

## Suggested future asset manifest
| Field | Meaning |
|---|---|
| File | Exact repository-relative path |
| Title | Human-readable artwork title |
| Creator | Artist or photographer |
| Source | Original publication or source reference |
| License | Permission or license terms |
| Attribution | Required credit wording |
| Alt text | Concise visual description |
| Dimensions | Pixel width and height |
| Format | JPEG, PNG, WebP, AVIF, SVG |

## Image review checklist
- [ ] Image renders at expected aspect ratio.
- [ ] File path and case are correct.
- [ ] Alt text matches actual visual content.
- [ ] License and attribution are recorded.
- [ ] File size is reasonable.
- [ ] No sensitive metadata remains.
- [ ] Small-screen layout has been checked.
