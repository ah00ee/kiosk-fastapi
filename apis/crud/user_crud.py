from apis.schema.place import PlaceSchema
from models.client import User
from apis.schema.user_schema import UserSchema


def create_user(user: UserSchema):
    user = User(username=user.username,
                password=user.password
        )
    return user