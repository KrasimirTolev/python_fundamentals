def smallest_num(a, b, c):
    if a < b and a < c:
        print(a)
    elif b < c and b < a:
        print(b)
    else:
        print(c)


first_num = int(input())
second_num = int(input())
third_num = int(input())

smallest_num(first_num, second_num, third_num)