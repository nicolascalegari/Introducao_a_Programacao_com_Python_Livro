primeira = []
segunda = []
aux = 0

while True:
    aux = int(input("Valor da Primeira lista: [0 para sair] "))
    if aux == 0:
        break
    primeira.append(aux)

while True:
    aux = int(input("Valor da Segunda lista: [0 para sair] "))
    if aux == 0:
        break
    segunda.append(aux)


terceira = primeira[:]
terceira.extend(segunda)

cont = 0

while cont < len(terceira):
    print(f"Valor {cont} : {terceira[cont]}")
    cont += 1