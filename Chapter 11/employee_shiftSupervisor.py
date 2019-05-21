import shiftSupervisor


def get_data():
    name = input('Enter the name of the supervisor: ')
    emp_number = input('Enter the supervisor number: ')
    annual_salary = float(input('Enter the annual salary of the supervisor: '))
    bonus = float(input('Enter the bonus: '))
    obj = shiftSupervisor.ShiftSupervisor(name, emp_number, annual_salary, bonus)
    return obj


def display_data(obj):
    print('\nSupervisor Information')
    print('Supervisor Name:', obj.get_name())
    print('Supervisor Number:', obj.get_number())
    print('Annual Salary: $', obj.get_annual_salary())
    print('Bonus: $', obj.get_bonus())


def main():
    obj = get_data()
    display_data(obj)


main()