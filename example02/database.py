from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Set database connection
Engine = create_engine("sqlite:///example2.db", echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()


# Define database table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
