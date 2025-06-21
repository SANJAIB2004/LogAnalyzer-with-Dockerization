import streamlit as st
from alert import check_for_alerts
from utils import parse_log_file
from dotenv import load_dotenv
load_dotenv()

st.title("🧠 Real-Time Log File Analyzer")
st.markdown("Upload a `.log` file to monitor error/warning messages in real-time.")

uploaded_file = st.file_uploader("Upload Log File", type=["log", "txt"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Log Preview", content, height=300)

    parsed_logs = parse_log_file(content)
    st.subheader("🧾 Log Summary")
    st.write(parsed_logs)

    alert_summary = check_for_alerts(parsed_logs)
    st.subheader("🚨 Alerts")
    if alert_summary:
        for alert in alert_summary:
            st.error(alert)
    else:
        st.success("No alerts found!")