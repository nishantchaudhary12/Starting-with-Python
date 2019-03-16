#average of numbers


def main():
    file = open('numbers.txt','r')
    read = file.readline()
    total = 0
    count = 0
    while read != '':
        read = int(read)
        total += read
        count += 1
        read = file.readline()
    print('The average of numbers:', format(total/count, '.2f'))
    file.close()

main()