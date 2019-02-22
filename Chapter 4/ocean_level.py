#ocean levels

year = 25
print('Year\tLevel Rise')
level = 1.6

for num in range(1,year+1):
    print(num,'\t\t',format(level,'.2f'),'mm')
    level += 1.6