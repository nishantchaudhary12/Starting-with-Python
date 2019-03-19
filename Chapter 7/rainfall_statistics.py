# rainfall statistics


def get_input():
    user_input = list()
    for num in range(12):
        data = float(input('Enter the amount of rainfall in ' + str(num+1) + ' month: '))
        user_input.append(data)
    return user_input


def calculations(user_input):
    print('The total rainfall for the year was:', sum(user_input))
    print('The average rainfall for the year was:', format(sum(user_input)/12, '.2f'))
    print('The minimum rainfall amount was in:', min(user_input))
    print('The maximum rainfall amount was in:', max(user_input))


def main():
    calculations(get_input())


main()