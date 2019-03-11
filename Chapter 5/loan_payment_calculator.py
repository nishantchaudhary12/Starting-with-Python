#loan payment calculator


def payment_calculator(rate, amount, months):
    payment_per_month = (rate * amount)/(1 - (1 + rate)**-months)
    print('The month payment amount will be $',format(payment_per_month, '.2f'))


def main():
    rate = float(input('Enter the rate of interest as a decimal (e.g. 2.5% 5 0.025): '))
    amount = float(input('Enter the amount of the loan: $'))
    months = int(input('Enter the desired number of months: '))
    payment_calculator(rate, amount, months)


main()