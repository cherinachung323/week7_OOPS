from week7_OOPS.Yuliannas.accountPackage.insufficient_funds_exception import InsufficientFundsException


# defines a class named Account
class Account:
    def __init__(self, first_name, last_name, balance, account_number):
        # He constructor method __init__() for the Account class. It initialises the attributes first_name, last_name,
        # balance, and account_number with the values passed as arguments.
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self._account_number = account_number

    # retrieves and returns the _account_number attribute's value.
    def get_account_number(self):
        return self._account_number

    # setter lets us update the value of the _account_number attribute.
    # takes a parameter value, that represents the new value you want to set for the _account_number.
    # the _account_number attribute is updated with the new value provided by the value parameter
    def set_account_number(self, value):
        self._account_number = value

    # the __str__() method, is called when the object needs to be converted to a string. It returns a formatted string
    # containing information about the account.

    # method allows deposits to the account. It increases the balance by the specified amount.
    def deposit(self, amount):
        self.balance += amount

    # method allows withdrawals from the account, checks if the balance is sufficient to cover the withdrawal
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficient funds")

    def __str__(self):
        info = f"Account Information:\n"
        info += f"Account Number: {self._account_number}\n"
        info += f"Balance: £{self.balance}\n"
        if self.first_name:
            info += f"First Name: {self.first_name}\n"
        if self.last_name:
            info += f"Last Name: {self.last_name}\n"
        return info
