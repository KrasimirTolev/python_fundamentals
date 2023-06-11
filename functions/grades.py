def define_grade(grade):
    grade = float(grade)
    if grade < 3:
        print('Fail')
    elif grade < 3.5:
        print('Poor')
    elif grade < 4.5:
        print('Good')
    elif grade < 5.5:
        print('Very Good')
    else:
        print('Excellent')


define_grade(input())
