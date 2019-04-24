#Random number frequencies


import random


def main():
    freq_dict = dict()
    for num in range(100):
        rand_num = random.randint(1, 10)
        if rand_num not in freq_dict:
            freq_dict[rand_num] = 1
        else:
            freq_dict[rand_num] += 1
    print('The frequency of all the random numbers generated is:', freq_dict)


main()
