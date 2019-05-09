class RetailItem:
    def __init__(self, description, unit, price):
        self.__description = description
        self.__unit = unit
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_unit(self, unit):
        self.__unit = unit

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_unit(self):
        return self.__unit

    def get_price(self):
        return self.__price
