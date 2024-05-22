#!/usr/bin/python3
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_url = 'mysql+mysqldb://eric:1016@localhost/ubagri'

engine = create_engine(database_url)

Base = declarative_base()

class User(Base):
    """User table"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_number = Column(String(10), unique=True, nullable=False)
    

    def __repr__(self):
        return f"User('{self.firstname}' '{self.lastname}' '{self.phone_number}')"


class Address(Base):
    """Address table"""
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    country = Column(String(20), nullable=False)
    province = Column(String(20), nullable=False)
    district = Column(String(20), nullable=False)
    sector = Column(String(20), nullable=False)
    cell = Column(String(20), nullable=False)
    village = Column(String(20), nullable=False)
    
    def __repr__(self):
        return f"Address('{self.district}' - '{self.country}')"
    

class Weather(Base):
    """weather predication with API"""
    address_id = Column(Integer, ForeignKey=True)
    Temperature = Column(String(10), nullable=False)
    Weather = Column(String(20))

class product():
    """Product information"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(String(20), nullable=False)
    quantity = Column(String(20), nullable=False)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()