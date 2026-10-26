# ToolNest

Live website: https://fashiondesign4all786-tech.github.io/Tools/

This repository is the source of truth for ToolNest. It is a static GitHub Pages website: HTML pages and browser-side JavaScript are published directly from the repository root.

## Quick navigation

| Need to edit | File or folder |
|---|---|
| Homepage, navigation, tool catalogue, search and category filters | `index.html` |
| Full PDF tool catalogue and PDF tool workspace | `pdf-tools.html` |
| Audio/video tools and browser-based video compression | `video-tools.html` |
| Direct video URL helper | `video-downloader.html` |
| Video-to-MP3 converter | `video-to-mp3.html` |
| Background remover | `background-remover.html` |
| Image tools | `image-compressor.html`, `image-resizer.html`, `image-format-converter.html`, `heic-to-jpg.html` |
| Text and developer utilities | `word-counter.html`, `case-converter.html`, `json-formatter.html`, `url-encoder-decoder.html`, `csv-viewer.html` |
| PDF conversion and merge/compression tools | `word-excel-to-pdf.html`, `pdf-merger.html`, `pdf-compressor.html` |
| Generators and calculators | `qr-code-generator.html`, `password-generator.html`, `age-calculator.html`, `date-calculator.html`, `percentage-calculator.html`, `unit-converter.html` |
| General site information | `about.html`, `contact.html`, `faq.html`, `privacy.html`, `terms.html` |
| Search engine crawling | `robots.txt`, `sitemap.xml`, `sitemap.txt`, `google8090c8273271bd5d.html` |
| Automated checks | `.github/workflows/` and `.github/scripts/` |
| Optional YouTube downloader API source | `video-downloader-backend/` and `render.yaml` |
| Hosting and migration notes | `HOSTING-MIGRATION.md` |

## Repository layout

- **Root HTML files:** published pages and tool entry points. Keep these in the root so existing public URLs, internal links, search indexing, and bookmarks continue to work.
- **`.github/workflows/`:** GitHub Actions workflows for SEO and video-tool smoke tests.
- **`.github/scripts/`:** scripts used by automated repository checks.
- **`video-downloader-backend/`:** separate Python/Flask API source; it is not deployed by GitHub Pages. `render.yaml` is its optional Render deployment configuration.
- **`.nojekyll`:** tells GitHub Pages not to run Jekyll processing on the static site.

## Safe maintenance rules

1. Do not move published HTML pages into folders unless every internal link, navigation link, sitemap URL, canonical URL, and redirect is updated and tested. Root placement is intentional for URL stability.
2. Do not delete the Google verification file, robots file, sitemap files, legal/contact pages, `.nojekyll`, or GitHub Actions workflows without checking their purpose first.
3. Keep `sitemap.xml` and `sitemap.txt` synchronized with published pages. Submit `sitemap.xml` in Google Search Console.
4. The optional backend is separate from the static site. The browser UI cannot call a backend that has not actually been deployed and configured.
5. Before deleting a file, search the repository for its filename and confirm that no page, workflow, sitemap, or deployment config refers to it.

## Test automation

- `.github/workflows/seo-audit.yml` runs the repository SEO audit.
- `.github/workflows/video-tools-smoke.yml` runs an automated browser smoke test for the video compression tool.

Check the **Actions** tab in GitHub for the latest run status. A workflow file existing in the repository does not by itself mean the test has passed.

## Hosting

The current site works as a static site on GitHub Pages. See [HOSTING-MIGRATION.md](HOSTING-MIGRATION.md) before changing hosting or URL structure.

## Known feature limitations

- The direct video URL helper only works when the source host permits browser downloads; it is not a universal social-media downloader.
- Video compression outputs WebM.
- Check each tool's own interface for format, browser, and external-library limitations. Do not advertise a tool as working until it has been tested on the deployed site.
