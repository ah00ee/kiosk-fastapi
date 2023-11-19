from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates

from jose import jwt

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.client.place.place_crud import create_place, load_place, create_menu, load_menu, quantity_update
from apis.client.place.place_schema import PlaceSchema, MenuSchema


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

    return RedirectResponse(url="/user/place/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/{place_id}")
def get_mode(request: Request, place_id: int):

    return templates.TemplateResponse("userSelection.html", {"request": request, "data":{"place_id": place_id}})

@router.get("/{place_id}/manage")
def place_manage(request:Request,
                place_id: int,
                db:Session=Depends(get_db),
                ):

    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)
    username: str = payload.get("sub")

    data = load_menu(db, place_id, username)

    return templates.TemplateResponse("manageMenu.html", {"request": request, "data": data})

@router.put("/{place_id}/manage")
async def update_place(request:Request,
                place_id: int,
                db:Session=Depends(get_db),):
                
    data = await request.json()
    quantity_update(db, place_id, data)

@router.get("/{place_id}/menu/create")
def menu_create(request:Request,
                place_id:int):

    return templates.TemplateResponse("createMenu.html", {"request": request, "data": {"place_id":place_id}})

@router.post("/{place_id}/menu/create")
def menu_create(place_id: int,
                menu: Form=Depends(MenuSchema.form),
                db: Session=Depends(get_db)
                ):

    create_menu(db, place_id, menu)

    return RedirectResponse(url=f"/user/place/{place_id}/manage", status_code=status.HTTP_303_SEE_OTHER)
