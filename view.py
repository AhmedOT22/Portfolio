from flask import Blueprint, render_template
from flask import request, redirect, flash, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
	projects = [
		{
			"title": "Loan Eligibility Prediction",
			"image": "images/loan.png",
			"description": (
				"A real-time ML web app that predicts loan approval likelihood using Random Forest and Logistic Regression." 
                                 "Features interactive user input, dynamic model switching, and a visual gauge for instant, explainable feedback."
			),
			"skills": "Python, Scikit-learn, Streamlit, Pandas, Matplotlib",
			"link": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction/tree/main"
		},
		{
			"title": "Real Estate Price Prediction",
			"image": "images/realestate.png",
			"description": (
				"Predicts house prices based on property features using regression models. Built with Streamlit and includes real-time user input,"
                                 "data preprocessing, and market-adjusted pricing insights."
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
                                 "Optimizes segmentation using the Elbow Method and Silhouette Score, and presents results in a simple dashboard."
			),
			"skills": "Python, Scikit-learn, Matplotlib, Streamlit",
			"link": "https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Mall-Customers-Segmentation"
		},
		{
			"title": "UCLA Admission Prediction",
			"image": "images/ucla.png",
			"description": (
				"Unsupervised ML app that clusters mall customers by income and spending behavior using K-Means."
                                 "Optimizes segmentation using the Elbow Method and Silhouette Score, and presents results in a simple dashboard."
			),
			"skills": "Python, Scikit-learn, Streamlit",
			"link": "https://ucla-admission-prediction-yuozl4rzy3dryn2gkuspwc.streamlit.app/",
			"github": "https://github.com/AhmedOT22/UCLA-Admission-Prediction"
		},
		{
			"title": "Air Quality Forecasting",
			"description": (
				"Forecasts AQI trends using historical pollutant and weather data across seven predictive models." 
                                 "Built an ETL pipeline and integrated time-series forecasting for environmental monitoring and planning."
			),
			"skills": "Alteryx, Python, Pandas, Power BI, ETS",
			#"link": "https://example.com/air-quality-demo",
			"github": "https://github.com/AhmedOT22/Air-Quality-Forecasting"
		},
		{
			"title": "Stock Watcher",
			"description": (
				"Fetches live market data via API and visualizes key financial metrics like SMA, EMA, ATR, and returns." 
                                 "Designed to support informed investment decisions with trend analysis and portfolio breakdowns."
			),
			"skills": "Python, Pandas, NumPy, Seaborn, Matplotlib",
			#"link": "https://example.com/stock-demo",
			"github": "https://github.com/AhmedOT22/Stock-Watcher-Notebook"
		}
	]

	return render_template("index.html", projects=projects)

@main.route('/submit', methods=['POST'])
def submit():
	first_name = request.form.get('first_name')
	last_name = request.form.get('last_name')
	email = request.form.get('email')
	message = request.form.get('message')

	# Later save to a file, send to email, etc.
	print("New Contact Message:")
	print(f"From: {first_name} {last_name}")
	print(f"Email: {email}")
	print(f"Message: {message}")

	# Flash message (optional) and redirect
	flash('Thanks for your message!', 'success')
	return redirect(url_for('main.home'))
