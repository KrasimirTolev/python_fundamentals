person = int(input())
capacity = int(input())
courses = 0
extra_cours = 0

while True:
    if capacity <= person:
        person -= capacity
        courses += 1
    if person == 0:
        break
    if capacity >= person:
        courses += 1
        break
print(courses)
