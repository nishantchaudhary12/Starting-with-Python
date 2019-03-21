# Number Analysis Program


def input_num():
    user_input = list()
    for num in range(20):
        num_inp = int(input('Enter the ' + str(num+1) + ' number: '))
        user_input.append(num_inp)
    return user_input


def calculations(user_input):
    print('The lowest number is the list:', min(user_input))
    print('The highest number is the list:', max(user_input))
    print('The total of all the numbers in the list:', sum(user_input))
    print('The average of all the numbers in the list:', format(sum(user_input)/len(user_input), '.2f'))


def main():
    user_input = input_num()
    calculations(user_input)


if __name__ == '__main__':
    main()