from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    password: str
    own: str=None
    address: str=None
