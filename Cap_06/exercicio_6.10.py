L = [15, 7, 27, 39]

p = int(input("Primeiro valor [p]:"))
v = int(input("Segundo valor [v]:"))
x = 0
achou_p = False
achou_v = False
primeiro = 0
posicao_p = 0
posicao_v = 0

while x < len(L):
    if L[x] == p:
        achou_p = True
        posicao_p = x
        if not achou_v:
            primeiro = 1

    if L[x] == v:
        achou_v  = True
        posicao_v = x
        if not achou_p:
            primeiro = 2

    x += 1

if achou_p:
    print(f"p: {p} encontrado, posicao: {posicao_p}")
else:
    print(f"p: {p} nao encontrado")

if achou_v:
    print(f"v: {v} encontrado, posicao: {posicao_v}")
else:
    print(f"v: {v} nao encontrado")

if primeiro == 1:
    print("p foi encontrado antes de v")
elif primeiro == 2:
    print("v foi encontrado antes de p")