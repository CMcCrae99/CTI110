    # Calculating Expenses
    # 06/09/22
    # CTI-110 P1HW2 - Basic Math
    # Charles McCrae
    #Ask user to enter the name of the expense.
    #Ask user to enter how much they are charged for that expense/bill monthly (without tax).
    #Calculate monthly tax
    #Calculate amount paid monthly
    #Calculate amount paid for entire year.
    #Display results.
x = 6.60
print('Enter name of expenses')
y = input()
print('Enter monthly charge')
z = int(input())
print('Bill:', (y), '--------- Before Tax:', '$', z)
print('Monthly Tax:', '$', (x))
print('Monthly Charge', '$', z + x)
print('Annual Charge', '$', z + x * 12)
