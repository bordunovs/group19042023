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


