#grade calculator

import sys

#test 1 score
score1 = int(input("Enter the score for the first test: "))
if (score1 > 25 or score1 < 0):
    sys.exit("Error! Enter the score between 0-25")

#test 2 score
score2 = int(input("Enter the score for the second test: "))
if (score2 > 25 or score2 <0):
    sys.exit("Error! Enter the score between 0-25")

#main test score
score_main = int(input("Enter the score for the main test: "))
if (score_main > 50 or score_main < 0):
    sys.exit("Error! Enter the score between 0-50")

#total score
total = score1 + score2 + score_main

if (total < 50 or score_main < 25):
    print("Total Points " +str(total)+ " Result Status: Fail")
elif (total >= 80):
    print("Total Points " +str(total)+ " Result Status: Distinction")
elif (60 <= total < 80):
    print("Total Points " +str(total)+ " Result Status: Credit")
elif (50 <= total <59):
    print("Total Points " +str(total)+ " Result Status: Pass")