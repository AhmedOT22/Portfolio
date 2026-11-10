from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Curated public work; limitations are stated explicitly."""
    featured = [
        {
            "slug": "hospital",
            "title": "Hospital Insights Dashboard",
            "category": "Business intelligence",
            "number": "01",
            "description": "Healthcare reporting built around a relational SQL Server model, data-quality checks, and Power BI report design.",
            "detail": "Eleven linked tables and reproducible synthetic data. Desktop visual and DAX acceptance checks remain pending.",
            "skills": ["SQL Server", "Power BI", "DAX", "Data Modeling"],
            "github": "https://github.com/AhmedOT22/Hospital-Insights-Dashboard",
            "status": "Synthetic data · In development",
        },
        {
            "slug": "procurement",
            "title": "Procurement Contract Analysis",
            "category": "Data engineering · Applied AI",
            "number": "02",
            "description": "An evidence-first contract review prototype combining cited PDF findings, human review, and structured data acquisition.",
            "detail": "React/FastAPI interface with a separate PostgreSQL research warehouse. Semantic extraction and pricing have not been validated for release.",
            "skills": ["Python", "PostgreSQL", "ETL", "FastAPI", "React"],
            "github": None,
            "status": "Private prototype · Validation ongoing",
        },
        {
            "slug": "air",
            "title": "Toronto Air Quality Forecasting",
            "category": "Data science · Forecasting",
            "number": "03",
            "description": "An end-to-end data pipeline for reconstructed station-level AQI, with chronological forecasting evaluation and monitoring.",
            "detail": "On a retrospective 2025 evaluation, day-ahead MAE improved 27% against a persistence baseline; not a live accuracy guarantee.",
            "skills": ["Python", "ETL", "scikit-learn", "Time Series"],
            "github": "https://github.com/AhmedOT22/Air-Quality-Forecasting",
            "status": "Retrospective model evaluation",
        },
    ]

    additional = [
        {
            "title": "Loan Eligibility Prediction",
            "category": "Classification · Streamlit",
            "description": "A reproducible classification workflow with preprocessing, baseline comparison, and interactive inference.",
            "image": "images/loan.png",
            "github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction",
            "demo": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
        },
        {
            "title": "Real Estate Price Estimation",
            "category": "Regression · Streamlit",
            "description": "Property-price modeling with multiple regression approaches and a deployed demonstration.",
            "image": "images/realestate.png",
            "github": "https://github.com/AhmedOT22/Real-Estate-Price-Estimation",
            "demo": "https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/",
        },
        {
            "title": "Mall Customer Segmentation",
            "category": "Clustering · Streamlit",
            "description": "K-means segmentation with exploratory diagnostics and illustrative customer personas.",
            "image": "images/mall.png",
            "github": "https://github.com/AhmedOT22/Mall-Customers-Segmentation",
            "demo": "https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/",
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
