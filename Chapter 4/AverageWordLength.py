#average word length

length = []

word = input('Enter the word: ')
length.append(len(word))


while word != '':
    word = input('Enter the word: ')
    length.append(len(word))


average = sum(length)/len(length)


print('The average length of words entered is:',round(average))
