#file head display


def main():
    f_name = input('Enter the file name: ')
    file = open(f_name,'r')
    for num in range(5):
        read = file.readline()
        print(read.strip('\n'))


main()