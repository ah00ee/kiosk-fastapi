from sqlalchemy.orm import Session

from models.client import Place


def load_menu(db: Session, 
            place_id: int,
            username
            ):

    place = db.query(Place).get(place_id)

    return {"username": username, "place": place.name, "menus": place.menus}