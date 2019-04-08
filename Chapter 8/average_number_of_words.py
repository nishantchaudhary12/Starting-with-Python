#average number of words


def average_words(length_list):
    print('The average number of words in a sentence is:', format(sum(length_list)/len(length_list), '.2f'))
    

def main():
    file = open('text.txt', 'r')
    length_list = list()
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        words = line.split(' ')
        length = len(words)
        length_list.append(length)
        line = file.readline()
    file.close()
    average_words(length_list)


if __name__ == '__main__':
    main()