from flask import Blueprint, render_template
from flask import request, redirect, flash, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
	projects = [
		{
			"title": "Loan Eligibility Prediction",
			"description": (
				"A real-time machine learning web app that predicts loan approval likelihood based on user inputs. "
				"Implements Random Forest and Logistic Regression models, featuring an interactive form and dynamic gauge visualization built with Streamlit."
			),
			"skills": "Python, Scikit-learn, Streamlit, Pandas, Matplotlib",
			"link": "https://loan-eligibility-prediction-djdstcprojdapfxugpdqwi.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Loan-Eligibility-Prediction/tree/main"
		},
		{
			"title": "Real Estate Price Prediction",
			"description": (
				"A regression-based machine learning app for predicting house prices based on property attributes. "
				"Includes data preprocessing, EDA visualizations, and a Streamlit-based UI for interactive predictions."
			),
			"skills": "Python, Scikit-learn, Pandas, Streamlit, Matplotlib",
			"link": "https://real-estate-price-estimation-utm6wfs9dykdimegfmmwrw.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Real-Estate-Price-Estimation"
		},
		{
			"title": "Mall Customer Segmentation",
			"description": (
				"A clustering project that segments mall customers by income and spending score using the K-Means algorithm. "
				"Optimal cluster count determined using the Elbow Method and Silhouette Score. Includes a simple interactive dashboard in Streamlit."
			),
			"skills": "Python, Scikit-learn, Matplotlib, Streamlit",
			"link": "https://mall-customers-segmentation-a5kdbi8xu3bps7vxaf5am2.streamlit.app/",
			"github": "https://github.com/AhmedOT22/Mall-Customers-Segmentation"
		},
		{
			"title": "UCLA Admission Prediction",
			"description": (
				"A deep learning project that predicts graduate admission chances at UCLA based on GPA, GRE, TOEFL, SOP, and LOR scores. "
				"The project includes explainability using SHAP values, an interactive input form, and visual feedback via Streamlit."
			),
			"skills": "Python, Scikit-learn, Streamlit",
			"link": "https://ucla-admission-prediction-yuozl4rzy3dryn2gkuspwc.streamlit.app/",
			"github": "https://github.com/AhmedOT22/UCLA-Admission-Prediction"
		},
		{
			"title": "Air Quality Forecasting",
			"description": (
				"Developed an ETL pipeline to process historical weather and air quality data. "
				"Built predictive models using Exponential Smoothing for air quality forecasting. "
				"Created interactive visualizations to analyze trends."
			),
			"skills": "Alteryx, Python, Pandas, Power BI, ETS",
			#"link": "https://example.com/air-quality-demo",
			"github": "https://github.com/AhmedOT22/Air-Quality-Forecasting"
		},
		{
			"title": "Stock Watcher",
			"description": (
				"Built a real-time stock analysis tool that fetches financial data via API. "
				"Implemented key financial metrics and visualized market trends."
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

