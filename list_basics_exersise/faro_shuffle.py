from typing import List

cards = input().split()
n = int(input())


for index_of_shuffle in range(n):
    middle_of_deck = len(cards) // 2
    left_side = cards[0:middle_of_deck]
    right_side = cards[middle_of_deck:]
    cards = []
    for index_of_card in range(len(left_side)):
        cards.append(left_side[index_of_card])
        cards.append(right_side[index_of_card])
print(cards)