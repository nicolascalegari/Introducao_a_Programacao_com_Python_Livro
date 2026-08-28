primeira = []
segunda = []

while True:
    aux = int(input("Digite o valor da primeira lista: [0 para sair] "))
    if aux == 0:
        break
    primeira.append(aux)

while True:
    aux = int(input("Digite o valor da segunda lista: [0 para sair] "))
    if aux == 0:
        break
    segunda.append(aux)

terceira = []
duas_listas = primeira[:]
duas_listas.extend(segunda)

for item in duas_listas:
    if item not in terceira:
        terceira.append(item)

x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x += 1

