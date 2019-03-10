#odd_even calculator

import random

def even_odd():
    even_count = 0
    odd_count = 0
    for x in range(100):
        num = random.randint(1,100)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def main():
    print('The even number count and odd number count is:',even_odd(),'respectively.')

main()