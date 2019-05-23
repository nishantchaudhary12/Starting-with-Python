import employee

class ProductionWorker(employee.Employee):
    def __init__(self, name, employee_num, shift, hourly_pay):
        employee.Employee.__init__(self, name, employee_num)
        self.__shift = shift
        self.__hourly_pay = hourly_pay

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift(self):
        return self.__shift

    def get_hourly_pay(self):
        return self.__hourly_pay