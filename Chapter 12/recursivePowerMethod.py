def exponent(num, pow):
    if pow == 0:
        return 1
    else:
        return num * exponent(num, pow-1)
    

def main():
    num = 10
    pow = 3
    print(exponent(num, pow))


main()
