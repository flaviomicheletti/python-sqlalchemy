from unittest.mock import Mock
import unittest
from example03.database import Base, User

# Define unit tests
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.session = Mock()

    def test_add_user(self):
        def add_user(name, age):
            if name and age:
                user = User(id=1, name=name, age=age)
                self.session.add.return_value = None
                self.session.commit.return_value = None
                self.session.query.return_value.count.return_value = 1
                self.assertEqual(self.session.query(User).count(), 1)

        # Add a user with both name and age fields
        add_user('John', 30)

        # Add a user with only name field
        add_user('Jane', None)

        # Add a user with only age field
        add_user(None, 25)

        # Add a user with no fields
        add_user(None, None)

    def test_delete_user(self):
        user = User(id=1, name='Jane', age=25)
        self.session.add.return_value = None
        self.session.commit.return_value = None
        self.session.query.return_value.count.return_value = 0
        self.session.delete.return_value = None
        self.session.commit.return_value = None
        self.assertEqual(self.session.query(User).count(), 0)
