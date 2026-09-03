L = [15,7,27,39]

p = int(input("Digite o valor a procurar:"))

x = 0

while x < len(L):
    if L[x] == p:
        break
    x += 1

if x < len(L):
    print(f"{p} achado na posicao {x}")
else:
    print(f"{p} nao encontrado")