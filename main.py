from fastapi import FastAPI, Request, Depends, Form

from api.user_api.main import user_router
from db import Base, engine
from api.task_api.main import task_router
from api.category_api.main import category_router
from api.reminder_api.main import reminder_router
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from db import get_db  # подключи свою функцию подключения к БД
from db.models import Task, User, Reminder, Category
templates = Jinja2Templates(directory="templates")


app = FastAPI(docs_url="/docs")
Base.metadata.create_all(engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
# Подключаем роутеры
app.include_router(user_router)
app.include_router(category_router)
app.include_router(reminder_router)
app.include_router(task_router)

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
@app.get("/add_task", response_class=HTMLResponse)
def add_task_form(request: Request, db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return templates.TemplateResponse("addtask.html", {
        "request": request,
        "categories": categories
    })

# Обработка формы добавления задачи
from datetime import datetime

@app.post("/add_task")
def add_task(
    title: str = Form(...),
    description: str = Form(""),
    deadline: str = Form(None),  # ← приходит как строка из формы
    priority: int = Form(None),
    category_id: int = Form(None),
    reminder: int = Form(None),
    db: Session = Depends(get_db)
):
    due_date = None
    if deadline:
        due_date = datetime.fromisoformat(deadline)  # Преобразование строки в datetime

    new_task = Task(
        title=title,
        description=description,
        due_date=due_date,  # ← правильно!
        priority=priority,
        category_id=category_id,
    )

    db.add(new_task)
    db.commit()

    # Добавление напоминания (если reminder указан)
    if reminder is not None:
        reminder_minutes = int(reminder)
        reminder_time = due_date - timedelta(minutes=reminder_minutes)
        new_reminder = Reminder(task=new_task, remind_at=reminder_time)
        db.add(new_reminder)
        db.commit()

    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

@task_router.get("/get_by_telegram_id/{telegram_id}")
def get_tasks_by_telegram_id(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        return []
    tasks = db.query(Task).filter(Task.user_id == user.id).all()
    return [{"title": t.title, "description": t.description} for t in tasks]
@app.get("/task/{task_id}", response_class=HTMLResponse)
def task_detail(task_id: int, request: Request, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return HTMLResponse("Задача не найдена", status_code=404)
    return templates.TemplateResponse("task_detail.html", {"request": request, "task": task})
