# CTI-110
# P4HW1 - Score List
# Charles McCrae 
# 06/30/22

    

i = int(input('How many scores do you want to enter?'))
c = i
score_list = [-1]
min_scr = min(score_list)

mod_list = score_list.remove(min_scr)
avg = (f'{(sum(score_list) / len(score_list)):.2f}')
        


for score in score_list:
    if score >= 90:
        grade = 'A'
    else:
        if score >= 80:
            grade = 'B'
        else:
            if score >= 70:
                grade = 'C'
            else:
                if score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'



for i in range(0, 101):
    if (c < 1) or (c >= 101):
        print('Invalid Score')
        print('Score should be between 0 and 100')
        print('Please enter again')
        int(input('How many scores do you want to enter?'))
        if (c > 0) and (c <= 100):
            continue
    elif (c > 0) and (c <= 100):
        score_list.append(int(input('Enter score:')))
        print(c)
        c -= 1
        if (c < 1):
            print('----------Results----------')
            print(f'Lowest Score: {min_scr}')
            print(f'Modified List: {mod_list}')
            print(f'Scores Average: {avg}')
            print(f'Grade: {grade}')
            print('----------------------------')
            break




