from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/")
def home():
    # Keep these descriptions synchronized with each project's documented status.
    projects = [
        {
            "title": "Toronto Air Quality Forecasting",
            "category": "Machine learning & AI",
            "description": (
                "Reconstructed station-specific AQI and evaluated one-to-seven-day forecasts "
                "using chronological splits and persistence baselines. The selected Ridge model "
                "reduced 2025 MAE by 27.0% (day 1) and 25.7% (day 7) against persistence. "
                "Includes validated ETL, scheduled updates and monitoring."
            ),
            "skills": "Python, scikit-learn, ETL, Time Series, GitHub Actions",
            "link": "https://github.com/AhmedOT22/Air-Quality-Forecasting",
            "link_label": "View project",
            "github": "https://github.com/AhmedOT22/Air-Quality-Forecasting",
            "preview": "Validated data → Ridge forecasts → monitoring",
            "status": "Retrospective model results; public dashboard hosting pending",
        },
        {
            "title": "Hospital Insights Dashboard",
            "category": "Business intelligence",
            "description": (
                "SQL Server and Power BI reporting project with eleven linked tables, "
                "five report pages and reproducible synthetic data. Automated SQL, "
                "data-quality and metric reconciliation checks support the design."
            ),
            "skills": "SQL Server, Power BI, DAX, Data Modeling, Python",
            "link": "https://github.com/AhmedOT22/Hospital-Insights-Dashboard",
            "link_label": "View project",
            "github": "https://github.com/AhmedOT22/Hospital-Insights-Dashboard",
            "preview": "SQL Server → semantic model → Power BI",
            "status": "Synthetic data; Power BI Desktop acceptance pending",
        },
        {
            "title": "Procurement Contract Analysis",
            "category": "Data engineering",
            "description": (
                "Local React/FastAPI prototype for text-PDF review with exact evidence "
                "citations, manual corrections and exportable reports. Separate source "
                "acquisition, Parquet ETL and PostgreSQL research-coverage warehouse; "
                "optional local LLM findings require human verification."
            ),
            "skills": "Python, PostgreSQL, Parquet, FastAPI, React, LLM Evaluation",
            "preview": "Document evidence → review → research warehouse",
            "status": "Private prototype; AI extraction and pricing are not validated for release",
        },
        {
            "title": "Loan Eligibility Prediction",
            "category": "Machine learning & AI",
            "image": "images/loan.png",
            "description": (
                "Educational classification with Logistic Regression and Random Forest, "
                "train-only preprocessing, repeated cross-validation, a majority-class "
                "baseline and versioned inference artifacts."
            ),
            "skills": "Python, scikit-learn, Classification, Streamlit",
            "link": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
            "link_label": "View demo",
            "github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction",
            "status": "Educational demo; not a lending decision system",
        },
        {
            "title": "Amazon Sales Analysis",
            "category": "Business intelligence",
            "description": (
                "Power BI sales reporting supported by exploratory Python notebooks "
                "for data preparation, regression and classification."
            ),
            "skills": "Power BI, Python, Pandas, Sales Analytics",
            "link": "https://github.com/AhmedOT22/Amazon-Sales-Analysis",
            "link_label": "View project",
            "github": "https://github.com/AhmedOT22/Amazon-Sales-Analysis",
            "preview": "Sales data → analysis → reporting",
            "status": "Exploratory portfolio analysis",
        },
        {
            "title": "Real Estate Price Estimation",
            "category": "Machine learning & AI",
            "image": "images/realestate.png",
            "description": (
                "Historical property-price modelling comparing Random Forest, Decision "
                "Tree and linear regression against a median baseline. The latest "
                "evaluation and older serving artifacts are documented separately."
            ),
            "skills": "Python, Regression, scikit-learn, Streamlit",
            "link": "https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/",
            "link_label": "View demo",
            "github": "https://github.com/AhmedOT22/Real-Estate-Price-Estimation",
            "status": "Historical demonstration; not a current property valuation",
        },
        {
            "title": "Mall Customer Segmentation",
            "category": "Machine learning & AI",
            "image": "images/mall.png",
            "description": (
                "Educational K-means customer clustering with exploratory diagnostics "
                "and illustrative, not empirically validated, persona labels."
            ),
            "skills": "Python, K-Means, scikit-learn, Streamlit",
            "link": "https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/",
            "link_label": "View demo",
            "github": "https://github.com/AhmedOT22/Mall-Customers-Segmentation",
            "status": "Educational clustering example",
        },
        {
            "title": "Graduate Admission Classification",
            "category": "Machine learning & AI",
            "image": "images/ucla.png",
            "description": (
                "MLP-based classification of a dataset-derived admission-chance threshold. "
                "The target is not an observed university admission decision."
            ),
            "skills": "Python, MLP, scikit-learn, Streamlit",
            "link": "https://ucla-admission-prediction-yuozl4rzy3dryn2gkuspwc.streamlit.app/",
            "link_label": "View demo",
            "github": "https://github.com/AhmedOT22/UCLA-Admission-Prediction",
            "status": "Educational threshold classification",
        },
        {
            "title": "Stock Watcher",
            "category": "Data engineering",
            "description": (
                "Python notebook and utilities for retrieving historical market prices, "
                "calculating indicators and maintaining a local watchlist."
            ),
            "skills": "Python, Pandas, APIs, Time Series",
            "link": "https://github.com/AhmedOT22/Stock-Watcher-Notebook",
            "link_label": "View project",
            "github": "https://github.com/AhmedOT22/Stock-Watcher-Notebook",
            "preview": "Market API → indicators → local watchlist",
            "status": "Research utility; no trading execution",
        },
    ]
    filters = ["All projects", "Business intelligence", "Data engineering", "Machine learning & AI"]
    return render_template(
        "index.html",
        projects=projects,
        project_filters=filters,
        current_year=datetime.now().year,
    )


@main.route("/submit", methods=["POST"])
def submit():
    # Preserve old form links without accepting messages that cannot be delivered.
    return redirect(url_for("main.home", _anchor="contact"), code=303)
