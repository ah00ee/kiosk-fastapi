from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from jose import jwt


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

        
@router.get("/")
async def get_place(request:Request):

    token = request.cookies.get("access-token")

    payload = jwt.decode(token, SECRET_KEY)
    username: str = payload.get("sub")

    return templates.TemplateResponse("userPlace.html", {"request": request, "username": username})
