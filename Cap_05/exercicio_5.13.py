divida = float(input("Informe o valor da dívida: "))
juros = float(input("Informe o juros mensal: "))
valor_pago_mensal = float(input("Informe o valor mensal que será pago: "))

x = divida
meses = 0
juros_pago = 0
total_pago = 0

while x > 0:

    divida += divida * (juros/100)
    juros_pago += divida * (juros/100)
    total_pago += juros_pago + valor_pago_mensal
    divida = divida - valor_pago_mensal
    x = divida
    meses += 1
    
print(f"Qtd de meses: {meses}")
print(f"Valor de juros pago: R$ {juros_pago:.2f}")
print(f"Total da dívida R$: {total_pago:.2f}")