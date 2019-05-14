class Procedure:
    def __init__(self, name, date, name_practitioner, charges):
        self.__name = name
        self.__date = date
        self.__name_practitioner = name_practitioner
        self.__charges = charges

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_name_practitioner(self, name_practitioner):
        self.__name_practitioner = name_practitioner

    def set_charges(self, charges):
        self.__charges = charges

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_name_practitioner(self):
        return self.__name_practitioner

    def get_charges(self):
        return self.__charges