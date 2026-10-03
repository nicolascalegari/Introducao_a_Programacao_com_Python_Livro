vogais = "aeiou"

frase = input("Digite uma frase: ")

frase_minuscula = frase.lower()

for vogal in vogais:

    ocorrencia_vogal = frase_minuscula.count(vogal)

    if ocorrencia_vogal > 0:
        print(f"{vogal} aparece {ocorrencia_vogal} vez(es)")