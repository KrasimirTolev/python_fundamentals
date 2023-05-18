divisor = int(input())
boundary = int(input())

while True:
    if boundary % divisor == 0:
        print(boundary)
        break
    boundary -= 1