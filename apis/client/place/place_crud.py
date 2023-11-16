from sqlalchemy.orm import Session

from models.client import Place, UserPlace, User

from apis.client.user.user_schema import Token
from apis.client.place.place_schema import PlaceSchema


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