# Ahmed Ouazzani — Data Portfolio

A Flask website for my business intelligence, data analysis, and applied machine learning projects. I am based in Ottawa and work in English and French.

[Portfolio website](https://portfolio-9o9p.onrender.com/) · [LinkedIn](https://www.linkedin.com/in/ahmed-ouazzani-5b078b205/) · [Email](mailto:ahmedouazzani225@gmail.com)

## Projects

The website links to these projects. Each repository contains its own code and project documentation.

| Project | Focus | Preview |
| --- | --- | --- |
| [Air Quality Forecasting](https://github.com/AhmedOT22/Air-Quality-Forecasting) | Toronto air-quality data preparation and forecasting model comparisons | [Notebook](https://github.com/AhmedOT22/Air-Quality-Forecasting/blob/main/AirQuality.ipynb) |
| [Loan Eligibility Prediction](https://github.com/AhmedOT22/Loan-Eligibility-Prediction) | Classification with Logistic Regression and Random Forest | [Streamlit app](https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/) |
| [Real Estate Price Estimation](https://github.com/AhmedOT22/Real-Estate-Price-Estimation) | Regression model comparison and property-price estimation | [Streamlit app](https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/) |
| [Mall Customers Segmentation](https://github.com/AhmedOT22/Mall-Customers-Segmentation) | Customer clustering with KMeans | [Streamlit app](https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/) |
| [UCLA Admission Prediction](https://github.com/AhmedOT22/UCLA-Admission-Prediction) | Educational classification exercise using an MLP | [Streamlit app](https://ucla-admission-prediction-yuozl4rzy3dryn2gkuspwc.streamlit.app/) |
| [Stock Watcher](https://github.com/AhmedOT22/Stock-Watcher-Notebook) | Stock-data retrieval, technical indicators, and portfolio visualization | [Notebook](https://github.com/AhmedOT22/Stock-Watcher-Notebook/blob/main/notebook/main.ipynb) |

Another BI project is [Hospital Insights Dashboard](https://github.com/AhmedOT22/Hospital-Insights-Dashboard), which combines a relational SQL schema with Power BI reports and includes dashboard screenshots.

The prediction apps are portfolio demonstrations. Dataset scope, evaluation results, and limitations belong in the individual project documentation.

## Run locally

Use Python 3.10 or newer. From a terminal:

```bash
git clone https://github.com/AhmedOT22/Portfolio.git
cd Portfolio
python -m venv .venv
```

Activate the virtual environment:

- macOS/Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

Then install dependencies and start Flask:

```bash
python -m pip install -r requirements.txt
python -m flask --app 'app:create_app()' run --debug
```

Open http://127.0.0.1:5000. Debug mode is for local development.

## Deployment

The listed website is hosted on Render. To deploy the app as a Python web service, use:

- **Build command:** `python -m pip install -r requirements.txt`
- **Start command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT`

`wsgi.py` exposes the Flask application created by `create_app()`.

## Project structure

```text
app.py                  Flask application factory
view.py                 Homepage route and project entries
wsgi.py                 Gunicorn entry point
templates/base.html     Navigation, shared layout, and footer
templates/index.html    Introduction, filterable projects, about, and contact
static/css/style.css    Responsive design tokens, layouts, and accessibility styles
static/js/main.js       Progressive project filtering
tests/                  Homepage and WSGI integration checks
static/images/          Profile photo and project previews
```

## Updating the website

Edit the project entries in `view.py` to change titles, descriptions, skills, and links. Add preview images under `static/images/`; image paths in project entries are relative to `static/`.

Contact uses email and LinkedIn links. The website does not deliver contact-form messages. The legacy `POST /submit` route redirects to the contact section without processing submitted fields.

## License

[MIT](LICENSE)

## UI and accessibility

The interface uses a white and navy palette with restrained teal accents, a compact
introduction, consistent project cards, and direct contact actions. System fonts
and a local favicon keep the page independent of third-party font/icon CDNs.

- Project filters show machine learning or data analysis work and announce the result count.
- Without JavaScript, every project remains visible and navigation/contact links still work.
- Keyboard users get a skip link, visible focus indicators, and native filter buttons.
- Layouts adapt to phones and tablets; motion follows the reduced-motion preference.
- External project links identify their destination and open safely in a new tab.

Project categories live in each entry's `category` field in `view.py`; keep them
aligned with the filter labels in `templates/index.html`. Colors and layout tokens
are defined at the top of `static/css/style.css`.

## Checks

With the virtual environment activated:

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py view.py wsgi.py tests
python -m pip check
node --check static/js/main.js
```

Node is optional for development and is used here only to check JavaScript syntax;
Flask serves the site directly with no frontend build step. Integration tests cover
homepage rendering, the production WSGI entry point, local assets, anchor targets,
project category consistency, external-link attributes, and the legacy contact redirect.
