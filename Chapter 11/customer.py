import person

class Customer(person.Person):
    def __init__(self, name, address, number, customer_num, mail):
        person.Person.__init__(self, name, address, number)
        self.__customer_num = customer_num
        if mail == 1:
            self.__mail = True
        elif mail == 0:
            self.__mail = False

    def set_customer_num(self, customer_num):
        self.__customer_num = customer_num

    def set_mail(self, mail):
        self.__mail = mail

    def get_customer_num(self):
        return self.__customer_num

    def get_mail(self):
        return self.__mail