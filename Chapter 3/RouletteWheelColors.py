#roulette wheel colors

import sys

num = int(input('Enter a number from 0 to 36: '))

#if the number is out of range
if(num < 0 or num > 36):
    sys.exit('Enter a number from 0 to 36')

if(num == 0):
    print('Green')

elif(1 <= num <= 10):
    if(num % 2 == 0):
        print('Black')
    else:
        print('Red')

elif(11 <= num <=18):
    if (num % 2 == 0):
        print('Red')
    else:
        print('Black')

elif(19 <= num <= 28):
    if (num % 2 == 0):
        print('Black')
    else:
        print('Red')

else:
    if (num % 2 == 0):
        print('Red')
    else:
        print('Black')