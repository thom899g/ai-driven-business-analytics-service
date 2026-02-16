from sqlalchemy import Column, Integer, String, Date, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Business(Base):
    __tablename__ = "businesses"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    industry = Column(String(50))
    registration_date = Column(Date)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    date = Column(Date)

# Create the database engine and tables
engine = create_engine('sqlite:///evolution_analytics.db')
Base.metadata.create_all(engine)