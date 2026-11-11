# Ahmed Ouazzani — Data Analyst & BI Developer

Professional portfolio featuring three case studies in business intelligence, data engineering, forecasting and applied AI.

**[GitHub](https://github.com/AhmedOT22)** · **[LinkedIn](https://www.linkedin.com/in/ahmed-ouazzani-5b078b205/)**

## Cloudflare Pages deployment

This project uses Flask for local development and exports a **static site** for Cloudflare Pages. No Flask server or paid Python runtime is required in production.

1. In [Cloudflare Workers & Pages](https://dash.cloudflare.com/), create a **Pages** project and connect the GitHub repository `AhmedOT22/Portfolio`.
2. Choose the production branch `main` and **Framework preset: None**.
3. Set the **Build command** to `python -m pip install -r requirements.txt && python export_static.py`.
4. Set the **Build output directory** to `dist` and **Root directory** to `/` (repository root).
5. Set the environment variable **`PYTHON_VERSION`** to `3.11`.
6. Select **Save and Deploy**, then visit the generated `*.pages.dev` address.

Cloudflare automatically rebuilds the site on later pushes to `main`. Cloudflare supplies `CF_PAGES_URL` at build time, which the exporter uses for the Open Graph preview image.

**After verifying the new public URL:** Update any GitHub, LinkedIn and résumé links still pointing to Render, and then retire the old Render service. The Render site is intentionally not removed by this repository change.

## Local development and verification

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python app.py
```

To generate the Cloudflare deployable files locally:

```bash
python export_static.py
```

The output is written to `dist/`. The site is static: it links to external applications and uses an email link for contact; it does not require a server-side submission endpoint.

Licensed under [MIT](LICENSE).
