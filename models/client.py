from ast import In
from enum import Flag
from re import I
from sys import flags
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from apis.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Place(Base):
    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)


class UserPlace(Base):
    __tablename__ = "user_place"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    place_id = Column(Integer, ForeignKey("place.id"), primary_key=True)


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    place_id = Column(Integer, ForeignKey("place.id"))
    place = relationship("Place", backref="menus")
    quantity = Column(Integer, nullable=False, default=1)
    out_of_stock = Column(Boolean, nullable=False, default=False)


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer, nullable=False)
    place_id = Column(Integer, ForeignKey("place.id"))
    ordered_amount = Column(Integer, nullable=False)
    ordered_price = Column(Float, nullable=False)


class CartMenu(Base):
    __tablename__ = "cart_menu"

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer, nullable=False)
    menu_id = Column(Integer, ForeignKey("menu.id"))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)


class Order(Base):
    __tablename__ = "order"
    
    cart_id = Column(Integer, ForeignKey("cart.id"), primary_key=True)
    cart_menu_id = Column(Integer, ForeignKey("cart_menu.id"), primary_key=True)
