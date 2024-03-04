from week7_OOPS.Yuliannas.personPackage.person import Person


# Customer class is defined, and it inherits from the Person class.
class Customer(Person):
    # constructor method initialises a Customer object with three parameters: name, age, and customer_id.
    # It calls the constructor of the superclass (Person) using super().__init__(name, age) to initialize the name and
    # age attributes inherited from the Person class.It initialises the _customer_id attribute specific to the Customer
    # class.
    def __init__(self, first_name, last_name, age, gender, loyalty_card_num, loyalty_points):
        super().__init__(first_name, last_name, age, gender)
        self._loyalty_card_num = loyalty_card_num
        self._loyalty_points = loyalty_points

    # customer_id method (property getter) that returns the value of the _customer_id attribute.
    def get_loyalty_card_num(self):
        return self._loyalty_card_num

    def get_loyalty_points(self):
        return self._loyalty_points

    def change_last_name(self, new_last_name):
        self._last_name = new_last_name

    def __str__(self):
        return (f"Firstname: {self.firstname}\nLastname: {self.get_last_name()}\nAge: {self.get_age()}\n"
                f"Loyalty Card ID: {self.get_loyalty_card_num()}\nLoyalty Points: {self.get_loyalty_points()}")