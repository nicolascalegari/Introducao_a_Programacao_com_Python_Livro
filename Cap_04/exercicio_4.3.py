a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b and a > c:
    print(f"{a} é o maior valor")

if b > a and b > c:
    print(f"{b} é o maior valor")

if c > a and c > b:
    print(f"{c} é o maior valor")