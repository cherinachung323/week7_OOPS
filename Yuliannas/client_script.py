from week7_OOPS.Yuliannas.personPackage.person import Person
from week7_OOPS.Yuliannas.personPackage.employee import Employee
from week7_OOPS.Yuliannas.personPackage import Customer


# Function to display information for a Person
def display_person_info(person):
    print("Person Information:")
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")


# Function to display information for an Employee
def display_employee_info(employee):
    display_person_info(employee)
    print(f"Employee ID: {employee.employee_id}")
    print(f"Salary: £{employee.calculate_salary()}")


# Function to display information for a Customer
def display_customer_info(customer):
    display_person_info(customer)
    print(f"Customer ID: {customer.customer_id}")


# Creating instances of Person, Employee, and Customer
person1 = Person("John Doe", 30)
employee1 = Employee("Alice Smith", 25, "EMP123", 20, 40)
customer1 = Customer("Bob Johnson", 40, "CUST456")

# Display information for each instance
display_person_info(person1)
print()

display_employee_info(employee1)
print()

display_customer_info(customer1)
