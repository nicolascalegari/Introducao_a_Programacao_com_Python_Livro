estoque = { 
        "tomate": [1000, 2.30],
        "alface": [500, 0.45],
        "batata": [2001, 1.20],
        "feijao": [100, 1.50]
}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0

print("Vendas:\n")

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    total += custo

print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preco: {dados[1]:6.2f}\n")