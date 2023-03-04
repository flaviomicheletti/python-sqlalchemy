from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=Engine)
Base = declarative_base()
