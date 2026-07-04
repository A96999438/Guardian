import joblib
import re

model = joblib.load("phishing_model.pkl")

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,
        sum(word in url.lower() for word in ["login", "verify", "bank", "secure"]),
        1 if url.startswith("https") else 0
    ]

def ml_predict(url):
    features = [extract_features(url)]
    prediction = model.predict(features)[0]
    return "PHISHING" if prediction == 1 else "SAFE"
