# 🧠 Real-Time Log File Analyzer with Alerts

A Streamlit + Python + Docker app to analyze `.log` files and send alerts based on thresholds.

## 🚀 Features
- Upload and analyze log files (ERROR, WARNING, INFO counts)
- Alerts when error/warning count exceeds threshold
- Sends Email and Slack notifications
- Fully Dockerized

## 📦 Setup Locally

```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Docker Usage

```bash
docker build -t log-analyzer .
docker run -p 8501:8501 --env-file .env log-analyzer
```

## 🔐 Environment Variables

```
ERROR_THRESHOLD=5
WARNING_THRESHOLD=10
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-email-app-password
EMAIL_RECEIVER=receiver-email@gmail.com
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXXX/XXXX/XXXX
```