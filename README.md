# AlphaIT Engineering website

This repository is the permanent source of truth for the website published at [alphaitengineering.com](https://alphaitengineering.com).

The source was recovered and verified on 2026-09-19 from the exact source commit attached to the live OpenAI Sites version. The production source commit was `bd05a38f89d0f4ef0d3dedddc6a578d55cdb87bf`.

## Pages

The site contains 19 HTML pages, including the 404 page.

| File | Purpose |
| --- | --- |
| `dist/index.html` | Main AlphaIT Engineering company and product landing page. |
| `dist/platforms.html` | Overview of the systems AlphaIT has already engineered. |
| `dist/verdika.html` | Verdika product page. |
| `dist/varren.html` | Varren product page. |
| `dist/varren-aegis.html` | Varren Aegis product page. |
| `dist/varren-herald.html` | Varren Herald product page. |
| `dist/lisbon-signal.html` | LisBon Signal Infrastructure product page. |
| `dist/lisbon-trust.html` | LisBon Trust Infrastructure product page. |
| `dist/liscredit.html` | LisCredit marketplace product page. |
| `dist/trust-app.html` | LisBon Trust App product page. |
| `dist/lisbon-flow.html` | LisBon Flow Infrastructure product page. |
| `dist/flow-app.html` | LisBon Flow App product page. |
| `dist/pollenair.html` | Pollenair product page. |
| `dist/business-systems-engineering.html` | AlphaIT focused business systems engineering service page. |
| `dist/company.html` | Company identity, leadership and locations. |
| `dist/contact.html` | Enquiry form and direct contact routes. |
| `dist/proof.html` | Product proof and systems already engineered. |
| `dist/engagements.html` | Engagement routes for deployment, integration and focused builds. |
| `dist/404.html` | Branded not-found page. |

## Source and asset layout

| Path | Contents |
| --- | --- |
| `build.py` | Generates the static website in `dist/`. |
| `products.json` | Structured product content used by the builder. |
| `validate.py` | Static source and output validation. |
| `test-form.mjs` | Contact form integration check. It must not be run against production without approval because it submits a test enquiry. |
| `preview.mjs` | Dependency-free local preview server. |
| `.openai/hosting.json` | OpenAI Sites project and static output configuration. |
| `dist/` | Complete publishable website. |
| `dist/assets/brand/` | AlphaIT brand assets copied from the canonical brand system. |
| `dist/assets/products/` | Product marks and product identity assets. |
| `dist/assets/fonts/` | Instrument Sans and Public Sans font files and licence. |
| `dist/assets/css/` | Site and interactive experience stylesheets. |
| `dist/assets/js/` | Shared site behaviour and the homepage experience. |
| `dist/assets/icons/` | Interface icons. |
| `dist/assets/images/` | Website imagery. |
| `dist/AlphaIT-Company-and-Product-Profile.pdf` | Downloadable customer profile. |
| `dist/robots.txt` | Search crawler instructions. |
| `dist/sitemap.xml` | Canonical public page index. |
| `dist/_headers` | Hosting header rules. |

## Recovery note

`site.webmanifest` was named in the recovery brief, but it was not present in the exact production source commit or its published file set, and `https://alphaitengineering.com/site.webmanifest` returned 404 during verification on 2026-09-19. It has not been fabricated because this repository must match the live site.

The canonical design system remains outside this repository at `AlphaIT_Brand\AlphaIT_Brand_System`. Files under `dist/assets/brand/` are deployment copies. Do not edit the canonical design system while maintaining the website.

## Build and validate

Run from the repository root in PowerShell:

```powershell
python build.py
python validate.py
node --check dist/assets/js/experience.js
```

The publishable output is `dist/`.

## Preview locally

From the repository root:

```powershell
node preview.mjs
```

Open `http://127.0.0.1:4173/`. Stop the server with `Ctrl+C`.

## Deployment

Deployment is through OpenAI Sites, project `AlphaIT Engineering`, project ID `appgprj_6aaa8ad1178881918aadb2aa33de03de`. The custom domain is [alphaitengineering.com](https://alphaitengineering.com).

The exact preparation command used by the Sites workflow is:

```powershell
node "C:\Users\alpha\.codex\plugins\cache\openai-curated-remote\sites\0.1.65\scripts\package-site.mjs" "." ".\alphait-site.tar.gz"
```

The archive is then saved as a new version of the existing Sites project and that saved version is deployed. Sites deployment is performed through the Sites connector, not through a standalone public command-line deploy tool. The exact connector sequence and all account facts are recorded in [DEPLOY.md](DEPLOY.md).

Do not create a replacement Sites project. Do not deploy from a dirty working tree. Commit and push the exact source first, then deploy that same commit and archive.
