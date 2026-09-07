L = [1, 7, 2, 4]

menor = float("inf")

for e in L:
    if e < menor:
        menor = e

print(menor)

menor = min(L)
print(menor)