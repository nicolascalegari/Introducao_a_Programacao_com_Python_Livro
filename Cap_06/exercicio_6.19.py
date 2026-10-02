estoque = { 
        "tomate": [1000, 2.30],
        "alface": [500, 0.45],
        "batata": [2001, 1.20],
        "feijao": [100, 1.50]
}

for chave in estoque.items():
    print(chave)

total = 0
print("\nVendas:\n")

while True:
    produto = input("Nome do produto ('fim' para sair):")

    if produto == "fim":
        break

    if produto in estoque:
        quantidade = int(input("Quantidade:"))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada nao disponivel.")
    else:
        print("Nome de produto invalido.")

print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")