#tuition increase

year = 5
print('Year\tProjected fee for this year')
tuition = 8000

for num in range(1,year+1):
    print(num,'\t\t$',format(tuition,'.2f'))
    tuition = tuition + (0.03 * tuition)