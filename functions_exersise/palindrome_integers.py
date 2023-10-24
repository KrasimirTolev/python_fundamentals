numbers = input().split(', ')
for number in range(len(numbers)):
    list_number = [int(symbol) for symbol in numbers[number]]
    reversed_number = list(reversed(list_number))
    if list_number == reversed_number:
        print('True')
    else:
        print('False')