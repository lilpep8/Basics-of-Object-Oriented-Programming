class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        return self.get_balance()


    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.__balance < amount:
            raise ValueError("Insufficient funds in the account")
        self.__balance -= amount
        return self.get_balance()


    def get_balance(self) -> float:
        return self.__balance


    def _set_balance(self, new_balance: float) -> None:
        """метод для изменения баланса (для использования в дочерних классах)"""
        self.__balance = new_balance


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        new_balance = self.get_balance() - amount
        self._set_balance(new_balance)
        return new_balance
