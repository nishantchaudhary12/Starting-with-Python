#population

organism = int(input('Enter the number of organisms: '))
increase = float(input('Enter the percent increase of the organisma per day: '))
days = int(input('Enter the number of days to multiply: '))

print('Day approximate \t Population')

for num in range(1,days+1):
    print(num, '\t\t\t\t\t', format(organism, '.2f'))
    organism = organism + (organism * (increase / 100))

