#word list file reader


def main():
    file = open('words.txt', 'r')
    read = file.readline()
    count = 0
    len_list = []
    longest = read
    while read != '':
        count += 1
        #length = len(read)
        read = read.strip('\n')
        len_list.append(len(read))
        if len(longest) < len(read):
            longest = read
        read = file.readline()

    print('The number of words in the file:', count)
    print('The longest word in the file is:', longest)
    print('The average length of words in the file:', sum(len_list)/len(len_list))
    file.close()


main()