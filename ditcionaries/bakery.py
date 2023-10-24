food_value = input().split()
bakery = {}

for _ in range(0, len(food_value), 2):
    key = food_value[_]
    value = int(food_value[_ + 1])
    bakery[key] = value

print(bakery)