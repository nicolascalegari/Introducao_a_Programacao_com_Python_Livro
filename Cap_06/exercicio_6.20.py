d = {}

frase = input("Digite uma frase para contar as letras:")

for letra in frase:
    if letra in d:
        d[letra] = d[letra] + 1 # Pegue o valor atual da contagem dessa letra e some mais 1
    else:
        d[letra] = 1 # Crie essa letra no dicionário e defina a contagem dela como 1

print(d)