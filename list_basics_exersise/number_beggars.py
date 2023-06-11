money = input().split(', ')
num_beggars = int(input())
beggar_money_list = []
money = list(map(int, money))
start_index = 0

while True:
    if start_index >= num_beggars:
        break
    earned_money = 0
    for current_index in range(start_index, len(money), num_beggars):
        earned_money += money[current_index]
    beggar_money_list.append(earned_money)
    start_index += 1


print(beggar_money_list)