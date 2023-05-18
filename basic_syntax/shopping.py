budget = int(input())
all_products = 0

while True:
    product = input()
    if product == 'End':
        print('You bought everything needed.')
        break
    product = int(product)
    all_products += product
    if all_products > budget:
        print('You went in overdraft!')
        break


