#lap_times

#list to store the lap time
time = []

laps = int(input('Enter the total number of laps: '))

for num in range(laps):
    print('Enter the lap timing for', num, 'lap: ')
    lap_time = float(input(''))
    time.append(lap_time)

#calculating fastest and slowest lap time
print('The fastest lap time is:',min(time))
print('The slowest lap time is:',max(time))

#calculating average lap time
total = sum(time)
average = total/laps

print('The average lap time is:',format(average,'.2f'))