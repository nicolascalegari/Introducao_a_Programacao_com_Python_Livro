print("Calculadora Básica")
primeiro = float(input("Digite o primeiro valor: "))
operacao = input("Escolha a operação: [+, -, *, /]")
segundo = float(input("Digite o segundo valor: "))

if operacao == "+":
    print(f"Resultado: {primeiro + segundo:.2f}")
elif operacao == "-":
    print(f"Resultado: {primeiro - segundo:.2f}")
elif operacao == "*":
    print(f"Resultado: {primeiro * segundo:.2f}")
elif operacao == "/":
    if segundo != 0:
        print(f"Resultado: {primeiro / segundo:.2f}")
    else:
        print("Erro! Divisão por Zero!")
else:
    print("Erro! Operação inválida. [+, -, *, /]")