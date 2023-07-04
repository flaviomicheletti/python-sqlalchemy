import unittest
from sqlalchemy import create_engine

Engine = create_engine('sqlite:///:memory:')

class TestDatabase(unittest.TestCase):
    def test_engine(self):
        self.assertEqual(str(Engine.url), 'sqlite:///:memory:')
        self.assertTrue(Engine.connect())

