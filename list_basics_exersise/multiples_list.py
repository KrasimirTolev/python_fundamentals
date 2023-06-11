first_num = int(input())
last_num = int(input())
multiplied_num = 0
multiplied_list = []
for current_num in range(1, last_num + 1):
    multiplied_num = first_num * current_num
    multiplied_list.append(multiplied_num)

print(multiplied_list)