valores = [9, 8, 7, 12, 0, 13, 21]

pares = []

impares = []

for e in valores:

    if e % 2 == 0:
        pares.append(e)

    else:
        impares.append(e)

print("Pares: ", pares)
print("Impares: ", impares)