dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quo = 0

x = dividendo

while x >= divisor:
    x -= divisor
    quo += 1

resto = x

print(f"O resto de {dividendo} / {divisor} é {quo} e sobra {resto}")