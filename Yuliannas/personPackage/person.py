# attributes for storing a person's name and age, and provides getter methods to access these attributes.
# properties ensure that the attributes are accessed in a controlled manner, following the principle of encapsulation.
class Person:
    # a constructor method __init__ which takes two parameters: name and age. When a Person object is created, these
    # parameters are used to initialise the object's attributes _name and _age.
    def __init__(self, first_name, last_name, age, gender):
        self.firstname = first_name
        self._last_name = last_name
        self._age = age
        self._gender = gender

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

# @property decorator is used to define getter methods for accessing the _name and _age attributes.
# These getter methods are named name and age, respectively.
# The getter methods name and age simply return the values of the _name and _age attributes, allowing external code
# to access the name and age of a Person object using dot notation without directly accessing the attributes.

    def __str__(self):
        return (f"First name: {self.firstname}\nLast name: {self.get_last_name()}\nAge: {self.get_age()}\nGender: "
                f"{self.get_gender()}\n**************")

