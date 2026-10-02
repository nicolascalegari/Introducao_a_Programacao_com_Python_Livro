l1 = [1, 2, 6, 8]
l2 = [3, 6, 8, 9]

print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")

set_1 = set(l1)
set_2 = set(l2)

print("Valores comuns nas duas listas:", set_1 & set_2)
print("Valores que so existem na primeira lista:", set_1 - set_2)
print("Valores que so existem na segunda lista:", set_2 - set_1)
print("Elementos nao repeditos das duas lista:", set_1 ^ set_2)
print("Primeira lista sem elementos repetidos na segunda:", set_1 - set_2)