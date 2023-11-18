from sqlalchemy.orm import Session
from sqlalchemy import func, distinct

from typing import List

from models.client import Menu, Order, Cart, CartMenu


def create_order(db: Session, 
                place_id: int,
                cart_menu: List
                ):

    order_number = db.query(func.count(distinct(Order.cart_id))).scalar()+1
    cart = Cart(
                order_number = order_number,
                place_id = place_id,
                ordered_amount = len(cart_menu),
                ordered_price = sum([int(menu["total_price"]) for menu in cart_menu])
            )
    db.add(cart)
    db.commit()
    
    for menu in cart_menu:
        menu_id = db.query(Menu).filter(Menu.name==menu["menu_name"]).first().id
        menu_in_cart = CartMenu(
                                order_number = order_number,
                                menu_id = menu_id,
                                quantity = int(menu["quantity"]),
                                total_price = int(menu["total_price"])
                                )
        db.add(menu_in_cart)
        db.commit()

    current_cart = db.query(Cart).filter(Cart.order_number==order_number).first()
    current_menus = db.query(CartMenu).filter(CartMenu.order_number==order_number)
    for i in range(len(cart_menu)):
        order = Order(
            cart_id=current_cart.id,
            cart_menu_id=current_menus[i].id
        )
        db.add(order)
    db.commit()
    