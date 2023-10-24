from typing import List
numbers = list(map(int, input().split(', ')))
used_numbers = []
interval = 10

while True:
    interval_list = []
    if not numbers:
        break
    for number in numbers:
        if number <= interval:
            interval_list.append(number)
    print(f"Group of {interval}'s: {interval_list}")
    interval += 10
    numbers = [number for number in numbers if number not in interval_list]
