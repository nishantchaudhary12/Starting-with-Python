#population data


def data():
    file = open("USPopulation.txt", "r")
    population = list()
    while True:
        item = file.readline()
        item = (item.rstrip('\n'))
        if item == '':
            break
        population.append(int(item))
    file.close()
    return population


def pop_increase(population):
    increase_per_year = list()
    year = [1950]
    for elem in range(len(population)-1):
        increase = population[elem + 1] - population[elem]
        increase_per_year.append(increase)
        year.append(year[elem] + 1)
    return increase_per_year, year


def calculations(increase_per_year, year):
    print('The average change in the population during that time period is:', format(sum(increase_per_year)/len(increase_per_year), '.2f'))
    maximum = increase_per_year.index(max(increase_per_year))
    minimum = increase_per_year.index(min(increase_per_year))
    print('The year with the greatest population increase is:', year[maximum + 1])
    print('The year with the smallest population increase is:', year[minimum + 1])


def main():
    population = data()
    increase_per_year, year = pop_increase(population)
    calculations(increase_per_year, year)


if __name__ == '__main__':
    main()
