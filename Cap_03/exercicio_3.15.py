cigarros_dia = int(input("Quantos cigarros fuma por dia: "))

anos_fumou = int(input("Quantos anos fumou: "))

min_perdidos_dia = cigarros_dia * 10

dias_perdidos = ((anos_fumou * 365) * min_perdidos_dia) / 1440

print(f"Redução de vida em dias [aprox]: {dias_perdidos:.0f}")

