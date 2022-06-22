# Grade Calculater using 10-point grading scale
# 06/21/22
# CTI-110 P3HW1
# Charles McCrae

def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    
    # TO DO: define the rest of the scores (X)
    score = int(input('Enter grade: '))
    if score >= 90:
        print('Your grade is: A')
    else:
        if score >= 80:
            print('Your grade is: B')
        else:
            if score >= 70:
                print('Your grade is: C')
            else:
                if score >= 60:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F') # TO DO: finish this (X)
                    # Scores only go down to d before the rest are f
                    # Check indentation 
# program start
main()
