import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import ArgumentError
from example06 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    def test_engine(self):
        self.assertEqual(str(Engine.url), "sqlite:///:memory:")
        self.assertTrue(Engine.connect())

    def test_create_engine(self):
        with self.assertRaises(ArgumentError):
            create_engine('some invalid connection string')        

    def test_session(self):
        session = Session()
        self.assertEqual(session.bind, Engine)
        self.assertEqual(session.__class__, Session().__class__)
        session.close()

    def test_base(self):
        self.assertTrue(Base)
        self.assertTrue(Base.metadata)
        self.assertGreater(len(Base.metadata.tables), -1)
        self.assertIsInstance(Base.metadata, object)
        self.assertEqual(Base.__class__, declarative_base().__class__)
        self.assertEqual(Base.metadata.__class__, declarative_base().metadata.__class__)        
