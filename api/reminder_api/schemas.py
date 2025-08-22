from datetime import datetime

from pydantic import BaseModel
from typing import Optional
class ReminderCreate(BaseModel):
    user_id: int
    task_id: int
    remind_at: datetime
    is_sent: bool

class ReminderUpdate(BaseModel):
    remind_at: Optional[datetime] = None
    is_sent: Optional[bool] = None
    task_id: Optional[int] = None
    user_id: Optional[int] = None

class ReminderRead(BaseModel):
    user_id: Optional[int] = None
    task_id: Optional[int] = None
    remind_at: Optional[datetime] = None
    is_sent: Optional[bool] = None





