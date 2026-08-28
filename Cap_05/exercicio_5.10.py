pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if (questao == 1 and resposta == "b") or (questao == 1 and resposta == "B"):
        pontos += 1
    elif (questao == 2 and resposta == "a") or (questao == 2 and resposta == "A"):
        pontos += 1
    elif (questao == 3 and resposta == "d") or (questao == 3 and resposta == "D"):
        pontos += 1
    questao += 1
print(f"O aluno fez {pontos} ponto(s)")