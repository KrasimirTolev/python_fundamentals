country = input().split(', ')
city = input().split(', ')

capitals = dict(zip(country, city))

for k, v in capitals.items():
    print(f'{k} -> {v}')
