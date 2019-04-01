#expense pie chart


import matplotlib.pyplot as plt


def get_data():
    file = open("expenses.txt", "r")
    expenses = list()
    while True:
        item = file.readline()
        item = item.strip("$")
        item = item.rstrip('\n')
        if item == '':
            break
        expenses.append(item)
    return expenses


def main():
    expenses = get_data()
    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    plt.title('Monthly Expenses')
    plt.pie(expenses, labels=slice_labels)
    plt.show()


main()