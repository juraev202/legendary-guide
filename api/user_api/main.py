from fastapi import APIRouter
from api.user_api.schemas import UserCreate
from db.userservice import create_user_db

user_router = APIRouter(prefix="/user", tags=["User API"])


@user_router.post("/create_user")
async def create_user_api(user: UserCreate):
    response = create_user_db(user)
    return response