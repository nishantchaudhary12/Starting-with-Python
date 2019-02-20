#book club points

import sys

num = int(input('Enter the number of books purchased: '))

#number can't be negative
if( num < 0):
    sys.exit('Enter the correct amount')

#function to calculate the points
def points(num):
    if(num < 2):
        print('You have 0 points for this month')
    elif(2 <= num < 4):
        print('You have 5 points for this month')
    elif (4 <= num < 6):
        print('You have 15 points for this month')
    elif (6 <= num < 8):
        print('You have 30 points for this month')
    else:
        print('You have 60 points for this month')

#calls the function
points(num)