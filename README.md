# ToolNest improved website

Includes the homepage, 10 separate tool pages, About, Contact, Privacy Policy, Terms of Use, sitemap.xml and robots.txt.

## Before publishing
Replace the placeholder contact details in `contact.html` with a real monitored contact method. Review privacy and terms pages; these are starter templates, not legal advice. Test the tools on mobile and desktop.

## Upload to your existing GitHub repository
1. Download and extract this ZIP.
2. Open https://github.com/fashiondesign4all786-tech/Tools
3. Choose Add file → Upload files.
4. Upload every file in this folder directly into the repository root. Replace the existing `index.html` when prompted.
5. Commit changes and wait a few minutes for GitHub Pages to update.

Site: https://fashiondesign4all786-tech.github.io/Tools/
Sitemap: https://fashiondesign4all786-tech.github.io/Tools/sitemap.xml

Submitting a sitemap and requesting indexing can help Google discover pages but does not guarantee indexing or ranking.


## Added tools
This update adds QR Code Generator, Password Generator, Unit Converter, HEIC to JPG Converter, Image Format Converter, PDF Compressor (file-size checker only; it does not compress the PDF), and PDF Merger.

**External libraries:** QR generation, HEIC conversion, and PDF merging load free open-source libraries from public CDNs. These tools need an internet connection to load those libraries. Password generation, unit conversion, and image format conversion work locally in the browser. Files are not uploaded to a ToolNest server.

**Important limitation:** The PDF Compressor is deliberately labelled as a size checker only. It does not claim to compress PDFs. A real PDF compression feature would need a tested compression library and quality checks.


## Professional UI update
The homepage now uses a more polished layout inspired by common usability patterns from established online tool suites: prominent search, clear category filters, consistent tool cards, responsive layout, and focused tool panels. This is an original design and does not copy any competitor's branding or exact interface.


## Background Remover
Added a browser-based background removal tool that attempts to load the open-source @imgly/background-removal library from a public CDN. It requires an internet connection and model compatibility; test on the deployed site before promoting it. No paid API is used.


## Video Downloader
Added a browser-only direct video-link helper. It supports links that point directly to common video file extensions and that the host permits the browser to download. It intentionally does not download from platform page URLs or bypass DRM, login gates, paywalls, or platform restrictions. Use only content you own or are authorized to save.


## Word, Excel & Files to PDF
Added a browser-based converter for DOCX text and XLSX cell contents to PDF. It loads jsPDF, Mammoth.js, and SheetJS from public CDNs. DOCX conversion extracts text and does not preserve exact layout/images/tables; XLSX conversion prints sheet cell contents and may not preserve charts, formulas or formatting. Legacy DOC/XLS are intentionally not supported; convert them to DOCX/XLSX first. Test output carefully.


Background Remover troubleshooting update: the integration now reports more specific errors and disables the action while processing. The external model/CDN still requires live browser testing and may fail if the CDN bundle does not expose the expected browser API.


Background Remover implementation: now loads the official @imgly/background-removal ES module through jsDelivr's +esm endpoint and uses the documented IMG.LY data CDN path. Uses the quantized model to reduce download size. First run requires internet and may take several minutes. Must still be verified on the deployed GitHub Pages site because browser/CDN execution cannot be fully tested in this generation environment.
