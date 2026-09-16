# AlphaIT Engineering — website review edition

Nineteen static HTML pages. The founder-approved v2 position and current product briefs govern the copy. The site reuses Aether Mineral brand assets, Public Sans, Instrument Sans, current product identities and the Clear Route hero. No framework or paid asset dependency.

## Build and validate

Run `python build.py`, `python validate.py`, and `node --check dist/assets/js/experience.js`. The build imports public product content from the local profile builder when available. The published output is `dist/`.

## Deployment boundary

Private review only. Production domain and DNS are unchanged. All pages currently carry noindex; robots.txt disallows indexing. Before public release, approve the preview, confirm the enquiry service works from the production origin, update canonical/social URLs to the final origin and enable indexing. A real enquiry has deliberately not been submitted during QA.

The existing Web3Forms public access key is retained in the contact page. This is a client-facing form routing key, not a privileged server credential. Confirm domain restrictions with the account owner before release. Mail and WhatsApp links provide fallback contact paths.

Customer PDF only is included. Internal team documents and corporate records are not published. Product logos represent AlphaIT's own products, not customers. Sample workflows are labelled illustrative; no fabricated performance numbers, clients or endorsements are used.

## Spatial experience and motion

The homepage uses one lightweight spatial operating model to explain opportunity, system and outcome. Its state changes with the buyer-selected outcome and updates the relevant product route. Fine-pointer devices receive restrained depth; mobile receives a simplified composition with the same explanation. Keyboard arrow/Home/End navigation and reduced-motion styles are included. There is no scroll hijacking, automatic tab rotation or decorative motion without meaning.

## Commercial handoff

Home → outcome example → systems → dedicated product page → product-selected enquiry. Company, delivery approach, secondary PDF, email, WhatsApp and UAE/Kenya/Nigeria addresses are included. The live production website remains untouched pending approval.
