#average rainfall

years = int(input('Enter the number of years: '))

inch = []

def rain():
    this_month = float(input('Enter the average inch rainfall for this month: '))
    inch.append(this_month)

for num in range(1, years+1):
    for month in range(1, 13):
        print('Year:',num,'\nMonth:',month)
        rain()

print('The number of months taken into consideration=', len(inch))

total = sum(inch)

print('The total inches of rainfall during this time:',total)

average = total/len(inch)

print('The average rainfall per month for this period:',format(average,'.2f')


