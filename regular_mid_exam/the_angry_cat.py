price_rating = list(map(int, input().split(', ')))
entry_point = int(input())
type_items = input()


left_side = price_rating[:entry_point]
right_side = price_rating[entry_point + 1:]
left_sum = 0
right_sum = 0
left_filtered = []
right_filtered = []
if type_items == "cheap":
    for number in left_side:
        if number < price_rating[entry_point]:
            left_filtered.append(number)
    for number_right in right_side:
        if number_right < price_rating[entry_point]:
            right_filtered.append(number_right)
    left_sum = sum(left_filtered)
    right_sum = sum(right_filtered)
elif type_items == "expensive":
    for number in left_side:
        if number >= price_rating[entry_point]:
            left_filtered.append(number)
    for number_right in right_side:
        if number_right >= price_rating[entry_point]:
            right_filtered.append(number_right)
    left_sum = sum(left_filtered)
    right_sum = sum(right_filtered)
# Output
if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
