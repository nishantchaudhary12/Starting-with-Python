#File Analysis


def file1():
    file = open("contact.txt", "r")
    data = file.read()
    data_string = ''
    for each in data:
        if each.isalpha():
            data_string = data_string + each
        if each.isspace():
            data_string = data_string + ' '
    word_list = data_string.split(' ')
    unique_words = set(word_list)
    file.close()
    return unique_words


def file2():
    file = open("contact1.txt", "r")
    data = file.read()
    data_string = ''
    for each in data:
        if each.isalpha():
            data_string = data_string + each
        if each.isspace():
            data_string = data_string + ' '
    word_list = data_string.split(' ')
    unique_words = set(word_list)
    file.close()
    return unique_words


def results(words1, words2):
    print('The unique words in both the files are:', words1.union(words2))
    print('The words that appears in both the files are:', words1.intersection(words2))
    print('The words that appear in the first file but not second are;', words1.difference(words2))
    print('The words that appear in the second file but not first are:', words2.difference(words1))
    print('The words that appear in one of the file but not both are:', words1.symmetric_difference(words2))


def main():
    words1 = file1()
    words2 = file2()
    results(words1, words2)


main()

