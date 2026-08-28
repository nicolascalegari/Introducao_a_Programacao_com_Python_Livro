
total_pago = 0
total_itens = 0

while True:
    codigo = int(input("Digite o codigo do produto: [ou 0 para encerrar] "))
    if codigo == 0:
            break
    qtd = int(input("Digite a quantidade comprada: "))
    if codigo == 1:
        preco = qtd * 0.5
    elif codigo == 2:
        preco = qtd * 1.0
    elif codigo == 3:
        preco = qtd * 4.0
    elif codigo == 5:
        preco = qtd * 7.0
    elif codigo == 9:
        preco = qtd * 8.0
    else:
        print("Código inválido!")
        break
    total_pago += preco
    total_itens += 1

print(f"Valor total da compra: R$ {total_pago:.2f}")
print(f"Quantida de itens comprados: {total_itens}")