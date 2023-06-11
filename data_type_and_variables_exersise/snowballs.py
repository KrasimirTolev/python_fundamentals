import sys

num_snowball = int(input())
max_points = - sys.maxsize
max_weight = - sys.maxsize
max_time = - sys.maxsize
max_quality = - sys.maxsize
points = 0

for snowball in range(num_snowball):
    weight = int(input())
    time = int(input())
    quality = int(input())
    points = (weight / time) ** quality
    if points > max_points:
        max_points = points
        max_weight = weight
        max_time = time
        max_quality = quality
print(f"{max_weight} : {max_time} = {max_points:.0f} ({max_quality})")
