from fastapi import APIRouter
from api.category_api.schemas import CategoryCreate, CategoryUpdate, CategoryRead
from typing import List

from db.categoryservice import create_category_db, get_category_by_user_db, update_category_db, delete_category_db
category_router = APIRouter(prefix="/category", tags=["Category API"])
@category_router.post("/create_category")
async def create_category_api(category: CategoryCreate):
    return create_category_db(category)
@category_router.get("/get_category_user", response_model=CategoryRead)
async def get_category_by_user_api(user_id):
    return get_category_by_user_db()
@category_router.put("/update_category")
async def update_category_api(category_id: int, category: CategoryUpdate):
    return update_category_db(category_id, category.name,category.color)
@category_router.delete("/delete_category")
async def delete_category_api(category_id: int):
    return delete_category_db(category_id)


