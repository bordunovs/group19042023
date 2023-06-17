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

