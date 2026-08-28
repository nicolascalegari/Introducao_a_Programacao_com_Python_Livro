preco = float(input("Informe o preço da mercadoria: "))

perc = float(input("Informe o percentual de desconto da mercadoria: "))

desconto = preco * perc / 100

print(f"Desconto = R$ {desconto:5.2f}")

print(f"Preco a pagar: R$ {preco - desconto:5.2f}")