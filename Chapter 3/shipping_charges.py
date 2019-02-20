#shipping charges

import sys

quantity = float(input('Enter the weight of the package: '))

if(quantity < 0):
    sys.exit('Enter the right weight')

if(quantity <= 2):
    print('Shipping Charges = $1.50')
elif(2 < quantity <= 6):
    print('Shipping Charges = $3.50')
if(6 < quantity <= 10):
    print('Shipping Charges = $4.00')
else:
    print('Shipping Charges = $4.75')