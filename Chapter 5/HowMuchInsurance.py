#how much insurance

replacement_cost = float(input('Enter the replacement cost for the building: $'))

def min_amount(x):
    amount = 0.8 * x
    print('The minimum amount of insurance you should buy: $',amount)


if __name__ == "__main__":
    min_amount(replacement_cost)
