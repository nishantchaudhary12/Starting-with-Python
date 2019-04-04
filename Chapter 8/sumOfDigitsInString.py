#Sum of digits in a string


def cal_sum(num):
    num_list = list()
    for ch in num:
        ch = int(ch)
        num_list.append(ch)
    print('The sum of all the numbers in the string is:', sum(num_list))


def main():
    num = input('Enter a series of single-digit numbers with nothing separating them: ')
    cal_sum(num)


main()