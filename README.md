# 🛡️ Distributed Intrusion Detection System (D-IDS)

This project implements a lightweight Distributed Intrusion Detection System (D-IDS) using Python. It monitors real-time system activities such as CPU usage, memory usage, and running processes across multiple client machines. A central server receives, analyzes, and alerts based on this data.

---

## 🔧 Features

- 🔍 Real-time monitoring of CPU, RAM, and active processes
- 🔐 Secure data transmission using AES (Fernet) encryption
- 📡 Client-server architecture with RESTful API (Flask)
- 🚨 Alerts via Telegram bot and desktop notification
- 💾 Logs stored in local SQLite database
- 🔄 Agent retry mechanism for fault-tolerance
- 🤖 Telegram bot commands: `/status`, `/top`, `/kill <pid>`, `/log`, `/help`

---

## 📁 Project Structure

```
didps_project/
├── agent/
│   ├── agent_main.py
│   ├── telegram_bot.py
│   ├── config.py
│   └── database.py
├── server/
│   ├── server_main.py
│   ├── collect_service.py
│   ├── detection.py
│   ├── utils.py
│   └── database.py
├── shared/
│   └── crypto_utils.py
├── logs.db
├── start_agent.py
├── start_server.py
├── start_bot.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/didps_project.git
cd didps_project
```

### 2. Create virtual environment

```bash
python3 -m venv didps-env
source didps-env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Running the System

### Start the server

```bash
python start_server.py
```

### Start the agent (on client machine)

```bash
python start_agent.py
```

### Start the Telegram bot

```bash
python start_bot.py
```

---

## 💬 Telegram Bot Commands

| Command        | Description                          |
|----------------|--------------------------------------|
| `/status`      | Get system usage summary             |
| `/top`         | Show top 5 CPU-consuming processes   |
| `/kill <pid>`  | Kill a process by PID                |
| `/log`         | View last log entry from database    |
| `/help`        | List available commands              |

---

## ⚙️ Configuration

Edit `agent/config.py` to set:

```python
SERVER_URL = "http://localhost:8000"
AUTH_TOKEN = "your_auth_token"
TELEGRAM_BOT_TOKEN = "your_bot_token"
ADMIN_CHAT_ID = "your_telegram_chat_id"
```

---

## 📦 Dependencies

- Flask
- SQLAlchemy
- Cryptography
- python-telegram-bot==13.15
- Requests
- Plyer
- psutil

---

## 📌 Notes

- Ensure `logs.db` is writable by the server
- Project tested on macOS and Linux
- Desktop notification may require permissions depending on OS

---


## 📜 License

This project is for educational use under the Distributed Systems course (CT30A3401).
