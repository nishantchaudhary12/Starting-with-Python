#leap year

year = int(input('Enter the year to check whether it is a leap year or not: '))

if year % 100 == 0:
    if year % 400 == 0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')
else:
    if year % 4 == 0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')


