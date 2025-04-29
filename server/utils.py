import requests
import subprocess
from server.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[ALERT] Telegram alert sent successfully!")
        else:
            print(f"[ALERT] Failed to send Telegram alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"[ALERT] Error sending Telegram alert: {e}")

def send_desktop_alert(message):
    try:
        subprocess.run([
            "osascript",
            "-e",
            f'display notification "{message}" with title "Distributed IDS Alert"'
        ])
        print("[ALERT] Desktop notification sent successfully!")
    except Exception as e:
        print(f"[ALERT] Error sending desktop notification: {e}")
