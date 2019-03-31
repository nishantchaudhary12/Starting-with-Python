#file line viewer


def readFile():
    fileName = input('Enter the file name along with the extension: ')
    file = open(fileName, 'r')
    fileInfo = list()
    total_lines = 0
    while True:
        line = file.readline()
        line = line.rstrip('\n')
        if line == '':
            break
        total_lines += 1
        fileInfo.append(line)
    print('Number of lines of data in the file:', total_lines)
    return fileInfo


def main():
    fileInfo = readFile()
    number = int(input('Enter the line number you want to read from the file: '))
    print('The data at this line number is:', fileInfo[number+1])


main()
