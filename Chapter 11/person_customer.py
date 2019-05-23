import customer


def get_data():
    name = input('Enter the name of the customer: ')
    address = input('Enter the address of the customer: ')
    number = input('Enter the telephone number: ')
    customer_num = input('Enter the customer number: ')
    mail = int(input('Press 1 if the customer wants to be on the mailing list else press 0: '))
    obj = customer.Customer(name, address, number, customer_num, mail)
    return obj


def display_data(obj):
    print('\nCustomer information')
    print('Customer Name:', obj.get_name())
    print('Customer Address:', obj.get_address())
    print('Customer Telephone Number:', obj.get_number())
    print('Customer Number:', obj.get_customer_num())
    print('Mailing List: ', obj.get_mail())


def main():
    obj = get_data()
    display_data(obj)


main()