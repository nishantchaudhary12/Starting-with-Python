# Name Search

def boyNames():
    fBoy = open("BoyNames.txt", "r")
    boyList = list()
    boy_name = fBoy.readline()
    while boy_name != '':
        boy_name = boy_name.rstrip('\n')
        boyList.append(boy_name)
        boy_name = fBoy.readline()
    return boyList


def girlNames():
    fGirl = open("GirlNames.txt", "r")
    girlList = list()
    girl_name = fGirl.readline()
    while girl_name != '':
        girl_name = girl_name.rstrip('\n')
        girlList.append(girl_name)
        girl_name = fGirl.readline()
    return girlList


def main():
    boyList = boyNames()
    girlList = girlNames()
    names = input('Enter the names you want to search for separated by space and press enter(make sure to capitalize the first alphabet of each name): ')
    nameList = names.split(' ')
    for item in nameList:
        if item in boyList:
            print(item, 'is a common boy name.')
        elif item in girlList:
            print(item, 'is a common girl name.')
        else:
            print(item, 'is not a common name.')


if __name__ == '__main__':
    main()


