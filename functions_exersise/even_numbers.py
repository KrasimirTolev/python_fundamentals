all_numbers = input().split()
numbers_digits = [int(number) for number in all_numbers]

check_even = lambda x: x % 2 == 0

even_numbers = list(filter(check_even, numbers_digits))
print(even_numbers)
