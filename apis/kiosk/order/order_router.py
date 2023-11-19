from urllib import response
from fastapi import APIRouter, Depends, Request, status
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apis.database import get_db
from apis.kiosk.order.order_crud import create_order, get_order_number, get_quantity


router = APIRouter(
    prefix="/kiosk/place"
)
templates = Jinja2Templates(directory="templates")

@router.get("/{place_id}/order")
async def get_payment(place_id: int,
                    db: Session=Depends(get_db)
                    ):
    order_number = get_order_number(db)

    return RedirectResponse(url=f"/kiosk/place/{place_id}/order/{order_number}", status_code=status.HTTP_303_SEE_OTHER)
    
@router.post("/{place_id}/order")
async def pay_request(request: Request,
                place_id: int,
                db: Session=Depends(get_db)
                ):
    data = await request.json()

    menus = [menu for menu in data['menus']]
    
    create_order(db, place_id, menus)

@router.get("/{place_id}/order/{order_number}")
async def order_pay(request: Request,
                    order_number: int,
                    db: Session=Depends(get_db)
                    ):
    ### TODO ###
    # 1. 주문 목록 불러오기
    # 2. 재고 수정하기 (Menu 테이블 수정(update))
    get_quantity(db, order_number)

    return templates.TemplateResponse("orderPage.html", {"request": request})