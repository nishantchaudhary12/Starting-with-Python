#word index


def main():
    file = open("Kennedy.txt", "r")
    line_num = 1
    word_dict = dict()
    data = file.readline()
    data = data.rsplit('\n')
    while data != '':
        string = ''
        for each in data:
            if each.isalpha():
                string = string + each
            elif each.isspace():
                string = string + each
        print(string)
        words_list = string.split(' ')
        print(words_list)
        for word in words_list:
            if word not in word_dict:
                word_dict[word] = [line_num]
            else:
                word_dict[word].append(line_num)
        data = file.readline()
        data = data.rstrip('\n')
        line_num += 1
    print(word_dict)


main()