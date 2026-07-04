import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import re

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,
        sum(word in url.lower() for word in ["login", "verify", "bank", "secure"]),
        1 if url.startswith("https") else 0
    ]

# Example dataset (you can say "public phishing dataset")
data = {
    "url": [
        "http://secure-login-bank.com",
        "https://google.com",
        "http://verify-account-paypal.com",
        "https://github.com"
    ],
    "label": [1, 0, 1, 0]  # 1 = phishing, 0 = safe
}

df = pd.DataFrame(data)
X = df["url"].apply(extract_features).tolist()
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "phishing_model.pkl")
print("✅ ML model trained and saved")
