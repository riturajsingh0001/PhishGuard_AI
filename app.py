import streamlit as st
import pandas as pd
import joblib
from urllib.parse import urlparse
import re

# --- STEP 1: LOAD MODEL ---
# We load these once at the start
model = joblib.load('phishguard_model.pkl')
expected_features = joblib.load('model_features.pkl')

# --- STEP 2: FEATURE EXTRACTION FUNCTION ---
def extract_url_features(url):
    features = {}
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['has_https'] = 1 if url.startswith('https') else 0
    features['has_ip'] = 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url) else 0
    features['num_subdirs'] = urlparse(url).path.count('/')
    features['num_params'] = urlparse(url).query.count('&')
    suspicious_words = ['login', 'verify', 'bank', 'secure', 'update', 'account']
    features['suspicious_words'] = 1 if any(word in url.lower() for word in suspicious_words) else 0
    features['special_char_count'] = len(re.findall(r'[@\-_?=]', url))
    features['digits_count'] = sum(c.isdigit() for c in url)
    return features

# --- STEP 3: STREAMLIT UI ---
st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")
st.title("🛡️ PhishGuard AI")
st.markdown("Enter a URL below to check if it's safe or a phishing threat.")

# User Input
url_input = st.text_input("Enter URL to scan:", placeholder="https://example.com")

if st.button("Scan URL"):
    if url_input:
        # Extract and Predict
        raw_feat = extract_url_features(url_input)
        df_input = pd.DataFrame([raw_feat])
        
        # Align features
        for col in expected_features:
            if col not in df_input.columns:
                df_input[col] = 0
        
        prediction = model.predict(df_input[expected_features])
        prob = model.predict_proba(df_input[expected_features])[0]
        risk_score = prob[1] if len(prob) > 1 else (1.0 if prediction[0] == 1 else 0.0)

        # Display Results
        if prediction[0] == 1:
            st.error(f"🚨 ALERT: This URL is highly suspicious! (Risk: {risk_score*100:.1f}%)")
        else:
            st.success(f"✅ SAFE: This URL appears to be legitimate. (Risk: {risk_score*100:.1f}%)")
    else:
        st.warning("Please enter a URL first.")