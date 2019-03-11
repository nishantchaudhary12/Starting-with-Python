#random number guessing game


import random


def game(num):
    count = 1
    print(num)
    while True:
        guess = guess_number()
        if num > guess:
            print('Too low, try again.')
            count += 1
        elif num < guess:
            print('Too high, try again.')
            count += 1
        else:
            print('Congratulations, you won!!!')
            print('Total number of chances taken:', count)
            return True


def generate_number():
    num = random.randint(1, 100)
    return num


def guess_number():
    guess = int(input('Guess the number: '))
    return guess


def main():
    game(generate_number())


if __name__ == '__main__':
    main()