ultimo = 0
fila1 = []
fila2 = []

while True:

    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao final da fila 1 ou G para fila 2,")
    print("ou A para realizar o atendimento da fila 1 ou B para fila 2.")
    print("S para sair")

    operacao = input("Operação (F, G, A, B ou S): ") #String

    x = 0
    sair = False

    for x in range(len(operacao)):

        if operacao[x] == "A" or operacao[x] == "F":
            fila = fila1
        else:
            fila = fila2

        if operacao[x] == "A" or operacao[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F" or operacao[x] == "G":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida")

        x += 1

    if sair:
        break