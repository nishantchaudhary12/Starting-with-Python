#money counting game

quarters = int(input('Enter the number of quarters: '))
dime = int(input('Enter the number of dimes: '))
nickels = int(input('Enter the number of nickels: '))
penny = int(input('Enter the number of pennies: '))

amount = quarters * 0.25 + dime * 0.1 + nickels * 0.05 + penny * 0.01

if amount < 1:
    print('You lose, the amount is less than $1')

elif amount > 1:
    print('You lose, the amount is more than $1')

else:
    print('Congrats, you won')




