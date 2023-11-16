from models.client import User
from sqlalchemy.orm import Session

from apis.client.user.user_schema import UserSchema

def create_user(db: Session, user: UserSchema):
    user = User(username=user.username,
                password=user.password
        )
    db.add(user)
    db.commit()

    return user

def get_user(db: Session, user):
    if type(user) is int:
        user = db.query(User).get(user)
    else:
        user = db.query(User).filter(User.username==user).first()

    return user

def delete_user(db: Session, user_id):
    db.query(User).filter(User.id==user_id).delete()
    db.commit()

    return "deleted user"