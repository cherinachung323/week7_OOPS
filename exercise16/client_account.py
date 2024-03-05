from person import Person, Employee, Customer
from account import Account, BankAccount, SavingsAccount, CheckingAccount

# Task A: Person inheritance hierarchy demonstration
person1 = Person("John Smith", 30)
person1.display_info()
print('*'*50)
employee1 = Employee("Chloe Smith", 25, "EMP123")
employee1.display_info()
print('*'*50)
customer1 = Customer("David Smith", 35, "CUST456")
customer1.display_info()

# Task B: Account inheritance hierarchy demonstration
account1 = Account("ACC001", 5000)
account1.display_info()
print('*'*50)
bank_account1 = BankAccount("BANK001", 10000, "Savings")
bank_account1.display_info()
print('*'*50)
savings_account1 = SavingsAccount("SA001", 2000)
savings_account1.display_info()
print('*'*50)
checking_account1 = CheckingAccount("CA001", 3000)
checking_account1.display_info()
