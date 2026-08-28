plano = input("Qual é o seu plano de celular? [falapouco/falamuito]")

if plano == "falapouco":
    minutos = 100
    extra = 0.2
    preco = 50
else:
    minutos = 500
    extra = 0.15
    preco = 99

if plano != "falamuito" and plano != "falapouco":
    print("Plano Errado!")
else:
    minutos_consumidos = int(input("Quantos minutos você usou? "))
    print("Valor a pagar:")
    print(f"Preço do Plano: R${preco:10.2f}")
    suplemento = 0

    if minutos_consumidos > minutos:
        suplemento = extra * (minutos_consumidos - minutos)

    print(f"Suplemento: R$ {suplemento:10.2f}")
    print(f"Total: R$ {preco + suplemento:10.2f}")