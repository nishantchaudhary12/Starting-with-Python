#stadium seating

def income(ticket_A, ticket_B, ticket_C):
    total_income = ticket_A * 20 + ticket_B * 15 + ticket_C * 10
    print('The total income from the tickets is: $',total_income)

def main():
    ticket_A = int(input('Enter the number of tickets sold for class A: '))
    ticket_B = int(input('Enter the number of tickets sold for class B: '))
    ticket_C = int(input('Enter the number of tickets sold for class C: '))
    income(ticket_A, ticket_B, ticket_C)

main()