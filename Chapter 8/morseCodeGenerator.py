#Morse code generator


def morse_code(user_input):
    user_input = user_input.upper()
    for ch in user_input:
        if ch == ' ':
            print('space', end='')
        elif ch == ',':
            print('– – . . – –', end='')
        elif ch == '.':
            print('. – . – . –', end='')
        elif ch == '?':
            print('. . – – . .', end='')
        elif ch == '0':
            print('– – – – –', end='')
        elif ch == '1':
            print('. – – – –', end='')
        elif ch == '2':
            print('. . – – –', end='')
        elif ch == '3':
            print('. . . – –', end='')
        elif ch == '4':
            print('. . . . –', end='')
        elif ch == '5':
            print('. . . . .', end='')
        elif ch == '6':
            print('– . . . .', end='')
        elif ch == '7':
            print('– – . . .', end='')
        elif ch == '8':
            print('– – – . .', end='')
        elif ch == '9':
            print('– – – – .', end='')
        elif ch == 'A':
            print('. –', end='')
        elif ch == 'B':
            print('– . . .', end='')
        elif ch == 'C':
            print('– . – .', end='')
        elif ch == 'D':
            print('– . .', end='')
        elif ch == 'E':
            print('.', end='')
        elif ch == 'F':
            print('. . – .', end='')
        elif ch == 'G':
            print('– – .', end='')
        elif ch == 'H':
            print('. . . .', end='')
        elif ch == 'I':
            print('. .', end='')
        elif ch == 'J':
            print('. – – –', end='')
        elif ch == 'K':
            print('– . –', end='')
        elif ch == 'L':
            print('. – . .', end='')
        elif ch == 'M':
            print('– –', end='')
        elif ch == 'N':
            print('– .', end='')
        elif ch == 'O':
            print('– – –', end='')
        elif ch == 'P':
            print('. – – .', end='')
        elif ch == 'Q':
            print('– – . –', end='')
        elif ch == 'R':
            print('. – .', end='')
        elif ch == 'S':
            print('. . .', end='')
        elif ch == 'T':
            print('–', end='')
        elif ch == 'U':
            print('. . –', end='')
        elif ch == 'V':
            print('. . . –', end='')
        elif ch == 'W':
            print('. – –', end='')
        elif ch == 'X':
            print('– . . –', end='')
        elif ch == 'Y':
            print('– . –', end='')
        elif ch == 'Z':
            print('– – . .', end='')


def main():
    user_input = input('Enter the string: ')
    morse_code(user_input)


main()