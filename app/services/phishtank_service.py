import os
import json
import tldextract

phishing_domains = set()

def load_phishtank_data():
    path = "data/phishtank.json"

    if not os.path.exists(path):
        print("⚠ PhishTank dataset not found")
        return

    phishing_domains.clear()

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read().strip()

        if not raw:
            print("⚠ PhishTank file is empty")
            return

        # ===== TRY JSON MODE =====
        try:
            data = json.loads(raw)
            for entry in data:
                url = entry.get("url")
                if url:
                    ext = tldextract.extract(url)
                    phishing_domains.add(ext.domain)

            print(f"✅ PhishTank JSON loaded: {len(phishing_domains)} domains")
            return

        except json.JSONDecodeError:
            print("ℹ PhishTank not JSON, switching to TXT mode")

        # ===== TXT MODE =====
        for line in raw.splitlines():
            url = line.strip()
            if not url:
                continue

            ext = tldextract.extract(url)
            if ext.domain:
                phishing_domains.add(ext.domain)

        print(f"✅ PhishTank TXT loaded: {len(phishing_domains)} domains")

    except Exception as e:
        print("❌ PhishTank load error:", str(e))


def check_phishtank(url: str) -> bool:
    try:
        ext = tldextract.extract(url)
        return ext.domain in phishing_domains
    except Exception:
        return False
