#1994 weekly gas graph


import matplotlib.pyplot as plt


def get_data():
    file = open("1994_Weekly_Gas_Averages.txt", "r")
    gas = list()
    while True:
        item = file.readline()
        item = item.rstrip('\n')
        if item == '':
            break
        gas.append(item)
    return gas


def main():
    x_coord = list()
    x_data = list()
    for item in range(52):
        x_coord.append(item)
    y_coord = get_data()
    for item in range(1,53):
        x_data.append(item)
    plt.plot(x_coord, y_coord, marker='o')
    plt.title('1994 Weekly Gas Averages')
    plt.xlabel('Week')
    plt.ylabel('Price')
    plt.xticks(x_coord, x_data)
    plt.grid(True)
    plt.show()


main()
