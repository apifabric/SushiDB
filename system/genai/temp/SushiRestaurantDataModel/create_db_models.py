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


class Restaurant(Base):
    """description: Represents a sushi restaurant with basic information."""
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    established_date = Column(Date)
    is_chain = Column(Boolean)



class Menu(Base):
    """description: Represents the menu of a sushi restaurant."""
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    name = Column(String)
    description = Column(String)
    available = Column(Boolean)
    created_date = Column(Date)



class MenuItem(Base):
    """description: Represents individual items in a menu."""
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    name = Column(String)
    description = Column(String)
    price = Column(DECIMAL)
    is_vegan = Column(Boolean)
    is_gluten_free = Column(Boolean)



class Supplier(Base):
    """description: Represents a supplier for sushi ingredients."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)



class Ingredient(Base):
    """description: Represents ingredients used in sushi dishes."""
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    price_per_unit = Column(DECIMAL)



class Order(Base):
    """description: Represents customer orders at the restaurant."""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_date = Column(DateTime)
    total_amount = Column(DECIMAL)



class Customer(Base):
    """description: Represents customers of the sushi restaurant."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)



class OrderItem(Base):
    """description: Represents ordered items in a customer's order."""
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    quantity = Column(Integer)
    subtotal = Column(DECIMAL)



class Staff(Base):
    """description: Represents the staff working at the sushi restaurant."""
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    job_title = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    hire_date = Column(Date)
    salary = Column(DECIMAL)



class Rating(Base):
    """description: Represents the ratings given by customers for a sushi restaurant."""
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    rating = Column(Integer)
    comment = Column(String)



class Shift(Base):
    """description: Represents shifts assigned to staff at the restaurant."""
    __tablename__ = 'shift'

    id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)



class Reservation(Base):
    """description: Represents table reservations made by customers."""
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    reservation_date = Column(DateTime)
    number_of_guests = Column(Integer)



# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    restaurant1 = Restaurant(id=1, name="Sushi World", address="123 Sushi St.", phone_number="123-456-7890", email="info@sushiworld.com", established_date=date(2010, 5, 10), is_chain=False)
    restaurant2 = Restaurant(id=2, name="Sushi House", address="456 Tempura Ln.", phone_number="987-654-3210", email="contact@sushihouse.com", established_date=date(2015, 8, 20), is_chain=True)
    restaurant3 = Restaurant(id=3, name="Nori's", address="789 Maki Ave.", phone_number="564-789-1234", email="hello@norissushi.com", established_date=date(2012, 7, 18), is_chain=False)
    restaurant4 = Restaurant(id=4, name="Oishii Place", address="321 Nigiri Dr.", phone_number="321-987-6543", email="enquiries@oishiiplace.com", established_date=date(2018, 11, 25), is_chain=True)
    menu1 = Menu(id=1, restaurant_id=1, name="Lunch Specials", description="Affordable lunch options", available=True, created_date=date(2021, 4, 1))
    menu2 = Menu(id=2, restaurant_id=1, name="Dinner Delights", description="Gourmet dinner choices", available=True, created_date=date(2021, 6, 15))
    menu3 = Menu(id=3, restaurant_id=2, name="Evening Bites", description="Snacks for the evening", available=True, created_date=date(2021, 7, 20))
    menu4 = Menu(id=4, restaurant_id=3, name="Chef Specials", description="Exclusive dishes", available=False, created_date=date(2021, 8, 5))
    menu_item1 = MenuItem(id=1, menu_id=1, name="California Roll", description="Classic roll with crab and avocado", price=8.99, is_vegan=False, is_gluten_free=True)
    menu_item2 = MenuItem(id=2, menu_id=2, name="Spring Roll", description="Fresh vegetable rolls", price=6.99, is_vegan=True, is_gluten_free=True)
    menu_item3 = MenuItem(id=3, menu_id=3, name="Sashimi Mix", description="Assorted sashimi platter", price=12.99, is_vegan=False, is_gluten_free=True)
    menu_item4 = MenuItem(id=4, menu_id=4, name="Tempura Delight", description="Mixed tempura selection", price=10.99, is_vegan=False, is_gluten_free=False)
    supplier1 = Supplier(id=1, name="Fish Supply Co.", address="789 Fish Market Ave.", contact_number="800-456-2598")
    supplier2 = Supplier(id=2, name="Vegan Organics", address="123 Tofu St.", contact_number="800-123-0098")
    supplier3 = Supplier(id=3, name="Produce Partners", address="456 Greens Ln.", contact_number="800-999-8745")
    supplier4 = Supplier(id=4, name="Rice & More", address="321 Rice Rd.", contact_number="800-321-9873")
    ingredient1 = Ingredient(id=1, name="Salmon", description="Fresh Atlantic salmon", supplier_id=1, price_per_unit=5.99)
    ingredient2 = Ingredient(id=2, name="Nori", description="Dried seaweed sheets", supplier_id=4, price_per_unit=0.89)
    ingredient3 = Ingredient(id=3, name="Avocado", description="Fresh creamy avocados", supplier_id=3, price_per_unit=1.49)
    ingredient4 = Ingredient(id=4, name="Tofu", description="Organic firm tofu", supplier_id=2, price_per_unit=2.99)
    order1 = Order(id=1, restaurant_id=1, customer_id=1, order_date=datetime(2023, 9, 12, 18, 30), total_amount=22.97)
    order2 = Order(id=2, restaurant_id=2, customer_id=2, order_date=datetime(2023, 9, 13, 19, 15), total_amount=16.98)
    order3 = Order(id=3, restaurant_id=3, customer_id=3, order_date=datetime(2023, 9, 14, 12, 45), total_amount=11.98)
    order4 = Order(id=4, restaurant_id=1, customer_id=4, order_date=datetime(2023, 9, 15, 14, 30), total_amount=29.97)
    customer1 = Customer(id=1, first_name="John", last_name="Doe", email="john.doe@example.com", phone_number="555-1234", address="123 Example St.")
    customer2 = Customer(id=2, first_name="Jane", last_name="Smith", email="jane.smith@example.com", phone_number="555-5678", address="456 Example Ave.")
    customer3 = Customer(id=3, first_name="Alice", last_name="Johnson", email="alice.j@example.com", phone_number="555-8765", address="789 Example Blvd.")
    customer4 = Customer(id=4, first_name="Bob", last_name="Brown", email="bob.brown@example.com", phone_number="555-4321", address="321 Example Dr.")
    order_item1 = OrderItem(id=1, order_id=1, menu_item_id=1, quantity=2, subtotal=17.98)
    order_item2 = OrderItem(id=2, order_id=2, menu_item_id=2, quantity=1, subtotal=6.99)
    order_item3 = OrderItem(id=3, order_id=3, menu_item_id=3, quantity=1, subtotal=12.99)
    order_item4 = OrderItem(id=4, order_id=4, menu_item_id=4, quantity=3, subtotal=32.97)
    staff1 = Staff(id=1, first_name="Sue", last_name="Chef", job_title="Head Chef", restaurant_id=1, hire_date=date(2019, 3, 15), salary=55000.00)
    staff2 = Staff(id=2, first_name="Tom", last_name="Waiter", job_title="Server", restaurant_id=2, hire_date=date(2020, 4, 20), salary=35000.00)
    staff3 = Staff(id=3, first_name="Jen", last_name="Manager", job_title="Restaurant Manager", restaurant_id=3, hire_date=date(2018, 8, 5), salary=65000.00)
    staff4 = Staff(id=4, first_name="Max", last_name="Hostess", job_title="Hostess", restaurant_id=4, hire_date=date(2021, 2, 10), salary=32000.00)
    rating1 = Rating(id=1, restaurant_id=1, customer_id=1, rating=5, comment="Excellent sushi!")
    rating2 = Rating(id=2, restaurant_id=2, customer_id=2, rating=4, comment="Great ambiance")
    rating3 = Rating(id=3, restaurant_id=3, customer_id=3, rating=3, comment="Okay experience")
    rating4 = Rating(id=4, restaurant_id=4, customer_id=4, rating=2, comment="Needs improvement")
    shift1 = Shift(id=1, staff_id=1, start_time=datetime(2023, 9, 12, 9, 0), end_time=datetime(2023, 9, 12, 17, 0))
    shift2 = Shift(id=2, staff_id=2, start_time=datetime(2023, 9, 13, 10, 0), end_time=datetime(2023, 9, 13, 18, 0))
    shift3 = Shift(id=3, staff_id=3, start_time=datetime(2023, 9, 14, 11, 0), end_time=datetime(2023, 9, 14, 19, 0))
    shift4 = Shift(id=4, staff_id=4, start_time=datetime(2023, 9, 15, 9, 0), end_time=datetime(2023, 9, 15, 17, 0))
    reservation1 = Reservation(id=1, restaurant_id=1, customer_id=1, reservation_date=datetime(2023, 9, 16, 20, 0), number_of_guests=3)
    reservation2 = Reservation(id=2, restaurant_id=2, customer_id=2, reservation_date=datetime(2023, 9, 17, 19, 0), number_of_guests=2)
    reservation3 = Reservation(id=3, restaurant_id=3, customer_id=3, reservation_date=datetime(2023, 9, 18, 18, 30), number_of_guests=4)
    reservation4 = Reservation(id=4, restaurant_id=4, customer_id=4, reservation_date=datetime(2023, 9, 19, 20, 0), number_of_guests=5)
    
    
    
    session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, menu1, menu2, menu3, menu4, menu_item1, menu_item2, menu_item3, menu_item4, supplier1, supplier2, supplier3, supplier4, ingredient1, ingredient2, ingredient3, ingredient4, order1, order2, order3, order4, customer1, customer2, customer3, customer4, order_item1, order_item2, order_item3, order_item4, staff1, staff2, staff3, staff4, rating1, rating2, rating3, rating4, shift1, shift2, shift3, shift4, reservation1, reservation2, reservation3, reservation4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
