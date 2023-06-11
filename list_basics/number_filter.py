n = int(input())
list_of_num = []
filtered_list = []


for _ in range(n):
    number = int(input())
    list_of_num.append(number)

type_of_num = input()

for num_of_list in range(n):
    if type_of_num == 'even':
        if list_of_num[num_of_list] % 2 == 0:
            filtered_list.append(list_of_num[num_of_list])
    elif type_of_num == 'odd':
        if list_of_num[num_of_list] % 2 != 0:
            filtered_list.append(list_of_num[num_of_list])
    elif type_of_num == 'negative':
        if list_of_num[num_of_list] < 0:
            filtered_list.append(list_of_num[num_of_list])
    elif type_of_num == 'positive':
        if list_of_num[num_of_list] >= 0:
            filtered_list.append(list_of_num[num_of_list])
print(filtered_list)