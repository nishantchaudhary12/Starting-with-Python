#World Series Winners


def count():
    file = open("WorldSeries.txt", "r")
    count_dict = dict()
    data = file.readline()
    data = data.rstrip('\n')
    while data != '':
        if data not in count_dict:
            count_dict[data] = 1
        else:
            count_dict[data] += 1
        data = file.readline()
        data = data.rstrip('\n')
    file.close()
    return count_dict


def year():
    file = open("WorldSeries.txt", "r")
    year_dict = dict()
    num = 1903
    data = file.readline()
    data = data.rstrip('\n')
    while data != '':
        year_dict[num] = data
        data = file.readline()
        data = data.rstrip('\n')
        num += 1
    file.close()
    return year_dict



def main():
    count_dict = count()
    year_dict = year()
    user_input = int(input('Enter the year you want to check: '))
    print('The team who won in', user_input, 'is:', year_dict[user_input])
    team = year_dict[user_input]
    if user_input != 1904 and user_input != 1994:
        print('Number of times', team, 'has won overall:', count_dict[team])


main()