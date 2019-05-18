class Patient:
    def __init__(self, name, address, phone, emergency):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__emergency = emergency

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency(self, emergency):
        self.__emergency = emergency

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_emergency(self):
        return self.__emergency