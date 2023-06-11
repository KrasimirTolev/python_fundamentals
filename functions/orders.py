
def order(product, qty):
    price = 0
    if product == 'coffee':
        price = 1.5 * qty
    elif product == 'water':
        price = 1 * qty
    elif product == 'coke':
        price = 1.4 * qty
    elif product == 'snacks':
        price = 2 * qty
    return price


product_input = input()
qty_input = int(input())


print(f'{order(product_input, qty_input):.2f}')
