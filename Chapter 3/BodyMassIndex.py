#body mass index

weight = float(input('Enter the weight in pounds: '))
height = float(input('Enter the height in inches: '))

BMI = weight * 703/(height ** 2)

print('Your BMI is:',format(BMI, '.2f'))

if(BMI > 25):
    print('Overweight')
elif(BMI < 18.5):
    print('Underweight')
else:
    print('Optimal weight')