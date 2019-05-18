class RetailItem:
    def __init__(self, description, unit, price):
        self.__description = description
        self.__unit = unit
        self.__price = float(price)

    def set_description(self, description):
        self.__description = description

    def set_unit(self, unit):
        self.__unit = unit

    def set_price(self, price):
        self.__price = float(price)

    def get_description(self):
        return self.__description

    def get_unit(self):
        return self.__unit

    def get_price(self):
        return self.__price


class CashRegister:
    def __init__(self):
        self.__total = list()
        self.__item = list()

    def purchase_item(self, obj):
        self.__item.append(obj)
        self.__total.append(obj.get_price())
        print(self.__total)

    def show_items(self):
        for each in self.__item:
            print('Description:', each.get_description())
            print('Units in inventory:', each.get_unit())
            print('Price:', each.get_price())
            # print(self.__total.append(obj.get_price()))

    def clear_list(self):
        self.__item.clear()

    def get_total(self):
        return sum(self.__total)


