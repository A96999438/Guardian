from datetime import datetime
from app.db.mongo import alerts


def create_alert(*, user_email: str, url: str, risk_level: str, message: str):
    """
    Keyword-only arguments to avoid positional bugs
    """

    alerts.insert_one({
        "userEmail": user_email,
        "url": url,
        "riskLevel": risk_level,
        "message": message,
        "createdAt": datetime.utcnow()
    })

    print("🚨 ALERT GENERATED")
    print(f"👤 User: {user_email}")
    print(f"🔗 URL: {url}")
    print(f"⚠️ Risk: {risk_level}")
    print(f"📢 Message: {message}")
