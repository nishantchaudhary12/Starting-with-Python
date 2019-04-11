#Caesar Cipher


def caesarCipher(user_input, shift):
    new_string = ''
    for i in range(len(user_input)):
        char = user_input[i]
        if char.isalpha():
            if char.isupper():
                new = (ord(char) - (65 - shift)) % 26 + 65
            else:
                new = (ord(char) - (97 - shift)) % 26 + 97
            new_string = new_string + chr(new)
        else:
            new_string = new_string + char
    print(new_string)


def main():
    user_input = 'BEWARE THE IDES OF MARCH'
    shift = 13
    caesarCipher(user_input, shift)


main()