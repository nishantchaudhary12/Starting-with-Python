#pennies for pay

days = int(input('Enter the number of days: '))
salary = 0.01

print('Day\t\tSalary')

total = 0

for num in range(1,days+1):
    print(num,'\t\t',format(salary, '.3f'))
    total += salary
    salary *= 2

print('The total salary for that period is:',total)
