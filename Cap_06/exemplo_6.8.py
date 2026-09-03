#Pilha

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"Existem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um prato novo,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D, ou S): ")

    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1) #Retirar o ultimo elemento da Pilha
            print(f"Prato {lavado} lavado")
        else:
            print("pilha vazia.")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operacao invalida.")
    