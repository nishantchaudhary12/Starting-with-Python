#valid number information


def check_numbers(numbers):
    valid_numbers = list()
    for item in numbers:
        if item >= 0 and item <= 100:
            valid_numbers.append(item)
    return valid_numbers


def total_and_average(valid_numbers):
    print('The total of all the numbers in the list is:', sum(valid_numbers))
    print('The average of all the numbers in the list is:', format(sum(valid_numbers)/len(valid_numbers), '.2f'))


def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers = check_numbers(numbers)
    total_and_average(valid_numbers)


if __name__ == '__main__':
    main()