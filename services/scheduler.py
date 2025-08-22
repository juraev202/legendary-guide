from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from db import SessionLocal
from db.reminderservice import get_upcoming_reminders_db
from services.bot import send_telegram_message

scheduler = BackgroundScheduler()

def check_reminders():

    db = SessionLocal()
    now = datetime.utcnow()
    reminders = get_upcoming_reminders_db(db, user_id=None, current_time=now)

    for reminder in reminders:
        # Здесь reminder.user_id должен быть chat_id в Telegram
        send_telegram_message(reminder.user_id, f"🔔 Напоминание: {reminder.message}")

    db.close()

def start_scheduler():

    scheduler.add_job(check_reminders, "interval", minutes=1)
    scheduler.start()
