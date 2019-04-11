#word separator


def wordSeparator(user_input):
    init_index = 0
    wordsList = list()
    for each in user_input:
        if each == ' ' or each == '.':
            end_index = user_input.index(each, init_index + 1)
            new_string = user_input[init_index:end_index + 1]
            new_string = new_string.strip()
            wordsList.append(new_string.capitalize())
            init_index = end_index
    print(''.join(wordsList))


def main():
    user_input = 'Stop and smell the roses.'
    wordSeparator(user_input)


main()