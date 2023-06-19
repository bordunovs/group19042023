import pytest
from account import Account, AccountType


@pytest.fixture
def deposit_account():
    return Account(AccountType.DEPOSIT)

@pytest.fixture
def current_account():
    return Account(AccountType.CURRENT)
