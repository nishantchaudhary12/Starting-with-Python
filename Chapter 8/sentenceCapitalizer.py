#Sentence Capitalizer


def capitalize(user_input):
    flag = 1
    new_string = []
    i = 0
    #for i in range(len(user_input)):
    while i < len(user_input):
        while user_input[i] == ' ':
            new_string.append(user_input[i])
            i += 1
        if user_input[i].isalpha() and flag == 1:
            new_string.append(user_input[i].upper())
            flag = 0
        elif user_input[i].isalpha():
            new_string.append(user_input[i])
        elif user_input[i] == '.':
            new_string.append('.')
            flag = 1
        i += 1
    print(''.join(new_string))


def main():
    user_input = input('Enter a string: ')
    capitalize(user_input)


main()