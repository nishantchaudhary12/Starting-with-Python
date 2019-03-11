#rock paper scissors game


import random


def computer_choice():
    c_choice = random.randint(1, 3)
    return c_choice


def user_choice():
    u_choice = input('Enter your choice (rock, paper or scissors): ')
    u_choice = u_choice.lower()
    if u_choice == 'rock':
        user = 1
    elif u_choice == 'paper':
        user = 2
    else:
        user = 3
    return user


def winner():
    c_choice = computer_choice()
    u_choice = user_choice()
    while c_choice == u_choice:
        print('Same Choice, Try Again.')
        winner()
    if c_choice == 1:
        print('Computer Choice: Rock')
        if u_choice == 3:
            print('You lose.')
        else:
            print('Congratulation, You Won!!!')
    elif c_choice == 2:
        print('Computer Choice: Paper')
        if u_choice == 1:
            print('You lose.')
        else:
            print('Congratulation, You Won!!!')
    else:
        print('Computer Choice: Scissors')
        if u_choice == 2:
            print('You lose.')
        else:
            print('Congratulation, You Won!!!')


def main():
    winner()


if __name__ == '__main__':
    main()

