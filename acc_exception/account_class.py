class InsufficientFundsException(Exception):
    pass

class Account:
    numCreated = 0
    __bank_name = None

    def __init__(self, initial_amount, firstname, lastname):
        self._balance = initial_amount
        self.first_name = firstname
        self.last_name = lastname
        self._account_holder_name = firstname + " " + lastname


    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsException("You have insufficient funds in this account.")
        self._balance -= amount
        # elif amount is not int:


    def get_balance(self):
        return self._balance

    def get_firstname(self):
        return self.first_name

    def set_firstname(self, new_firstname):
        self.first_name = new_firstname

    def get_lastname(self, lastname):
        return self.last_name

    def set_lastname(self, new_lastname):
        self.last_name = new_lastname

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    @classmethod
    def set_bank_name(cls, name):
        cls.__bank_name = name