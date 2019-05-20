class Employee:
    def __init__(self, name, employee_num):
        self.__name = name
        self.__number = employee_num

    def set_name(self, name):
        self.__name = name

    def set_number(self, employee_num):
        self._number = employee_num

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

