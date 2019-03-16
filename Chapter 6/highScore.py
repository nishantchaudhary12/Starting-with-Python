#high score


def main():
    file = open('scores.txt','r')
    read = file.readline()
    count = 0
    highest = 0
    name = ''
    while read != '':
        a = read.split(' ')
        count += 1
        read = file.readline()
        a[1] = int(a[1])
        if a[1] > highest:
            highest = a[1]
            name = a[0]
    print('The total number of records:', count)
    print('Highest Score:', highest, 'Student Name:', name)
    file.close()


main()