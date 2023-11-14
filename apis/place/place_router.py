from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates

from jose import jwt

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.place.place_crud import create_place, load_place
from apis.place.place_schema import PlaceSchema


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

        
@router.get("/")
def get_place(request:Request,
            db: Session=Depends(get_db)):

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

