from db.models import Reminder
from datetime import datetime
from db import get_db
from api.reminder_api.schemas import ReminderCreate, ReminderUpdate
def create_reminder_db(reminder_data: ReminderCreate):
    db = next(get_db())
    new_reminder = Reminder(**reminder_data.model_dump())
    db.add(new_reminder)
    db.commit()
    return True
def get_reminder_by_user_db(user_id: int):
    db = next(get_db())
    reminder = db.query(Reminder).filter_by(user_id=user_id).all()
    return reminder
def get_reminder_by_task_db(task_id: int):
    db = next(get_db())
    reminder_task = db.query(Reminder).filter_by(task_id=task_id).all()
    return reminder_task
def get_upcoming_reminders_db(user_id, current_time):
    db = next(get_db())
    upcoming_reminders = db.query(Reminder).filter(Reminder.user_id == user_id, Reminder.remind_at > current_time).all()
    return upcoming_reminders

def update_reminder_db(reminder_id: int, updates: dict):
    db = next(get_db())
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()

    if not reminder:
        return {"error": "Reminder not found"}

    for key, value in updates.items():
        if hasattr(reminder, key):
            setattr(reminder, key, value)

    db.commit()
    db.refresh(reminder)
    return {"message": "Reminder updated", "updated": updates}

def delete_reminder_db(reminder_id: int):
    db = next(get_db())
    reminder = db.query(Reminder).filter_by(id=reminder_id).first()
    if reminder:
        db.delete(reminder)
        db.commit()
        return True
    return False




