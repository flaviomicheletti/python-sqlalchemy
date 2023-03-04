import unittest
from unittest.mock import patch
from sqlalchemy.orm import sessionmaker, declarative_base


class TestDatabase(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    def setUp(self, engine_mock):
        self.Engine = engine_mock.return_value
        self.Session = sessionmaker(bind=self.Engine)
        self.Base = declarative_base()

    def test_engine(self):
        self.assertIsNotNone(self.Engine)

    def test_session(self):
        session = self.Session()
        self.assertIsNotNone(session)
        session.close()

    def test_base(self):
        self.assertIsNotNone(self.Base)
        self.assertIsNotNone(self.Base.metadata)
        self.assertIsInstance(self.Base.metadata, object)

"""
based example06.test_core1.py
"""