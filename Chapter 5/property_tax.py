#property tax

def assessment_value(actual_value):
    assess_value = actual_value * 0.60
    print('The assessment value of the property is: $',assess_value)
    return assess_value


def property_tax(assess_value):
    tax = (assess_value // 100) * 0.72
    print('The property tax on this property is: $',format(tax,'.2f'))


def main():
    actual_value = float(input('Enter the actual value of the property: $'))
    value = assessment_value(actual_value)
    property_tax(value)

if __name__ == '__main__':
    main()
