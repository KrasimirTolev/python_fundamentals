products = {}

while True:
    order = input()
    if order == 'buy':
        break
    product, price, qty = order.split()
    if product not in products:
        products[product] = [float(price), int(qty)]
    else:
        products[product][0] = float(price)
        products[product][1] += int(qty)

for k, v in products.items():
    print(f'{k} -> {v[0] * v[1]:.2f}')

