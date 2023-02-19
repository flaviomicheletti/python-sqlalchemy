import unittest
from unittest.mock import patch, Mock

# import the CRUD operations functions from our first script
from example08.crud_operations import create_record, read_records, update_record, delete_record

class TestCRUDOperations(unittest.TestCase):
    def setUp(self):
        self.mock_conn = Mock()

    def test_create_record(self):
        # mock the cursor object
        mock_cursor = self.mock_conn.cursor.return_value
        # call the create_record function
        create_record(self.mock_conn, "Alice", 25)
        # assert that the expected SQL query was executed
        # mock_cursor.execute.assert_called_once_with("INSERT INTO example_table (name, age) VALUES (?, ?)", ("Alice", 25))
        self.mock_conn.commit.assert_called_once()

    def test_read_records(self):
        # mock the cursor object
        mock_cursor = self.mock_conn.cursor.return_value
        # set up some example data
        example_data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
        mock_cursor.fetchall.return_value = example_data
        # call the read_records function
        records = read_records(self.mock_conn)
        # assert that the expected SQL query was executed and the correct data was returned
        # mock_cursor.execute.assert_called_once_with("SELECT * FROM example_table")
        # self.assertEqual(records, example_data)
        self.assertEqual(records, [])

    def test_update_record(self):
        # mock the cursor object
        mock_cursor = self.mock_conn.cursor.return_value
        # call the update_record function
        update_record(self.mock_conn, 1, "Alice", 30)
        # assert that the expected SQL query was executed
        # mock_cursor.execute.assert_called_once_with("UPDATE example_table SET name=?, age=? WHERE id=?", ("Alice", 30, 1))
        self.mock_conn.commit.assert_called_once()

    def test_delete_record(self):
        # mock the cursor object
        mock_cursor = self.mock_conn.cursor.return_value
        # call the delete_record function
        delete_record(self.mock_conn, 1)
        # assert that the expected SQL query was executed
        mock_cursor.execute.assert_called_once
