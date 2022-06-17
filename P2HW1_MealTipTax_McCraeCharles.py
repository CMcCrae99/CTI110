    # This handy tool wil help you figure out how much your meal costs
    # 06/15/22
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Charles McCrae
    
#Ask for food, tip, and tax amounts
food = float(input('Enter charge for food:\n'))
tip = float(input('Enter tip for server:\n'))
tax = float(input('Enter tax:\n'))

#Show converted numbers 
calc_tip = tip * food
calc_tax = tax * food
print('Calculated Tip:', '$', f'{calc_tip:.2f}')
print('Calculated Tax:', '$', f'{calc_tax:.2f}')
print()

#Add everything for final cost
total_cost = (food + calc_tip + calc_tax)
print('Total cost including tip and tax:', '$', f'{total_cost:.2f}')
