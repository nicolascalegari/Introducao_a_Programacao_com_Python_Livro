kms = float(input("Informe a quantidade de quilometros percorridos com o carro alugado: "))

dia = int(input("Informe a quantidade de dias que o carro ficou alugado: "))

v_dia = float(dia) * 60

v_km = kms * 0.15

print(f"Custo total do aluguel: R$ {v_dia + v_km:5.2f}")

