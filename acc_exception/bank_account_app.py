from week_7.people.acc_exception.account_class import Account, InsufficientFundsException

# DATA
joey_account = Account(100, "Joey", "Tribiani")

try:
    bank_name = joey_account.set_bank_name("Piggy Bank")    #setting bank name
    print(joey_account.get_bank_name())     #getting bank name
    print(joey_account.account_holder_name)     #get method to retrieve data
    current_balance = joey_account.get_balance()
    print(f"Current Balance = £ {current_balance}")

    print(50 * "#")

    joey_account.withdraw(-12)  #input withdrawal amount
    print("New Balance after withdrawal = £", joey_account.get_balance())

except InsufficientFundsException as ex:
    print("-!-" * 20)
    print(ex)
    print(f"Your current balance is £ {current_balance}")

else:
    print("END - No exception occurred")



# except NotValid as nv:
#     print("-!-" * 20)
#     print(nv)

