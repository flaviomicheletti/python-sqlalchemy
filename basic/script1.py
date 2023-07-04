from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Set database connection
Engine = create_engine("sqlite:///example1.db", echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

"""
If you run or import this code, it won't interact with the database.
 It simply populates the variables, but it doesn't create a database.
"""