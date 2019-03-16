#line numbers

def main():
    f_name = input('Enter the file name: ')
    file = open(f_name,'r')
    read = file.readline()
    count = 1
    while read != '':
        print('Line', count, '-', read.strip('\n'))
        count += 1
        read = file.readline()


main()