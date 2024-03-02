from week_7.people.baseclass_People import People

class Employees:
    def __init__(self, firstname, lastname, status, staff_num, service_length, department):
        super().__init__(self, firstname, lastname, status)
        self.staff_num = staff_num
        self.service_length = service_length
        self.department = department

    def get_service_length(self, service_length):
        return self.service_length()