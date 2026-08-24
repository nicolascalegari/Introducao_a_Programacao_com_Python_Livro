s = input("Digite o número: ")
i = 0
f = len(s) - 1 

while f > i and s[i] == s[f]:
    f -= 1
    i += 1

if s[i] == s[f]:
    print(f"{s} é palindromo") 
else:
    print(f"{s} não é palindromo")