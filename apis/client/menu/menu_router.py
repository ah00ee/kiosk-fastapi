from logging import PlaceHolder
from fastapi import APIRouter, Depends, Request, Response
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from sqlalchemy.orm import Session

from jose import jwt

from apis.database import get_db
from apis.menu.menu_crud import load_menu


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

@router.post("/{place_id}/menu")
def get_menu(request: Request,
            place_id: int,
            db: Session=Depends(get_db)
            ):

    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    username: str = payload.get("sub")

    data = load_menu(db, place_id, username)

    return templates.TemplateResponse("menu.html", {"request": request, "data": data})
