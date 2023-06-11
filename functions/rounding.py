numbers = input().split()

numbers_digits = [float(num) for num in numbers]

rounded_numbers = [round(num) for num in numbers_digits]

print(rounded_numbers)