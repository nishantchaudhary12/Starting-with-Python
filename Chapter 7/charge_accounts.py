#charge accounts


def account_num():
    file = open("charge_accounts.txt", "r")
    acc_number = list()
    while True:
        number = file.readline()
        number = number.rstrip('\n')
        if number == '':
            break
        number = int(number)
        acc_number.append(number)
    file.close()
    return acc_number


def main():
    account = int(input('Enter the seven digit account number: '))
    acc_list = account_num()
    if account in acc_list:
        print('The account number is valid.')
    else:
        print('The account number is not valid.')


main()

