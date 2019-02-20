#magic dates

date = int(input('Enter the date: '))
month = int(input('Enter the month in numeric format: '))
year = int(input('Enter the last two digits of the year: '))

if((date * month) == year):
    print('The date is a magic date')
else:
    print('The date is not a magic date')