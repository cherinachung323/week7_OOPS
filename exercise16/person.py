class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self._employee_id}")


class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self._customer_id = customer_id

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def display_info(self):
        super().display_info()
        print(f"Customer ID: {self._customer_id}")
