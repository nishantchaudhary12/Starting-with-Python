# Driver's Licence Exam


def main():
    results = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    file = open("results.txt", "r")
    exam_result = []
    incorrect = []
    correct = 0
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        exam_result.append(line)
        line = file.readline()
    for index in range(len(exam_result)):
        if results[index] == exam_result[index]:
            correct += 1
        else:
            incorrect.append(index)
    if correct >= 15:
        print('Congratulations!!! You passed the exam.')
    else:
        print("You didn't pass the exam, Try again")
    print('The number of correct answers are:', correct)
    print('The wrong answers were:')
    for index in incorrect:
        print(index + 1)


main()
