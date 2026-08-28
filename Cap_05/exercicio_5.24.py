qtd_primos = int(input("Digite a quantidade de numeros primos desejada: "))

if qtd_primos < 0:
    print("Número invalido!")
else:

    if qtd_primos >= 1:
        print("2")
    primos_gerados = 1
    proximo_primo = 3

    while primos_gerados < qtd_primos:
        divisor = 3

        while divisor < proximo_primo:
            if proximo_primo % divisor == 0:
                break

            divisor += 2

        if divisor == proximo_primo:
            print(proximo_primo)
            primos_gerados += 1

        proximo_primo += 2