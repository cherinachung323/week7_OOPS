from week_7.people.baseclass_People import People

class Employees(People):

    def __init__(self, firstname, lastname, gender, status, staff_num, service_length, department): #instantiating all attributes required for Object, Employees

        super().__init__(firstname, lastname, gender, status)   #preparing the base class attributes
        self.staff_num = staff_num  #preparing the sub class attributes
        self.service_length = service_length
        self.department = department

    def get_service_length(self):
        return self.service_length

    def get_staff_num(self):
        return self.staff_num

    def get_department(self):
        return self.department

    def amend_service(self, add_year):
        self.service_length += add_year
