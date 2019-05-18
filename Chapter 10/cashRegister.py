import cashRegisterClass


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


def buy(obj, obj1, obj2, obj3):
    purchase = int(input('Select the item you want to purchase:(Press 1 for first, 2 for second and 3 for third) '))

    while purchase != 0:

        if purchase == 1:
            obj.purchase_item(obj1)
        elif purchase == 2:
            obj.purchase_item(obj2)
        elif purchase == 3:
            obj.purchase_item(obj3)
        else:
            print('Make a valid choice')
        purchase = int(input('Select the item you want to purchase:(Press 1 for first, 2 for second, 3 for third and 0 to exit) '))

    print('Items in the cart: ')
    obj.show_items()
    print('Total cost of all the items in the cart: $', obj.get_total())
    clr = int(input('Press 0 to clear the cart or 1 to Buy '))
    if clr == 0:
        obj.clear_list()
        print('Cart Empty. Thank you')
    else:
        print('Thank you for shopping')


def my_info():
    print('Item 1')
    description, units, price = get_data()
    obj1 = cashRegisterClass.RetailItem(description, units, price)
    print('Item 2')
    description, units, price = get_data()
    obj2 = cashRegisterClass.RetailItem(description, units, price)
    print('Item 3')
    description, units, price = get_data()
    obj3 = cashRegisterClass.RetailItem(description, units, price)

    obj = cashRegisterClass.CashRegister()

    buy(obj, obj1, obj2, obj3)





    # print('Item Records: ')
    # print_data(obj1)
    # print_data(obj2)
    # print_data(obj3)


def main():
    my_info()


main()