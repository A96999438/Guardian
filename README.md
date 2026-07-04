# 🛡️ Guardian – AI Powered Gmail Monitoring & Phishing Detection System

Guardian is an AI-powered Gmail monitoring system that automatically scans incoming emails, extracts URLs, detects phishing attempts using Machine Learning and Threat Intelligence APIs, and alerts users about potentially malicious links.

The system continuously monitors a Gmail inbox using OAuth 2.0 authentication and classifies suspicious URLs into different risk levels to improve email security.

---

# 📌 Features

- 🔐 Secure Gmail Authentication using OAuth 2.0
- 📧 Automatic Gmail Inbox Monitoring
- 🔗 Automatic URL Extraction from Emails
- 🤖 Machine Learning Based Phishing Detection
- 🌐 Google Safe Browsing API Integration
- ⚠️ Risk Classification (Low / Medium / High)
- 🚨 Real-Time Alert Generation
- 💾 Secure Scan History Storage in MongoDB Atlas
- ⏱️ Continuous Background Monitoring using APScheduler

---

# 🏗️ System Architecture

```
                  Gmail Account
                        │
                 OAuth 2.0 Login
                        │
                        ▼
                Gmail Monitoring
                        │
                        ▼
                URL Extraction
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
 Machine Learning Model      Google Safe Browsing API
         │                             │
         └──────────────┬──────────────┘
                        ▼
                Risk Classification
          (Low / Medium / High Risk)
                        │
                        ▼
              Store Results in MongoDB
                        │
                        ▼
                 Generate Alerts
```

---

# 🚀 Technologies Used

## Programming Language

- Python 3.11+

## Backend

- FastAPI

## Database

- MongoDB Atlas

## Authentication

- Google OAuth 2.0

## Scheduler

- APScheduler

## APIs

- Gmail API
- Google Safe Browsing API

## Machine Learning

- Scikit-learn

## Libraries

- FastAPI
- httpx
- python-dotenv
- APScheduler
- Joblib
- PyMongo

---

# 📂 Project Workflow

1. User authenticates Gmail using OAuth 2.0.
2. Guardian continuously monitors the inbox.
3. URLs are extracted from incoming emails.
4. URLs are analyzed using:
   - Machine Learning Model
   - Google Safe Browsing API
   - Rule-Based Detection
5. URLs are classified into:
   - Low Risk
   - Medium Risk
   - High Risk
6. Scan results are stored in MongoDB Atlas.
7. Alerts are generated for suspicious or phishing links.

---

# 🎯 Objectives

- Automate Gmail inbox monitoring
- Detect phishing URLs automatically
- Reduce phishing attacks
- Generate real-time security alerts
- Store historical scan reports
- Improve email security using AI

---

# 🧠 Machine Learning

The project uses a Machine Learning model developed with **Scikit-learn** to classify URLs as:

- Legitimate
- Suspicious
- Phishing

The model works together with Google Safe Browsing API and rule-based checks to improve detection accuracy.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/guardian-phishing-detector.git
```

```bash
cd guardian-phishing-detector
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file and add:

```env
MONGODB_URI=

GOOGLE_CLIENT_ID=

GOOGLE_CLIENT_SECRET=

GOOGLE_SAFE_BROWSING_API_KEY=

SECRET_KEY=
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

---

# 📊 Risk Levels

| Risk | Meaning |
|------|---------|
| 🟢 Low | Safe URL |
| 🟡 Medium | Suspicious URL |
| 🔴 High | Phishing / Malicious URL |

---

# 📁 Project Structure

```
Guardian/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── scheduler/
│   ├── utils/
│
├── ml_model/
│
├── requirements.txt
├── main.py
├── .env
└── README.md
```

---

# 📸 Sample Output

✔ Gmail Connected Successfully

✔ Emails Monitored Automatically

✔ URLs Extracted Successfully

✔ Risk Analysis Completed

✔ Phishing Links Detected

✔ Alerts Generated

✔ Scan Stored in MongoDB Atlas

---

# 💻 Hardware Requirements

- Intel Core i5 or Higher
- 8 GB RAM
- 256 GB Storage
- Internet Connection

---

# 🖥️ Software Requirements

- Windows / Linux / macOS
- Python 3.11+
- Visual Studio Code
- MongoDB Atlas
- Gmail API
- Google Safe Browsing API

---

# 🚧 Challenges Faced

- Implementing secure Gmail OAuth authentication
- Reducing false positives during phishing detection
- Continuous background monitoring
- Secure cloud database integration
- Combining ML prediction with threat intelligence APIs

---

# 🔮 Future Improvements

- Web Dashboard
- Email Notifications
- SMS Alerts
- Weekly Security Reports
- Support for Outlook and Yahoo Mail
- Cloud Deployment
- Deep Learning Based Detection
- Browser Extension
- User Analytics Dashboard

---

# 📈 Results

- Successfully connected Gmail using OAuth 2.0
- Automatically monitored incoming emails
- Extracted URLs from emails
- Detected phishing links using Machine Learning
- Classified URLs based on risk
- Generated real-time alerts
- Stored all scan records securely in MongoDB Atlas

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is developed for educational and research purposes.

---

# 👨‍💻 Developer

**Aman Aslam Patel**

Artificial Intelligence & Data Science Student

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

It motivates further development and improvements.
