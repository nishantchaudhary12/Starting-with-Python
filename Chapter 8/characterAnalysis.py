#character analysis


def read_file():
    file = open('text.txt', 'r')
    uppercase = 0
    lowercase = 0
    whitespace = 0
    digits = 0

    line = file.read()
    while line != '':
        for each in line:
            if each.isupper():
                uppercase += 1
            elif each.islower():
                lowercase += 1
            elif each == ' ':
                whitespace += 1
            elif each.isdigit():
                digits += 1
        line = file.readline()
    file.close()

    print('Uppercase letters:', uppercase)
    print('Lowercase letters:', lowercase)
    print('Whitespace:', whitespace)
    print('Digits:', digits)


def main():
    read_file()


main()
