#powerball lottery


def records(file):
    number_dict = dict()
    pow_num_dict = dict()
    overdue_num = list()
    line = file.readline()
    line = line.rstrip('\n')
    while line != '':
        num_list = line.split(' ')
        for each in num_list:
            if each in overdue_num:
                overdue_num.remove(each)
                overdue_num.append(each)
            else:
                overdue_num.append(each)

        for i in range(6):
            num_list[i] = int(num_list[i])
        for each in range(5):
            if num_list[each] not in number_dict:
                number_dict[num_list[each]] = 1
            else:
                number_dict[num_list[each]] += 1
        power_num = num_list[-1]

        if power_num not in pow_num_dict:
            pow_num_dict[power_num] = 1
        else:
            pow_num_dict[power_num] += 1
        line = file.readline()
        line = line.rstrip('\n')
    return number_dict, pow_num_dict, overdue_num


def sort_dict(number_dict):
    new_sorted_list = sorted(number_dict.items(), key=lambda x: x[1])
    return new_sorted_list


def most_common(new_sorted_list):
    print('Most Common Numbers with frequencies: ')
    for i in range(-1, -10, -1):
        print(new_sorted_list[i])


def least_common(new_sorted_list):
    print('\n')
    print('Least Common Numbers with frequencies: ')
    for i in range(0, 10):
        print(new_sorted_list[i])


def overdue(overdue_num_list):
    print('\n')
    print('Most overdue numbers(ordered from most to least):')
    for i in range(10):
        print(overdue_num_list[i])


def frequency(number_dict, pow_num_dict):
    print('\n')
    print('Number frequencies:')
    for i in range(1, 70):
        print(i,'=', number_dict[i])
    print('Powerball numbers:')
    for i in range(1, 27):
        print(i, '=', pow_num_dict[i])


def main():
    file = open('pbnumbers.txt', 'r')
    number_dict, pow_num_dict, overdue_num_list = records(file)
    file.close()
    new_sorted_list = sort_dict(number_dict)
    most_common(new_sorted_list)
    least_common(new_sorted_list)
    overdue(overdue_num_list)
    frequency(number_dict, pow_num_dict)


main()