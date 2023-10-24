rooms = int(input())
free_space = 0
not_enough = 0
for room in range(1, rooms + 1):
    chairs_people = input().split()
    if len(chairs_people[0]) >= int(chairs_people[-1]):
        free_space += len(chairs_people[0]) - int(chairs_people[-1])
    elif int(chairs_people[-1]) > len(chairs_people[0]):
        not_enough += 1
        print(f'{int(chairs_people[-1]) - len(chairs_people[0])} more chairs needed in room {room}')

if not_enough == 0:
    print(f'Game On, {free_space} free chairs left')