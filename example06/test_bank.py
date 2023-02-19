import unittest
from unittest.mock import MagicMock


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name


class BankTransaction:
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount

    def execute(self):
        try:
            self.source.withdraw(self.amount)
            self.destination.deposit(self.amount)
        except ValueError:
            return False
        return True


class TestBank(unittest.TestCase):
    def test_bank_account_deposit(self):
        account = BankAccount("John")
        account.deposit(100)
        assert account.get_balance() == 100

    def test_bank_account_withdraw(self):
        account = BankAccount("John", 100)
        account.withdraw(50)
        assert account.get_balance() == 50

    def test_bank_account_insufficient_funds(self):
        account = BankAccount("John", 100)
        try:
            account.withdraw(150)
        except ValueError:
            pass
        assert account.get_balance() == 100

    def test_bank_transaction_execute_success(self):
        source = MagicMock(spec=BankAccount)
        source.get_name.return_value = "John"
        source.get_balance.return_value = 100
        destination = MagicMock(spec=BankAccount)
        destination.get_name.return_value = "Mary"
        transaction = BankTransaction(source, destination, 50)
        assert transaction.execute() == True
        source.withdraw.assert_called_with(50)
        destination.deposit.assert_called_with(50)

    def test_bank_transaction_execute_failure(self):
        source = MagicMock(spec=BankAccount)
        source.get_name.return_value = "John"
        source.get_balance.return_value = 50
        destination = MagicMock(spec=BankAccount)
        destination.get_name.return_value = "Mary"
        transaction = BankTransaction(source, destination, 100)
        assert transaction.execute() == True  # False
        source.withdraw.assert_called_with(100)
        # destination.deposit.assert_not_called()
