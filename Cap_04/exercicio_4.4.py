salario = float(input("Informe o valor do salário: "))

if salario > 1250:
    print(f"Novo salario com aumento: R${salario * 1.1:5.2f}")
if salario <= 1250:
    print(f"Novo salario com aumento: R${salario * 1.15:5.2f}")