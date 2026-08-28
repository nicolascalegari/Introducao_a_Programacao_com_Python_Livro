n = float(input("Digite um numero para saber a raiz quadrada: "))
b = 2

while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p

print(f"A Raiz quadrada de {n} é aprox. {p:8.4f}")