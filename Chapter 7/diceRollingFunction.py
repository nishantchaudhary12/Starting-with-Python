# Dice Rolling Function


import random


def roll(number_of_throws):
    roll_num = list()
    for item in range(number_of_throws):
        num = random.randint(1,6)
        roll_num.append(num)
    return roll_num


def main():
    number_of_throws = int(input('Enter the number of throws: '))
    print(roll(number_of_throws))


main()
