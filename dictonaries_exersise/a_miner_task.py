miner = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    qty = int(input())
    if resource not in miner:
        miner[resource] = qty
    else:
        miner[resource] += qty

for r, q in miner.items():
    print(f'{r} -> {q}')