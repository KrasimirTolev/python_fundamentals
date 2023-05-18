budget = float(input())
kg_flour_price = float(input())
pack_of_eggs_price = kg_flour_price * 0.75
milk_250_ml = (kg_flour_price * 1.25) / 4
flour_1_piece_price = kg_flour_price + pack_of_eggs_price + milk_250_ml
max_flour = budget // flour_1_piece_price
amount_spend = max_flour * flour_1_piece_price
remaining_amount = budget - amount_spend
colored_eggs = 0
for egg in range(1, int(max_flour) + 1):
    colored_eggs += 3
    if egg % 3 == 0:
        colored_eggs -= (egg - 2)

print(f"You made {max_flour:.0f} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {remaining_amount:.2f}BGN left.")