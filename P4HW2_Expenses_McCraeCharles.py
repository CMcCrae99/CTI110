# CTI-110
# P4HW2 - Expenses
# Charles McCrae
# 06/29/22

def main():

    total = 1
    #Number of expenses entered
    ini_amt = int(input('Please enter starting amount in account:'))
    exp = []
    #Empty list for keeping track
    exp1 = exp.append(int(input('Enter expense:')))
    u_chc = input('Do you want to enter another expense? (y/n)')
    while u_chc == 'y':
        exp.append(int(input('Enter expense:')))
        input('Do you want to enter another expense? (y/n)')
        total += 1
        #How do I fix this?
        u_chc = 'n'
    if u_chc == 'n':
        print(f'Amount in account before expenses subtracted ${ini_amt}')
        print(f'Number of expenses entered: {total}')
        print(f'Amount in account After expenses subtracted is ${ini_amt - sum(exp)}')

   
        
    
main()
