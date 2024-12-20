# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DECIMAL, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 20, 2024 15:18:06
# Database: sqlite:////tmp/tmp.cUpmxkVqvf-01JFJA48E1KQET3X4BP48ET18G/SushiRestaurantDataModel/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Represents customers of the sushi restaurant.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    RatingList : Mapped[List["Rating"]] = relationship(back_populates="customer")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="customer")



class Restaurant(SAFRSBaseX, Base):
    """
    description: Represents a sushi restaurant with basic information.
    """
    __tablename__ = 'restaurant'
    _s_collection_name = 'Restaurant'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    established_date = Column(Date)
    is_chain = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuList : Mapped[List["Menu"]] = relationship(back_populates="restaurant")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="restaurant")
    RatingList : Mapped[List["Rating"]] = relationship(back_populates="restaurant")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="restaurant")
    StaffList : Mapped[List["Staff"]] = relationship(back_populates="restaurant")



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents a supplier for sushi ingredients.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    IngredientList : Mapped[List["Ingredient"]] = relationship(back_populates="supplier")



class Ingredient(SAFRSBaseX, Base):
    """
    description: Represents ingredients used in sushi dishes.
    """
    __tablename__ = 'ingredient'
    _s_collection_name = 'Ingredient'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    supplier_id = Column(ForeignKey('supplier.id'))
    price_per_unit : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("IngredientList"))

    # child relationships (access children)



class Menu(SAFRSBaseX, Base):
    """
    description: Represents the menu of a sushi restaurant.
    """
    __tablename__ = 'menu'
    _s_collection_name = 'Menu'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    name = Column(String)
    description = Column(String)
    available = Column(Boolean)
    created_date = Column(Date)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("MenuList"))

    # child relationships (access children)
    MenuItemList : Mapped[List["MenuItem"]] = relationship(back_populates="menu")



class Order(SAFRSBaseX, Base):
    """
    description: Represents customer orders at the restaurant.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    customer_id = Column(ForeignKey('customer.id'))
    order_date = Column(DateTime)
    total_amount : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Rating(SAFRSBaseX, Base):
    """
    description: Represents the ratings given by customers for a sushi restaurant.
    """
    __tablename__ = 'rating'
    _s_collection_name = 'Rating'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    customer_id = Column(ForeignKey('customer.id'))
    rating = Column(Integer)
    comment = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("RatingList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("RatingList"))

    # child relationships (access children)



class Reservation(SAFRSBaseX, Base):
    """
    description: Represents table reservations made by customers.
    """
    __tablename__ = 'reservation'
    _s_collection_name = 'Reservation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    customer_id = Column(ForeignKey('customer.id'))
    reservation_date = Column(DateTime)
    number_of_guests = Column(Integer)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReservationList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("ReservationList"))

    # child relationships (access children)



class Staff(SAFRSBaseX, Base):
    """
    description: Represents the staff working at the sushi restaurant.
    """
    __tablename__ = 'staff'
    _s_collection_name = 'Staff'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    job_title = Column(String)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    hire_date = Column(Date)
    salary : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("StaffList"))

    # child relationships (access children)
    ShiftList : Mapped[List["Shift"]] = relationship(back_populates="staff")



class MenuItem(SAFRSBaseX, Base):
    """
    description: Represents individual items in a menu.
    """
    __tablename__ = 'menu_item'
    _s_collection_name = 'MenuItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    menu_id = Column(ForeignKey('menu.id'))
    name = Column(String)
    description = Column(String)
    price : DECIMAL = Column(DECIMAL)
    is_vegan = Column(Boolean)
    is_gluten_free = Column(Boolean)

    # parent relationships (access parent)
    menu : Mapped["Menu"] = relationship(back_populates=("MenuItemList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="menu_item")



class Shift(SAFRSBaseX, Base):
    """
    description: Represents shifts assigned to staff at the restaurant.
    """
    __tablename__ = 'shift'
    _s_collection_name = 'Shift'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    staff_id = Column(ForeignKey('staff.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    staff : Mapped["Staff"] = relationship(back_populates=("ShiftList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Represents ordered items in a customer's order.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    menu_item_id = Column(ForeignKey('menu_item.id'))
    quantity = Column(Integer)
    subtotal : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("OrderItemList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
