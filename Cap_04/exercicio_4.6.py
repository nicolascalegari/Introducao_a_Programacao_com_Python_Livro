dis = float(input("Informe a distância que deseja percorrer: "))

if dis <= 200:
    print(f"Valor da passagem: R$ {dis * 0.5:5.2f}")
else:
    print(f"Valor da passagem: R$ {dis * 0.45:5.2f}")