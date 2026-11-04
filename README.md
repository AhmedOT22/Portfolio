# Ahmed Ouazzani — Data Analytics, Engineering & Applied AI Portfolio

Flask-based portfolio for my business intelligence, data engineering, forecasting, and applied AI work. Based in Ottawa, Canada; working in English, French and Arabic.

[Live portfolio](https://portfolio-9o9p.onrender.com/) · [GitHub profile](https://github.com/AhmedOT22) · [LinkedIn](https://www.linkedin.com/in/ahmed-ouazzani-5b078b205/)

## Featured projects

| Project | Evidence and scope |
| --- | --- |
| **Toronto Air Quality Forecasting** | Locked multi-source ETL, chronological Ridge evaluation, automated forecasts and monitoring. On the 2025 retrospective evaluation, day-one and day-seven MAE decreased by 27.0% and 25.7% against persistence. AQI is reconstructed for a single station, not an official Toronto/AQHI forecast. |
| **Hospital Insights Dashboard** | SQL Server model, reproducible synthetic data, five-page Power BI source and automated SQL metric reconciliation. Power BI Desktop acceptance remains pending. |
| **Procurement Contract Analysis** | Private local React/FastAPI text-PDF evidence review and separate research coverage warehouse. Optional local LLM interpretations require manual review; real-world extraction quality and pricing logic have not been validated. |

The homepage also links to educational and exploratory projects: Loan Eligibility Prediction, Amazon Sales Analysis, Real Estate Price Estimation, Mall Customer Segmentation, Graduate Admission Classification and Stock Watcher.

## Local setup

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app 'app:create_app()' run --debug
```

Windows PowerShell activation: `.venv\\Scripts\\Activate.ps1`.

## Deployment

Render web service:
- Build: `python -m pip install -r requirements.txt`
- Start: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`

`wsgi.py` exposes the Flask application. The app renders repository-verified project descriptions through `view.py` and `templates/index.html`; styles live in `static/css/style.css`.

## Validation

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py view.py wsgi.py tests
python -m pip check
node --check static/js/main.js
```

Integration checks cover homepage rendering, project category filters, static assets, links and WSGI behavior. JavaScript progressively enhances filters; all projects remain readable when JavaScript is disabled.

## Scope and disclosure

Project descriptions are deliberately specific to implemented work. Historical backtests are not prospective operational skill, synthetic hospital data are not clinical evidence, and the procurement prototype is not a validated autonomous contract-analysis service. The private procurement repository is not publicly linked.

The site uses the [MIT License](LICENSE) and provides email/LinkedIn contact links, not a functioning contact-message backend.
