#Alphabetic Telephone Number Translator


def print_num(user_input):
    user_input = user_input.upper()
    for ch in user_input:
        if ch == 'A' or ch == 'B' or ch == 'C':
            print('2', end='')
        elif ch == 'D' or ch == 'E' or ch == 'F':
            print('3', end='')
        elif ch == 'G' or ch == 'H' or ch == 'I':
            print('4', end='')
        elif ch == 'J' or ch == 'K' or ch == 'L':
            print('5', end='')
        elif ch == 'M' or ch == 'N' or ch == 'P':
            print('6', end='')
        elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
            print('7', end='')
        elif ch == 'T' or ch == 'U' or ch == 'V':
            print('8', end='')
        elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
            print('9', end='')
        else:
            print(ch, end='')


def main():
    user_input = input('Enter the number in the format XXX-XXX-XXXX: ')
    print_num(user_input)


if __name__ == '__main__':
    main()