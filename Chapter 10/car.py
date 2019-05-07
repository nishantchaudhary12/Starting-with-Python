import carClass

def main():
    year_model = input('Enter the year model of the car: ')
    make = input('Enter the make name: ')
    carObj = carClass.Car(year_model, make)
    for each in range(5):
        carObj.accelerate()
        print(carObj.get_speed())
    for each in range(5):
        carObj.brake()
        print(carObj.get_speed())


main()