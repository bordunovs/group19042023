from account import Account, AccountType
import pytest


def test_current_account_initial_balance(current_account):
    assert current_account.get_balance() == 0

def test_current_account_deposit(current_account):
    current_account.deposit(100)
    assert current_account.get_balance() == 100

def test_current_account_withdraw_allowed(current_account):
    current_account.deposit(100)
    assert current_account.withdraw(50)
    assert current_account.get_balance() == 50

def test_current_account_withdraw_not_allowed(current_account):
    current_account.deposit(30)
    current_account.withdraw(50)
    assert current_account.get_balance() == 30
