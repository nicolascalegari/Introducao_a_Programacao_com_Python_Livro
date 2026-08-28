vel = int(input("Qual a velocidade do carro? "))
if vel > 80:
    print("Você foi multado")
    val = (vel-80)*5
    print(f"Valor da multa: R$ {(vel-80)*5:5.2f}")
    