body_list = []

for _ in range(3):
    part_of_body = input()
    body_list.append(part_of_body)
body_list[0], body_list[2] = body_list[2], body_list[0]
print(body_list)