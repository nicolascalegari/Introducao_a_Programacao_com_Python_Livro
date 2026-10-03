primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = ""

for letra in primeira:
    if letra not in segunda:
        terceira += letra

if terceira == "":
    print("Todas letras removidas.")
else:
    print(f"Letras: {segunda} foram removidas de {primeira}, formando: {terceira}")