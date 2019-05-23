def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


def main():
    m = 2
    n = 2
    print(ackermann(m, n))


main()
