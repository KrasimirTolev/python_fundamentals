employees_happiness = list(map(int, input().split()))
factor = int(input())


multiplied_happiness = [employee * factor for employee in employees_happiness]
average_happiness = sum(multiplied_happiness) / len(employees_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, multiplied_happiness))
if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")

