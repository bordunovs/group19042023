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

