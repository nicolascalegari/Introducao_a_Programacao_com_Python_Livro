while True:
    op = input("Escolha a operação: [+, -, *, /, 'sair'] ")
    
    if op == 'sair':
        break

    print("Informe dois valores: [ex: 5 7]")
    num1, num2 = map(float, input().split())
    
    if op == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("Erro, divisão por zero!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
