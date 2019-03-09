#addition test

import random

def generate_number():
    num = random.randint(1,10)
    return num

def main():
    for x in range(5):
        print('Question',x+1)
        first_num = generate_number()
        second_num = generate_number()
        print(first_num, '+', second_num, '=', first_num+second_num, '\n')

if __name__ == "__main__":
    main()
