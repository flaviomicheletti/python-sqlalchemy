import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=Engine)
Base = declarative_base()


class TestDatabase(unittest.TestCase):
    def test_engine(self):
        self.assertIsNotNone(Engine)

    def test_session(self):
        session = Session()
        self.assertIsNotNone(session)
        session.close()

    def test_base(self):
        self.assertIsNotNone(Base)
        self.assertIsNotNone(Base.metadata)
        self.assertIsInstance(Base.metadata, object)
