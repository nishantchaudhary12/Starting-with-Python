import employeeClass


def get_data():
    name = input('Enter the name: ')
    ID = input('Enter the ID: ')
    department = input('Enter the department: ')
    job_title = input('Enter the job_title: ')
    return name, ID, department, job_title


def print_data(obj):
    print('\n')
    print('Name:', obj.get_name())
    print('ID:', obj.get_ID())
    print('Department:', obj.get_department())
    print('Job Title:', obj.get_job_title())


def my_info():
    print('Employee 1')
    name, ID, department, job_title = get_data()
    obj1 = employeeClass.Employee(name, ID, department, job_title)
    print('Employee 2')
    name, ID, department, job_title = get_data()
    obj2 = employeeClass.Employee(name, ID, department, job_title)
    print('Employee 3')
    name, ID, department, job_title = get_data()
    obj3 = employeeClass.Employee(name, ID, department, job_title)
    print_data(obj1)
    print_data(obj2)
    print_data(obj3)


def main():
    my_info()


main()