from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

# Create database connection
Base = declarative_base()


# Define database table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)