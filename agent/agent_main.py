import time
import requests
import threading
import socket
import psutil
import json
from agent.config import SERVER_URL, AUTH_TOKEN
from shared.crypto_utils import encrypt_message

SEND_INTERVAL = 5  # seconds between sending

def collect_system_info():
    """Collect detailed system resource usage and running process info."""
    hostname = socket.gethostname()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_info = proc.info
            process_list.append({
                "pid": process_info['pid'],
                "name": process_info['name'],
                "cpu_percent": process_info['cpu_percent'],
                "memory_percent": process_info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return {
        "hostname": hostname,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,
        "processes": process_list
    }

def send_data():
    """Encrypt and send system information to the server."""
    while True:
        try:
            data = collect_system_info()
            json_data = json.dumps(data)
            encrypted_data = encrypt_message(json_data)

            headers = {
                "Authorization": f"Bearer {AUTH_TOKEN}"
            }
            response = requests.post(f"{SERVER_URL}/collect", headers=headers, data=encrypted_data)
            if response.status_code == 200:
                print(f"[+] Encrypted data sent successfully!")
            else:
                print(f"[!] Failed to send data, status code: {response.status_code}. Retrying...")
        except Exception as e:
            print(f"[!] Error sending encrypted data: {e}")
        time.sleep(SEND_INTERVAL)

def run_agent():
    print("[*] Agent is running...")
    thread = threading.Thread(target=send_data)
    thread.start()
