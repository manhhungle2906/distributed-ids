from flask import Blueprint, request, jsonify
from server.utils import send_telegram_alert, send_desktop_alert

alert_bp = Blueprint('alert', __name__)

@alert_bp.route('/alert', methods=['POST'])
def alert_handler():
    try:
        data = request.get_json()
        message = data.get('message', 'ALERT from Distributed IDS System')
        send_telegram_alert(message)
        send_desktop_alert(message)
        return jsonify({"message": "Alert sent successfully"}), 200
    except Exception as e:
        print(f"[!] Error sending alert: {e}")
        return jsonify({"error": str(e)}), 500
