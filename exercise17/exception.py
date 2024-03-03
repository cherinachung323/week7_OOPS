from insufficient_fund import InsufficientFundsException, Account, SavingsAccount, CheckingAccount

# Create Account objects
account1 = Account("ACC001", 5000)
account1.display_info()

# Create SavingsAccount object
savings_account1 = SavingsAccount("SAV001", 10000, 0.05)
savings_account1.display_info()

# Create CheckingAccount object
checking_account1 = CheckingAccount("CHK001", 2000, 1000)
checking_account1.display_info()

# Handling InsufficientFundsException
try:
    account1.withdraw(6000)  # Trying to withdraw more than the balance
except InsufficientFundsException as e:
    print(f"Error: {e}")

try:
    checking_account1.withdraw(3000)  # Trying to withdraw more than the balance
except InsufficientFundsException as e:
    print(f"Error: {e}")

# Successful withdrawal
try:
    savings_account1.withdraw(500)
    savings_account1.display_info()
except InsufficientFundsException as e:
    print(f"Error: {e}")
