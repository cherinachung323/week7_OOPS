class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This class represents a generic person with attributes name and age.
# The __init__ method serves as the constructor. It initializes the name and age attributes
# when a new object of the class is created.
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# The display_info method prints out the name and age of the person.

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.emp_id}")
# Inherits from the Person class, implying that it shares common attributes and behaviors with a Person.
# Additional attribute emp_id is added to represent the employee ID.
# The __init__ method initializes both the attributes inherited from Person and the emp_id.
# The display_info method overrides the method of the same name in the Person class.
# It first calls the display_info method of the parent class using super().display_info(),
# then prints out the employee ID.

class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def display_info(self):
        super().display_info()
        print(f"Customer ID: {self.customer_id}")
# Also inherits from the Person class.