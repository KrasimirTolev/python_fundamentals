year = int(input())

while True:
    year = int(year)
    year += 1
    year = str(year)
    set_year = set(year)
    if len(set_year) == len(year):
        break
print(year)
