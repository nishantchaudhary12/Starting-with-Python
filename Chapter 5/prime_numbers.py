#prime numbers

import math


def prime_calc(num):
    prime = 1
    if num == 2 or num == 3:
        prime = 0
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            prime = 1
            break
        else:
            prime = 0
    if prime == 0:
        return True
    else:
        return False


def main():
    num = int(input('Enter a number: '))
    if prime_calc(num):
        print("The given number is prime.")
    else:
        print("The given number is not prime.")


if __name__ == '__main__':
    main()


