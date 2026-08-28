dep_inicial = float(input("Informe o valor do deposito inicial: "))
taxa = float(input("Informe a taxa de juros da poupança: "))
x = 1
while x <= 24:
    print(f"Valor referente ao {x}º mês: R$ {dep_inicial * (taxa/100) + dep_inicial:.2f}")
    dep_inicial += (dep_inicial * (taxa/100))
    x += 1