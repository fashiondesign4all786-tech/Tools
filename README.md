# ToolNest — Free Online Tools Website

This starter website is built with plain HTML, CSS, and JavaScript. It does not require a build step, database, server, paid API, or account system.

## Included tools
1. Word Counter
2. Image Resizer
3. Case Converter
4. Percentage Calculator
5. Age Calculator
6. JSON Formatter
7. CSV Viewer
8. Image Compressor
9. Date Calculator
10. URL Encoder / Decoder

## Run it on your computer
1. Extract `ToolNest.zip`.
2. Open the `ToolNest` folder.
3. Double-click `index.html` to open it in a modern browser.
4. Test each tool with sample inputs and files.

Some browser features (such as clipboard access) work best when the site is opened through HTTPS or localhost. The main tools work in current modern browsers.

## Publish free using GitHub Pages
1. Create or sign in to a GitHub account at https://github.com/.
2. Create a new **public** repository, for example `toolnest`.
3. Upload `index.html` to the repository's root folder. You can also upload `README.md`.
4. Open repository **Settings → Pages**.
5. Under the build/deployment source, choose **Deploy from a branch**.
6. Select branch `main` and folder `/(root)`, then save.
7. Wait for GitHub Pages to publish. The site address is usually `https://YOUR-USERNAME.github.io/toolnest/`.

GitHub's interface may change; follow its current Pages instructions if labels differ. A free GitHub Pages site uses a GitHub subdomain. A custom domain usually costs money.

Alternative: Netlify and Cloudflare Pages have free static-site options; review their current plans and terms before use.

## Before launching publicly
- Test the site on mobile and desktop and check all 10 tools.
- Add a contact page and clear Terms of Use.
- Review the privacy notice if you add analytics, ads, external services, or tracking.
- Do not claim files are processed locally unless you have verified the published code and all added scripts.
- Add an appropriate privacy policy and consent setup before using advertising services, if required by the provider and applicable law.
- Do not expect advertising income immediately. Ad networks have eligibility and policy requirements, and traffic is not guaranteed.
- The name “ToolNest” is a working name only. Check trademark and domain availability before investing in branding.

## Technical notes
- Image resizing outputs PNG.
- Image compression outputs JPEG and uses a white background for transparent images.
- CSV preview displays the first 100 data rows plus header when present; download exports the original CSV content.
- All calculations and file processing are client-side. No data is sent to a ToolNest server by this standalone file.
- This is a functional starter, not a security or accessibility certification. Test before relying on it.
