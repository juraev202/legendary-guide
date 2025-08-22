from pydantic import BaseModel
from typing import Optional
class UserCreate(BaseModel):
    username: str
    password: str
    surname: Optional[str] = None
    username: str
    email: str
    birthday: Optional[str] = None
    city: Optional[str] = None
    