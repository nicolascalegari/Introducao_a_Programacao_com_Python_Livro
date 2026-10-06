def maior(num1, num2):

    return max(num1, num2) 


num1, num2 = map(int, input("Digite dois numeros separados por espaço:").split())

print(f"Maior numero: {maior(num1, num2)}")

