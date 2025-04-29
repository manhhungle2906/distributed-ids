from flask import Blueprint, request, jsonify
from server.detection import detect_anomaly

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze_data():
    try:
        data = request.get_json()
        alert = detect_anomaly(data)
        if alert:
            return jsonify({"alert": alert}), 200
        else:
            return jsonify({"message": "No anomalies detected"}), 200
    except Exception as e:
        print(f"[!] Error in analyzing data: {e}")
        return jsonify({"error": str(e)}), 500
