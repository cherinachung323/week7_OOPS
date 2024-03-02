from week_7.people.baseclass_People import People
from week_7.people.employee_class import Employees

# Person1 =
person1 = People("Chandler","Bing", "Male", "Employee"), Employees("67890", 10, "Accounting")
# Person2 =
person2 = People("Monica","Geller", "Female", "Customer")

person3 = People("Rachel","Green", "Female", "Employee"), Employees("12345",2,"Merchandise")

gender = person1.get_gender()
print(gender)

tenure = person2.get_service_length
print(tenure)