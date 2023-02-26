import unittest
from unittest.mock import patch, Mock

from example08.crud import create, read, update, delete

class TestCrudOperations(unittest.TestCase):
    def setUp(self):
        self.mock_conn = Mock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    def test_create(self):
        # call the create function
        create(self.mock_conn, "Alice", 25)
        # assert that the expected SQL query was executed
        self.mock_conn.execute.assert_called_once_with("INSERT INTO example_table (name, age) VALUES (?, ?)", ("Alice", 25))
        self.mock_conn.commit.assert_called_once()

    def test_read(self):
        # set up some example data
        example_data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
        self.mock_cursor.fetchall.return_value = example_data
        # call the read function
        records = read(self.mock_conn)
        self.assertEqual(records, [])
        self.mock_conn.execute.assert_called_once_with("SELECT * FROM example_table")

    def test_update(self):
        # call the update function
        update(self.mock_conn, 1, "Alice", 30)
        self.mock_conn.execute.assert_called_once_with("UPDATE example_table SET name=?, age=? WHERE id=?", ("Alice", 30, 1))
        self.mock_conn.commit.assert_called_once()

    def test_delete(self):
        # call the delete function
        delete(self.mock_conn, 1)
        # assert that the expected SQL query was executed
        self.mock_conn.execute.assert_called_once_with("DELETE FROM example_table WHERE id=?", (1,))
        self.mock_conn.commit.assert_called_once()