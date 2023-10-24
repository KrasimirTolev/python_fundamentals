product_list = input().split()
stock = {}
for _ in range(0, len(product_list), 2):
    k = product_list[_]
    v = product_list[_ + 1]
    stock[k] = v

search = input().split()

for product in search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")