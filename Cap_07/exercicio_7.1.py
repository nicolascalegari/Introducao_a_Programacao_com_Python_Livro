primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
posicao = primeira.find(segunda)

if posicao == -1:
    print(f"{segunda} nao encontrada em {primeira}")
else:
    print(f"{segunda} encontrada na posicao {posicao} de {primeira}")