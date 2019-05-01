#word index


def get_index():
    file = open("Kennedy.txt", "r")
    line_num = 1
    word_dict = dict()
    data = file.readline()
    data = data.rstrip('\n')
    while data != '':
        string = ''
        for each in data:
            if each.isalpha():
                string = string + each
            elif each.isspace():
                string = string + each

        words_list = string.split(' ')

        for word in words_list:
            if word not in word_dict:
                word_dict[word] = [line_num]
            else:
                if line_num not in word_dict[word]:
                    word_dict[word].append(line_num)
        data = file.readline()
        data = data.rstrip('\n')
        line_num += 1

    file.close()

    return word_dict


def write_index(word_index_dict):
    file = open('index.txt', 'w')
    for each in word_index_dict:
        string_new = ''
        for num in word_index_dict[each]:
            string_new = string_new + str(num) + ' '
        line = each + ':' + string_new
        file.write(line)
        file.write('\n')



def main():
    word_index_dict = get_index()
    write_index(word_index_dict)

main()