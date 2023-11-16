from sqlalchemy.orm import Session

from models.client import Menu, Place

from apis.client.menu.menu_schema import MenuSchema


def create_menu(db: Session, 
                place_id: int,
                menu: MenuSchema, 
                ):
    menu = Menu(name=menu.name,
                price=menu.price,
                place_id=place_id,
                quantity=menu.quantity,
                out_of_stock=menu.out_of_stock
        )

    db.add(menu)
    db.commit()

    return menu

def load_menu(db: Session, 
            place_id: int,
            username
            ):

    place = db.query(Place).get(place_id)

    return {"username": username, "place": place.name, "menus": place.menus}