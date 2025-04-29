from flask import Flask
from server.collect_service import collect_bp
from server.analyze_service import analyze_bp
from server.alert_service import alert_bp
from server.config import SERVER_PORT

def run_server():
    app = Flask(__name__)

    # Register microservices
    app.register_blueprint(collect_bp)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(alert_bp)

    print("[*] Server is running...")
    app.run(host="0.0.0.0", port=SERVER_PORT)
