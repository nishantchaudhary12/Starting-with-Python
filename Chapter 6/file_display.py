#file display


def main():
    file = open('numbers.txt','r')
    read = file.readline()
    while read != '':
        print(read.strip('\n'))
        read = file.readline()


main()