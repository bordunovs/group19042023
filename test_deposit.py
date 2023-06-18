from account_1 import Account, AccountType
import pytest
def test_deposit(deposit_account):
    deposit_account.deposit(100)
    assert deposit_account.get_balance() == 100


def test_withdraw_sufficient_balance(deposit_account):
    deposit_account.deposit(100)
    result = deposit_account.withdraw(50)
    assert result is True
    assert deposit_account.get_balance() == 50


def test_withdraw_insufficient_balance(deposit_account):
    deposit_account.deposit(100)
    result = deposit_account.withdraw(150)
    assert result is False
    assert deposit_account.get_balance() == 100


def test_withdraw_overdraft_from_current_account(current_account):
    current_account.deposit(100)
    result = current_account.withdraw(150)
    assert result is True
    assert current_account.get_balance() == -50


def test_withdraw_overdraft_not_allowed(current_account):
    current_account.deposit(100)
    current_account.credit_allowed = False
    result = current_account.withdraw(150)
    assert result is False
    assert current_account.get_balance() == 100

