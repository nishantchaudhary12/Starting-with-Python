import productionWorker


def get_data():
    name = input('Enter the name of the employee: ')
    emp_number = input('Enter the employee number: ')
    shift = int(input('Enter the shift of the employee (Press 1 for day shift and 2 for night shift): '))
    hourly_pay = float(input('Enter the hourly pay: '))
    obj = productionWorker.ProductionWorker(name, emp_number, shift, hourly_pay)
    return obj


def display_data(obj):
    print('\nEmployee Information')
    print('Employee Name:', obj.get_name())
    print('Employee Number:', obj.get_number())
    shift = obj.get_shift()
    if shift == 1:
        print('Shift: Day shift')
    elif shift == 2:
        print('Shift: Night shift')
    print('Hourly pay: $', obj.get_hourly_pay())


def main():
    obj = get_data()
    display_data(obj)


main()
