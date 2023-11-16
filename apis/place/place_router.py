from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates

from jose import jwt

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.menu.menu_crud import create_menu
from apis.menu.menu_schema import MenuSchema
from apis.place.place_crud import create_place, load_place
from apis.place.place_schema import PlaceSchema


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/user/place"
)
templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_place(request:Request,
            db: Session=Depends(get_db)
            ):
    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    username: str = payload.get("sub")

    data = load_place(db, username)
    
    return templates.TemplateResponse("userPlace.html", {"request": request, "data": data})

@router.get("/create")
def place_create(request:Request):

    return templates.TemplateResponse("createPlace.html", {"request": request})

@router.post("/create")
def place_create(request:Request,
                place: Form=Depends(PlaceSchema.form),
                db: Session=Depends(get_db)
                ):

    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    create_place(db, place, payload)

    return RedirectResponse(url="/kiosk/place/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/{place_id}")
def get_mode(request: Request, place_id: int):

    return templates.TemplateResponse("userSelection.html", {"request": request, "data":{"place_id": place_id}})

@router.post("/{place_id}/manage")
def place_manage():
    return {"message": "manage user place"}

@router.get("/{place_id}/menu/create")
def menu_create(request:Request,
                place_id:int):

    return templates.TemplateResponse("createMenu.html", {"request": request, "data": {"place_id":place_id}})

@router.post("/{place_id}/menu/create")
def menu_create(request:Request,
                place_id: int,
                menu: Form=Depends(MenuSchema.form),
                db: Session=Depends(get_db)
                ):

    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    create_menu(db, place_id, menu, payload)

    return RedirectResponse(url=f"/kiosk/place/{place_id}/menu", status_code=status.HTTP_303_SEE_OTHER)
