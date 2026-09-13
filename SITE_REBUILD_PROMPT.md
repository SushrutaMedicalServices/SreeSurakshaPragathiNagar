# Rebuild Prompt: Sree Suraksha Multispeciality Hospital Website

This is a detailed, step-by-step prompt/spec for recreating **sreesurakshahospitals.com** as a static HTML/CSS/JS site. It was reverse-engineered by crawling the live site page-by-page and image-by-image on 2026-09-13. Hand this whole document to a developer or an AI coding assistant and it is sufficient, on its own, to reproduce the site in this repository.

---

## 1. Brief

Build a static, multi-page marketing website for **Sree Suraksha Multispeciality Hospital** (A Unit of Viyan Sri Health Care Pvt. Ltd.), a 24/7 multispeciality hospital in Pragathi Nagar, Kukatpally, Hyderabad. No CMS, no backend, no build tooling — plain HTML/CSS/JS deployable to any static host (Cloudflare Pages, Netlify, GitHub Pages).

**Brand identity**
- Primary accent color: orange `#f5821f` (buttons, links, highlights)
- Secondary accent: teal `#0d9488` (icon accents, matches the green/teal cross in the logo)
- Headings: near-black `#101828`; body text: slate gray `#475467`
- Typography: a clean sans-serif (Inter works well); original site used Roboto (body) / B612 (headings)
- Logo: horizontal wordmark "SURAKSHA MULTISPECIALITY HOSPITAL" with a cross+heart icon, plus the tagline "(A Unit of Viyan Sri Health Care Pvt. Ltd.)" underneath
- Overall tone: clean, card-based, generous whitespace, rounded corners, soft shadows — typical modern healthcare marketing site

**Global identity data**
```
Name:      Suraksha Multispeciality Hospital
Full name: Sree Suraksha Multispeciality Hospital
Unit of:   Viyan Sri Health Care Pvt. Ltd.
Phones:    +91 96664 69911, +91 7288 080 222, +91 7288 080 333
Email:     info@sushrutamedicalservices.com
Address:   6-1540/DNP/G1. Beside Reliance Trends, Near Allur Seetharamaraju
           Statue, Pragathi Nagar, Hyderabad-500090.
Socials:   Facebook, X/Twitter, Instagram, LinkedIn, YouTube (see footer)
Copyright: © 2026 Suraksha Multispeciality Hospital. All Rights Reserved.
```

---

## 2. Site map (27 pages)

Use folder + `index.html` for every page so URLs are clean (`/contact-us/` not `/contact-us.html`), matching the original site's permalinks.

| URL | Purpose |
|---|---|
| `/` | Home |
| `/our-services/` | Full A–Z list of all 18 departments |
| `/blog/` | Blog index (4 posts) |
| `/contact-us/` | Contact form + address/phone/email + map |
| `/book-an-appointment/` | Appointment request form |
| `/general-medicine/` | Department detail |
| `/diabetology/` | Department detail |
| `/paediatrics-and-neonatology/` | Department detail |
| `/orthopaedics/` | Department detail (has a 13-item condition list) |
| `/trauma-and-critical-care/` | Department detail |
| `/joint-replacement/` | Department detail |
| `/general-and-laparoscopic-surgery/` | Department detail |
| `/surgical-gastroenterology/` | Department detail |
| `/medical-gastroenterology/` | Department detail |
| `/neurology/` | Department detail |
| `/neuro-surgery/` | Department detail |
| `/oncology/` | Department detail |
| `/ent/` | Department detail |
| `/dermatology/` | Department detail |
| `/pulmonology/` | Department detail |
| `/physiotherapy/` | Department detail |
| `/radiology-and-intervention-radiology/` | Department detail |
| `/laboratory-medicine/` | Department detail |
| `/best-trauma-care-centre-in-kukatpally-hyderabad/` | Blog post |
| `/best-neurosurgery-hospitals-in-kukatpally-hyderabad/` | Blog post |
| `/best-orthopedic-hospital-in-kukatpally-hyderabad/` | Blog post |
| `/best-joint-replacement-doctors-in-kukatpally-hyderabad/` | Blog post |

Every page shares the same header and footer (see §4). Every department/blog page shares the same two-column layout: content on the left, a sidebar with a department index + "Call Now" CTA on the right (single column, sidebar below content, on mobile).

---

## 3. Assets to source

Download every image and the hero video from the live site and store locally (do not hotlink):

```
assets/original-site/images/logo.png
assets/original-site/images/appointment.png
assets/original-site/images/24by7services.jpg
assets/original-site/images/profile.jpg                    (generic testimonial avatar)
assets/original-site/images/services/services-1.jpg …6.jpg
assets/original-site/images/services/paediatrics.jpg
assets/original-site/images/services/gastroenterology.jpg
assets/original-site/images/services/medical-gastroenterology.jpg
assets/original-site/images/services/neurology.jpg
assets/original-site/images/services/neurosurgery.jpg
assets/original-site/images/services/oncology.jpg
assets/original-site/images/services/ent.jpg
assets/original-site/images/services/dermatology.jpg
assets/original-site/images/services/pulmonology.jpg
assets/original-site/images/services/physiotherapy.jpg
assets/original-site/images/services/radiology.jpg
assets/original-site/images/services/laboratory-medicine.jpg
assets/original-site/images/facilities/1.jpg …8.jpg
assets/original-site/images/doctors/dr-divya-teja.jpg
assets/original-site/images/doctors/dr-harinath-bellamkonda.jpg
assets/original-site/images/doctors/dr-sanjeeva-rao.jpg
assets/original-site/images/doctors/dr-kishore.jpg
assets/original-site/images/doctors/dr-manasa.jpg
assets/original-site/images/doctors/dr-vishvanath.jpg
assets/original-site/images/blog/suraksha_blog_1.jpg …4.jpg
assets/original-site/video/video-1.mp4                     (homepage hero background video)
```

---

## 4. Shared layout

### 4.1 Top strip (thin bar above the nav)
Left: mailto + tel links with icons. Right: 5 social icons (Facebook, X, Instagram, LinkedIn, YouTube), dark background.

### 4.2 Main navigation (sticky)
- Logo (links home)
- Nav links: **Home**, **Our Services**, **Blog**, **Contact Us**
- "Call Now" block with phone icon + primary number (hidden on mobile)
- Primary button: **Book An Appointment** → `/book-an-appointment/`
- Hamburger toggle on screens ≤960px, opening a stacked mobile menu (include the Book An Appointment CTA inside the mobile menu too, styled as a filled button — don't just rely on the header button, which is hidden on narrow phones to avoid overflow)
- Highlight the current page's nav link (do this in JS by comparing `location.pathname`, not by hardcoding per page, so every page can share one identical header markup)

### 4.3 Page header (every non-home page)
Dark gradient banner: `<h1>` page title + breadcrumb trail (`Home › Services › <Page>` or `Home › Blog › <Page>`).

### 4.4 Footer
4 columns: About (logo + blurb + social icons), Quick Links (Home/Our Services/Blog/Contact Us), Services (the 6 featured departments), Useful Links (address/phone/email with icons). Bottom bar: copyright line.

Also include: a floating "back to top" button (bottom-right, appears after scrolling ~400px) and a floating call button (bottom-left, mobile only).

---

## 5. Home page (`/`)

1. **Hero** — full-bleed section with the hospital-exterior/interior **video** (`video-1.mp4`) autoplaying, muted, looped, with a dark gradient scrim for text contrast. Eyebrow "Your Health, Our Priority", H1 "Sree Suraksha Multispeciality Hospital", subtitle referencing "The best way to predict the future is to create it" and 24/7 emergency/trauma care, two CTAs: "Book An Appointment" and "Call Now".
2. **Our Services** — 6 featured service cards (image + title + 2-sentence description + "Read More" link), linking to the matching department page:
   - General Medicine → `services/services-1.jpg`
   - Diabetology → `services/services-2.jpg`
   - Paediatrics & Neonatology → `services/paediatrics.jpg`
   - Orthopaedics → `services/services-3.jpg`
   - Trauma & Critical Care → `services/services-4.jpg`
   - Joint Replacement → `services/services-5.jpg`
   Below the grid: a "View All Services" button → `/our-services/`.
3. **Our Facilities** — two image+list cards covering: General Ward A/C, Pharmacy, Hematology, Clinical Pathology, Histopathology, Clinical Biochemistry, Ultrasound, Antenatal Scan, Digital X-Ray, ECG, EEG, 2D Echo, TMT, PFT, Advanced ICU, Advanced OT Units, Laminar Air Flow & Hepa Filter, Single Room/Sharing Room.
4. **Our Doctors** — 6 doctor cards (circular photo, name, qualifications, role):
   - Dr. Divya Teja — MBBS, DCH — Paediatrician
   - Dr. Hrinath Bellamkonda — MS (Ortho), Mch (Ortho), FIASM — Sr. Consultant Orthopedic Surgeon
   - Dr. Sanjeeva Rao K — MBBS, DNB (Gen. Surgery), MNAMS DRNB — Vascular & Endovascular Surgeon
   - Dr. Ravikishore — MD Neuropsychiatry (Osmania), FISM (USA), CAP — Child & Adolescent Psychiatrist
   - Dr. Manasa Chaitanya Ratna — MS OBG — Gynecologist & Paediatrician
   - Dr. Vishwanath — MBBS (Gold Medalist), DNB (Gen. Surg), MNAMS, FMBS, FMAS, FIAGES, FALS — Advanced Laparoscopic & Bariatric Surgeon
5. **Our 24/7 Services** — dark strip, 6 items: Trauma Care, Critical Care, Pharmacy, Lab, Radiology, Ambulance.
6. **Testimonials** — 5 cards (quote + generic avatar + name): Soujanya Patthi, Siri J, Ajay Tadakara, Badharinadh, Saraswati. (Full quotes are in `build/generate.py` under `TESTIMONIALS`.)

---

## 6. Department page template (18 pages)

Layout: page header (title + breadcrumb) → two-column content section:
- **Left (main):** banner image (`services/<slug>.jpg`), `<h2>` repeating the department name, then either:
  - 2–3 plain paragraphs (most departments), or
  - paragraphs with `<h3>` subheads (e.g. Trauma & Critical Care has "Comprehensive Trauma Services" / "Advanced Critical Care" / "Patient-Centered Approach"), or
  - a grid of labeled condition cards (Orthopaedics only — 13 items: Arthritis, Bursitis, Chronic Muscle Joint Pains, Multiple Fractures, Replacement (TKR/THR), Non Cancerous Benign Tumors, Cancerous Tumors, Arthroscopy (Shoulder/Knee), Trauma & Fracture, Spine Surgery, Musculoskeletal Disorders, Sports Injuries, Physiotherapy)
- **Right (sidebar):** "All Departments" link list (all 18, alphabetically as listed in §2) + a "Need Immediate Care?" call-to-action card with a Call Now button.

All 18 departments' exact copy is transcribed in `build/generate.py` (`DEPARTMENTS` list) and in the generated `build/bodies/inner/*.html` files — reuse that copy verbatim; it is the hospital's own content.

---

## 7. `/our-services/` page

Page header, then a grid of all 18 department cards (image + title + 1-sentence summary + "Read More"), each linking to its detail page. Same card component as the homepage's 6 featured services.

---

## 8. `/blog/` and blog post pages

**`/blog/`**: page header, then a 4-card grid (image + title + 1-sentence excerpt + "Read More"), linking to each post:
- Best Trauma Care Centre in Kukatpally, Hyderabad (`blog/suraksha_blog_4.jpg`)
- Best Neurosurgery Hospital in Kukatpally, Hyderabad (`blog/suraksha_blog_2.jpg`)
- Best Orthopedic Hospital in Kukatpally, Hyderabad (`blog/suraksha_blog_1.jpg`)
- Best Joint Replacement Doctors In Kukatpally Hyderabad (`blog/suraksha_blog_3.jpg`)

**Each post page** uses the same content-page + sidebar template as department pages (breadcrumb: Home › Blog › <Post>), with the post's banner image and full body (multiple `<h3>` subsections + a "Conclusion" section). Full copy for all 4 posts is in `build/generate.py` (`BLOG_POSTS`) and `build/bodies/inner/best-*.html`.

---

## 9. `/contact-us/`

Two columns: left = 3 info cards (Address / Phone / Email, each with an icon) + an embedded Google Map iframe (`https://www.google.com/maps?q=Pragathi+Nagar,+Kukatpally,+Hyderabad,+Telangana,+India&output=embed`); right = a contact form with fields **Your Name, Your Email, Your Phone, Subject, Your Message** and a "Send Message" submit button.

## 10. `/book-an-appointment/`

Single centered form card: **Name, Email Address, Phone Number, Preferred Date (date picker), Message**, "Submit" button.

Neither form has a real backend in the source site's public HTML — for this rebuild, make forms client-side functional at minimum (e.g., open a pre-filled `mailto:` on submit) and document in the README that a real form backend (Cloudflare Pages Functions, Formspree, etc.) should be wired up for production lead capture.

---

## 11. Component & CSS notes

- Buttons: pill-shaped (`border-radius: 999px`), orange fill for primary, outline for secondary, hover lift (`translateY(-2px)`).
- Cards: white background, 1px light-gray border, 14px radius, subtle shadow on hover.
- Section rhythm: alternate white and very-light-gray (`#f8f9fb`) section backgrounds to separate content blocks.
- All section headings use an "eyebrow" label above them (small, orange, uppercase, bold) + a larger dark `<h2>`.
- Sidebar on department/blog pages is `position: sticky` on desktop, static (stacks below content) on mobile.
- Responsive breakpoints: collapse to single-column layouts and hamburger nav at ≤960px; stack forms/footer columns at ≤640px.

---

## 12. Build & deploy notes

- No JS framework, no CSS framework, no build step — plain files served as-is.
- Deploy target: Cloudflare Pages via `wrangler pages deploy .` triggered by a GitHub Actions workflow on push to `main` (see `.github/workflows/deploy.yml`), matching the sibling site's deployment pattern. Requires `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` repo secrets and a Cloudflare Pages project created ahead of time.
- Include `robots.txt` and `sitemap.xml` listing all 27 URLs for SEO parity with the original.

---

*This prompt, plus the content tables in `build/generate.py`, is sufficient to regenerate every page in this repository from scratch.*
