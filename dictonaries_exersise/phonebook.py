phone_book = {}
n = None
while True:
    phone = input()
    if '-' not in phone:
        n = int(phone)
        break
    phone = phone.split('-')
    phone_book[phone[0]] = phone[1]

for i in range(n):
    name = input()
    if name not in phone_book:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phone_book[name]}')
