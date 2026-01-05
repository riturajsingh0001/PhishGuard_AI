# 🛡️ PhishGuard AI: Malicious URL Detector

PhishGuard AI is an advanced machine learning project designed to identify phishing websites in real-time. Unlike traditional signature-based detection, PhishGuard analyzes the **lexical structure** and **anatomy** of a URL to predict its intent with **98% accuracy**.



## 🚀 Key Features
- **Intelligent Feature Extraction:** Analyzes 12+ unique URL attributes including entropy, directory depth, and suspicious keyword patterns.
- **High-Performance Engine:** Powered by a Random Forest Classifier optimized with stratified sampling to handle imbalanced datasets.
- **Interactive UI:** A clean, user-friendly web interface built with Streamlit for instant link scanning.
- **Explainable AI:** Provides a risk probability score so users understand the level of threat.

## 🛠️ The Technical Workflow

### 1. Data Preprocessing & Cleaning
I performed extensive data cleaning on a dataset of 100k+ URLs:
- **Duplicate Removal:** Ensured no data leakage between training and testing sets.
- **Class Balancing:** Used stratified splitting to maintain the ratio of phishing vs. legitimate samples.
- **Feature Scaling:** Standardized numerical inputs for consistent model performance.



### 2. Feature Engineering
The model looks at several "Red Flags" including:
- **Lexical:** URL length, digit count, and special character frequency.
- **Patterns:** Presence of sensitive tokens (e.g., "login", "verify", "secure").
- **Security:** Use of IP addresses instead of domains and absence of HTTPS.

### 3. Model Performance
- **Accuracy:** 98.4%
- **Recall:** Optimized to minimize False Negatives (missing a real threat).
- **F1-Score:** Balanced for reliable real-world usage.

## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/PhishGuard-AI.git](https://github.com/yourusername/PhishGuard-AI.git)
   cd PhishGuard-AI
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**
  ```bash
   streamlit run app.py
   ```
📂 **Project Structure**
app.py: Streamlit web application.

phishguard_model.pkl: The trained Random Forest model.

model_features.pkl: List of feature names for input alignment.

research.ipynb: Initial EDA and model training experiments.

4. The `requirements.txt` File
*(Create a file named `requirements.txt` to ensure others can install your dependencies)*

```text
streamlit
pandas
scikit-learn
joblib
numpy
matplotlib
seaborn
