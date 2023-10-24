courses = {}

while True:
    student = input()
    if student == 'end':
        break
    course, name = student.split(' : ')
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)

for k, v in courses.items():
    print(f'{k}: {len(v)}')
    for names in v:
        print(f'-- {names}')