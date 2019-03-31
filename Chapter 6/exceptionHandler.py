#exception handling


def main():
    try:
        file = open('numbers.txt', 'r')
        total = 0
        count = 0
        read = file.readline()
        try:
            while read != '':
                read = int(read)
                total += read
                count += 1
                read = file.readline()
            print('The average of numbers:', format(total / count, '.2f'))
        except ValueError:
            print('ERROR: Numbers should be in valid form.')
        file.close()
    except IOError:
        print('No file with this name exists.')




main()