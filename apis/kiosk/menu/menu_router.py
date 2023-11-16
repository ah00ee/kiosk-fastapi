from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from jose import jwt

from apis.database import get_db
from apis.kiosk.menu.menu_crud import load_menu


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")


@router.get("/{place_id}/menu")
def get_menu(request: Request,
            place_id: int,
            db: Session=Depends(get_db)
            ):

    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    username: str = payload.get("sub")

    data = load_menu(db, place_id, username)

    return templates.TemplateResponse("kioskMenu.html", {"request": request, "data": data})
