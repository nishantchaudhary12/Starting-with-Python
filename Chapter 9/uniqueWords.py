#Unique Words


def main():
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
    print('The list of all the unique words in the file is:', unique_words)
    file.close()

main()

