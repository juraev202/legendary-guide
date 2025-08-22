from fastapi import APIRouter
from datetime import datetime, timedelta
from api.reminder_api.schemas import ReminderCreate, ReminderUpdate, ReminderRead
from typing import List
from db.reminderservice import create_reminder_db, get_reminder_by_user_db, get_reminder_by_task_db, get_upcoming_reminders_db, update_reminder_db, delete_reminder_db
reminder_router = APIRouter(prefix="/reminder", tags=["Reminder API"])
@reminder_router.post("/create_remainder")
def create_reminder_api(reminder: ReminderCreate):
    return create_reminder_db(reminder)
@reminder_router.get("/get_reminders_user{user_id}", response_model=List[ReminderRead] )
async def get_reminders_user_api(user_id: int):
    return get_reminder_by_user_db(user_id)
@reminder_router.get("/get_reminders_task{task_id}", response_model=List[ReminderRead] )
async def get_reminders_task_api(task_id: int):
    return get_reminder_by_task_db(task_id)
@reminder_router.get("/get_upcoming_reminders{user_id}", response_model=List[ReminderRead])
async def get_upcoming_reminders_api(user_id: int):
    return get_upcoming_reminders_db(user_id, datetime.now())
@reminder_router.post("/update_reminder")
async def update_reminder_api(reminder_id: int, update: ReminderUpdate):
    return update_reminder_db(reminder_id, update.dict(exclude_unset=True))
@reminder_router.delete("/delete_reminder", response_model=bool)
async def delete_reminder_api(reminder_id: int):
    return delete_reminder_db(reminder_id)
