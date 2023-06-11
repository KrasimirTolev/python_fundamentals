list_of_num_str = input().split()
num_removal = int(input())
list_of_num_int = []

for current_index in list_of_num_str:
    list_of_num_int.append(int(current_index))
sorted_list = sorted(list_of_num_int)
for remove_index in range(num_removal):
    list_of_num_int.remove(sorted_list[remove_index])
final_numbers = ', '.join(map(str, list_of_num_int))

print(final_numbers)