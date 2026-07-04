import re
from app.db.mongo import users
from app.services.gmail_service import fetch_recent_emails
from app.controllers.scan_controller import scan_link
from app.services.alert_service import create_alert


def extract_urls(text: str):
    url_regex = r"(https?://[^\s]+)"
    return re.findall(url_regex, text)


async def monitor_emails():
    guardian_users = list(users.find({
        "plan": "GUARDIAN",
        "gmailConnected": True
    }))

    if not guardian_users:
        print("👥 No Guardian users with Gmail connected")
        return

    for user in guardian_users:
        print(f"📩 Monitoring Gmail for {user['email']}")

        emails = fetch_recent_emails(
            user["gmailAccessToken"],
            user["gmailRefreshToken"]
        )

        for email in emails:
            snippet = email.get("snippet", "")
            urls = extract_urls(snippet)

            for url in urls:
                print(f"🔍 Scanning {url} for {user['email']}")

                result = await scan_link({
                    "url": url,
                    "userEmail": user["email"]
                })

                if result["risk"] in ("HIGH", "MEDIUM"):
                    create_alert(
                        user_email=user["email"],
                        url=url,
                        risk_level=result["risk"],
                        message="Suspicious link detected in Gmail"
                    )

                    print(
                        f"🚨 Alert created for {user['email']} "
                        f"({result['risk']})"
                    )
