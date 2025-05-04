from telegram.ext import Updater, CommandHandler
from agent.agent_main import collect_system_info
from agent.config import TELEGRAM_BOT_TOKEN
from agent.database import SessionLocal, SystemLog

import psutil
import os
import signal

def status(update, context):
    info = collect_system_info()
    msg = (
        f"📊 System Status:\n"
        f"🖥️ Host: {info['hostname']}\n"
        f"🧠 CPU: {info['cpu_usage']}%\n"
        f"💾 RAM: {info['memory_usage']}%\n"
        f"🧮 Processes: {len(info['processes'])}"
    )
    update.message.reply_text(msg)

def top(update, context):
    info = collect_system_info()
    valid_procs = [p for p in info['processes'] if p['cpu_percent'] is not None]
    sorted_proc = sorted(valid_procs, key=lambda p: p['cpu_percent'], reverse=True)
    top_5 = sorted_proc[:5]
    msg = "🔥 Top 5 CPU-consuming processes:\n"
    for p in top_5:
        msg += f"• {p['name']} (PID {p['pid']}) - CPU {p['cpu_percent']}% - RAM {p['memory_percent']}%\n"
    update.message.reply_text(msg)

def kill(update, context):
    if len(context.args) != 1:
        update.message.reply_text("❗ Usage: /kill <pid>")
        return

    try:
        pid = int(context.args[0])
        p = psutil.Process(pid)
        p.terminate()
        update.message.reply_text(f"✅ Process {pid} ({p.name()}) terminated.")
    except psutil.NoSuchProcess:
        update.message.reply_text("❌ No such process.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

def log(update, context):
    try:
        db = SessionLocal()
        last_log = db.query(SystemLog).order_by(SystemLog.id.desc()).first()
        if last_log:
            msg = (
                f"📄 Last Log Entry:\n"
                f"🖥 Host: {last_log.hostname}\n"
                f"🧠 CPU: {last_log.cpu_usage}%\n"
                f"💾 RAM: {last_log.memory_usage}%\n"
                f"📅 Time: {last_log.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        else:
            msg = "⚠️ No log entries found."
        update.message.reply_text(msg)
        db.close()
    except Exception as e:
        update.message.reply_text(f"❌ Failed to fetch log: {str(e)}")

def help_command(update, context):
    msg = (
        "🤖 Available Commands:\n"
        "/status - Show system resource usage\n"
        "/top - Show top 5 CPU processes\n"
        "/kill <pid> - Kill a process\n"
        "/log - Show last log entry\n"
        "/help - Show this message"
    )
    update.message.reply_text(msg)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("top", top))
    dp.add_handler(CommandHandler("kill", kill))
    dp.add_handler(CommandHandler("log", log))
    dp.add_handler(CommandHandler("help", help_command))

    print("[BOT] Telegram bot is running...")
    updater.start_polling()
    updater.idle()
