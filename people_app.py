from week_7.people.baseclass_People import People
from week_7.people.employee_class import Employees

#DATA
# Person1 =
person1 = People("Chandler","Bing", "Male", "Employee")

# Person2 =
person2 = People("Monica","Geller", "Female", "Customer")

# Person3 =
person3 = People("Rachel","Green", "Female", "Employee"),


#APP - getters and setter used
firstname = person1.get_firstname()
print(f"First Name = {firstname}")

lastname = person1.get_lastname()
print(f"Last Name = {lastname}")

gender = person1.get_gender()
print(f"Gender = {gender}")

print("\n", 50 * "#", "\n")

person1.set_firstname("Chandler Muriel")    #setter used
print(f"Chandler's old firstname is {firstname} and his new first name is {person1.get_firstname()}")

status = person1.get_status()
print(f"Status = {status}")

print(f"Do they work for John Lewis? {person1.check_status(status)}")