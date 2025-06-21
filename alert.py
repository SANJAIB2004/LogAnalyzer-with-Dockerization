import os
from alerts.email_alert import send_email_alert
from alerts.slack_alert import send_slack_alert
from dotenv import load_dotenv
load_dotenv()


def check_for_alerts(log_summary):
    alerts = []
    ERROR_THRESHOLD = int(os.getenv("ERROR_THRESHOLD", 5))
    WARNING_THRESHOLD = int(os.getenv("WARNING_THRESHOLD", 10))

    if log_summary["ERROR"] > ERROR_THRESHOLD:
        message = f"⚠️ High error count detected: {log_summary['ERROR']}"
        alerts.append(message)
        send_email_alert("🚨 Error Alert", message)
        send_slack_alert(message)

    if log_summary["WARNING"] > WARNING_THRESHOLD:
        message = f"⚠️ High warning count detected: {log_summary['WARNING']}"
        alerts.append(message)
        send_email_alert("🚨 Warning Alert", message)
        send_slack_alert(message)

    return alerts