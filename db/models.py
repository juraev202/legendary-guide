from sqlalchemy import Boolean
from sqlalchemy import (Integer, Column, String, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=True, unique=True)
    surname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    telegram_id = Column(Integer, unique=True)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    color = Column(String, nullable=False)

    user_fk = relationship(User, lazy="subquery")
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    task_id = Column(Integer, ForeignKey('tasks.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Integer, nullable=True)
    is_completed = Column(Boolean, default=False)
    user_fk = relationship(User, lazy="subquery")
    category_fk = relationship(Category, lazy="subquery")
    reminders = relationship("Reminder", back_populates="task")

class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    remind_at = Column(DateTime, default=datetime.now)
    is_sent = Column(Boolean, nullable=False)
    user_fk = relationship(User, lazy="subquery")
    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Task", back_populates="reminders")

    task = relationship("Task", back_populates="reminders")
class AIRecommendation(Base):
    __tablename__ = 'ai_recommendations'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_read = Column(Boolean, nullable=False)
    user_fk = relationship(User, lazy="subquery")



