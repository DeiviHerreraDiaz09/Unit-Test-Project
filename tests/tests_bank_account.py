import unittest
import src.bank_account as b

class BankAccountTests(unittest.TestCase):

    def test_deposit(self):
        account = b.BankAccount(balance=5)
        new_balance = account.deposit(100)
        assert new_balance == 105

    def test_withdraw(self):
        account = b.BankAccount(balance=1000)
        new_balance = account.withdraw(100)
        assert new_balance == 900

