import pytest
from enum import Enum, unique

@unique
class AccountType(Enum):
    CURRENT = 0
    DEPOSIT = 1


class Account:
    def __init__(self, account_type: AccountType):
        self.balance = 0
        self.account_type = account_type
        if account_type == AccountType.CURRENT:
            self.credit_allowed = True
        else:
            self.credit_allowed = False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if self.account_type == AccountType.CURRENT or (self.account_type == AccountType.DEPOSIT and self.balance >= amount):
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

# Test for Current Account
class TestCurrentAccount:
    @pytest.fixture
    def current_account(self):
        return Account(AccountType.CURRENT)

    def test_initial_balance(self, current_account):
        assert current_account.get_balance() == 0

    def test_deposit(self, current_account):
        assert current_account.deposit(100) is True
        assert current_account.get_balance() == 100

    def test_withdraw_sufficient_balance(self, current_account):
        current_account.deposit(100)
        assert current_account.withdraw(50) is True
        assert current_account.get_balance() == 50



    def test_withdraw_insufficient_balance(self, current_account):
        current_account.deposit(100)
        assert current_account.withdraw(150) is False
        assert current_account.get_balance() == 100


# Test for Deposit Account
class TestDepositAccount:
    @pytest.fixture
    def deposit_account(self):
        return Account(AccountType.DEPOSIT)

    def test_initial_balance(self, deposit_account):
        assert deposit_account.get_balance() == 0

    def test_deposit(self, deposit_account):
        assert deposit_account.deposit(100) is True
        assert deposit_account.get_balance() == 100

    def test_withdraw_sufficient_balance(self, deposit_account):
        deposit_account.deposit(100)
        assert deposit_account.withdraw(50) is True
        assert deposit_account.get_balance() == 50

    def test_withdraw_insufficient_balance(self, deposit_account):
        deposit_account.deposit(100)
        assert deposit_account.withdraw(150) is False
        assert deposit_account.get_balance() == 100
