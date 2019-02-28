#string repeater

string = input('Enter the string: ')

number = int(input('Enter the number of times you want to print the string: '))

def string_print(x, y):
    for num in range(y):
        print(x,end='')

if __name__ == '__main__':
    string_print(string,number)
