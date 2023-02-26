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
#         user = User(name="John", age=30)
#         self.session.add(user)
#         self.session.commit()
#         self.assertEqual(self.session.query(User).count(), 1)

#     def test_delete_user(self):
#         user = User(name="Jane", age=25)
#         self.session.add(user)
#         self.session.commit()
#         self.session.delete(user)
#         self.session.commit()
#         self.assertEqual(self.session.query(User).count(), 0)


# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
#     result = unittest.TextTestRunner(verbosity=2).run(suite)
#     assert result.wasSuccessful() and result.coverage == 100
