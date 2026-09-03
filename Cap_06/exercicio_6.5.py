ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"Existem {len(fila)} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao final da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operacao (F, A ou S): ")

    x = 0
    sair = False

    while x < len(operacao):
        if operacao[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} antendido.")
            else:
                print("Fila vazia!")
        elif operacao[x] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operacao invalida.")

        x += 1

    if sair:
        break
