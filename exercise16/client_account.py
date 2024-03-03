from account import Account, SavingsAccount, CheckingAccount

# Create Account objects
account1 = Account("ACC001", 5000)
account1.display_info()

# Create SavingsAccount object
savings_account1 = SavingsAccount("SAV001", 10000, 0.05)
savings_account1.display_info()

# Create CheckingAccount object
checking_account1 = CheckingAccount("CHK001", 2000, 1000)
checking_account1.display_info()
