def alert_doc(data):
    return {
        "userEmail": data["userEmail"],
        "url": data["url"],
        "riskLevel": data["riskLevel"],
        "message": data.get("message"),
        "source": "GMAIL",
        "resolved": False
    }
