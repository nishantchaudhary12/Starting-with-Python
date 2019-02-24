#calculating factorial

import sys

num = int(input('Enter a non-negative integer to find the factorial: '))
product = 1

if num < 0:
    sys.exit("Can't find factorial of a negative number")

if num == 0:
    product = 0

while num > 0:
    product = product * num
    num -= 1

print('The factorial of the number is',product)
