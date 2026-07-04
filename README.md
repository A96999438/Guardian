# 🛡️ Guardian – AI-Powered Gmail Monitoring & Phishing Detection System

Guardian is an **AI-powered Gmail Monitoring and Phishing Detection System** that leverages **Machine Learning**, **Threat Intelligence APIs**, and **real-time email monitoring** to identify malicious URLs before users interact with them.

The application securely connects to a Gmail account using **Google OAuth 2.0**, continuously monitors incoming emails, extracts embedded URLs, evaluates them using a trained **Machine Learning model**, Google Safe Browsing API, and rule-based security checks, classifies the URLs into different risk levels, and stores scan history in **MongoDB Atlas** for future analysis.

---

# 🚀 Features

- 🔐 Secure Gmail Authentication using Google OAuth 2.0
- 📧 Real-Time Gmail Inbox Monitoring
- 🔗 Automatic URL Extraction from Incoming Emails
- 🤖 AI & Machine Learning Based Phishing Detection
- 🌐 Google Safe Browsing API Integration
- 🛡️ Rule-Based Threat Detection
- ⚠️ URL Risk Classification (Low / Medium / High)
- 🚨 Real-Time Security Alerts
- 💾 Secure Scan History Storage in MongoDB Atlas
- ⏱️ Continuous Background Monitoring using APScheduler
- ⚡ FastAPI Backend for High Performance APIs

---

# 🏗️ System Architecture

```
                   Gmail Account
                         │
                  Google OAuth 2.0
                         │
                         ▼
              Continuous Email Monitoring
                         │
                         ▼
                 URL Extraction Module
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
 Machine Learning Model     Google Safe Browsing API
          │                             │
          └──────────────┬──────────────┘
                         ▼
               Rule-Based Validation
                         │
                         ▼
               Risk Classification
            (Low / Medium / High)
                         │
                         ▼
              Store Results in MongoDB
                         │
                         ▼
               Generate Security Alerts
```

---

# 🧠 AI & Machine Learning

Guardian integrates Artificial Intelligence with cybersecurity to improve phishing detection accuracy.

The Machine Learning model analyzes extracted URLs and predicts whether they are legitimate or phishing attempts. To further improve reliability, predictions are verified using Google's Safe Browsing API along with custom security rules.

This hybrid approach reduces false positives while improving phishing detection performance.

---

# 📂 Project Workflow

1. User authenticates Gmail using Google OAuth 2.0.
2. Guardian continuously monitors the Gmail inbox.
3. Newly received emails are fetched automatically.
4. URLs are extracted from email content.
5. URLs are analyzed using:
   - Trained Machine Learning Model
   - Google Safe Browsing API
   - Rule-Based Detection
6. URLs are classified into:
   - 🟢 Low Risk
   - 🟡 Medium Risk
   - 🔴 High Risk
7. Scan results are stored securely in MongoDB Atlas.
8. Security alerts are generated whenever suspicious or phishing URLs are detected.

---

# 🚀 Technologies Used

## Programming Language

- Python 3.11+

## Backend Framework

- FastAPI

## Machine Learning

- Scikit-learn
- Joblib
- Trained Phishing Detection Model (.pkl)

## Database

- MongoDB Atlas

## Authentication

- Google OAuth 2.0

## APIs

- Gmail API
- Google Safe Browsing API

## Scheduler

- APScheduler

## Development Environment

- Visual Studio Code

## Libraries

- FastAPI
- httpx
- python-dotenv
- pymongo
- scikit-learn
- joblib

---

# 📁 Project Structure

```
Guardian/
│
├── app/
│   ├── controllers/          # Business logic and request handling
│   ├── core/                 # Core configuration and utilities
│   ├── db/                   # MongoDB connection
│   ├── models/               # Database models
│   ├── routes/               # API endpoints
│   ├── services/             # Gmail monitoring and phishing detection services
│   └── main.py               # FastAPI application entry point
│
├── data/                     # Dataset used for training/testing
│
├── ml/                       # Machine Learning related modules
│
├── phishing_model.pkl        # Trained Machine Learning model
│
├── requirements.txt          # Python dependencies
│
├── README.md                 # Project documentation
│
└── .gitignore                # Ignored files
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/A96999438/Guardian.git

cd Guardian
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

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

Create a `.env` file and add the following:

```env
MONGODB_URI=your_mongodb_uri

GOOGLE_CLIENT_ID=your_client_id

GOOGLE_CLIENT_SECRET=your_client_secret

GOOGLE_SAFE_BROWSING_API_KEY=your_api_key

SECRET_KEY=your_secret_key
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

---

# 📊 Risk Levels

| Risk Level | Description |
|------------|-------------|
| 🟢 Low | Safe URL |
| 🟡 Medium | Suspicious URL |
| 🔴 High | Malicious / Phishing URL |

---

# 🎯 Objectives

- Automate Gmail inbox monitoring
- Detect phishing URLs using AI & Machine Learning
- Reduce phishing attacks
- Generate real-time security alerts
- Securely store scan history
- Improve email security using intelligent threat detection

---

# 📸 Sample Output

✔ Gmail Connected Successfully

✔ Emails Monitored Automatically

✔ URLs Extracted Successfully

✔ AI-Based URL Analysis Completed

✔ Phishing Links Detected

✔ Risk Classification Generated

✔ Scan History Stored in MongoDB Atlas

✔ Security Alerts Generated

---

# 💻 Hardware Requirements

- Intel Core i5 or Higher
- Minimum 8 GB RAM
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

# 🚧 Challenges

- Secure Gmail OAuth 2.0 Authentication
- Accurate AI-Based Phishing Detection
- Reducing False Positives
- Continuous Background Monitoring
- Integrating Machine Learning with Threat Intelligence APIs
- Secure Cloud Database Management

---

# 🔮 Future Enhancements

- Web Dashboard for Security Reports
- Email & SMS Notifications
- Support for Outlook and Yahoo Mail
- Cloud Deployment
- Browser Extension
- Deep Learning Based URL Detection
- Security Analytics Dashboard
- Weekly Security Reports
- Multi-User Support

---

# 📈 Results

- Successfully authenticated Gmail using OAuth 2.0.
- Continuously monitored Gmail inbox in real time.
- Extracted URLs automatically from incoming emails.
- Detected phishing links using AI & Machine Learning.
- Verified URLs using Google Safe Browsing API.
- Classified URLs into Low, Medium, and High risk.
- Stored scan history securely in MongoDB Atlas.
- Generated real-time alerts for malicious URLs.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is developed for educational and research purposes.

---

# 👨‍💻 Developer

## Aman Aslam Patel

Artificial Intelligence & Data Science Student

🔗 **GitHub**

https://github.com/A96999438

🔗 **LinkedIn**

https://www.linkedin.com/in/a-92-p/

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates future improvements and development.
