# Listas com elementos de tipos diferentes

produto_1 = ["maça", 10, 0.30]
produto_2 = ["pera", 5, 0.75]
produto_3 = ["kiwi", 4, 0.98]

compras = [produto_1, produto_2, produto_3]

for e in compras:

    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Valor: {e[2]:5.2f}")
    print()