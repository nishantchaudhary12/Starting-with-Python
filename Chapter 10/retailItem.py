import retailItemClass


def get_data():
    description = input('Enter the description of the item: ')
    unit = input('Enter the Units in inventory: ')
    price = input('Enter the price: ')
    return description, unit, price


def print_data(obj):
    print('\n')
    print('Description:', obj.get_description())
    print('Units in inventory:', obj.get_unit())
    print('Price:', obj.get_price())


def my_info():
    print('Item 1')
    description, units, price = get_data()
    obj1 = retailItemClass.RetailItem(description, units, price)
    print('Item 2')
    description, units, price = get_data()
    obj2 = retailItemClass.RetailItem(description, units, price)
    print('Item 3')
    description, units, price = get_data()
    obj3 = retailItemClass.RetailItem(description, units, price)
    print('Item Records: ')
    print_data(obj1)
    print_data(obj2)
    print_data(obj3)


def main():
    my_info()


main()