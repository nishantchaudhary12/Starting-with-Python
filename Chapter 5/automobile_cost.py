#automobile cost

def amount():
    loan = float(input('Enter the monthly amount for loan payment: '))
    insurance = float(input('Enter the monthly amount for insurance: '))
    gas = float(input('Enter the monthly amount for gas: '))
    oil = float(input('Enter the monthly amount for oil: '))
    tires = float(input('Enter the monthly amount for tires: '))
    maintenance = float(input('Enter the monthly amount for maintenance: '))
    total = (loan + insurance + gas + oil + tires + maintenance) * 12
    print('The total expenses for the year: $', total)

if __name__ == "__main__":
    amount()
