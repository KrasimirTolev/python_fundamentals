numbers = input().split()
numbers = [int(number) for number in numbers]
min_num = min(numbers)
max_num = max(numbers)
sum_numbers = sum(numbers)
print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {sum_numbers}')