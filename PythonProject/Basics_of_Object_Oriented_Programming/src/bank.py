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


class SavingsAccount(BankAccount):

    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


    def apply_interest(self) -> float:
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return self.get_balance()


class CheckingAccount(BankAccount):

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._set_balance(self.get_balance() - amount)
        return self.get_balance()


# savings_acc = SavingsAccount("Иван Иванов", 0)# создать экземпляр класса SavingsAccount
#
# savings_acc.deposit(500)  # Вносим депозит 500
#
# savings_acc.withdraw(100)  # списать с него 100
#
# savings_acc.apply_interest()  # применить начисление процентов
#
# print(f"Итоговый баланс: {savings_acc.get_balance()}")  # Выведет: 420