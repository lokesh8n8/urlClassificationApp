from urllib.parse import urlparse, parse_qs
import pandas as pd
import re
import shap
import matplotlib.pyplot as plt
import pickle
import streamlit as st


BAD_WORDS = {
    "sleep", "uid", "select", "waitfor", "delay", 
    "system", "union", "order by", "group by", 
    "admin", "drop", "script"
}

def extract_url_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parse_qs(parsed_url.query)

    simulated_body = '&'.join(f"{key}={value[0]}" for key, value in query.items())
    body_length = len(simulated_body)

    features = {
        'single_q': url.count("'"),
        'double_q': url.count('"'),
        'braces': url.count('{') + url.count('}'),
        'spaces': url.count(' '),
        'angle_brackets': url.count('<') + url.count('>'),
        'path_length': len(path),
        'body_length': body_length,
        'badwords_count': sum(1 for word in BAD_WORDS if word in path)
    }

    features['badwords_count'] += sum(1 for word in BAD_WORDS if any(word in v for v in query.values()))

    return features


@st.cache_resource 
def load_model():
    with open("models/trained_model_v2.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
st.title("URL Legitimacy Checker")
user_url = st.text_input("Enter a URL to analyze", "")

if user_url:
    features = extract_url_features(user_url)    
    out = pd.DataFrame([features])
    prediction = model.predict(out)
    prediction_label = "Legit" if prediction == 0 else "Malicious"
    
    st.write(f"Prediction: **{prediction_label}**")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(out)

    st.write("**Feature Contributions:**")
    choosen_instance = out
    shap_values = explainer.shap_values(choosen_instance)
    shap.initjs()
    fig = shap.force_plot(explainer.expected_value[prediction], shap_values[:,:,1], choosen_instance)
    force_plot_html = f"<head>{shap.getjs()}</head><body>{fig.html()}</body>"
    st.components.v1.html(force_plot_html, height=300)

