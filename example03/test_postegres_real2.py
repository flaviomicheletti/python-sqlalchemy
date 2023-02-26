import unittest
from example03.database import Engine, Base, Session, User

# class TestDatabase(unittest.TestCase):
#     def setUp(self):
#         Base.metadata.create_all(Engine)
#         self.session = Session()

#     def tearDown(self):
#         self.session.rollback()
#         self.session.close()
#         Base.metadata.drop_all(Engine)

#     def test_add_user(self):
#         def add_user(name, age):
#             if name and age:
#                 user = User(name=name, age=age)
#                 self.session.add(user)
#                 self.session.commit()

#         # Add a user with both name and age fields
#         add_user('John', 30)
#         self.assertEqual(self.session.query(User).count(), 1)

#         # Add a user with only name field
#         add_user('Jane', None)
#         self.assertEqual(self.session.query(User).count(), 1)

#         # Add a user with only age field
#         add_user(None, 25)
#         self.assertEqual(self.session.query(User).count(), 1)

#         # Add a user with no fields
#         add_user(None, None)
#         self.assertEqual(self.session.query(User).count(), 1)

#     def test_delete_user(self):
#         user = User(name='Jane', age=25)
#         self.session.add(user)
#         self.session.commit()
#         self.session.delete(user)
#         self.session.commit()
#         self.assertEqual(self.session.query(User).count(), 0)

# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
#     result = unittest.TextTestRunner(verbosity=2).run(suite)
#     assert result.wasSuccessful() and result.coverage == 100
