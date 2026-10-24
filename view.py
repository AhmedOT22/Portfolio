from datetime import datetime
from flask import Blueprint, render_template
from flask import redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
	projects = [
		{
			"title": "Air Quality Forecasting",
            "description": "Explores Toronto pollutant and weather records, with a separate past-only forecasting workflow and persistence baselines.",
            "skills": "Python, Pandas, Scikit-learn, Time Series",
            "link": "https://github.com/AhmedOT22/Air-Quality-Forecasting",
            "link_label": "Read Analysis",
            "github": "https://github.com/AhmedOT22/Air-Quality-Forecasting"

		},
  
		{
			"title": "Loan Eligibility Prediction",
			"image": "images/loan.png",
			"description": (
				"An educational loan classification app using Random Forest and Logistic Regression. " 
                "Includes a separate train-only preprocessing pipeline and baseline evaluation."
			),
			"skills": "Python, Scikit-learn, Streamlit, Pandas, Matplotlib",
			"link": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction/tree/main"
		},
  
		{
			"title": "Real Estate Price Estimation",
			"image": "images/realestate.png",
			"description": (
				"Compares regression models on historical property records. Includes a Streamlit interface, "
                "reproducible evaluation, and a median-price baseline."
			),
			"skills": "Python, Scikit-learn, Pandas, Streamlit, Matplotlib",
			"link": "https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Real-Estate-Price-Estimation"
		},
  
		{
			"title": "Mall Customer Segmentation",
			"image": "images/mall.png",
			"description": (
				"Unsupervised ML app that clusters mall customers by income and spending behavior using K-Means." 
                "Includes elbow/silhouette diagnostics and illustrative persona labels."
			),
			"skills": "Python, Scikit-learn, Matplotlib, Streamlit",
			"link": "https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Mall-Customers-Segmentation"
		},
  
		{
			"title": "Graduate Admission Classification",
			"image": "images/ucla.png",
			"description": (
				"Classifies a dataset-derived admission-chance threshold using an MLP. " 
    			"Includes preprocessing, feature alignment, and a Streamlit demonstration."
			),
			"skills": "Python, Scikit-learn, Streamlit",
			"link": "https://ucla-admission-prediction-yuozl4rzy3dryn2gkuspwc.streamlit.app/",
			"github": "https://github.com/AhmedOT22/UCLA-Admission-Prediction"
		},
		
		{
			"title": "Stock Watcher",
			"description": (
				"Retrieves market data via API and visualizes key financial metrics like SMA, EMA, ATR, and returns." 
                "Includes historical charting and local portfolio/watchlist management."
			),
			"skills": "Python, Pandas, NumPy, Matplotlib",
            "link_label": "View Notebook",
			"link": "https://github.com/AhmedOT22/Stock-Watcher-Notebook/blob/main/notebook/main.ipynb",
			"github": "https://github.com/AhmedOT22/Stock-Watcher-Notebook"
		}
	]

	return render_template("index.html", projects=projects, current_year=datetime.now().year)

@main.route('/submit', methods=['POST'])
def submit():
	# Preserve old form links without accepting messages that cannot be delivered.
	return redirect(url_for('main.home', _anchor='contact'), code=303)
