from Basics_of_Object_Oriented_Programming.src.bank import SavingsAccount

def test_savings_account_operations():
    acc = SavingsAccount('Test', 1000)

    acc.deposit(500)
    assert acc.get_balance() == 1500

    acc.withdraw(100)
    assert acc.get_balance() == 1400

    acc.apply_interest()
    assert acc.get_balance() == 1470 # (5 % от 1400 = 70)