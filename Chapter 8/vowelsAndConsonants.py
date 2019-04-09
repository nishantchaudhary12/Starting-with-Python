#Vowels and Consonants


def vowels(user_input):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    for each in user_input:
        if each in vowel:
            vowels_count += 1
    print('The number of vowels in the string are:', vowels_count)


def consonants(user_input):
    vowel = ['a', 'e', 'i', 'o', 'u', ' ']
    consonants_count = 0
    for each in user_input:
        if each not in vowel:
            consonants_count += 1
    print('The number of consonants in the string are:', consonants_count)


def main():
    user_input = input('Enter a string: ')
    user_input = user_input.lower()
    vowels(user_input)
    consonants(user_input)


main()