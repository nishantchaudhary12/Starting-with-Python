#time calculator

import sys

seconds = int(input('Enter the number of seconds: '))

if(seconds < 0):
    sys.exit('Enter a right number')

elif(seconds == 0):
    print('Seconds = 0')


elif(0 < seconds < 60):
    print('Seconds = '+str(seconds))


elif(60 <= seconds < 3600):
    minutes = int(seconds / 60)
    seconds = int(seconds - (minutes * 60))
    print('Minutes = ' +str(minutes)+ '\nSeconds = ' +str(seconds))

elif(3600 <= seconds < 86400):
    hours = int(seconds / 3600)
    seconds = int(seconds - (hours * 3600))
    minutes = int(seconds / 60)
    seconds = int(seconds - (minutes * 60))
    print('Hours = ' +str(hours)+ '\nMinutes = '+str(minutes)+ '\nSeconds = '+str(seconds))

elif (seconds >= 86400):
    days = int(seconds / 86400)
    seconds = int(seconds - (days * 86400))
    hours = int(seconds / 3600)
    seconds = int(seconds - (hours * 3600))
    minutes = int(seconds / 60)
    seconds = int(seconds - (minutes * 60))
    print('days = ' +str(days)+ '\nHours = ' + str(hours) + '\nMinutes = ' + str(minutes) + '\nSeconds = ' +str(seconds))
