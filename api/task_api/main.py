from fastapi import APIRouter
from typing import List
from api.task_api.schemas import TaskCreate, TaskUpdate, TaskRead
from db.taskservice import create_task_db, get_tasks_by_user_db, get_task_by_task_db, get_category_task_db, update_task_db, delete_task_db
task_router = APIRouter(prefix="/tasks", tags=["Tasks API"])
@task_router.post("/create_task")
async def create_task_api(task_create: TaskCreate):
    return create_task_db(task_create.user_id, task_create)
@task_router.get("/get_tasks_user{user_id}", response_model=List[TaskRead])
async def get_tasks_user_api(user_id: int):
    return get_tasks_by_user_db(user_id)
@task_router.get("/get_tasks_by_task{task_id}")
async def get_tasks_by_task_api(task_id: int):
    return get_task_by_task_db(task_id)
@task_router.get("/get_task_by_category{category_id}")
async def get_task_by_category_api(category_id: int):
    return get_category_task_db(category_id)
@task_router.put("/update_task/{task_id}", response_model=bool)
async def update_task_api(task_id: int, task: TaskUpdate):
    update_data = task.model_dump(exclude_unset=True)
    return update_task_db(task_id, update_data)
@task_router.delete("/delete_task/{task_id}", response_model=bool)
async def delete_task_api(task_id: int):
    return delete_task_db(task_id)



