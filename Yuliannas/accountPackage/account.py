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

    # These are property decorators for the first_name attribute. They define a getter method balance() and a setter
    # method balance.setter. The getter method returns the value of _balance, and the setter method sets the value
    # of _balance.
    # def get_balance(self):
    #     return self._balance
    #
    # def set_balance(self, value):
    #     self._balance = value

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, value):
        self._account_number = value

    # This is the __str__() method, which is called when the object needs to be converted to a string. It returns a
    # formatted string containing information about the account.
    def __str__(self):
        info = f"Account Number: {self._account_number}\n"
        info += f"Balance: £{self.balance}\n"
        if self.first_name:
            info += f"First Name: {self.first_name}\n"
        if self.last_name:
            info += f"Last Name: {self.last_name}\n"
        return info

    # This method allows deposits to the account. It increases the balance by the specified amount.
    def deposit(self, amount):
        self.balance += amount

    # This method allows withdrawals from the account. It checks if the balance is sufficient to cover the withdrawal
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficient funds")