#sum of numbers


def main():
    file = open('numbers.txt','r')
    read = file.readline()
    total = 0
    while read != '':
        read = int(read)
        total += read
        read = file.readline()
    print('The sum of numbers:', total)
    file.close()


main()