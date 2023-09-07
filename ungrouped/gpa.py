# A student makes honour roll if their average is >= 85
# and their lowest grade is not below 70
gpa = float(input('What was your grade point average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
 
# check if student is on honour roll, all i need to do is check
# the boolean variable i set earlier in my code
if honour_roll:
    print('You made the honour roll')