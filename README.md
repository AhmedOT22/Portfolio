# Ahmed Ouazzani — Data Analyst & BI Developer

Professional portfolio showcasing analytics, business intelligence, data engineering, forecasting, and applied machine learning work.

**[Live portfolio](https://portfolio-9o9p.onrender.com/)** · **[GitHub](https://github.com/AhmedOT22)** · **[LinkedIn](https://www.linkedin.com/in/ahmed-ouazzani-5b078b205/)**

## Featured work

| Project | Evidence & scope |
| --- | --- |
| **Hospital Insights Dashboard** | SQL Server and Power BI reporting, eleven linked tables, validation, and synthetic test data. Desktop DAX/visual acceptance pending. |
| **Procurement Contract Analysis** | Private evidence-first PDF review prototype; React, FastAPI, PostgreSQL research data and acquisition ETL. Automated semantic extraction and pricing not validated for release. |
| **Toronto Air Quality Forecasting** | Validated Python ETL and chronological forecasts. On the retrospective 2025 evaluation, day-one MAE improved 27% against a persistence baseline (not a live guarantee). |

Additional selected work: Loan Eligibility Prediction, Real Estate Price Estimation and Mall Customer Segmentation. Amazon Sales Analysis remains available in its independent repository but is intentionally not featured here.

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
