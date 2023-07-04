from unittest.mock import Mock
import unittest
from user1.main import User


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.session = Mock()

    def test_add_user(self):
        # self.session.add.return_value = None
        # self.session.commit.return_value = None
        self.session.query.return_value.count.return_value = 1

        user = User(id=1, name="John", age=30)
        self.session.add(user)
        self.session.commit()
        self.assertEqual(self.session.query(User).count(), 1)

    def test_delete_user(self):
        # self.session.add.return_value = None
        # self.session.commit.return_value = None
        # self.session.delete.return_value = None
        # self.session.commit.return_value = None
        self.session.query.return_value.count.return_value = 0

        user = User(id=1, name="Jane", age=25)
        self.session.add(user)
        self.session.commit()
        self.session.delete(user)
        self.session.commit()
        self.assertEqual(self.session.query(User).count(), 0)
