from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Curated public work; limitations are stated explicitly."""
    # Show evidence-backed work first. Educational demos are secondary.
    featured = [
        {
            "slug": "air",
            "title": "Toronto Air Quality Forecasting",
            "category": "Data Science & Data Engineering",
            "number": "01",
            "image": "https://raw.githubusercontent.com/AhmedOT22/Air-Quality-Forecasting/main/docs/images/dashboard.png",
            "image_alt": "Actual Toronto air quality dashboard showing observed and forecast AQI",
            "metric": "27% lower MAE",
            "metric_note": "2025 one-day holdout vs. persistence",
            "description": "Built a reproducible data pipeline and forecasting system using public pollution and weather observations.",
            "detail": "Validated historical sources, compared time-series models without look-ahead leakage, and automated forecast publication and monitoring.",
            "evidence": [
                "Decision: use a simple Ridge model after comparison with stronger nonlinear alternatives.",
                "2025 holdout: day-one MAE 10.84 vs. 14.85 for persistence; 27% lower error.",
                "Limit: forecasts are for a reconstructed Toronto West AQI; sudden smoke-related spikes remain difficult."
            ],
            "skills": ["Python", "ETL", "Forecasting", "scikit-learn", "GitHub Actions"],
            "github": "https://github.com/AhmedOT22/Air-Quality-Forecasting",
            "status": "Public source · Retrospective evaluation",
        },
        {
            "slug": "hospital",
            "title": "Hospital Insights Dashboard",
            "category": "Business Intelligence & Analytics",
            "number": "02",
            "image": "https://raw.githubusercontent.com/AhmedOT22/Hospital-Insights-Dashboard/main/screenshots/performance.png",
            "image_alt": "Actual Power BI hospital dashboard report preview",
            "metric": "5 report pages",
            "metric_note": "11-table SQL Server semantic model",
            "description": "Designed a healthcare reporting demonstration covering appointments, departments, doctors, patients and operational performance.",
            "detail": "Modeled relational records, built repeatable synthetic test data, and documented metric definitions and reconciliation checks.",
            "evidence": [
                "Business purpose: give operational stakeholders clear views of activity, cancellations, workloads and payments.",
                "Implementation: SQL Server model, DAX measures and five Power BI report pages.",
                "Limit: all records are synthetic; Power BI Desktop visual and DAX acceptance still require verification."
            ],
            "skills": ["SQL Server", "Power BI", "DAX", "Data Modeling"],
            "github": "https://github.com/AhmedOT22/Hospital-Insights-Dashboard",
            "status": "Synthetic data · Final validation pending",
        },
        {
            "slug": "procurement",
            "title": "Procurement Contract Analysis",
            "category": "Applied AI & Software Engineering",
            "number": "03",
            "image": None,
            "image_alt": None,
            "metric": "84 test contracts",
            "metric_note": "Offline CUAD clause-detection benchmark",
            "description": "Developed a local evidence-based contract review tool with cited findings, reviewer corrections and a CAD scenario calculator.",
            "detail": "Uses React, FastAPI, a constrained evidence model and a separate procurement research warehouse.",
            "evidence": [
                "Review workflow: exact source quotations and a traceable correction history rather than unsupported AI-generated answers.",
                "Evaluation: rule and classifier approaches benchmarked against 84 held-out CUAD contracts for eight clause types.",
                "Limit: private local prototype; benchmarked clause detection is not yet integrated with the review interface."
            ],
            "skills": ["React", "FastAPI", "Python", "PostgreSQL", "Evaluation"],
            "github": None,
            "status": "Private prototype · Demonstration on request",
        },
    ]

    additional = [
        {
            "title": "Real Estate Price Estimation",
            "category": "Regression · Streamlit",
            "description": "Compared regression models and delivered a practical interface for exploring property-price estimates.",
            "image": "images/realestate.png",
            "github": "https://github.com/AhmedOT22/Real-Estate-Price-Estimation",
            "demo": "https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/",
        },
        {
            "title": "Loan Eligibility Prediction",
            "category": "Classification · Streamlit",
            "description": "An educational binary classification demo with preprocessing, baseline evaluation and interactive inference; not a lending decision system.",
            "image": "images/loan.png",
            "github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction",
            "demo": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
        },
    ]
    return render_template(
        "index.html",
        featured=featured,
        additional=additional,
        current_year=datetime.now().year,
    )


@main.route("/submit", methods=["POST"])
def submit():
    """Legacy form endpoint: no messages are stored or sent."""
    return redirect(url_for("main.home", _anchor="contact"), code=303)
