price_without_tax = 0
price_with_tax = 0
special_price = 0


while True:
    price = input()
    if price == 'special':
        price_with_tax = price_without_tax * 1.2
        special_price = price_with_tax * 0.9
        break
    elif price == 'regular':
        price_with_tax = price_without_tax * 1.2
        break
    price = float(price)
    if price < 0:
        print('Invalid price!')
        continue
    elif price == 0:
        print('Invalid order!')
        continue
    price_without_tax += price

if special_price > 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_tax:.2f}$\nTaxes: {price_with_tax - price_without_tax:.2f}$\n-----------\nTotal price: {special_price:.2f}$")
elif special_price == 0 and price_with_tax > 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_tax:.2f}$\nTaxes: {price_with_tax - price_without_tax:.2f}$\n-----------\nTotal price: {price_with_tax:.2f}$")
else:
    print('Invalid order!')