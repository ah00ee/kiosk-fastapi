from fastapi import APIRouter

from database import SessionLocal
from models.client import Menu, User

from apis.crud.user_crud import create_user
from apis.schema.user_schema import UserSchema

router = APIRouter(
    prefix="/kiosk/user"
)

@router.post("/create")
def user_create(user:UserSchema):
    db = SessionLocal()
    _user = create_user(user)
    db.add(_user)
    db.commit()
    return user

@router.post("/{id}/delete")
def user_delete(id:int):
    db = SessionLocal()
    db.query(User).filter(User.id==id).delete()
    db.commit()
    return "deleted user"

@router.get("/{id}")
def get_user(id:int):
    db = SessionLocal()
    _user = db.query(User).get(id)
    return _user


@router.post("/menu/create")
def create_menu():
    db = SessionLocal()
    
    db.query(Menu).add_entity()