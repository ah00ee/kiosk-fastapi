from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from apis.database import get_db
from apis.kiosk.menu.menu_crud import load_menu
from apis.utils import login_required, get_payload


router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")


@router.get("/{place_id}/menu")
@login_required
def get_menu(request: Request,
            place_id: int,
            db: Session=Depends(get_db)
            ):
    payload = get_payload(request)
    username = payload.get("sub")

    data = load_menu(db, place_id, username)

    return templates.TemplateResponse("kioskMenu.html", {"request": request, "data": data})
