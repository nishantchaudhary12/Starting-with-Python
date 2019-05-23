import employee

class ShiftSupervisor(employee.Employee):
    def __init__(self, name, employee_num, annual_salary, bonus):
        employee.Employee.__init__(self, name, employee_num)
        self.__annual_salary = annual_salary
        self.__bonus = bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_bonus(self):
        return self.__bonus