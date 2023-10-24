electrons = int(input())
list_electrons = []
number = 1
while True:
    if electrons == 0:
        print(list_electrons)
        break
    formula = 2 * number * number
    if formula <= electrons:
        electrons -= formula
        list_electrons.append(formula)
    elif formula > electrons:
        list_electrons.append(electrons)
        electrons = 0
    number += 1