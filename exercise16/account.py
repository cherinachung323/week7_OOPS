class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
# This class represents a generic account with attributes account_number and balance.
# The __init__ method serves as the constructor. It initializes the account_number
# and balance attributes when a new object of the class is created.
# The display_info method prints out the account number and balance.

class BankAccount(Account):
    def __init__(self, account_number, balance, account_type):
        super().__init__(account_number, balance)
        self.account_type = account_type

    def display_info(self):
        super().display_info()
        print(f"Account Type: {self.account_type}")
# Inherits from the Account class, implying that it shares common attributes and behaviors with an Account.
# Additional attribute account_type is added to represent the type of bank account.
# The __init__ method initializes both the attributes inherited from Account and the account_type.
# The display_info method overrides the method of the same name in the Account class. I
# t first calls the display_info method of the parent class using super().display_info(),
# then prints out the account type.
# Polymorphism is shown through method overriding in the display_info method

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Savings")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Checking")
