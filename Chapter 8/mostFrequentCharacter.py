#most frequent character


def frequent_character(user_input):
    character_dict = {}
    for each in user_input:
        if each != ' ':
            if each not in character_dict:
                character_dict[each] = 1
            else:
                character_dict[each] += 1
    max_value = max(character_dict.keys(), key = lambda k: character_dict[k])
    print(max_value)


def main():
    user_input = input('Enter a string: ')
    frequent_character(user_input)


main()