from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from apis.database import get_db
from apis.kiosk.order.order_crud import create_order


SECRET_KEY = "it's secret"

router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

@router.get("/{place_id}/order")
def tmp():
    return {"message": "working good"}

@router.post("/{place_id}/order")
async def pay_request(request: Request,
                place_id: int,
                db: Session=Depends(get_db)
                ):
    
    data = await request.json()

    menus = [menu for menu in data['menus']]
    data = create_order(db, place_id, menus)

    # return templates.TemplateResponse("kioskMenu.html", {"request": request, "data": data})
