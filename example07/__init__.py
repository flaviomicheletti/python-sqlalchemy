from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Engine = create_engine("postgresql://username:password@localhost:5432/example")
Session = sessionmaker(bind=Engine)
Base = declarative_base()
