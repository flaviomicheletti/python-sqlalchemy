import unittest
from example06 import Engine, Session, Base


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
