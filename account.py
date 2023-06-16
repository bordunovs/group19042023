import pytest

class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


@pytest.fixture
def deposit_account():
    return Account(100)  # Початковий баланс - 100 для депозитного рахунку


@pytest.fixture
def current_account():
    return Account(500)  # Початковий баланс - 500 для поточного рахунку


# Тести для депозитного рахунку
def test_deposit(deposit_account):
    deposit_account.deposit(50)
    assert deposit_account.get_balance() == 150


def test_withdraw(deposit_account):
    deposit_account.withdraw(30)
    assert deposit_account.get_balance() == 70


# Тести для поточного рахунку
def test_deposit(current_account):
    current_account.deposit(200)
    assert current_account.get_balance() == 700


def test_withdraw(current_account):
    current_account.withdraw(100)
    assert current_account.get_balance() == 400


