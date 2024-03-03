from week_7.people.baseclass_People import People

class Customer(People): #subclass defined and inheriting from the People base class
    def __init__(self, firstname, lastname, gender, status, loyalty_num, points_balance):   #instantiating all attributes required for Object, Customer

        super().__init__(firstname, lastname, gender, status)   #initiating the base class attributes
        self.loyalty_num = loyalty_num  #preparing the sub class attributes
        self.points_balance = points_balance

    def get_points_balance(self):
        return self.points_balance

    def get_loyalty_num(self):
        return self.loyalty_num

    # def get_loyalty_num(self):    #sample encapsulating/making this method private. Therefore cannot retrieve in customer app
    #     return self.__loyalty_num

    def amend_balance(self, amount):
        self.points_balance += amount