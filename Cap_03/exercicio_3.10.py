salario = float(input("Valor do salario atual: "))

porcen = float(input("Porcentagem do aumento: "))

novo_sal = salario + (salario * porcen /100)

print(f"Novo salario com aumento: R$ {novo_sal:5.2f}")