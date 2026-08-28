valido = True
plano = input("Qual é o seu plano de celular? [falapouco / falamuito]")

if plano == "falapouco":
    minutos_do_plano = 100
    extra = 0.20
    preco = 50
elif plano == "falamuito":
    minutos_do_plano = 500
    extra = 0.15
    preco = 99
else:
    valido = False

if not valido:
    print(f"Erro: Não conheço esse plano {plano}")
else:
    minutos_consumidos = int(input("Quantos minutos voçê consumiu: "))
    print("Você vai pagar: ")
    print(f"Preço do plano R$ {preco:5.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_do_plano:
        suplemento = extra * (minutos_consumidos - minutos_do_plano)
    print(f"Suplemento R$ {suplemento:5.2f}")
    print(f"Total R$ {preco + suplemento:5.2f}")
