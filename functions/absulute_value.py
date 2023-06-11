num = input().split()
defined_num = [float(float_num) for float_num in num]
final_numbers = [abs(abs_num) for abs_num in defined_num]
print(final_numbers)