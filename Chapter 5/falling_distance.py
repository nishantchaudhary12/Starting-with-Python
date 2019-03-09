#falling distance


def falling_distance(time):
    g = 9.8
    distance = 1/2 * g * time**2
    return distance


def main():
    for x in range(10):
        time = float(input('Enter the time: '))
        print('The distance(in metres) that the object has fallen in that time:', format(falling_distance(time),'.2f'))


main()