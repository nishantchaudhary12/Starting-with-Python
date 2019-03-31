#golf score


def get_input():
    data = 'y'
    inline = open('golf.txt', 'a')
    while data == 'y' or data == 'Y':
        name = input('Enter the player name: ')
        score = input('Enter the score: ')
        inline.write(name + '\t')
        inline.write(score + '\n')
        data = input("Do you want to enter more data(Press 'Y' to enter more data: ")
    inline.close()


def print_data():
    inline = open('golf.txt', 'r')
    content = inline.read()
    print(content)
    inline.close


def main():
    inp_data = input("Do you want to enter data into the file('Press Y for yes): ")
    if inp_data == 'Y' or inp_data == 'y':
        get_input()
    data = input("Do you want to print the data(Press Y for yes): ")
    if data == 'Y' or data == 'y':
        print_data()


main()