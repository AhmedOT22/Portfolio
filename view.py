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
			"link": "https://example.com/loan-demo",
			"github": "https://github.com/yourusername/loan-eligibility-app"
		},
		{
			"title": "Real Estate Price Prediction",
			"description": (
				"A regression-based machine learning app for predicting house prices based on property attributes. "
				"Includes data preprocessing, EDA visualizations, and a Streamlit-based UI for interactive predictions."
			),
			"skills": "Python, Scikit-learn, Pandas, Streamlit, Matplotlib",
			"link": "https://example.com/real-estate",
			"github": "https://github.com/yourusername/real-estate-price-predictor"
		},
		{
			"title": "Mall Customer Segmentation",
			"description": (
				"A clustering project that segments mall customers by income and spending score using the K-Means algorithm. "
				"Optimal cluster count determined using the Elbow Method and Silhouette Score. Includes a simple interactive dashboard in Streamlit."
			),
			"skills": "Python, Scikit-learn, Matplotlib, Streamlit",
			"link": "https://example.com/mall-segmentation",
			"github": "https://github.com/yourusername/mall-customer-segmentation"
		},
		{
			"title": "UCLA Admission Prediction",
			"description": (
				"A deep learning project that predicts graduate admission chances at UCLA based on GPA, GRE, TOEFL, SOP, and LOR scores. "
				"The project includes explainability using SHAP values, an interactive input form, and visual feedback via Streamlit."
			),
			"skills": "Python, TensorFlow, Keras, SHAP, Streamlit",
			"link": "https://example.com/ucla-admissions",
			"github": "https://github.com/yourusername/ucla-admission-predictor"
		},
		{
			"title": "Air Quality Forecasting",
			"description": (
				"Developed an ETL pipeline to process historical weather and air quality data. "
				"Built predictive models using Exponential Smoothing for air quality forecasting. "
				"Created interactive visualizations to analyze trends."
			),
			"skills": "Alteryx, Python, Pandas, Power BI, ETS",
			"link": "https://example.com/air-quality-demo",
			"github": "https://github.com/AhmedOT22/Air-Quality-Forecasting"
		},
		{
			"title": "Stock Watcher",
			"description": (
				"Built a real-time stock analysis tool that fetches financial data via API. "
				"Implemented key financial metrics and visualized market trends."
			),
			"skills": "Python, Pandas, NumPy, Seaborn, Matplotlib",
			"link": "https://example.com/stock-demo",
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

