from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    id: int
    name: str
    user_id: int
    color: str


class CategoryRead(BaseModel):
    id: int
    name: str
    user_id: int
    color: str

class CategoryUpdate(BaseModel):
    user_id: int
    color: str
    name: str




