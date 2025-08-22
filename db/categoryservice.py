from db.models import Category
from db import get_db
from api.category_api.schemas import CategoryCreate
from db.models import Category

def create_category_db(category: CategoryCreate):
    db = next(get_db())


    existing_category = db.query(Category).filter_by(name=category.name).first()
    if existing_category:
        return False

    new_category = Category(**category.model_dump())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category.id

def get_category_by_user_db(user_id=0):
    db = next(get_db())
    category = db.query(Category).filter_by(id=user_id).first()
    return category
def get_category_by_id_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()
    return category
def update_category_db(category_id, change_info, new_info):
    db = next(get_db())
    exact_category = db.query(Category).filter_by(id=category_id).first()
    if exact_category:
        if change_info == "name":
            exact_category.name = new_info
        elif change_info == "color":
            exact_category.color = new_info
        db.commit()
        return True
    return False
def delete_category_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return True
    return False
