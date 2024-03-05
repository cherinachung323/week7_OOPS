from week7_OOPS.Yuliannas.accountPackage.account import Account
from week7_OOPS.Yuliannas.accountPackage.savings_account import SavingsAccount
from week7_OOPS.Yuliannas.accountPackage.checking_account import CheckingAccount
from week7_OOPS.Yuliannas.accountPackage.insufficient_funds_exception import InsufficientFundsException

# Creating instances of Account, SavingsAccount, and CheckingAccount
account1 = Account("Yulianna", "Garcia", 1000, "87589")
savings_account1 = SavingsAccount("685965", 1000, 1.5)
checking_account1 = CheckingAccount("769544", 200, 500)

account2 = Account("Paulene", None, 2000, "56783")
savings_account2 = SavingsAccount("685875", 5000, 1.5)
checking_account2 = CheckingAccount("724344", 3000, 550)

account3 = Account("Cherina", None, 4000, "56903")
savings_account3 = SavingsAccount("685865", 700, 1.5)
checking_account3 = CheckingAccount("764344", 260, 1000)

# Display account information
print(f"{account1}")
print(f"{savings_account1}")
print(f"{checking_account1}")

print(f"{account2}")
print(f"{savings_account2}")
print(f"{checking_account2}")

print(f"{account3}")
print(f"{savings_account3}")
print(f"{checking_account3}")

# Attempting to withdraw an amount from the checking account. If the withdrawal exceeds the balance but does not
# exceed the overdraft limit, it will be allowed. Otherwise, it will raise an InsufficientFundsException.
print(f"{checking_account1}")  # Print before withdrawal attempt
try:
    checking_account1.withdraw(5500)
except InsufficientFundsException as e:
    print("Caught InsufficientFundsException:", e)
print(f"{checking_account1}")


print(f"\nAccount Info:\n{account1}\n")

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
