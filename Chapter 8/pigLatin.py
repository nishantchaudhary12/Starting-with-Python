#PIG Latin


def pigLatin(user_input):
    words_list = user_input.split(' ')
    words_sub_list = list()
    new_string = ''
    for each in words_list:
        words_sub_list.append(list(each))
    for each in words_sub_list:
        first = each.pop(0)
        each.append(first)
        each.append('A')
        each.append('Y')
        new_string = new_string + ''.join(each) + ' '
    print(new_string)


def main():
    user_input = 'I SLEPT MOST OF THE NIGHT'
    pigLatin(user_input)


main()