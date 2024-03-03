
# attributes for storing a person's name and age, and provides getter methods to access these attributes.
# properties ensure that the attributes are accessed in a controlled manner, following the principle of encapsulation.
class Person:
    # a constructor method __init__ which takes two parameters: name and age. When a Person object is created, these
    # parameters are used to initialise the object's attributes _name and _age.
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

# @property decorator is used to define getter methods for accessing the _name and _age attributes.
# These getter methods are named name and age, respectively.
# The getter methods name and age simply return the values of the _name and _age attributes, allowing external code
# to access the name and age of a Person object using dot notation without directly accessing the attributes.
