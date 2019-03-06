#monthly sales tax


def county_tax(sales):
    c_tax = sales * 0.025
    print('The county tax: $', c_tax)
    return c_tax


def sales_tax(sales):
    s_tax = sales * 0.05
    print('The sales tax: $',s_tax)
    return s_tax


def total_tax(county, sale):
    total = county + sale
    print('The total tax: $', total)


def main():
    sales = float(input('Enter the sales for the month: $'))
    total_tax(county_tax(sales), sales_tax(sales))


if __name__ == "__main__":
    main()