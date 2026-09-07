lugares_vagos = [10,2,1,3,0]
vendidos = [0] * len(lugares_vagos)

while  True:

    sala = int(input("Sala: [0 p/ sair]"))

    if sala == 0:
        print("Fim.")
        break

    if sala > len(lugares_vagos) or sala < 1:
        print("Sala Invalida!")
    elif lugares_vagos[sala - 1] == 0:
        print("Sala Cheia!")
    else:
        lugares = int(input(f"Quantos lugares você deseja: ({lugares_vagos[sala - 1]} vagos):"))

        if lugares > lugares_vagos[sala - 1]:
            print("Esse lugar não esta disponivel!")
        elif lugares < 0:
            print("Número inválido!")
        else:
            lugares_vagos[sala - 1] -= lugares
            vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")

print("Utilização das salas")

for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")

print("\nVendas por sala")
total_vendido = 0

for sala, vendas in enumerate(vendidos):
    print(f"Sala {sala + 1} - {vendas} ingressos vendidos(s)")
    total_vendido += vendas

print(f"Total de ingressos vendidos: {total_vendido}")