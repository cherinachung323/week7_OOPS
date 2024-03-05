class InsufficientFundsException(Exception):
    pass


# Defines a custom exception class InsufficientFundsException
# that inherits from the built-in Exception class.
# This exception is raised when a withdrawal is attempted with insufficient funds.

class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def display_info(self):
        print(f"Account Number: {self._account_number}, Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsException("Insufficient funds in the account.")
        self._balance -= amount


# Defines an Account class representing a generic bank account. It has attributes account_number and balance. It also
# includes methods to get and set these attributes, display account information, and withdraw funds. The withdrawal
# method raises InsufficientFundsException if the withdrawal amount exceeds the balance.

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self._interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self._overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self._overdraft_limit = overdraft_limit

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: {self._overdraft_limit}")
# Defines two specialised classes SavingsAccount and CheckingAccount, each inheriting from the Account class. They
# have additional attributes (interest_rate for SavingsAccount and overdraft_limit for CheckingAccount) and override
# the display_info method to include their specific information.

