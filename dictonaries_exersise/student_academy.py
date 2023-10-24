academy = {}
n = int(input())

for student in range(n):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = [grade]
    else:
        academy[name].append(grade)

for student, grades in academy.items():
    if sum(grades) / len(grades) >= 4.5:
        print(f'{student} -> {sum(grades) / len(grades):.2f}')
