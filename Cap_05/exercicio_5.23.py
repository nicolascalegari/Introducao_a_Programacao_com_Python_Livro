n = int(input("Digite um numero: "))

if n < 0:
    print("Digite numeros positivos")
if n == 0 or n == 1:
    print(f"{n} não é primo")
else:
    if n == 2:
        print("2 é primo")
    elif n % 2 == 0:
        print(f"{n} não é primo, pois 2 é o único par que é primo")
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
            x += 2
        if x == n:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo, pois é divisivel por {x}")