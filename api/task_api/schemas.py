from datetime import datetime

from typing import Optional
from pydantic import BaseModel
class TaskCreate(BaseModel):
    user_id: int
    task_id: int
    title: str
    category_id: int
    description: str
    created_at: datetime
    due_date: datetime
    priority: int
    is_completed: bool
class TaskUpdate(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[int] = None
    is_completed: Optional[bool] = None
class TaskRead(BaseModel):
    user_id: int
    title: str
    category_id: int
    description: str