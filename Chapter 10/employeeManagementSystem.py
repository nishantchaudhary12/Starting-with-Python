import employee_Class
import pickle


def get_data():
    name = input('Enter the name: ')
    ID = input('Enter the ID: ')
    department = input('Enter the department: ')
    job_title = input('Enter the job_title: ')
    return name, ID, department, job_title


def save_data(employee_dict):
    output_file = open('employeeData.dat', 'wb')
    pickle.dump(employee_dict, output_file)
    output_file.close()


def employee_info():
    try:
        input_file = open('employeeData.dat', 'rb')
        employee_dict = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dict = dict()

    return employee_dict


def look_up(employee_dict):
    employee_id = input('Enter the id of the employee you want to look for: ')
    print(employee_dict.get(employee_id, 'ID not found'))


def add(employee_dict):
    name = input('Enter the name: ')
    ID = input('Enter the ID: ')
    department = input('Enter the department: ')
    job_title = input('Enter the job_title: ')
    obj = employee_Class.Employee(name, ID, department, job_title)
    if ID not in employee_dict:
        employee_dict[ID] = obj
        print('Employee information added to the database')
    else:
        print('Entry already exists')


def change(employee_dict):
    ID = input('Enter the ID of the employee for whom you want to update the info: ')
    if ID in employee_dict:
        name = input('Enter the name: ')
        department = input('Enter the department: ')
        job_title = input('Enter the job_title: ')
        obj = employee_Class.Employee(name, ID, department, job_title)
        employee_dict[ID] = obj
        print('Employee information updated in the database')
    else:
        print('No employee with this ID exists.')


def delete(employee_dict):
    ID = input('Enter the ID of the employee ypu wanna delete: ')
    if ID in employee_dict:
        del employee_dict[ID]
        print('Employee info deleted')
    else:
        print('No employee with this ID exists')


def my_menu():
    print('MENU')
    print('1. View details of the employees')
    print('2. Add a new employee')
    print('3. Change details for an employee')
    print('4. Delete an employee')
    print('5. Quit')
    usr_input = int(input('Enter your choice: '))
    while 5 < usr_input or usr_input < 1:
        print('Enter a valid choice')
        usr_input = int(input('Enter your choice: '))
    return usr_input


def main():
    employee_dict = employee_info()
    print('Welcome to the employee portal!!!!')
    choice = my_menu()
    while choice != 5:
        if choice == 1:
            look_up(employee_dict)
        elif choice == 2:
            add(employee_dict)
        elif choice == 3:
            change(employee_dict)
        elif choice == 4:
            delete(employee_dict)
        choice = my_menu()
    save_data(employee_dict)


main()