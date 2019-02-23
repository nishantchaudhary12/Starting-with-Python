#sleep debt

sleep = []

#function to take input of the sleep hours
def record():
    this_week = float(input('Enter the number of hours you slept: '))
    sleep.append(this_week)

#desired number of hours per week
desired = 8 * 7

for num in range(1,8):
    print('Day:', num)
    record()

total = sum(sleep)
debt = desired - total

if debt >= 0:
    print('Sleep Debt for this week:',debt,'hours')
else:
    print('You should sleep less, this makes me feel jealous.')
