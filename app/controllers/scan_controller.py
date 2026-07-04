import os
import re
import httpx
from datetime import datetime
from app.db.mongo import scans, audits
from app.services.phishtank_service import check_phishtank
from app.services.ml_service import ml_predict


async def check_google_safe_browsing(url: str) -> bool:
    key = os.getenv("GOOGLE_SAFE_BROWSING_KEY")
    if not key:
        return False

    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.post(
            f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={key}",
            json={
                "client": {
                    "clientId": "guardian",
                    "clientVersion": "1.0"
                },
                "threatInfo": {
                    "threatTypes": [
                        "MALWARE",
                        "SOCIAL_ENGINEERING",
                        "UNWANTED_SOFTWARE"
                    ],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [{"url": url}],
                },
            },
        )

    return bool(res.json().get("matches"))


async def scan_link(data: dict):
    """
    Expected input:
    {
        "url": "http://example.com",
        "userEmail": "user@gmail.com"
    }
    """

    url = data.get("url")
    user_email = data.get("userEmail")

    if not url:
        return {"risk": "LOW", "score": 0, "reasons": []}

    reasons = []
    score = 0
    lower = url.lower()

    # PhishTank check
    if check_phishtank(url):
        reasons.append("Matched known phishing domain (PhishTank)")
        score += 90

    # Google Safe Browsing
    if await check_google_safe_browsing(url):
        reasons.append("Flagged by Google Safe Browsing")
        score += 70

    # Suspicious keywords
    suspicious_words = ["free", "login", "verify", "crypto", "reward", "bank"]
    for w in suspicious_words:
        if w in lower:
            reasons.append(f"Contains suspicious word: {w}")
            score += 10

    # IP-based URL
    if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", lower):
        reasons.append("IP-based URL detected")
        score += 40

    # Risk calculation
    risk = "LOW"
    if score >= 80:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    
    ml_result = ml_predict(url)
    if ml_result == "PHISHING":
        reasons.append("Detected by ML phishing classifier")
        score += 40


    # Store scan result
    scans.insert_one({
        "type": "LINK",
        "input": url,
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "userEmail": user_email,
        "scannedAt": datetime.utcnow()
    })

    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "recommendation":
            "🚨 DO NOT OPEN this link" if risk == "HIGH"
            else "⚠ Suspicious — open carefully" if risk == "MEDIUM"
            else "✅ No major threats detected"
    }
