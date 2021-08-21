def check_balance(balance):
    if balance is None:
        raise ValueError("Na-a")


def check_amount(amount):
    if amount < 0:
        raise ValueError("Trying to pull a short one?")


class BankAccount:
    def __init__(self):
        self.balance = None
        self.hasAccount = False

    def open(self):
        if self.hasAccount:
            raise ValueError("You have an open account")

        self.balance = 0
        self.hasAccount = True

    def close(self):
        check_balance(self.balance)
        self.hasAccount = False
        self.balance = None

    def get_balance(self):
        check_balance(self.balance)
        return self.balance

    def deposit(self, amount):
        check_balance(self.balance)
        check_amount(amount)
        self.balance += amount

    def withdraw(self, amount):
        check_balance(self.balance)
        check_amount(amount)
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            raise ValueError("Not enough in the bank")
