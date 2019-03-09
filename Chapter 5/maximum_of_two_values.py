#maximum of two values

def greater(first_num, second_num):
    if first_num > second_num:
        greater_one = first_num
    else:
        greater_one = second_num

    return greater_one

def main():
    first_num = int(input('Enter the first number: '))
    second_num = int(input('Enter the second number: '))
    if first_num == second_num:
        print('Both the numbers are equal.')
    else:
        print('The greater number is:',greater(first_num, second_num))

main()