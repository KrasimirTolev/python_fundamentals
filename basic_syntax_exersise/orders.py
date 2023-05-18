n = int(input())
total_per_order = 0
total = 0


for i in range(n):
    per_capsule = float(input())
    days = float(input())
    capsules_per_day = float(input())
    if per_capsule < 0.01 or per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total_per_order = per_capsule * capsules_per_day * days
    total += total_per_order
    print(f'The price for the coffee is: ${total_per_order:.2f}')


print(f'Total: ${total:.2f}')
