version = list(map(int, input().split('.')))
version[2] += 1

if version[2] > 9:
    version[2] = 0
    version[1] += 1
if version[1] > 9:
    version[1] = 0
    version[0] += 1

version = list(map(str, version))
print('.'.join(version))