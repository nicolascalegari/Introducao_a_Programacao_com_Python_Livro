antes = [1, 2, 5, 6, 9]
depois = [1, 2, 8, 10]

set_antes = set(antes)
set_depois = set(depois)

print("Antes:", antes)
print("Depois:", depois)

print("Elementos que não mudaram: ", set_antes & set_depois)
print("Elementos novos: ", set_depois - set_antes)
print("Elementos que foram removidos: ", set_antes - set_depois)