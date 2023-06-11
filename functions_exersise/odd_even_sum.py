def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for index in number:
        index = int(index)
        if index % 2 == 0:
            even_sum += index
        elif index % 2 != 0:
            odd_sum += index
    return odd_sum, even_sum


numbers = input()
sum_odd_and_even = odd_even_sum(numbers)
print(f'Odd sum = {sum_odd_and_even[0]}, Even sum = {sum_odd_and_even[1]}')