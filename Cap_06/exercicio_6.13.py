T = [-10, -8, 0, 1, 2, 5, -5, -4]

# Usando Python

print(f"Menor Temp: {min(T):.2f}")
print(f"Maior Temp: {max(T):.2f}")
print(f"Temp Media: {sum(T) / len(T):.2f}")

# Sem usar Python

menor = float("inf")
maior = float("-inf")
media = 0
soma = 0
cont = 0

for e in T:
    if e < menor:
        menor = e
    if e > maior:
        maior = e
    soma += e
    cont += 1

media = soma /  cont

print(f"Menor Tempo: {menor:.2f}")
print(f"Maior Tempo: {maior:.2f}")
print(f"Temp Media: {media:.2f}")
    