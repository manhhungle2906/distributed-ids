from flask import Blueprint, request, jsonify
from shared.crypto_utils import decrypt_message
from server.database import save_log
from server.detection import detect_anomaly
from server.utils import send_telegram_alert, send_desktop_alert
from server.config import AUTH_TOKEN
import json

collect_bp = Blueprint('collect', __name__)

@collect_bp.route('/collect', methods=['POST'])
def collect_data():
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header != f"Bearer {AUTH_TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401

        encrypted_data = request.get_data()
        decrypted_json = decrypt_message(encrypted_data)
        data = json.loads(decrypted_json)

        print(f"[+] Decrypted data: {data}")

        alert = detect_anomaly(data)
        if alert:
            print(f"[!] ALERT: {alert}")
            message = f"ALERT from {data.get('hostname')}: {alert}"
            send_telegram_alert(message)
            send_desktop_alert(message)

        save_log(data)
        return jsonify({"message": "Data collected successfully"}), 200
    except Exception as e:
        print(f"[!] Error in collecting data: {e}")
        return jsonify({"error": str(e)}), 500
