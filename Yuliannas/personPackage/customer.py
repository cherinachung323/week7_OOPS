from week7_OOPS.Yuliannas.personPackage.person import Person


# Customer class is defined, and it inherits from the Person class.
class Customer(Person):
    # constructor method initialises a Customer object with three parameters: name, age, and customer_id.
    # It calls the constructor of the superclass (Person) using super().__init__(name, age) to initialize the name and
    # age attributes inherited from the Person class.It initialises the _customer_id attribute specific to the Customer
    # class.
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self._customer_id = customer_id

    @property
    # customer_id method (property getter) that returns the value of the _customer_id attribute.
    def customer_id(self):
        return self._customer_id

