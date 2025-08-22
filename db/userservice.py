from db.models import User
from db import get_db
from api.user_api.schemas import UserCreate
def create_user_db(user_data: UserCreate):
    db = next(get_db())
    user_dict = user_data.model_dump()
    user = db.query(User).filter_by(username=user_data.username).first()
    if user:
        return False
    new_user = User(**user_dict)
    db.add(new_user)
    db.commit()
    return new_user.id
def get_all_or_exact_user_db(user_id=0):
    db = next(get_db())
    if user_id:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return exact_user
        return False
    return db.query(User).all()


def update_user_db(user_id, change_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        if change_info == "name":
            exact_user.name = new_info
        elif change_info == "surname":
            exact_user.surname = new_info
        elif change_info == "username":
            exact_user.username = new_info
        elif change_info == "email":
            exact_user.email = new_info
        elif change_info == "password":
            exact_user.password = new_info
        elif change_info == "birthday":
            exact_user.birthday = new_info
        elif change_info == "city":
            exact_user.city = new_info
        db.commit()
        return True
    return False


def delete_user_db(user_id):
    db = next(get_db())

    to_delete_user = db.query(User).filter_by(id=user_id).first()

    if to_delete_user:
        db.delete(to_delete_user)
        db.commit()
        return True
    return False
