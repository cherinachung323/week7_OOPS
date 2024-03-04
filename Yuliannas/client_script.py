from week7_OOPS.Yuliannas.personPackage.person import Person
from week7_OOPS.Yuliannas.personPackage.employee import Employee
from week7_OOPS.Yuliannas.personPackage.customer import Customer


# Function to display information for a Person
def display_person_info(person):
    print("Person Information:")
    print(f"Firstname: {person.firstname}")
    print(f"Lastname: {person.get_last_name()}")  # Call the get_name() method
    print(f"Age: {person.get_age()}")


# Function to display information for an Employee
def display_employee_info(employee):
    display_person_info(employee)
    print(f"Employee ID: {employee.get_employee_id()}")
    print(f"Salary: £{employee.get_calculate_salary()}")


# Function to display information for a Customer
def display_customer_info(customer):
    display_person_info(customer)
    print(f"Loyalty Card ID: {customer.get_loyalty_card_num()}")
    print(f"Loyalty Points: {customer.get_loyalty_points()}")


# Creating instances of Person, Employee, and Customer
person1 = Person("John", "Hamilton", "Male", 30)
employee1 = Employee("Ana", "Garcia", 25, "Female", "45632", 20, 40)
customer1 = Customer("Paulene", "Del-Crux", 40, "Male", 28490, 10000)

# Display information for each instance
print(f"{person1}\n")

print(f"{employee1}\n")

print(f"{customer1}\n")

customer1.change_last_name("Benson")
print(f"{customer1}\n")