L = [1, 7, 2, 4]

maior = float("-inf")

for e in L:

    if e > maior:
        maior = e

print(maior)

maior = max(L)
menor = min(L)

print(maior)
print(menor)