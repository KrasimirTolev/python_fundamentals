qty = int(input())
num = 0

for i in range(qty):
    num = int(input())
    if num % 2 != 0:
        print(f'{num} is odd!')
        break
else:
    print('All numbers are even.')