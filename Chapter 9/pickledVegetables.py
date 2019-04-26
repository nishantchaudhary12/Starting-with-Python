#Pickled Vegetables


import pickle


def menu():
    print('SELECT YOUR CHOICE')
    print('1. List of vegetables and their prices.')
    print('2. Add a new vegetable and price.')
    print('3. Change the price of an existing vegetable.')
    print('4. Delete an existing vegetable and price.')
    print('0. Exit')


def get_data():
    veg_dict = dict()
    end_of_file = False
    file = open('mydata.dat', 'rb')
    while not end_of_file:
        try:
            veg = pickle.load(file)
            for key, value in veg.items():
                veg_dict[key] = value
            file = pickle.load(file)
        except EOFError:
            end_of_file = True
    return veg_dict


def pickle_data(veg_dict):
    file = open("mydata.dat", "wb")
    pickle.dump(veg_dict, file)
    file.close()


def add_veg(veg_dict):
    name = input('Enter the name of the vegetable: ')
    price = input('Enter the price of the vegetable(quantity wise): ')
    veg_dict[name] = price
    pickle_data(veg_dict)


def view_veg(veg_dict):
    print(veg_dict)



def change(veg_dict):
    user_input = input("Enter the name of the vegetable: ")
    price = input('Enter the new price: ')
    veg_dict[user_input] = price
    pickle_data(veg_dict)


def delete_veg(veg_dict):
    user_input = input("Enter the name of the vegetable: ")
    del veg_dict[user_input]
    pickle_data(veg_dict)


def main():
    print('WELCOME!!!')
    choice = '1'
    while choice != '0':
        menu()
        veg_dict = get_data()
        user_input = input('Enter your choice: ')
        if user_input == '2':
            add_veg(veg_dict)
        if user_input == '1':
            view_veg(veg_dict)
        if user_input == '3':
            change(veg_dict)
        if user_input == '4':
            delete_veg(veg_dict)
        if user_input == '0':
            choice = '0'


main()