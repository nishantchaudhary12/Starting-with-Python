#lottery number generator


import random


def num_generator():
    ran_number = [0, 0, 0, 0, 0, 0, 0]
    for num in range(7):
        ran_number[num] = random.randint(0, 9)
    return ran_number


def print_num(inp_list):
    for each in inp_list:
        print(each)


def main():
    print_num(num_generator())


main()

