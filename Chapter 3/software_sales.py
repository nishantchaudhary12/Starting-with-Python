#software sales

import sys

num = int(input("Enter the number of packets purchased: "))
amount = int(num * 99)

if(num < 0):
    sys.exit("Enter a correct number")
elif(num == 0):
    print("Discount Given = 0% \nTotal amount = $0")
elif(0 < num < 10):
    f_amount = float(amount)
    print("Discount Given = 0% \nTotal amount = $"+str(amount)+ "\nTotal amount after discount = $"+str(f_amount))
elif(10 <= num < 20):
    discount = float(amount * 0.1)
    f_amount = float(amount - discount)
    print("Discount Given = 10% \nTotal amount = $"+str(amount)+ "\nDiscount amount = $"+str(discount)+ "\nTotal amount after discount = $"+str(f_amount))
elif (20 <= num < 50):
    discount = float(amount * 0.2)
    f_amount = float(amount - discount)
    print("Discount Given = 20% \nTotal amount = $"+str(amount)+ "\nDiscount amount = $"+str(discount)+ "\nTotal amount after discount = $"+str(f_amount))
elif (50 <= num < 100):
    discount = float(amount * 0.3)
    f_amount = float(amount - discount)
    print("Discount Given = 30% \nTotal amount = $"+str(amount)+ "\nDiscount amount = $"+str(discount)+ "\nTotal amount after discount = $"+str(f_amount))
elif (num >= 100):
    discount = float(amount * 0.4)
    f_amount = float(amount - discount)
    print("Discount Given = 40% \nTotal amount = $"+str(amount)+ "\nDiscount amount = $"+str(discount)+ "\nTotal amount after discount = $"+str(f_amount))

