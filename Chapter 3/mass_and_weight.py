#mass and weight

const = 9.8

mass = float(input('Enter the mass of an object in kilograms: '))

#calculate weight in newton
weight = mass * const

print('Weight in newtons =',format(weight,'.2f'))

if(weight > 500):
    print('Object is too heavy')
elif(weight < 100):
    print('Object is too light')

