# AlphaIT Engineering — website review edition

19 static HTML pages. Approved 12 September customer profile is the copy baseline. Reuses the Aether Mineral brand assets, Public Sans, Instrument Sans, current product identities and Clear Route hero. No framework or paid asset dependency.

## Build and validate

Run `python build.py`, `python validate.py`, and `node --check dist/assets/js/experience.js`. The build imports public product content from the local profile builder when available. The published output is `dist/`.

## Deployment boundary

Private review only. Production domain and DNS are unchanged. All pages currently carry noindex; robots.txt disallows indexing. Before public release, approve the preview, confirm the enquiry service works from the production origin, update canonical/social URLs to the final origin and enable indexing. A real enquiry has deliberately not been submitted during QA.

The existing Web3Forms public access key is retained in the contact page. This is a client-facing form routing key, not a privileged server credential. Confirm domain restrictions with the account owner before release. Mail and WhatsApp links provide fallback contact paths.

Customer PDF only is included. Internal team documents and corporate records are not published. Product logos represent AlphaIT's own products, not customers. Sample workflows are labelled illustrative; no fabricated performance numbers, clients or endorsements are used.

## Motion

Gentle hero pointer depth on fine-pointer devices, viewport entry transitions and an animated operation flow. Touch users get selectable example tabs and a vertical flow. Keyboard arrow/Home/End navigation and reduced-motion styles are included. No scroll hijacking or automatic tab rotation.

## Commercial handoff

Home → systems or outcome example → dedicated product page → product-selected enquiry. Company, delivery approach, PDF, email, WhatsApp and UAE/Kenya/Nigeria addresses are included. The current live production website remains untouched pending approval.
