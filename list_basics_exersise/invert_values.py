list_num = input().split()
opposite_list = []
for number in list_num:
    curr_number = - int(number)
    opposite_list.append(curr_number)
print(opposite_list)