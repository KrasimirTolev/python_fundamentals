
numbers = list(map(int, input().split(', ')))
indices_fund = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))
even_nums = list(filter(lambda a: a != 'no', indices_fund))
print(even_nums)