#prime numbers list

import math


def is_prime(num):
    prime = 1
    if num == 2 or num == 3:
        prime = num
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            prime = 1
            break
        else:
            prime = 0
    if prime == 0:
        return num


def main():
    print('Prime numbers between 1-100: ')
    for num in range(1,101):
        if is_prime(num):
            print(is_prime(num))



if __name__ == '__main__':
    main()


