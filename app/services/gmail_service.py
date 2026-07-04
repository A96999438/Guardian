from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_gmail_client(access_token, refresh_token):
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=None,
        client_secret=None,
        scopes=["https://www.googleapis.com/auth/gmail.readonly"]
    )

    return build("gmail", "v1", credentials=creds)


def fetch_recent_emails(access_token, refresh_token, max_results=5):
    gmail = get_gmail_client(access_token, refresh_token)

    response = gmail.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = response.get("messages", [])
    emails = []

    for msg in messages:
        msg_data = gmail.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        snippet = msg_data.get("snippet", "")

        emails.append({
            "id": msg["id"],
            "snippet": snippet
        })

    return emails
