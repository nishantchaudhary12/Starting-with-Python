#magic 8 ball


import random


def answer():
    file = open("8_ball_responses.txt", "r")
    answers = list()
    while True:
        line = file.readline()
        line = line.rstrip('\n')
        if line == '':
            break
        answers.append(line)
    return answers


def main():
    answers = answer()
    data = 'y'
    while data == 'y' or data == 'Y':
        question = input('Ask a question: ')
        print(random.choice(answers))
        data = input('Do you have more questions(Enter y for yes): ')


main()
