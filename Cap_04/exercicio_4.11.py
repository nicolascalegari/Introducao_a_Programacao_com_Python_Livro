print("Empréstimo Bancário")

valor_casa = float(input("Informe o valor da Casa a comprar: "))
salario = float(input("Informe o valor do salário: "))
anos_a_pagar = int(input("Informe o total de anos a pagar: "))

salario_30_porc = salario * 0.30

prestacao = valor_casa / (anos_a_pagar * 12)

if prestacao <= salario_30_porc:
    print("Empréstimo Aprovado!!!")
else:
    print("Empréstimo Reprovado!!!")
    print("Prestação superior a 30% da renda mensal!")