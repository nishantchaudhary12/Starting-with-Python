#distance travelled

speed = float(input('Enter the speed of the vehicle in mph: '))
time = int(input('Enter the number of hours travelled: '))

print('Hours\tDistance travelled')

distance = 0

for num in range(1,time+1):
    distance = speed + distance
    print(num, '\t\t', distance)
