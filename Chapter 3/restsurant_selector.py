#restaurant selector

vegetarian = True
vegan = True
gluten = True

veg = input("Is anyone in your party a vegetarian: ")

vega = input("Is anyone in your party a vegan: ")

glu = input("Is anyone in your party gluten-free: ")

if(veg == 'yes' or veg == 'Yes' or veg == "YES"):
    vegetarian = True
else:
    vegetarian = False

if(vega == 'yes' or vega == 'Yes' or vega == "YES"):
    vegan = True
else:
    vegan = False


if(glu == 'yes' or glu == 'Yes' or glu == "YES"):
    gluten = True
else:
    gluten = False


print('\nHere are your restaurant choices: \n')

if(vegetarian == False and vegan == False and gluten == False):
    print("Joe's Gourmet Burgers")
elif(vegan == False and gluten == False):
    print("Mama's Fine Italian")
elif(vegan == False):
    print("Main Street Pizza Company")

print("Corner Cafe")
print("Chef's Kitchen")

