from db.models import Task
from db import get_db
from api.task_api.schemas import TaskCreate
def create_task_db(user_id: int, task_data: TaskCreate):
    db = next(get_db())
    task_dict = task_data.model_dump()

    task = db.query(Task).filter_by(title=task_data.title, user_id=user_id).first()
    if task:
        return False

    new_task = Task(**task_dict)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task.id
def get_tasks_by_user_db(user_id):
    db = next(get_db())
    exact_user_task = db.query(Task).filter_by(user_id=user_id).all()
    return exact_user_task
def get_task_by_task_db(task_id: int):
    db = next(get_db())
    tasks = db.query(Task).filter(Task.task_id == task_id).all()
    return [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "created_at": t.created_at.isoformat()
        }
        for t in tasks
    ]

def get_category_task_db(category_id):
    db = next(get_db())
    exact_category_task_task = db.query(Task).filter_by(category_id=category_id).all()
    return exact_category_task_task
def update_task_db(task_id: int, update_data: dict) -> bool:
    db = next(get_db())
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False
    for key, value in update_data.items():
        setattr(task, key, value)
    db.commit()
    return True

def delete_task_db(task_id):
    db = next(get_db())
    to_delete_task = db.query(Task).filter_by(id=task_id).first()
    if to_delete_task:
        db.delete(to_delete_task)
        db.commit()
        return True
    return False


