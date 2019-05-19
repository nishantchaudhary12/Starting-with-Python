import personal_InfoClass


def get_data():
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    age = input('Enter the age: ')
    phone = input('Enter the phone number: ')
    return name, address, age, phone


def print_data(obj):
    print('Name:', obj.get_name())
    print('Address:', obj.get_address())
    print('Age:', obj.get_age())
    print('Phone:', obj.get_phone())


def my_info():
    print('Your info')
    name, address, age, phone = get_data()
    obj1 = personal_InfoClass.PerInfo(name, address, age, phone)
    print_data(obj1)


def others_info():
    print('Friends or Family Info')
    name, address, age, phone = get_data()
    obj2 = personal_InfoClass.PerInfo(name, address, age, phone)
    print_data(obj2)
    name, address, age, phone = get_data()
    obj3 = personal_InfoClass.PerInfo(name, address, age, phone)
    print_data(obj3)


def main():
    my_info()
    others_info()


main()