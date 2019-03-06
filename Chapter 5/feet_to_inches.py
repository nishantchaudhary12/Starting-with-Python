#feet to inches


def feet_to_inch(feet):
    inch = feet * 12
    return inch


def main():
    print('Feet to inch converter!!!')
    feet = int(input("Enter the number of feets: "))
    print('The number of inches in', feet, 'feets:', feet_to_inch(feet))

main()