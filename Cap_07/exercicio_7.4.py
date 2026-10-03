s = input("Digite a string: ")
dic = {}

for c in s:
    dic[c] = dic.get(c, 0) + 1

for chave, valor in dic.items():
    print(f"{chave}: {valor}x")