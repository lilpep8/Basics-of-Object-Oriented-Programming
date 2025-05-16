import pytest
from ..src.bank import SavingsAccount, CheckingAccount


def test_savings_account_operations():
    acc = SavingsAccount('Test', 1000)

    acc.deposit(200)
    assert acc.get_balance() == 1200

    acc.withdraw(100)
    assert acc.get_balance() == 1100

    acc.apply_interest()
    assert acc.get_balance() == 1155 # (5 % от 1100 = 55)

    acc._set_balance(0)
    assert acc.get_balance() == 0


def test_e2e():
    # Test SavingsAccount
    savings = SavingsAccount("Иван")

    savings.deposit(500)
    assert savings.get_balance() == 500

    savings.withdraw(100)
    assert savings.get_balance() == 400

    savings.apply_interest()
    assert savings.get_balance() == 420

    # Test CheckingAccount
    checking = CheckingAccount("Петр", 100)
    checking.withdraw(200)
    assert checking.get_balance() == -100


def test_negative_cases():
    acc = SavingsAccount('Test', 100)
    assert acc.get_balance() == 100

    with pytest.raises(ValueError):
        acc.deposit('a')

    with pytest.raises(ValueError):
        acc.deposit('')

    with pytest.raises(ValueError):
        acc.deposit(0)

    with pytest.raises(ValueError):
        acc.deposit(-100)

    with pytest.raises(ValueError):
        acc.withdraw(0)

    with pytest.raises(ValueError):
        acc.withdraw(-200)

    with pytest.raises(ValueError):
        acc.withdraw(2000)