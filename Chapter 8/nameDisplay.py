#Name Display


def display(f_name, l_name):
    fName_list = list(f_name)
    lName_list = list(l_name)
    print('Initials:', fName_list[0] + '.' + lName_list[0] + '.')
    print('Name in address book:', f_name, l_name.upper())
    print('Username:', fName_list[0].lower() + l_name.lower())


def main():
    f_name = input('Enter the first name: ')
    l_name = input('Enter the last name: ')
    display(f_name, l_name)


main()