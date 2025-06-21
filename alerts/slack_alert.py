import requests
import os
from dotenv import load_dotenv
load_dotenv()


def send_slack_alert(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    payload = {"text": message}
    
    try:
        res = requests.post(webhook_url, json=payload)
        if res.status_code == 200:
            print("✅ Slack alert sent successfully")
        else:
            print(f"❌ Slack alert failed with status {res.status_code}")
    except Exception as e:
        print(f"❌ Slack alert exception: {e}")