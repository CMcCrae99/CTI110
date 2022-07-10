# A brief description of the project
# 07/07/22
# CTI-110 P5HW2 - Math Quiz
# Charles McCrae


def print_menu():
    print('       MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Quit')
    
quit_program = False
g = 1

while not quit_program :
    print_menu()
    chc = int(input("Please choose one of the menu options:"))
    if chc == 3:
        print("Goodbye, Thanks for playing!")
        quit_program = True
    else:
        if chc == 1:
            print("Adding Random Numbers")
            print('Enter -1 to go back')
            while quit_program == False:
                import random
                random_num = random.randint(1, 100)
                random_num1 = random.randint(1, 100)
                print(f'{random_num} + {random_num1} =')
                random_sum = random_num + random_num1
                chc1 = int(input())
                if chc1 == -1:
                    break
                elif chc1 < random_sum:
                    print('Too Low!')
                    g += 1
                    continue
                elif chc1 > random_sum:
                    print('Too High!')
                    g += 1
                    continue
                elif chc1 == random_sum:
                    print('Congratulations, you answered correctly')
                    print(f'You made {g} guesses')
            
        elif chc == 2:
            print("Subtracting Random Numbers")
            print('Enter +1 to go back')
            while quit_program == False:
                import random
                random_num = random.randint(1, 100)
                random_num1 = random.randint(1, 100)
                print(f'{random_num} - {random_num1} =')
                random_sub = random_num - random_num1
                chc1 = int(input())
                if chc1 == +1:
                    break
                if chc1 < random_sub:
                    print('Too Low!')
                    g += 1
                    continue
                elif chc1 > random_sub:
                    print('Too High!')
                    g += 1
                    continue
                elif chc1 == random_sub:
                    print('Congratulations, you answered correctly')
                    print(f'You made {g} guesses')
     
        else:
            print("Not Valid Choice")
    
