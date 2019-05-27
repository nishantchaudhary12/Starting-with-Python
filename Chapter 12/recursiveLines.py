def asterisk(x):
    if x == 0:
        return 0
    else:
        print('*', end='')
        return asterisk(x-1)


def lines(n, x):
    if n >= x:
        asterisk(x)
        print()
        return lines(n, x+1)
    else:
        return 0


def main():
    n = 10
    x = 1
    lines(n, x)


main()