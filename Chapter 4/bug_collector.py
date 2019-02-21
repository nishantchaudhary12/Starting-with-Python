#bug collector

#number of days
num = 5

#total number of bugs
total = 0

for x in range(num):
    bug = int(input("Enter the number of bugs found today: "))
    total = total + bug

print('The total number of bugs found in the last five days:',total)