def printing(n):
    if n == 0:
        print(n)
        return 0
    else:
        print(n)
        return printing(n-2)


def main():
    n = int(input('Enter a positive integer: '))
    printing(n)


main()