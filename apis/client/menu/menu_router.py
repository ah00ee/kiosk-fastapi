from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from apis.database import get_db
from apis.menu.menu_crud import load_menu


router = APIRouter(
    prefix="/kiosk/menu"
)

@router.post("/")
def get_menus(db: Session=Depends(get_db)):
    menus = load_menu(db, 1, "username")

    return menus
