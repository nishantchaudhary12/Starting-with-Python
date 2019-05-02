#Gas Prices


def average_price_per_year():
    file = open("GasPrices.txt", "r")
    price = file.readline()
    price = price.strip('\n')
    price_dict = dict()
    while price != '':
        price_list = price.split(':')

        year = price_list[0].split('-')

        if year[2] in price_dict:
            price_dict[year[2]].append(float(price_list[1]))
        else:
            price_dict[year[2]] = [float(price_list[1])]
        price = file.readline()
        price = price.strip('\n')

    print('Average price per year: ')
    for each in price_dict:
        average = sum(price_dict[each])/len(price_dict[each])
        print(each, ':', format(average, '.2f'))

    file.close()


def average_price_per_month():
    file = open("GasPrices.txt", "r")
    price = file.readline()
    price = price.strip('\n')
    price_dict = dict()
    while price != '':
        price_list = price.split(':')

        date = price_list[0].split('-')

        month_year = date[0] + '-' + date[2]

        if month_year in price_dict:
            price_dict[month_year].append(float(price_list[1]))
        else:
            price_dict[month_year] = [float(price_list[1])]

        price = file.readline()
        price = price.strip('\n')

    print('\n')
    print('Average price per month: ')
    for each in price_dict:
        average = sum(price_dict[each])/len(price_dict[each])
        print(each, ':', format(average, '.2f'))

    file.close()


def highest_and_lowest_per_year():
    file = open("GasPrices.txt", "r")

    price = file.readline()
    price = price.strip('\n')
    price_dict = dict()
    while price != '':
        price_list = price.split(':')

        year = price_list[0].split('-')

        if year[2] in price_dict:
            price_dict[year[2]].append(float(price_list[1]))
        else:
            price_dict[year[2]] = [float(price_list[1])]
        price = file.readline()
        price = price.strip('\n')

    print('\n')
    print('Maximum and Minimum price per year: ')
    for each in price_dict:
        print(each)
        print('Maximum:', max(price_dict[each]))
        print('Minimum:', min(price_dict[each]))

    file.close()


def highest_to_lowest():
    file = open("GasPrices.txt", "r")
    price = file.readline()
    price = price.strip('\n')
    price_dict = dict()
    while price != '':
        price_list = price.split(':')

        price_dict[price_list[0]] = (float(price_list[1]))

        price = file.readline()
        price = price.strip('\n')

    price_dict_sorted = sorted(price_dict.items(), key=lambda x:x[1])

    file.close()
    file = open("highest_to_lowest.txt", "w")
    for key, value in price_dict_sorted:
        file.write('%s : %s\n' % (key, value))

    file.close()


def lowest_to_highest():
    file = open("GasPrices.txt", "r")
    price = file.readline()
    price = price.strip('\n')
    price_dict = dict()
    while price != '':
        price_list = price.split(':')

        price_dict[price_list[0]] = (float(price_list[1]))

        price = file.readline()
        price = price.strip('\n')


    price_dict_sorted = sorted(price_dict.items(), key=lambda x:x[1] ,reverse=True)

    file.close()
    file = open("lowest_to_highest.txt", "w")
    for key, value in price_dict_sorted:
        file.write('%s : %s\n' % (key, value))

    file.close()


def main():
    average_price_per_year()
    average_price_per_month()
    highest_and_lowest_per_year()
    highest_to_lowest()
    lowest_to_highest()


main()