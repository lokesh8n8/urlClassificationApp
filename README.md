# URL Legitimacy Checker

## Overview
The URL Legitimacy Checker is a web application designed to analyze URLs and classify them as either legitimate or malicious. By utilizing machine learning models and network traffic logs, this project aims to enhance web security by identifying potentially harmful URLs.

## Features
- **URL Analysis:** Extracts various features from input URLs to assess their legitimacy.
- **Machine Learning Model:** Trained model for classifying URLs as legitimate or malicious.
- **SHAP (SHapley Additive exPlanations):** Visualizes feature contributions for predictions to improve interpretability.
- **Streamlit Interface:** User-friendly web interface for easy URL input and results display.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- SHAP
- Streamlit
- Regular Expressions

## Installation

1. Clone the repository:
   git clone https://github.com/lokesh8n8/urlClassificationApp.git
   cd url-legitimacy-checker

2. Install the required packages:
    pip install -r requirements.txt

3. Make sure to have a trained model saved as trained_model_v2.pkl in the specified path or update the code to point to your model's location.

4. Usage:
    streamlit run app/app.py

