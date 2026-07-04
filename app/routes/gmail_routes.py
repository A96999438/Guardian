from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, PlainTextResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from datetime import datetime
import os

from app.db.mongo import users

router = APIRouter()

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/userinfo.email",
    "openid",
]


def create_flow():
    return Flow.from_client_config(
        {
            "web": {
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [os.getenv("GOOGLE_REDIRECT_URI")],
            }
        },
        scopes=SCOPES,
        redirect_uri=os.getenv("GOOGLE_REDIRECT_URI"),
    )


# =========================
# START GMAIL AUTH (SYNC)
# =========================
@router.get("/auth")
def gmail_auth():
    flow = create_flow()
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        prompt="consent",
    )
    return RedirectResponse(auth_url)


# =========================
# GMAIL CALLBACK (SYNC)
# =========================
@router.get("/callback")
def gmail_callback(request: Request):
    try:
        flow = create_flow()
        flow.fetch_token(authorization_response=str(request.url))
        creds = flow.credentials

        oauth2 = build("oauth2", "v2", credentials=creds)
        userinfo = oauth2.userinfo().get().execute()
        email = userinfo.get("email")

        if not email:
            raise Exception("Email not found")

        users.update_one(
            {"email": email},
            {"$set": {
                "email": email,
                "plan": "GUARDIAN",
                "gmailConnected": True,
                "gmailAccessToken": creds.token,
                "gmailRefreshToken": creds.refresh_token,
                "gmailLastChecked": datetime.utcnow(),
            }},
            upsert=True
        )

        print(f"✅ Gmail connected & Guardian activated for {email}")

        return PlainTextResponse(
            "✅ Gmail connected successfully. Guardian is now LIVE."
        )

    except Exception as e:
        print("❌ Gmail OAuth Error:", str(e))
        return PlainTextResponse(
            "Gmail authentication failed",
            status_code=500
        )
