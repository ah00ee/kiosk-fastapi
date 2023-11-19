from sqlalchemy.orm import Session

from models.client import Place, UserPlace, User, Menu

from apis.client.user.user_schema import Token
from apis.client.place.place_schema import PlaceSchema, MenuSchema


def create_place(db: Session, 
                place: PlaceSchema,
                token: Token):
    place = Place(name=place.name,
                address=place.address
        )
    db.add(place)
    db.commit()

    user = db.query(User).filter(User.username==token.get("sub")).first()

    user_place = UserPlace(user_id=user.id, place_id=place.id)
    db.add(user_place)
    db.commit()

    return place

def load_place(db: Session, username):
    user = db.query(User).filter(User.username == username).first()
    user_place_all = db.query(UserPlace).filter(UserPlace.user_id == user.id).all()
    place = []
    for user_place in user_place_all:
        place.append(db.query(Place).get(user_place.place_id))

    return {"username": username, "place": place}

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

def quantity_update(db: Session,
                    place_id: int,
                    data
                    ):
    menu_name, quantity = data['name'], int(data['quantity'])

    db.query(Menu).filter(Menu.place_id==place_id, Menu.name==menu_name).update({"quantity": quantity})
    if quantity > 0:
        db.query(Menu).filter(Menu.place_id==place_id, Menu.name==menu_name).update({"out_of_stock": False})
    db.commit()
