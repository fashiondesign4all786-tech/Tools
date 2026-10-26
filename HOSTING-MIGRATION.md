# ToolNest: domain and hosting migration plan

Last reviewed: 2026-10-26

## Current setup

- Public site: https://fashiondesign4all786-tech.github.io/Tools/
- Source of truth: GitHub repository `fashiondesign4all786-tech/Tools`, branch `main`
- Site type: static HTML, CSS and browser-side JavaScript.
- Current publishing: GitHub Pages.
- Domain: not selected yet.
- Server/database: none required for the current static tools.

## Recommended hosting strategy

**Stay on GitHub Pages until a custom domain is chosen.** When ready, buy a domain you can renew reliably, attach it to the current site first, and keep GitHub as the source repository.

For a future static-host move, evaluate **Cloudflare Pages** first (static files, Git-based deployment, CDN and custom-domain support); compare current plan limits and terms before switching. Netlify is a reasonable alternative. Do not buy PHP/MySQL hosting just for browser-based tools. Consider a server or database only if ToolNest later needs accounts, stored user data, paid plans, server-side file processing, or other backend features.

Hosting does not guarantee advertising approval or earnings. Revenue depends on useful original content, audience, policy compliance and advertiser demand. Keep privacy disclosures accurate about each tool's actual data flow and third-party libraries/APIs.

## Portability rules for every future change

1. Keep source files and change history in this repository; do not make the hosting dashboard the only copy.
2. Keep the site build-free where possible. If a build step is added, document the exact command and output directory.
3. Use relative paths for assets and links between pages where practical. The current GitHub Pages project site lives under `/Tools/`; a custom domain normally serves from `/`. Check paths carefully before changing this base path.
4. Do not add a guessed domain to canonical tags, Open Graph URLs, structured data, robots.txt, or sitemaps. Set those only after the domain is purchased and configured.
5. Keep one preferred HTTPS hostname (www or apex) and redirect the alternate hostname to it at the hosting/DNS layer.
6. Keep secrets, private API keys, credentials and personal data out of public HTML, JavaScript and this repository. Browser-side code is visible to visitors.
7. Maintain a page inventory and test each tool on desktop and mobile after any deployment. In particular, test tools that load large libraries or models from third-party CDNs.
8. Keep `robots.txt`, `sitemap.xml`, `sitemap.txt`, verification files and privacy/terms/contact pages in the published root. Update all absolute URLs after the final domain is known.

## Migration checklist

### A. Before buying a domain
- [ ] Keep this repository current and verify the live site after each deployment.
- [ ] Check that the chosen name is available as a domain and social handle; check trademarks before committing to a brand.
- [ ] Decide the canonical hostname (for example, apex or www) before configuring DNS.
- [ ] Export a list of all published page URLs and record important traffic/search data.

### B. Attach a domain while still on GitHub Pages
- [ ] Buy the domain from a registrar and keep renewal and account recovery details safe.
- [ ] Add the custom domain in GitHub Pages settings and configure the exact DNS records GitHub specifies.
- [ ] Enable HTTPS after DNS validation; do not publish a guessed CNAME or A record.
- [ ] Update canonical tags, Open Graph URLs, internal absolute links, `robots.txt`, and both sitemaps to the verified domain.
- [ ] Test every URL and tool, then verify the domain property in Google Search Console and submit the new sitemap.

### C. Move hosting later (keep the custom domain and public URLs unchanged)
- [ ] Deploy the same repository to the new host and test its preview URL before touching DNS.
- [ ] Set the new host's build settings to static/no build and publish the repository root unless the project structure has changed.
- [ ] Configure the domain and HTTPS on the new host first, following that host's current instructions.
- [ ] Change DNS only after the new site is verified. Keep the old host available during the transition.
- [ ] Test homepage, all tool pages, downloads, browser console, mobile layout, robots.txt and sitemaps.
- [ ] Monitor Search Console and analytics; retire the old host only after the new host serves correctly.

### D. If the domain or page URLs change
- [ ] Create a one-to-one old-URL → new-URL mapping for every page and important asset.
- [ ] Set server-side permanent redirects (301/308) on the old host/domain wherever possible; do not redirect every page to the homepage.
- [ ] Update canonicals, internal links, metadata, structured data, robots.txt and sitemaps.
- [ ] Verify both sites in Search Console, submit the new sitemap, use Change of Address when applicable, and monitor indexing/errors.
- [ ] Keep old-domain redirects for at least a year if possible, and renew the old domain so it cannot be taken over.

## Current URL inventory

The existing project URL prefix is:

`https://fashiondesign4all786-tech.github.io/Tools/`

Published pages include the homepage and the HTML files listed in the repository root. Use the live `sitemap.xml` as the page inventory before migration. Do not assume every file is working just because it is listed; verify each tool in a browser.

## Official references

- GitHub Pages custom domains: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- Google Search Central — hosting change without URL changes: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
- Google Search Central — move with URL changes: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- Cloudflare Pages: https://developers.cloudflare.com/pages/
- Netlify docs: https://docs.netlify.com/

This guide is a migration plan, not a claim that a domain or alternate host has already been configured.
