#hot dog cookout calculator

count = int(input('Enter the number of people attending the event: '))
hot_dogs = int(input('Enter the number of hot dogs given to one person: '))

total = count * hot_dogs

#each packet of have 10 hot dogs
#each packet have 8 buns

#packets required
if((total % 8) > 0):
    buns = (total // 8) + 1
else:
    buns = total // 8

if((total % 10) > 0):
    hDogs = (total // 10) + 1
else:
    hDogs = total // 10


#leftovers

left_buns = buns * 8 - total
left_dogs = hDogs *10 - total

print('The minimum number of packages of hot dogs required =', hDogs,
      '\nThe minimum number of packages of hot dog buns required =', buns,
      '\nThe number of hot dogs that will be left over =', left_dogs,
      '\nThe number of hot dog buns that will be left over = ', left_buns)