import petClass

def main():
    name = input('Enter the name of the pet: ')
    animal_type = input('Enter the animal type: ')
    age = input('Enter the age of the pet: ')
    petObj = petClass.Pet(name, animal_type, age)
    print('Name:', petObj.get_name())
    print('Animal type:', petObj.get_animal_type())
    print('Age:', petObj.get_age())


main()