from week7_OOPS.Yuliannas.accountPackage.account import Account
from week7_OOPS.Yuliannas.accountPackage.insufficient_funds_exception import InsufficientFundsException


# CODE: defines a CheckingAccount class with functionality to withdraw funds and display account information, while also
# handling overdraft limits and exceptions related to insufficient funds

#  defining the CheckingAccount class, which inherits from the Account class.
class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        # constructor method for the CheckingAccount class. It takes four parameters: account_number, balance, and
        # overdraft_limit. It initialises a new CheckingAccount object with the provided account number, balance,
        # and overdraft limit.
        super().__init__(None, None, balance, account_number)  # No first_name or last_name needed
        # calls the constructor of the superclass (Account) to initialise attributes inherited from the Account class.
        # It passes None for the first_name and last_name parameters because they are not required for a CheckingAccount.
        self._overdraft_limit = overdraft_limit
        # initialises the overdraft_limit attribute of the CheckingAccount object with the provided overdraft limit.

    # Retrieving the value of the _overdraft_limit attribute. Not taking any arguments besides self, which is a reference
    # to the instance of the class itself. self._overdraft_limit is returned it provides the current value of the
    # overdraft limit attribute.
    def get_overdraft_limit(self):
        return self._overdraft_limit

    # setter method, responsible for setting/updating the value of the _overdraft_limit attribute.
    # It takes an additional argument value, which represents the new value to assign to the overdraft limit.
    # Inside the method, self._overdraft_limit = value assigns the provided value to the _overdraft_limit attribute
    # of the instance.
    def set_overdraft_limit(self, value):
        self._overdraft_limit = value

    def withdraw(self, amount):
        if self.balance + self.get_overdraft_limit() >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Exceeds overdraft limit")

    #  allows withdrawing funds from the checking account. If the withdrawal amount is within the balance plus the
    #  overdraft limit, the amount is subtracted from the balance. Otherwise, an InsufficientFundsException is raised
    #  with the message "Exceeds overdraft limit".

    def __str__(self):
        info = f"\nBalance: £{self.balance}\nAccount Number: {self._account_number}\nOverdraft Limit: £{self._overdraft_limit}\n"
        if self.first_name:
            info += f"First Name: {self.first_name}\n"
        if self.last_name:
            info += f"Last Name: {self.last_name}\n"
        info += "********************\n"
        return info
    # special method in Python classes, it defines how instances of the class should be represented as strings
    # info is initialised as an empty string.This string will accumulate information about the object to be returned
    # as the final string representation.
    # The method checks if the object has a first_name and last_name attribute. If it does, it appends the first name
    # to info.  "********************\n" is added to info to serve as a separator.