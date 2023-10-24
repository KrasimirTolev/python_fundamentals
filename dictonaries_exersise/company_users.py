company = {}

while True:
    employee = input()
    if employee == 'End':
        break
    name, ID = employee.split(' -> ')
    if name not in company:
        company[name] = [ID]
    else:
        if ID not in company[name]:
            company[name].append(ID)

for k, v in company.items():
    print(k)
    for i in v:
        print(f'-- {i}')