n = int(input())
for num in range(1, n + 1):
    sum_digit = 0
    digit = num
    while digit >= 10:
        sum_digit += num % 10
        digit = 0
        digit += num // 10
    sum_digit += digit
    if (sum_digit == 5) or (sum_digit == 7) or (sum_digit == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
