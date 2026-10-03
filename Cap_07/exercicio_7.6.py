primera = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""

    for letra in primera:
        posicao = segunda.find(letra)
        if posicao != -1:
            resultado += terceira[posicao]
        else:
            resultado += letra

    if resultado == "":
        print("Todas as letras foram removidas.")
    else:
        print(
            f"As letras {segunda} foram substituidas por "
            f"{terceira} em {primera}, formando: {resultado}"
        )

else:
    print("Erro: A segunda e terceira string devem ter o mesmo tamanho.")