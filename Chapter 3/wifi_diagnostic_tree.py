#wifi diagnostic tree

troubleshoot = False

user = input('Do you want to troubleshoot your WiFi: Press Y for yes and N for no \n')
user.lower()

if user == 'y':
    troubleshoot = True
else:
    exit()

#function for troubleshooting
def troubleshooting():
    response = input('Did that fix the problem? Press Y for yes and N for no ')
    response.lower()
    if response == 'y':
        troubleshoot = False
        exit()

if troubleshoot:
   print('Reboot the computer and try to connect')
   troubleshooting()
   print('Reboot the router and try to connect.')
   troubleshooting()
   print('Make sure the cables between the router and modem are plugged in firmly')
   troubleshooting()
   print('Move the router to a new location.')
   troubleshooting()
   print('Get a new router.')

