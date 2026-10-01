# AlphaIT Engineering deployment handoff

## Hosting facts

| Item | Value |
| --- | --- |
| Host | OpenAI Sites |
| Owner account | `alphalucky.c@gmail.com` |
| Site name | `AlphaIT Engineering` |
| Sites project ID | `appgprj_6aaa8ad1178881918aadb2aa33de03de` |
| Sites slug | `alphait-engineering-experience` |
| Provider URL | `https://alphait-engineering-experience.alphalucky-c.chatgpt.site` |
| Custom domain | `https://alphaitengineering.com` |
| Static output | `dist/` |
| Sites manifest | `.openai/hosting.json` |
| GitHub source of truth | `https://github.com/alphaitengineering/AlphaIT-Engineering-Website` |
| Recovered live Sites version | Version 5 |
| Recovered production source commit | `bd05a38f89d0f4ef0d3dedddc6a578d55cdb87bf` |

The recovery brief named `site.webmanifest`, but the exact deployed source did not contain it and the live URL returned 404 on 2026-09-19. It was not invented during recovery.

## Secrets and variables

The website is static and requires no runtime environment variable in OpenAI Sites.

Deployment access requires a short-lived Sites source repository token. Treat it as the variable `SITES_SOURCE_TOKEN`. Obtain a new value through the OpenAI Sites `create_source_repository_write_credential` operation for the existing project. Never save the value in this repository, a Git remote, a document or a command history.

GitHub push access may use an authenticated GitHub CLI session or an environment variable named `GITHUB_TOKEN`. Never commit that token.

The contact page currently contains the existing Web3Forms public access key in the generated HTML. It is a client-side routing key, not a privileged server secret. Do not replace it without confirming the form account and domain restrictions.

## Exact build and validation commands

Run from this repository root:

```powershell
python build.py
python validate.py
node --check dist/assets/js/experience.js
```

Preview before deployment:

```powershell
node preview.mjs
```

Open every route listed in `README.md` and confirm that internal navigation, images, fonts, stylesheets and scripts resolve.

## Exact package command

```powershell
node "C:\Users\alpha\.codex\plugins\cache\openai-curated-remote\sites\0.1.65\scripts\package-site.mjs" "." ".\alphait-site.tar.gz"
```

If the installed Sites plugin version changes, use the `package-site.mjs` script from the installed version and keep the same two arguments: the repository root and the output archive path.

## Exact deployment sequence

1. Confirm `.openai/hosting.json` still names project ID `appgprj_6aaa8ad1178881918aadb2aa33de03de` and static directory `dist`.
2. Run the build and validation commands above.
3. Commit the exact source state and push it to the default branch of the GitHub source-of-truth repository.
4. Obtain a short-lived source write credential for this existing OpenAI Sites project. Do not create a new project.
5. Push the same commit to the Sites source repository using the credential only as a per-command HTTP authorization header.
6. Run `git rev-parse --verify HEAD` and retain the complete commit SHA.
7. Run the package command above without changing the source after the commit.
8. Call the OpenAI Sites `save_site_version` operation with the project ID, complete commit SHA and absolute archive path.
9. Call `deploy_site_version` with the returned version ID. The site is public, so do not use the owner-private deployment operation.
10. Poll `get_deployment_status` until it succeeds. Confirm both the provider URL and the custom domain.

For Codex, the exact deployment instruction is:

```text
Publish the exact committed source in this folder to the existing OpenAI Sites project appgprj_6aaa8ad1178881918aadb2aa33de03de. Preserve public access and the custom domain alphaitengineering.com. Do not create a new site. Build, validate, push the same commit to the Sites source repository, package it, save one new version and deploy that version.
```

## Rollback

OpenAI Sites keeps saved versions. Select the last known good version and deploy that existing version. Do not rebuild it and do not create a replacement project. GitHub contains the permanent human-readable source and commit history from the 2026-09-19 recovery onward.

## Safety

- Never force-push the GitHub repository.
- Never deploy from an uncommitted or unpushed source state.
- Never store `SITES_SOURCE_TOKEN`, `GITHUB_TOKEN` or any other secret in source files.
- Never recover files from `90_REVIEW_BEFORE_DELETION\2026-09-19_Superseded_Website_Sources`.
- Never edit `AlphaIT_Brand\AlphaIT_Brand_System` as part of a website deployment.
- Confirm the custom domain remains attached after every deployment.

---

## Hosting moved to Cloudflare Pages, 2 October 2026

**The site is no longer published through OpenAI Sites.** The founder ran out of Codex credits, which was the only route to that platform, and nothing built on 1 and 2 October could reach the public. Hosting moved to Cloudflare Pages, in the same Cloudflare account that already holds the DNS for the domain.

| Item | Value |
| --- | --- |
| Cloudflare account | `Alphaitengineering@gmail.com's Account`, id `3e9c62ca023402d625ee78a499c96618` |
| Pages project | `alphait-site` |
| Project URL | `https://alphait-site.pages.dev` |
| Custom domain | `alphaitengineering.com`, CNAME to `alphait-site.pages.dev`, added 2 October 2026 |
| Production branch | `main` |

### Deploy command

Run from this repository root after `python build.py` and `python validate.py`:

```bash
npx --yes wrangler@4 pages deploy dist --project-name alphait-site --branch main --commit-dirty=true
```

Wrangler holds an OAuth token for the account in `C:\Users\alpha\.wrangler`. **No API key is read from any file and none belongs in this repository.** If the token loses a scope, `npx wrangler@4 login` re-issues it; the consent page must be approved in a browser signed in to that Cloudflare account.

**Two traps, both hit on the first run:**

- Wrangler writes a `wrangler.jsonc` into the working directory and derives the project name from the folder name. `AlphaIT Engineering Website` contains spaces and capitals, so it produced an invalid name and every later command failed on the stray file rather than on the real problem. **Delete any `wrangler.jsonc` it leaves behind**, in this folder and in the parent.
- `pages project create` now delegates to Cloudflare Workers and fails. **Create the project once with `--force`**, which uses the Pages path directly. Do not pass `--force` afterwards.

### The OpenAI Sites project

`appgprj_6aaa8ad1178881918aadb2aa33de03de` still exists and still holds the old version. It is the rollback if the Pages move ever has to be undone. **Nothing deploys to it any more.** The exact sequence it needed is preserved above this section.
