n_salas = int(input("Numero de salas: "))
lugares_vagos = []

for sala in range(n_salas):
    lugares_vagos.append(int(input(f"Lugares vagos na sala {sala+1}: ")))

vendidos = [0] * len(lugares_vagos)

while True:

    sala = int(input("Sala: [0 p/ sair]"))

    if sala == 0:
        print("FIM")
        break

    if sala > len(lugares_vagos) or sala < 1:
        print("Sala Invalida")
    elif lugares_vagos[sala - 1] == 0:
        print("Sala Lotada")
    else:
        lugares = int(input(f"Quantos lugares voce deseja ({lugares_vagos[sala-1]} vagos):"))
        if lugares > lugares_vagos[sala-1]:
            print("Esse numero de lugares nao esta disponivel")
        elif lugares < 0:
            print("Numero Invalido")
        else:
            lugares_vagos[sala-1] -= lugares
            vendidos[sala-1] += lugares
            print(f"{lugares} lugares vendidos")

print("\nUtilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala+1} - {vagos} lugar(es) vazio(s)")


print("\nVendas por sala")
total_vendido = 0
for sala, vendas in enumerate(vendidos):
    print(f"Sala {sala+1} - {vendas} ingresso(s) vendido(s)")
    total_vendido += vendas

print(f"Total de ingressos vendidos: {total_vendido}")
