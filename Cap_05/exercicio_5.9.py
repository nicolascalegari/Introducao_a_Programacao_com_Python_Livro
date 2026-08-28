dividendo = int(input())
divisor = int(input())

quociente = 0
x = dividendo

while x >= divisor:
    x -= divisor
    quociente += 1

print(f"{dividendo} / {divisor} = {quociente}")


