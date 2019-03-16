#word list file writer


def main():
    num = int(input('Enter the number of words you want to write to a file: '))
    file = open('words.txt', 'w')
    for item in range(num):
        word = input('Enter the word: ')
        file.write(word + '\n')
    print('Data written successfully!')
    file.close()


main()