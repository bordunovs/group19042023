from account import Account, AccountType
import pytest

import pytest

@pytest.fixture
def deposit_account():
    return Account(AccountType.DEPOSIT)

def test_deposit_account_initial_balance(deposit_account):
    assert deposit_account.get_balance() == 0

def test_deposit_account_deposit(deposit_account):
    deposit_account.deposit(100)
    assert deposit_account.get_balance() == 100

def test_deposit_account_deposit_negative_amount(deposit_account):
    deposit_account.deposit(-50)
    assert deposit_account.get_balance() == 0

def test_deposit_account_withdraw_allowed(deposit_account):
    deposit_account.deposit(100)
    assert deposit_account.withdraw(50)
    assert deposit_account.get_balance() == 50
