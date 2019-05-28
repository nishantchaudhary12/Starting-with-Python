def multiplication(num1, num2):
    if num1 == 0:
        return 0
    else:
        return num2 + multiplication(num1-1, num2)


def main():
    num1 = 7
    num2 = 4
    print(multiplication(num1, num2))


main()