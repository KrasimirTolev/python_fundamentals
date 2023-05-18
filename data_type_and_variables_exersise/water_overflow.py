n = int(input())
capacity = 255
filled_water = 0

for i in range(n):
    liters_water = int(input())
    if (filled_water + liters_water) > capacity:
        print('Insufficient capacity!')
    else:
        filled_water += liters_water
print(filled_water)