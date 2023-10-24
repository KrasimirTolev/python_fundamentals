items = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
curr_items = input().split()
obtained = False
while not obtained:
    for i in range(0, len(curr_items), 2):
        value = int(curr_items[i])
        key = curr_items[i + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items['shards'] >= 250:
            print('Shadowmourne obtained!')
            items['shards'] -= 250
            obtained = True
        if items['fragments'] >= 250:
            print('Valanyr obtained!')
            items['fragments'] -= 250
            obtained = True
        if items['motes'] >= 250:
            print('Dragonwrath obtained!')
            items['motes'] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    curr_items = input().split()

for material, qty in items.items():
    print(f'{material}: {qty}')
