numbers = input().split(', ')
positive_numbers = [positive for positive in numbers if int(positive) >= 0]
negative_numbers = [negative for negative in numbers if int(negative) < 0]
even_numbers = [even for even in numbers if int(even) % 2 == 0]
odd_numbers = [odd for odd in numbers if int(odd) % 2 != 0]

print(f'Positive: {", ".join(positive_numbers)}')
print(f'Negative: {", ".join(negative_numbers)}')
print(f'Even: {", ".join(even_numbers)}')
print(f'Odd: {", ".join(odd_numbers)}')
