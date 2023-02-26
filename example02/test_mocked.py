import logging
logging.disable(logging.WARNING)

import unittest
from unittest.mock import Mock
from example02.database import Base, User

# Define unit tests
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.session = Mock()

    def test_add_user(self):
        user = User(id=1, name="John", age=30)
        self.session.query.return_value.count.return_value = 0
        self.session.add.return_value = None
        self.session.commit.return_value = None

        self.session.query.return_value.count.return_value = 1
        self.assertEqual(self.session.query(User).count(), 1)

    def test_delete_user(self):
        user = User(id=1, name="Jane", age=25)
        self.session.query.return_value.count.return_value = 1
        self.session.add.return_value = None
        self.session.commit.return_value = None

        self.session.query.return_value.count.return_value = 0
        self.session.delete.return_value = None
        self.session.commit.return_value = None
        self.assertEqual(self.session.query(User).count(), 0)
