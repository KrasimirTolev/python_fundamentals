stock = {}
while True:
    product = input()

    if product == 'statistics':
        break

    product = product.split(': ')
    if product[0] not in stock:
        stock[product[0]] = int(product[1])
    else:
        stock[product[0]] += int(product[1])

print('Products in stock:')
for k, v in stock.items():
    print(f'- {k}: {v}')

print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')


