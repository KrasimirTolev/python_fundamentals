list_numbers = list(map(int, input().split()))


while True:
    command = input()
    if command == 'Finish':
        break
    command = command.split()
    if command[0] == 'Add':
        list_numbers.append(int(command[1]))
    elif command[0] == 'Remove':
        list_numbers.remove(int(command[1]))
    elif command[0] == 'Replace':
        for index in range(len(list_numbers)):
            if list_numbers[index] == int(command[1]):
                list_numbers[index] = int(command[2])
                break
    if command[0] == 'Collapse':
        for i in reversed(list_numbers):
            if i < int(command[1]):
                list_numbers.remove(i)
list_numbers = list(map(str, list_numbers))
numbers_str = ' '.join(list_numbers)
print(numbers_str)
