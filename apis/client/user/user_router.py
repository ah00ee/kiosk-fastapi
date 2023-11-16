from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from http.client import HTTPException

from jose import jwt

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.client.user.user_crud import create_user, delete_user, get_user
from apis.client.user.user_schema import UserSchema


SECRET_KEY="it's secret"

router = APIRouter(
    prefix="/user"
)
templates = Jinja2Templates(directory="templates")

@router.post("/create")
def user_create(user: UserSchema, db: Session=Depends(get_db)):
    _user = create_user(db, user)
    return _user

@router.get("/login")
def user_login(request:Request):

    return templates.TemplateResponse("login.html", {"request":request})

@router.post("/login")
def user_login(response: Response, 
            login_form: OAuth2PasswordRequestForm=Depends(),
            db: Session=Depends(get_db)):

    _user = get_user(db, login_form.username)
    if not _user or not (login_form.password==_user.password):
        raise HTTPException(
            "Login error. Check username or password."
        )

    data = {
        "sub": _user.username
    }
    access_token = jwt.encode(data, SECRET_KEY)  

    # 쿠키 저장
    response = RedirectResponse(url="/user/place/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access-token", value=access_token)
    
    return response
    # {
    #     "access_token": access_token, "token_type": "bearer"
    # }

@router.post("/logout")
def user_logout():
    # 쿠키 삭제
    response = RedirectResponse(url="/user/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(key="access-token")
    
    return response

@router.post("/{id}/delete")
def user_delete(id:int, db:Session=Depends(get_db)):
    return delete_user(db, id)

@router.get("/{id}")
def user_info(id:int, db:Session=Depends(get_db)):
    _user = get_user(db, id)
    return _user
