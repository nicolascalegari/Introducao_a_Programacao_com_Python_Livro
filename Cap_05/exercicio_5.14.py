soma = 0
contador = 0
media = 0
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    contador += 1
    soma += v
    media = soma / contador

print(f"Quantidade de números digitados: {contador}")
print(f"Soma total dos números digitados: {soma}")
print(f"Média: {media}")