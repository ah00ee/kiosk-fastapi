from fastapi import APIRouter, Depends, Request, status
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.kiosk.order.order_crud import create_order


router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

@router.get("/{place_id}/order")
async def get_payment(request: Request):

    return templates.TemplateResponse("orderPage.html", {"request": request})

@router.post("/{place_id}/order")
async def pay_request(request: Request,
                place_id: int,
                db: Session=Depends(get_db)
                ):
    data = await request.json()

    menus = [menu for menu in data['menus']]
    
    create_order(db, place_id, menus)

    return RedirectResponse(url=f"/kiosk/place/{place_id}/order", status_code=status.HTTP_303_SEE_OTHER)