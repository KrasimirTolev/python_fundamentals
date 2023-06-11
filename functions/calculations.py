multiply = lambda first_num, second_num: int(first_num * second_num)

divide = lambda first_num, second_num: int(first_num / second_num)

add = lambda first_num, second_num: first_num + second_num

subtract = lambda first_num, second_num: first_num - second_num

operation = input()
first_number = int(input())
second_number = int(input())

if operation == 'multiply':
    print(multiply(first_number, second_number))
elif operation == 'divide':
    print(divide(first_number, second_number))
elif operation == 'add':
    print(add(first_number, second_number))
elif operation == 'subtract':
    print(subtract(first_number, second_number))
