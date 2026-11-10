# Ahmed Ouazzani — Data Analyst & BI Developer

Professional portfolio showcasing analytics, business intelligence, data engineering, forecasting, and applied machine learning work.

**[Live portfolio](https://portfolio-9o9p.onrender.com/)** · **[GitHub](https://github.com/AhmedOT22)** · **[LinkedIn](https://www.linkedin.com/in/ahmed-ouazzani-5b078b205/)**

## Portfolio positioning

Focused on **Data Analyst / BI Developer** opportunities while demonstrating broader data engineering, forecasting, and applied AI skills. The homepage uses the supplied professional portrait and shows project evidence, measured results, scope, and limitations.

## Featured work

| Project | Why it's featured |
| --- | --- |
| **Toronto Air Quality Forecasting** | Strongest publicly reproducible technical case study: validated data sources, leak-free evaluation, automated forecasting, and **27% lower 2025 holdout day-one MAE** than persistence. |
| **Hospital Insights Dashboard** | Direct BI relevance: SQL Server, synthetic healthcare reporting, dimensional modeling, DAX and five report pages. Desktop acceptance remains pending. |
| **Procurement Contract Analysis** | Private local full-stack and data engineering prototype with cited evidence review, CAD cost calculator, and a documented clause-detection benchmark on 84 contracts; production validation remains incomplete. |

Two supplementary Streamlit projects—Real Estate Price Estimation and Loan Eligibility Prediction—offer accessible demonstrations of model-driven interfaces. The Amazon project is intentionally not displayed on the portfolio.

## Run locally

Requires Python 3.10+.

```bash
python -m venv .venv
# Activate the virtual environment for your shell
python -m pip install -r requirements.txt
python -m flask --app 'app:create_app()' run --debug
```

For Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Hosting

**Recommended: static export + Cloudflare Pages.** This portfolio has no database, authentication, or server-side form handling, so keeping a Flask process awake is unnecessary.

```bash
python -m pip install -r requirements.txt
python export_static.py
```

This generates `dist/index.html` and `dist/static/`. For Cloudflare Pages, connect this repository and configure:

- **Build command:** `python -m pip install -r requirements.txt && python export_static.py`
- **Output directory:** `dist`
- **Root directory:** repository root

Cloudflare Pages can then deploy the static content without Render's free-service cold starts. Do not switch the public portfolio URL until the new build and its assets work correctly. The original Flask deployment remains supported.

**Existing Render deployment:**

- Build: `python -m pip install -r requirements.txt`
- Start: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`

## Validation

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py view.py wsgi.py export_static.py tests
python export_static.py
```

The integration tests cover curated project order, photo assets, anchors, contact destinations, and legacy redirect behavior.

## Disclosure

The hospital dataset is synthetic, the procurement application is a private prototype undergoing validation, and air quality evaluation metrics are retrospective. Public examples are not represented as production-grade services.

Licensed under [MIT](LICENSE).
