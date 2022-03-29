lista = list(range(100))
for i in lista:
    print(lista[i])

double = [i * 2 for i in lista]
for i in double:
    print(double[i])

pares = [i for i in lista if i % 2 == 0]
for i in pares:
    print(pares[i])