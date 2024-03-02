class People:
    def __init__(self, firstname, lastname, gender, status):
        self.firstname = firstname
        self.lastname = lastname
        self.__gender = gender
        self.status = status

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname.upper

    def get_gender(self):
        return self.__gender  #HOW DO YOU MAKE IT "PRIVATE USING DUNDERS?"

    def check_status(self, status):
        if self.status == "Employee":
            return True
        else:
            return False

