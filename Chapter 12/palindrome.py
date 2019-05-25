def palindrome(string, start, end):
    if start >= end:
        return True
    else:
        if string[start] == string[end]:
            return palindrome(string, start+1, end-1)
        else:
            return False


def main():
    string = 'abcba'
    flag = palindrome(string, 0, len(string)-1)
    if flag:
        print('Yes it is a palindrome')
    else:
        print('No it is not a palindrome')


main()
