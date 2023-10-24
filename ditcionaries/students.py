students = []
search_course = None
while True:
    student_info = input()
    if ':' not in student_info:
        search_course = student_info
        break

    name, ID, course = student_info.split(':')

    students.append({'name': name, 'ID': ID, 'course': course})


for student in students:
    if search_course[0:3] in student['course']:
        print(f"{student['name']} - {student['ID']}")
