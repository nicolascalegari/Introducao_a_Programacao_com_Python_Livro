print("Cálculo de Kw/h")

kw_consumida = float(input("Informe a quantidade de KW consumida: "))
tipo_instalacao = input("Informe o tipo de instalação: [R/I/C]")

if tipo_instalacao == "R":
    if kw_consumida <= 500:
        valor_a_pagar = kw_consumida * 0.40
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
    else:
        valor_a_pagar = kw_consumida * 0.65
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
elif tipo_instalacao == "C":
    if kw_consumida <= 1000:
        valor_a_pagar = kw_consumida * 0.55
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
    else:
        valor_a_pagar = kw_consumida * 0.60
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
elif tipo_instalacao == "I":
    if kw_consumida <= 5000:
        valor_a_pagar = kw_consumida * 0.55
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
    else:
        valor_a_pagar = kw_consumida * 0.60
        print(f"Valor a pagar R$ {valor_a_pagar:5.2f}")
else:
    print("Categoria Inválida! [R/I/C]")

