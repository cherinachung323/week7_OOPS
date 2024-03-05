from week_7.people.baseclass_People import People
from week_7.people.employee_class import Employees
from week_7.people.customer_class import Customer

#DATA
# Person1 =
person1 = Employees("Chandler","Bing", "Male", "Employee", "67890", 10, "Accounting")
person2 = Customer("Monica","Geller", "Female", "Customer", "JL5678", 100)
person3 = Employees("Rachel","Green", "Female", "Employee", "12345", 2, "Merchandise")

# PEOPLE CLASS
print("----Attributes from Base class, People:")
firstname = person1.get_firstname()
lastname = person1.get_lastname()
gender = person1.get_gender()
employee_name = {person1.get_firstname(): person1.get_lastname()}   #employee name as a dictionary
print(employee_name)
print(f"Gender = {gender}")

print("\n", 50 * "#", "\n")

person1.set_firstname("Chandler Muriel")    #setter used
print(f"Chandler's old firstname is {firstname} and his new first name is {person1.get_firstname()}")
status = person1.get_status()
print(f"Status = {status}")
print(f"Do they work for John Lewis? {person1.check_status(status)}")

print("\n", 50 * "#", "\n")

# EMPLOYEES CLASS
print("----Attributes from Sub class, Employees:")    #getters used
print(f"Department = {person1.get_department()}")
print(f"Staff Number = {person1.get_staff_num()}")
print(f"Tenure(years) = {person1.get_service_length()}")

person1.amend_service(2)    #added 2 years to their service length.
new_tenure = person1.get_service_length()
print(f"{person1.get_firstname()}'s new service length is {new_tenure}years")

print("\n", 50 * "#", "\n")

# CUSTOMER CLASS
print("----Attributes from Base class, People:")
customer_name = {person2.get_firstname(): person2.get_lastname()}   #customer name as a dictionary
print(customer_name)
gender = person2.get_gender()
print(f"Gender = {gender}")

print("\n", 50 * "#", "\n")

print("----Attributes from Sub class, Customer:")
print(f"Loyalty Card Number = {person2.get_loyalty_num()}")
print(f"Loyalty Card Points Balance = {person2.get_points_balance()}")
person2.amend_balance(20)    #added 20 points to their loyalty card balance
new_balance = person2.get_points_balance()
print(f"{person2.get_firstname()}'s new loyalty card balance is {new_balance} points")