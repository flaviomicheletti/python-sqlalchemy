import unittest
from user2.main import Engine, Base, Session, User


class TestDatabase(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(Engine)
        self.session = Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()
        Base.metadata.drop_all(Engine)

    def test_add_user(self):
        user = User(name="John", age=30)
        self.session.add(user)
        self.session.commit()
        self.assertEqual(self.session.query(User).count(), 1)

    def test_delete_user(self):
        user = User(name="Jane", age=25)
        self.session.add(user)
        self.session.commit()
        self.session.delete(user)
        self.session.commit()
        self.assertEqual(self.session.query(User).count(), 0)

    def test_duplicate_email(self):
        user1 = User(name="Alice", email="alice@example.com")
        self.session.add(user1)
        self.session.commit()

        user2 = User(name="Bob", email="alice@example.com")
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()

