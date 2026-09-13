# Sree Suraksha Multispeciality Hospital — Website

A full rebuild of [sreesurakshahospitals.com](https://www.sreesurakshahospitals.com/) as a plain static HTML/CSS/JS site (no framework, no build step), ready to deploy on Cloudflare Pages — mirroring the structure used for the sibling [AxisClinicalDiagnosticsPragathiNagar](https://github.com/SushrutaMedicalServices/AxisClinicalDiagnosticsPragathiNagar) site.

## What's here

- **27 pages**, content-matched to the live site: home, our-services, blog (+ 4 posts), contact-us, book-an-appointment, and 18 department pages — each at a clean URL (`/contact-us/`, `/general-medicine/`, etc.) via `folder/index.html`, matching the original site's permalink structure.
- **`assets/original-site/`** — every image and the homepage hero video, downloaded from the live site (logo, doctor photos, facility photos, service banners, blog images).
- **`css/styles.css`** — a single hand-written stylesheet (no external UI framework) implementing the brand look: orange `#f5821f` accent, dark navy headings, card-based sections.
- **`js/main.js`** — mobile nav toggle, active-link highlighting, back-to-top button, and lead-form handling (forms currently open the visitor's email client with the message pre-filled — see "Contact forms" below).

## Local preview

No build tools are required. Any static file server works, e.g.:

```bash
npx serve .
```

Or, on a machine without Node/Python, use the PowerShell static server included for development:

```bash
powershell -File build/serve.ps1 -Port 8098
```

Then open `http://localhost:8098/`.

## Rebuilding pages from the content data

`build/generate.py` is a Python static-site generator that regenerates every HTML page from the structured content in that same file (department descriptions, doctor list, testimonials, etc.). It was written for convenience but **was not used to produce the committed HTML** in this repo, because this environment had no Python or Node installed — the pages were hand-assembled instead via the shell helpers in `build/make-page.sh` and `build/make-dept-page.sh`, which splice the shared header/footer partials in `build/partials/` around each page's content in `build/bodies/`.

If you have Python 3 available and want a single source of truth for future edits:

```bash
python build/generate.py
```

This regenerates every page from the data structures at the top of `generate.py` — edit the content there (e.g. to update a department description or add a doctor) and re-run.

## Contact forms

The "Contact Us" and "Book an Appointment" forms are client-side only right now: submitting one opens the visitor's email app with the message pre-filled (`mailto:info@sushrutamedicalservices.com`). This works everywhere with no backend, but depends on the visitor having a configured email client, and you won't get submissions in one place.

For production, connect a real form backend — options that work well with a static Cloudflare Pages site:
- **Cloudflare Pages Functions** (`functions/api/contact.js`) posting to email via an API (e.g. Resend, SendGrid, Mailgun) or writing to a D1/KV store.
- A third-party form service (Formspree, Web3Forms, Basin) — point the form's `action` at their endpoint.

## Deployment (Cloudflare Pages)

`.github/workflows/deploy.yml` deploys on every push to `main`, matching the sibling repo's pattern. It needs two repository secrets:

- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`

...and a Cloudflare Pages project named `sree-suraksha-pragathi-nagar` (or update `--project-name` in the workflow to match whatever you create). Until those secrets exist, the workflow will simply fail — it won't break anything else.

## Content source & images

All text content and images were extracted directly from the live site at sreesurakshahospitals.com (owned by Sushruta Medical Services) on 2026-09-13. See [SITE_REBUILD_PROMPT.md](SITE_REBUILD_PROMPT.md) for a full page-by-page, asset-by-asset specification of what was captured and how it maps to this codebase.
