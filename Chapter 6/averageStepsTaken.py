#average steps taken


def steps_data():
    steps = list()
    file = open("steps.txt", "r")
    while True:
        step = file.readline()
        step = step.rstrip('\n')
        if step == '':
            break
        step = int(step)
        steps.append(step)
    return steps


def main():
    steps = steps_data()
    print('Average steps taken in January:', format(sum(steps[0:31])/31, '.2f'))
    print('Average steps taken in February:', format(sum(steps[31:59])/28, '.2f'))
    print('Average steps taken in March:', format(sum(steps[59:90])/31, '.2f'))
    print('Average steps taken in April:', format(sum(steps[90:120])/30, '.2f'))
    print('Average steps taken in May:', format(sum(steps[120:151])/31, '.2f'))
    print('Average steps taken in June:', format(sum(steps[151:181])/30, '.2f'))
    print('Average steps taken in July:', format(sum(steps[181:212])/31, '.2f'))
    print('Average steps taken in August:', format(sum(steps[212:243])/31, '.2f'))
    print('Average steps taken in September:', format(sum(steps[243:273])/30, '.2f'))
    print('Average steps taken in October:', format(sum(steps[273:304])/31, '.2f'))
    print('Average steps taken in November:', format(sum(steps[304:334])/30, '.2f'))
    print('Average steps taken in December:', format(sum(steps[334:365])/31 , '.2f'))


main()