    # This handy tool wil help you figure out how much your meal costs - New and Improved!
    # CTI-110
    # P3HW2 - MealTipTax
    # Charles McCrae
    # 06/21/22
    
#Ask for food, tip, and tax amounts
food = float(input('Please enter cost of meal:\n'))
tip = float(input('Enter tip amount of 15, 18, or 20:\n'))
print()
tax = .06
tip_1 = [0.15, 0.18, 0.20] 

#Minor cosmetic adjustments 
calc_tax = tax * food
print('Meal price:', '$', f'{food:.1f}')
print('Tax: 6%')


#For future reference - Please start with zero for list callbacks. Ex: my_list[0]
#There is probably an easier way to do this
if tip == 15:
    print('Tip: 15')
    print('Total cost including tip and tax:', '$', f'{food + calc_tax +(tip_1[0] * food)}')
elif tip == 18:
    print('Tip: 18')
    print('Total cost including tip and tax:', '$', f'{food + calc_tax +(tip_1[1] * food)}')
elif tip == 20:
    print('Tip: 20')
    print('Total cost including tip and tax:', '$', f'{food + calc_tax +(tip_1[2] * food)}')
else:
    print('Error!')


