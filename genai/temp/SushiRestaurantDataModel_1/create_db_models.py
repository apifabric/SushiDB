# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Restaurant(Base):\n    __tablename__ = 'restaurant'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    address = Column(String)\n    description = Column(Text)


class Chef(Base):\n    __tablename__ = 'chef'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    specialty = Column(String)\n    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))


class Menu(Base):\n    __tablename__ = 'menu'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(Text)\n    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))


class Ingredient(Base):\n    __tablename__ = 'ingredient'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(String)


class Dish(Base):\n    __tablename__ = 'dish'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    price = Column(Integer, nullable=False)\n    menu_id = Column(Integer, ForeignKey('menu.id'))\n    description = Column(Text)


class MenuItem(Base):\n    __tablename__ = 'menu_item'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    dish_id = Column(Integer, ForeignKey('dish.id'))\n    menu_id = Column(Integer, ForeignKey('menu.id'))


class Supplier(Base):\n    __tablename__ = 'supplier'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    contact_info = Column(String)


class Supply(Base):\n    __tablename__ = 'supply'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))\n    supplier_id = Column(Integer, ForeignKey('supplier.id'))\n    quantity = Column(Integer)


class Reservation(Base):\n    __tablename__ = 'reservation'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    customer_name = Column(String, nullable=False)\n    date_time = Column(DateTime)\n    guests = Column(Integer, nullable=False)\n    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))


class Customer(Base):\n    __tablename__ = 'customer'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    phone = Column(String)\n    email = Column(String)


class Feedback(Base):\n    __tablename__ = 'feedback'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    customer_id = Column(Integer, ForeignKey('customer.id'))\n    comments = Column(Text)\n    rating = Column(Integer, nullable=True)


class Review(Base):\n    __tablename__ = 'review'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    chef_id = Column(Integer, ForeignKey('chef.id'))\n    review_comments = Column(Text)\n    date_time = Column(DateTime)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    restaurant1 = Restaurant(name=\
    restaurant2 = Restaurant(name=\"Sushi Zen\", address=\"654 Elm St\", description=\"A fusion of tradition and modern sushi techniques.\")
    restaurant3 = Restaurant(name=\"Omakase Heaven\", address=\"789 Pine St\", description=\"Dedicated to Omakase style sushi dining.\")
    restaurant4 = Restaurant(name=\"Tokyo Sushi House\", address=\"321 Oak St\", description=\"Authentic Tokyo-style sushi experience.\")
    chef1 = Chef(name=\"Hiro Tanaka\", specialty=\"Sashimi\", restaurant_id=1)
    chef2 = Chef(name=\"Masako Yoshi\", specialty=\"Nigiri\", restaurant_id=2)
    chef3 = Chef(name=\"Ken Ichiro\", specialty=\"Maki\", restaurant_id=3)
    chef4 = Chef(name=\"Akira Suzuki\", specialty=\"Tempura\", restaurant_id=4)
    menu1 = Menu(name=\"Lunch Special\", description=\"Affordable sushi lunch items\", restaurant_id=1)
    menu2 = Menu(name=\"Dinner Feast\", description=\"Sumptuous dinner sashimi selections\", restaurant_id=2)
    menu3 = Menu(name=\"Weekend Brunch\", description=\"Weekend special brunch menu\", restaurant_id=3)
    menu4 = Menu(name=\"Omakase Collection\", description=\"Chef's finest Omakase\", restaurant_id=4)
    ingredient1 = Ingredient(name=\"Salmon\", description=\"Freshly sourced Atlantic salmon.\")
    ingredient2 = Ingredient(name=\"Tuna\", description=\"Deep-sea wild tuna.\")
    ingredient3 = Ingredient(name=\"Eel\", description=\"Grilled eel with a sweet sauce.\")
    ingredient4 = Ingredient(name=\"Rice\", description=\"Premium sushi rice.\")
    dish1 = Dish(name=\"Spicy Tuna Roll\", price=10, menu_id=1, description=\"Spicy tuna wrapped with fresh avocado and rice.\")
    dish2 = Dish(name=\"Salmon Sashimi\", price=15, menu_id=2, description=\"Exquisitely sliced salmon sashimi.\")
    dish3 = Dish(name=\"Eel Nigiri\", price=8, menu_id=3, description=\"Freshwater eel atop vinegared rice.\")
    dish4 = Dish(name=\"Omakase Special\", price=30, menu_id=4, description=\"Chef's choice special dish.\")
    menuItem1 = MenuItem(dish_id=1, menu_id=1)
    menuItem2 = MenuItem(dish_id=2, menu_id=2)
    menuItem3 = MenuItem(dish_id=3, menu_id=3)
    menuItem4 = MenuItem(dish_id=4, menu_id=4)
    supplier1 = Supplier(name=\"Atlantic Seafood Co.\", contact_info=\"atlantic@seafood.com\")
    supplier2 = Supplier(name=\"Ocean's Harvest\", contact_info=\"harvest@seafoodsupply.com\")
    supplier3 = Supplier(name=\"Rice Masters\", contact_info=\"info@ricemasters.com\")
    supplier4 = Supplier(name=\"Eel Emporium\", contact_info=\"sales@eelemporium.com\")
    supply1 = Supply(ingredient_id=1, supplier_id=1, quantity=50)
    supply2 = Supply(ingredient_id=2, supplier_id=2, quantity=30)
    supply3 = Supply(ingredient_id=3, supplier_id=4, quantity=20)
    supply4 = Supply(ingredient_id=4, supplier_id=3, quantity=200)
    reservation1 = Reservation(customer_name=\"John Doe\", date_time=date(2023, 12, 24), guests=4, restaurant_id=1)
    reservation2 = Reservation(customer_name=\"Jane Smith\", date_time=date(2023, 12, 25), guests=2, restaurant_id=2)
    reservation3 = Reservation(customer_name=\"Mike Johnson\", date_time=date(2023, 12, 26), guests=3, restaurant_id=3)
    reservation4 = Reservation(customer_name=\"Emily Davis\", date_time=date(2023, 12, 27), guests=5, restaurant_id=4)
    customer1 = Customer(name=\"Alice\", phone=\"123-456-7890\", email=\"alice@example.com\")
    customer2 = Customer(name=\"Bob\", phone=\"234-567-8901\", email=\"bob@example.com\")
    customer3 = Customer(name=\"Charlie\", phone=\"345-678-9012\", email=\"charlie@example.com\")
    customer4 = Customer(name=\"David\", phone=\"456-789-0123\", email=\"david@example.com\")
    feedback1 = Feedback(customer_id=1, comments=\"Excellent sushi and great service!\", rating=5)
    feedback2 = Feedback(customer_id=2, comments=\"Good experience, will come again.\", rating=4)
    feedback3 = Feedback(customer_id=3, comments=\"Average, worth a visit.\", rating=3)
    feedback4 = Feedback(customer_id=4, comments=\"Not upto the standards expected.\", rating=2)
    review1 = Review(chef_id=1, review_comments=\"Amazing artist, great presentation.\", date_time=date(2023, 10, 5))
    review2 = Review(chef_id=2, review_comments=\"Skilled in cutting techniques.\", date_time=date(2023, 10, 10))
    review3 = Review(chef_id=3, review_comments=\"Innovative and delicious.\", date_time=date(2023, 10, 15))
    review4 = Review(chef_id=4, review_comments=\"Needs improvement in time management.\", date_time=date(2023, 10, 20))
    
    
    
    session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, chef1, chef2, chef3, chef4, menu1, menu2, menu3, menu4, ingredient1, ingredient2, ingredient3, ingredient4, dish1, dish2, dish3, dish4, menuItem1, menuItem2, menuItem3, menuItem4, supplier1, supplier2, supplier3, supplier4, supply1, supply2, supply3, supply4, reservation1, reservation2, reservation3, reservation4, customer1, customer2, customer3, customer4, feedback1, feedback2, feedback3, feedback4, review1, review2, review3, review4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
