import unittest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def test_engine(self):
        self.assertIsNotNone(self.engine)

    def test_session(self):
        session = self.Session()
        self.assertIsNotNone(session)
        session.close()

    def test_base(self):
        self.assertIsNotNone(self.Base)
        self.assertIsNotNone(self.Base.metadata)
        self.assertIsInstance(self.Base.metadata, object)
