words = input().split()
even_words = [even for even in words if len(even) % 2 == 0]
print('\n'.join(even_words))