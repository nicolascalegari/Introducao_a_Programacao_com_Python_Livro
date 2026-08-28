a = int(input())
b = int(input())

cont = 1
resp = 0

while cont <= b:
    resp += a
    cont += 1

print(f"{a} * {b} = {resp}")
