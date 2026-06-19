class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount} deposited."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"₹{amount} withdrawn."
        return "Insufficient balance!"

    def show_balance(self):
        return f"Current Balance: ₹{self.balance}"


class SavingsAccount(BankAccount):
    interest_rate = 0.06

    def withdraw(self, amount):
        if amount > 30000:
            return "Cannot withdraw more than ₹30,000 at a time!"
        return super().withdraw(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest Added: ₹{interest}"


class CurrentAccount(BankAccount):
    interest_rate = 0.02

    def deposit(self, amount):
        if amount > 300000:
            return "Cannot deposit more than ₹3,00,000 at a time!"
        return super().deposit(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest Added: ₹{interest}"


class LoanAccount(BankAccount):
    def withdraw(self, amount):
        return "Withdrawal is not allowed from Loan Account!"


# Testing
sa = SavingsAccount("Harsh", 50000)

print(sa.withdraw(25000))
print(sa.add_interest())
print(sa.show_balance())