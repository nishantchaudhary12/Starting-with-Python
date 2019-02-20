#areas_of_rectangle

#input for first rectangle
len1 = int(input('Enter the length of first rectangle: '))
width1 = int(input('Enter the width of the first rectangle: '))

#input for second rectangle
len2 = int(input('Enter the length of first rectangle: '))
width2 = int(input('Enter the width of the first rectangle: '))

#computing areas
area1 = len1 * width1
area2 = len2 * width2

if (area1 > area2):
    print('Rectangle 1 have the more area')

elif (area2 > area1):
    print('Rectangle 2 have more area')

else:
    print('Both the rectangles have the same area')