from week7_OOPS.Yuliannas.accountPackage.account import Account
from week7_OOPS.Yuliannas.accountPackage.insufficient_funds_exception import InsufficientFundsException



# SavingsAccount class extends  represent a savings account. It includes additional features from account such as
# calculating interest and displaying the interest rate, while maintaining basic account operations like withdrawing
# funds.

# SavingsAccount will have all the attributes and methods of the Account class, and it can also define its own
# additional attributes and methods.
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(None, None, balance, account_number)  # No first_name or last_name needed
        self._interest_rate = interest_rate

    # The __init__ method is a special method in Python classes used for initialising new objects.
    # it is taking four parameters: account_number, balance, and interest_rate.
    # super().__init__(None, None, balance, account_number) calls the constructor of the superclass (Account) with
    # arguments (None, None, balance, account_number). This initialises the inherited attributes of the Account class.
    # self.interest_rate = interest_rate initialises a new attribute specific to the SavingsAccount class, representing
    # the interest rate.
    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, value):
        self._interest_rate = value

    def calculate_interest(self):
        return self.balance * (self.get_interest_rate() / 100)

    # method calculates the interest earned on the account balance based on the provided interest rate. It multiplies
    # the balance by the interest rate (converted to a decimal by dividing by 100) and returns the result.

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance(self.balance - amount)
        else:
            raise InsufficientFundsException("Insufficient funds")
    # the method allows withdrawing a specified amount from the savings account. If the balance is sufficient
    # (self.balance >= amount), it deducts the amount from the balance. Otherwise, it raises an
    # InsufficientFundsException with the message "Insufficient funds".

    def __str__(self):
        info = f"Account Number: {self._account_number}\n"
        info += f"Balance: £{self.balance}\n"
        if self.first_name:
            info += f"First Name: {self.first_name}\n"
        if self.last_name:
            info += f"Last Name: {self.last_name}\n"
        info += f"Interest Rate: {self._interest_rate}%\n"
        info += f"Calculated Interest: £{self.calculate_interest()}\n"
        return info

