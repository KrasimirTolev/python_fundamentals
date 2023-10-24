first = input()
second = input()

while True:
    if first not in second:
        break
    second = second.replace(first, '')

print(second)