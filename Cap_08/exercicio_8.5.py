def pesquise(lista, valor):

    if valor in lista:
        return lista.index(valor)
    return None

L = [10, 20, 30, 40, 50]

print(pesquise(L, 20))
print(pesquise(L, 25))