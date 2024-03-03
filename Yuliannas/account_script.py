from week7_OOPS.Yuliannas.accountPackage.account import Account
from week7_OOPS.Yuliannas.accountPackage import SavingsAccount
from week7_OOPS.Yuliannas.accountPackage import CheckingAccount
from week7_OOPS.Yuliannas.accountPackage import InsufficientFundsException


def get_account_number(account):
    return account._account_number


def set_account_number(account, value):
    account._account_number = value


def get_interest_rate(account):
    return account._interest_rate


def get_overdraft_limit(account):
    return account._overdraft_limit


# function takes an account object as input and prints its account number and balance. If the account object is an
# instance of Account, it also prints the first and last name associated with the account
def display_account_info(account):
    print("\n********************\n")
    print(f"Account Information:")
    print(f"Account Number: {get_account_number(account)}")
    print(f"Balance: £{account1.balance}")

    # checks if the account object is an instance of the Account class. If it is, the code inside the if block executes.
    if isinstance(account, Account):
        # checks if the first_name attribute of the account object is not empty or None. if it is not empty, the code
        # inside this if block executes. it prints the first name associated with the account using account.first_name.
        if account.first_name:
            print(f"First Name: {account.first_name}")
        # checks if the last_name attribute of the account object is not empty or None. If it is not empty, the code
        # inside this if block executes. It prints the last name associated with the account using account.last_name.
        if account.last_name:
            print(f"Last Name: {account.last_name}")
    # checks if the account object belongs to a specific subclass (SavingsAccount or CheckingAccount) using the
    # isinstance() function. If the account object is an instance of SavingsAccount, it prints the interest rate
    # associated with the savings account. If it is an instance of CheckingAccount, it prints the overdraft limit
    # associated with the checking account.
    if isinstance(account, SavingsAccount):
        print(f"Interest Rate: {get_interest_rate(account)}%")

    if isinstance(account, CheckingAccount):
        print(f"Overdraft Limit: £{get_overdraft_limit(account)}")

    print("\n********************\n")


# Creating instances of Account, SavingsAccount, and CheckingAccount
account1 = Account("Yulianna", "Garcia", 1000, "87589")
savings_account1 = SavingsAccount("685965", 1000, 1.5)
checking_account1 = CheckingAccount("769544", 2000, 500)

account2 = Account("Paulene", None, 2000, "56783")
savings_account2 = SavingsAccount("685875", 5000, 1.5)
checking_account2 = CheckingAccount("724344", 3000, 5650)

account3 = Account("Cherina", None, 4000, "56903")
savings_account3 = SavingsAccount("685865", 700, 1.5)
checking_account3 = CheckingAccount("764344", 260, 1000)

# Display account information
display_account_info(account1)
print()
display_account_info(savings_account1)
print()
display_account_info(checking_account1)

display_account_info(account2)
print()
display_account_info(savings_account2)
print()
display_account_info(checking_account2)

display_account_info(account3)
print()
display_account_info(savings_account3)
print()
display_account_info(checking_account3)


# Attempting to withdraw an amount from the checking account. If the withdrawal exceeds the balance but does not
# exceed the overdraft limit, it will be allowed. Otherwise, it will raise an InsufficientFundsException.
try:
    checking_account1.withdraw(20000)
except InsufficientFundsException as e:
    print("Caught InsufficientFundsException:", e)

# using the code from the lesson with account 1 info

print(f"Account Info:\n{account1}\n")

# Trying to withdraw an amount that exceeds the balance
try:
    account1.withdraw(500)
    print(f"After Withdrawal:\n{account1}\n")
except InsufficientFundsException as e:
    print("Caught InsufficientFundsException:", e)

# Depositing an amount into the account
account1.deposit(300)
print(f"After Deposit:\n{account1}\n")

# The FINALLY block always runs
print("The FINALLY block always runs")
print()
