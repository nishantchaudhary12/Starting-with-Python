#paint job estimator


def total_price(wall_space, price):
    total_cost = (((8/112) * wall_space) * 35) + ((1/112) * wall_space * price)
    return total_cost

def main():
    wall_space = float(input('Enter the square feet of wall space to be painted: '))
    price = float(input('Enter the price of paint per gallon: $'))
    print('The total cost of painting the wall would be: $', format(total_price(wall_space, price),'.2f'))


main()
