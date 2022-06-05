#Busca en todos los elemendos de manera secuencial
#¿Cuál es el peor caso?

import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__': #Sirve para importar modulos.
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)] #Llena la lista con numeros aleatorias

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {" esta" if encontrado else "no esta"} en la lista')
